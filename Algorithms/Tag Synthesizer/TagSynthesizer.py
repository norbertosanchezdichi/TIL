#!/usr/bin/env python3

import argparse
import json
import logging
import os
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

import fitz
import tempfile
import shutil
from openai import OpenAI
from openai._exceptions import RateLimitError
from textblob import TextBlob
import tiktoken
from tqdm import tqdm
from tqdm import trange

VERSION = "1.1.0"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
FAILED_TAGS_CACHE = "TagSynth_failed_tags.json"
LOG_FILE_PREFIX = "TagSynth_"

def generate_log_filename(prefix=LOG_FILE_PREFIX, folder="logs"):
    os.makedirs(folder, exist_ok=True)

    ns = time.time_ns()
    sec = ns // 1_000_000_000
    nano = ns % 1_000_000_000

    milliseconds = nano // 1_000_000
    microseconds = (nano // 1_000) % 1_000
    nanoseconds = nano % 1_000

    dt = datetime.fromtimestamp(sec)
    date_str = dt.strftime("%Y-%m-%d %H:%M:%S")

    timestamp = f"{date_str},{milliseconds:03d},{microseconds:03d},{nanoseconds:03d}"
    filename = f"{prefix}{timestamp}.log"
    return os.path.join(folder, filename)

def configure_log(level=logging.INFO):
    filename = generate_log_filename()

    class HighPrecisionFormatter(logging.Formatter):
        def formatTime(self, record, datefmt=None):
            base = datetime.fromtimestamp(record.created)
            date_str = base.strftime("%Y-%m-%d %H:%M:%S")
            total_ns = int(record.created * 1_000_000_000)

            milliseconds = (total_ns // 1_000_000) % 1000
            microseconds = (total_ns // 1_000) % 1000
            nanoseconds = total_ns % 1000

            return f"{date_str},{milliseconds:03},{microseconds:03},{nanoseconds:03}"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = HighPrecisionFormatter("[%(asctime)s] [%(levelname)s] %(message)s")

    file_handler = logging.FileHandler(filename, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)  
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("openai").setLevel(logging.WARNING)

    return filename

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_pdfs(root_dir, max_files=None):
    pdf_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".pdf"):
                full_path = os.path.join(dirpath, filename)
                pdf_files.append(full_path)
                if max_files is not None and len(pdf_files) >= max_files:
                    return pdf_files
    return pdf_files

def has_tagged_finder_tag(file_path):
    try:
        result = subprocess.run(
            ["mdls", "-name", "kMDItemUserTags", file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            check=True
        )
        output = result.stdout
        return "tagged" in output.lower()
    except subprocess.CalledProcessError:
        return False

def find_untagged_pdfs(root_dir, max_workers, max_files=None):
    all_pdfs = find_pdfs(root_dir, max_files)
    logging.info(f"🔎 Checking {len(all_pdfs)} PDFs for tags...")

    def check_and_return(path):
        try:
            return path if not has_tagged_finder_tag(path) else None
        except Exception as e:
            logging.warning(f"⚠️ Error checking tags for {os.path.basename(path)}: {e}")
            return None

    untagged_pdfs = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for result in tqdm(executor.map(check_and_return, all_pdfs), total=len(all_pdfs), desc="📄 Scanning"):
            if result:
                untagged_pdfs.append(result)

    return untagged_pdfs

def parse_problematic_pages(stderr_text):
    bad_pages = set()

    # 1. Known patterns like "page 123"
    for match in re.findall(r"[Pp]age (\d+)", stderr_text):
        bad_pages.add(int(match))

    # 2. Range pattern like "pages 10 through 15"
    for start, end in re.findall(r"[Pp]ages (\d+) through (\d+)", stderr_text):
        bad_pages.update(range(int(start), int(end) + 1))

    # 3. MuPDF/Ghostscript "cannot find resource" fallback
    mupdf_lines = [line for line in stderr_text.splitlines() if "XObject resource" in line or "ExtGState resource" in line]
    if mupdf_lines:
        # Just warn and skip the *first few pages* as a fallback guess
        logging.warning(f"⚠️ MuPDF resource errors found in OCR stderr. Unable to locate page numbers reliably.")
        bad_pages.update(range(1, 4))  # fallback to skip first 3 pages

    if "non-page object in page tree" in stderr_text:
        logging.error("📌 PDF contains a non-page object in the page tree — cannot recover. Skipping.")
        return []

    return sorted(bad_pages)

def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            if len(doc) == 0:
                logging.warning(f"⚠️ {os.path.basename(pdf_path)} appears to be empty or invalid (0 pages).")
            
            text_parts = []
            for page_index in range(len(doc)):
                try:
                    page = doc.load_page(page_index)
                    text_parts.append(page.get_text())
                except Exception as e:
                    logging.warning(f"⚠️ Skipping page {page_index + 1} in {os.path.basename(pdf_path)} due to error: {e}")

            text = " ".join(text_parts).strip()
            if text:
                return text
            else:
                logging.warning(f"⚠️ No text extracted from {os.path.basename(pdf_path)} — attempting OCR...")

        # --- OCR Fallback (overwrite original file) ---
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            ocr_output = tmp.name

        file_size_kb = os.path.getsize(pdf_path) // 1024
        logging.debug(f"📄 File info: {os.path.basename(pdf_path)} — Size: {file_size_kb} KB, Pages: {len(doc)}")

        try:
            with fitz.open(pdf_path) as doc_check:
                logging.debug(f"📄 {os.path.basename(pdf_path)} — Pages: {len(doc_check)}")
        except Exception as e:
            logging.error(f"❌ Could not open {pdf_path} to inspect pages: {e}")

        try:
            result = subprocess.run(
                ["ocrmypdf", "--force-ocr", "--jobs", str(os.cpu_count()), pdf_path, ocr_output],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                text=True
            )
            if result.returncode != 0:
                logging.error(f"❌ OCR failed for {os.path.basename(pdf_path)}:")
                logging.error(result.stderr.strip())

                bad_page = None
                match = re.search(r"Page (\d+)", result.stderr)
                if match:
                    bad_page = match.group(1)
                    logging.warning(f"⚠️ Detected possible problematic page: {bad_page}. Retrying OCR without it...")

                    try:
                        result_retry = subprocess.run(
                            ["ocrmypdf", "--force-ocr", f"--pages", f"1-{int(bad_page)-1},{int(bad_page)+1}-9999", pdf_path, ocr_output],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
                        )
                        if result_retry.returncode == 0:
                            logging.info(f"✅ OCR retry succeeded after skipping page {bad_page}")
                            shutil.move(ocr_output, pdf_path)
                            with fitz.open(pdf_path) as ocr_doc:
                                return " ".join([p.get_text() for p in ocr_doc]).strip()
                        else:
                            logging.error("❌ Retry also failed.")
                            logging.error(result_retry.stderr.strip())
                    except Exception as e2:
                        logging.error(f"❌ Retry OCR exception: {e2}")                
                return ""

            logging.info(f"📄 OCR complete for {os.path.basename(pdf_path)} — replacing original")

            # Replace original with OCR’d version
            shutil.move(ocr_output, pdf_path)

            # Re-extract from the updated file
            with fitz.open(pdf_path) as ocr_doc:
                ocr_text = " ".join([page.get_text() for page in ocr_doc]).strip()
                if ocr_text:
                    logging.info(f"✅ OCR text extracted and saved in {os.path.basename(pdf_path)}")
                else:
                    logging.warning(f"❌ OCR'd file still yielded no text: {os.path.basename(pdf_path)}")
                return ocr_text

        except subprocess.CalledProcessError as e:
            stderr_text = result.stderr.strip()
            logging.error(f"❌ OCR failed for {os.path.basename(pdf_path)}:")
            logging.error(stderr_text)

            # Attempt to parse and skip problematic pages
            problem_pages = parse_problematic_pages(stderr_text)
            if problem_pages:
                logging.warning(f"🩹 Detected problematic pages: {problem_pages}. Retrying with these pages skipped...")
                
                # Build a page exclusion list (e.g., if PDF has 10 pages, exclude page 3 → --pages 1,2,4-10)
                with fitz.open(pdf_path) as temp_doc:
                    total_pages = len(temp_doc)
                valid_pages = [str(i+1) for i in range(total_pages) if (i+1) not in problem_pages]
                if not valid_pages:
                    logging.error(f"❌ All pages problematic — cannot OCR {os.path.basename(pdf_path)}.")
                    return ""

                pages_arg = ",".join(valid_pages)
                try:
                    retry = subprocess.run(
                        ["ocrmypdf", "--force-ocr", "--pages", pages_arg, pdf_path, ocr_output],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    if retry.returncode == 0:
                        shutil.move(ocr_output, pdf_path)
                        logging.info(f"✅ OCR succeeded after skipping pages {problem_pages}")
                        with fitz.open(pdf_path) as final_doc:
                            return " ".join(page.get_text() for page in final_doc).strip()
                    else:
                        logging.error(f"❌ Retry OCR still failed for {os.path.basename(pdf_path)}")
                        logging.error(retry.stderr.strip())
                except Exception as retry_ex:
                    logging.error(f"❌ Exception during retry OCR for {os.path.basename(pdf_path)}: {retry_ex}")
            return ""

        finally:
            try:
                os.remove(ocr_output)
            except Exception:
                pass

    except Exception as e:
        logging.error(f"❌ Failed to extract from {os.path.basename(pdf_path)}: {e}")
        return ""

def dynamically_chunk_text(text, max_total_tokens=12000, min_chunk_tokens=1000, model_name="gpt-4o"):
    enc = tiktoken.encoding_for_model(model_name)
    tokens = enc.encode(text)

    total_tokens = len(tokens)
    if total_tokens < min_chunk_tokens:
        logging.debug(f"🧪 Single chunk size: {total_tokens} tokens")
        return [text]

    ideal_chunk_size = max(min_chunk_tokens, min(total_tokens // 3, 4000))
    logging.debug(f"📐 Target chunk size: {ideal_chunk_size} tokens")

    chunks = []
    current_chunk = []
    current_count = 0

    for token in tokens:
        current_chunk.append(token)
        current_count += 1

        if current_count >= ideal_chunk_size:
            chunk_text = enc.decode(current_chunk)
            chunks.append(chunk_text)
            current_chunk = []
            current_count = 0

    if current_chunk:
        chunks.append(enc.decode(current_chunk))

    logging.debug(f"🔪 Total chunks: {len(chunks)}")
    return chunks

def clean_text(text: str) -> str:
    lines = text.splitlines()
    seen = set()
    clean_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue 
        if stripped.lower() in seen:
            continue
        seen.add(stripped.lower())
        clean_lines.append(stripped)

    return " ".join(clean_lines)

def filter_by_pos(text):
    blob = TextBlob(text)
    allowed = ("NN", "VB", "JJ")  # Noun, Verb, Adjective
    filtered_words = [word for word, pos in blob.tags if pos.startswith(allowed)]
    return " ".join(filtered_words)

def extract_and_filter(pdf_path, skip_filter=False):
    text_extracted = extract_text_from_pdf(pdf_path)
    
    if skip_filter:
        return text_extracted

    if not text_extracted:
        logging.warning(f"⚠️ No text extracted from {os.path.basename(pdf_path)} — skipping filtering.")
        return ""

    text_extracted_clean = clean_text(text_extracted)
    text_extracted_clean_filter = filter_by_pos(text_extracted_clean)
    
    if len(text_extracted) > 0:
        reduction = -round((1 - len(text_extracted_clean_filter) / len(text_extracted)) * 100, 3)
        logging.debug(f"Text length decrease: {reduction}%")
    else:
        logging.debug("Text was empty before filtering, skipping percent calculation.")

    return text_extracted_clean_filter

def clean_tags(tag_list):
    if not tag_list:
        return []
    clean = []
    for tag in tag_list:
        tag = tag.strip().lower()
        
        # Rule: Only keep if it has at least one letter and doesn't look like code or junk
        if (
            tag
            and re.search(r"[a-zA-Z]", tag)               # must contain letters
            and not re.search(r"[^\w\s\-]", tag)           # exclude tags with emojis, punctuation, symbols
            and len(tag) > 1                               # no single characters
        ):
            clean.append(tag)
    return clean

def generate_tags_for_chunk_batch(relative_path, chunks, model, num_tags=25, max_retries=3, backoff=10):
    batch_prompt = f"""
                    You are a technical assistant helping tag engineering documents.
                    For each of the chunks below, generate **exactly {num_tags} lowercase, relevant tags** that summarize each chunk.
                    Format each output like:
                    Chunk 1 Tags:
                    - tag
                    - tag
                    ...
                    Chunks:
                    """
    for i, chunk in enumerate(chunks, 1):
        batch_prompt += f"\nChunk {i}:\n{chunk.strip()[:3000]}...\n"

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": batch_prompt}],
                temperature=0.3,
            )
            content = response.choices[0].message.content.strip()

            # Parse output
            tag_sets = []
            matches = re.findall(r"Chunk\s+\d+\s+Tags:([\s\S]+?)(?=(\nChunk\s+\d+\s+Tags:)|$)", content)
            for tags_raw, _ in matches:
                tags = [line.strip("•- \t") for line in tags_raw.strip().splitlines() if line.strip()]
                tag_sets.append(tags[:num_tags])

            return tag_sets

        except RateLimitError:
            wait_time = backoff * (2 ** attempt)
            logging.warning(f"⏳ GPT rate-limited on batch. Retrying in {wait_time}s...")
            time.sleep(wait_time)

        except Exception as e:
            logging.error(f"❌ GPT batch tagging error: {e}")
            break
    return []

def generate_tags_from_text(relative_path, text, model, num_tags=25, max_retries=3, backoff=10):
    prompt = f"""
            You are an expert technical assistant helping categorize academic and engineering documents.
            Your task is to read the following text and generate **exactly {num_tags} concise, relevant tags** that best summarize and capture the key themes, topics, and technical focus of the content.
            **Instructions:**
            - Tags should be **specific**, not generic (e.g., use "flyback converter" not just "electronics")
            - Tags must reflect **core concepts, technologies, design methods, or components** discussed
            - **Do not include full sentences**, explanations, or commentary
            - Use **lowercase** only
            - Format output as a simple list (one tag per line, no numbering)
            Text: {text}
            Return only the {num_tags} tags.
            """
    text = text.strip()
    logging.debug(f"🧠 Sending chunk to GPT: {relative_path} (length: {len(text.split())} words)")

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )

            content = response.choices[0].message.content.strip()
            tags = [line.strip("•- \t") for line in content.splitlines() if line.strip()]
            logging.debug(f"{tags[:num_tags]}")
            return tags[:num_tags]

        except RateLimitError as e:
            wait_time = backoff * (2 ** attempt)
            logging.warning(f"\n⏳ Rate limited. Retrying in {wait_time:.1f}s (attempt {attempt+1}/{max_retries})...")
            time.sleep(wait_time)

        except Exception as e:
            logging.error(f"❌ Unexpected error: {e}")
            break
    logging.info(f"🚫 Max retries reached. Skipping \"{relative_path}\".\n")
    return []

def merge_tags_with_gpt(chunk_tag_lists, model, num_tags=25, max_retries=3, backoff=10, depth=0):
    if not chunk_tag_lists:
        return []

    # Base case: if short enough, do the normal merge
    if len(chunk_tag_lists) <= 6:
        prompt = f"""
                You are a domain expert assistant tasked with distilling high-quality tags.
                Given the following sets of tags extracted from chunks of a single technical PDF,
                combine and synthesize them into **exactly {num_tags} unique, relevant tags**
                that best represent the full document's themes and concepts.
                **Instructions:**
                - Eliminate duplicates and overly broad terms
                - Prioritize specific, technical, and high-signal tags
                - Use lowercase only
                - Return the final list of tags as one tag per line (no numbering)
                Chunk Tags:
                """
        logging.debug(f"🌀 Merge recursion depth: {depth} | Tag sets: {len(chunk_tag_lists)}")
        for i, taglist in enumerate(chunk_tag_lists, 1):
            joined = ", ".join(taglist)
            prompt += f"\nChunk {i}: {joined}"

        for attempt in range(max_retries):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                )
                content = response.choices[0].message.content.strip()
                tags = [line.strip("•- \t") for line in content.splitlines() if line.strip()]
                logging.debug(f"🧪 GPT merge depth {depth} output: {tags}")
                return clean_tags(tags[:num_tags])

            except RateLimitError:
                wait = backoff * (2 ** attempt)
                logging.warning(f"⏳ Rate limit during merging (depth {depth}). Retrying in {wait}s...")
                time.sleep(wait)

            except Exception as e:
                logging.error(f"❌ Merge error at depth {depth}: {e}")
                break

        logging.error(f"🚫 Merge failed at depth {depth}. Returning empty list.")
        return []

    # Recursive merge: break into batches
    logging.debug(f"🔀 Recursively merging {len(chunk_tag_lists)} tag sets at depth {depth}")
    grouped = [chunk_tag_lists[i:i + 4] for i in range(0, len(chunk_tag_lists), 4)]
    merged_batches = []

    for i, batch in enumerate(grouped):
        logging.debug(f"🔁 Merging batch {i+1}/{len(grouped)} at depth {depth}")
        merged = merge_tags_with_gpt(batch, model, num_tags, max_retries, backoff, depth=depth+1)
        if merged:
            merged_batches.append(merged)

    return merge_tags_with_gpt(merged_batches, model, num_tags, max_retries, backoff, depth=depth+1)

def generate_tags_for_large_doc(relative_path, full_text, model, num_tags=25):
    chunks = dynamically_chunk_text(full_text, model_name=model)
    logging.debug(f"Chunked {relative_path} into {len(chunks)} parts.")

    merged_chunk_sets = []
    current_batch = []
    current_token_count = 0
    enc = tiktoken.encoding_for_model(model)

    # Group smaller chunks into batch prompts (targeting ~6000 tokens per batch)
    for chunk in chunks:
        tokens = enc.encode(chunk)
        if current_token_count + len(tokens) > 6000 and current_batch:
            merged_chunk_sets.append(current_batch)
            current_batch = []
            current_token_count = 0

        current_batch.append(chunk)
        current_token_count += len(tokens)

    if current_batch:
        merged_chunk_sets.append(current_batch)

    logging.debug(f"🪵 Merged into {len(merged_chunk_sets)} chunk batches for {relative_path}.")

    all_tags = []
    for i, batch_chunks in enumerate(merged_chunk_sets, 1):
        batch_text = "\n".join(batch_chunks)
        tags = generate_tags_from_text(f"{relative_path} [merged chunk {i}]", batch_text, model, num_tags)
        if tags:
            all_tags.append(tags)
        logging.debug(f"📦 Batch {i}/{len(merged_chunk_sets)} tags for {os.path.basename(relative_path)}: {tags}")

    if not all_tags:
        return []

    logging.debug(f"🧩 All merged chunk-level tags for {os.path.basename(relative_path)}:\n" +
                  "\n".join([f"Set {i+1}: {', '.join(tags)}" for i, tags in enumerate(all_tags)]))
    merged = merge_tags_with_gpt(all_tags, model, num_tags)
    return merged

def load_failed_tag_cache():
    if not os.path.exists(FAILED_TAGS_CACHE):
        return set()

    try:
        with open(FAILED_TAGS_CACHE, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):
                return set()
    except (json.JSONDecodeError, ValueError) as e:
        logging.warning(f"⚠️ Failed to parse {FAILED_TAGS_CACHE}: {e}")
        return set()
    return {p for p in data if os.path.exists(p)}

def save_failed_tag_cache(failed_paths):
    with open(FAILED_TAGS_CACHE, "w") as f:
        json.dump(sorted(list(failed_paths)), f, indent=2)

def apply_finder_tags(file_path, tags):
    try:
        safe_tags = [t.strip().encode("utf-8").decode("utf-8") for t in tags if "," not in t]
        if not safe_tags:
            logging.warning(f"\n⚠️ No valid tags for {file_path}\n")
            return

        tag_string = ",".join(safe_tags)
        if not os.path.exists(file_path):
            logging.error(f"❌ File not found: {file_path}")
            return
        subprocess.run(
            ["tag", "--set", tag_string, file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Failed to apply tags to {file_path}: {e}")

def process_tagging_queue(filtered_texts, queue, model, max_tags):
    tag_results = {}
    successful, failed = set(), set()
    
    def tag_doc_wrapper(rel_path):
        text = filtered_texts.get(rel_path)
        if not text:
            return rel_path, None
        tags = generate_tags_for_large_doc(rel_path, text, model, max_tags)
        if not tags:
            return rel_path, None
        return rel_path, clean_tags(tags)

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = {executor.submit(tag_doc_wrapper, path): path for path in queue}
        for future in tqdm(as_completed(futures), total=len(futures), desc="🤖 Tagging"):
            rel_path, tags = future.result()
            if not tags:
                failed.add(rel_path)
            else:
                tag_results[rel_path] = tags
                successful.add(rel_path)
        logging.debug(f"Cleaned tags: {tags}")
        logging.debug(f"tag_results = {tag_results} - successful = {successful} - failed = {failed}")
    return tag_results, successful, failed

def extract_all_texts(paths, root_dir, max_workers, skip_filter=False):
    filtered = {}
    failed = set()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(extract_and_filter, path, skip_filter): path for path in paths}
        for future in tqdm(as_completed(futures), total=len(futures), desc="🧠 Extracting"):
            path = futures[future]
            rel_path = os.path.relpath(path, root_dir)
            logging.debug(f"Extracting text from {rel_path}.")
            try:
                filtered[rel_path] = future.result()
            except Exception as e:
                logging.error(f"❌ Failed to process {rel_path}: {e}")
                failed.add(rel_path)
    return filtered, failed

def strip_and_redo_ocr(pdf_path):
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        stripped_output = tmp.name

    try:
        logging.info(f"🧽 Stripping and redoing OCR for {os.path.basename(pdf_path)}...")
        result = subprocess.run(
            [
                "ocrmypdf",
                "--redo-ocr",             # remove existing OCR and re-OCR
                "--output-type", "pdfa",
                "--optimize", "0",
                pdf_path,
                stripped_output,
                "--jobs", str(os.cpu_count())
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        shutil.move(stripped_output, pdf_path)
        logging.info(f"✅ Replaced with re-OCR’d version: {os.path.basename(pdf_path)}")

    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Failed to redo OCR for {os.path.basename(pdf_path)}: {e.stderr.strip()}")
        try:
            os.remove(stripped_output)
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(description="Tag PDFs in Finder using GPT-generated tags")
    parser.add_argument("--dir", type=str, default=os.getcwd(), help="Directory containing PDFs")
    parser.add_argument("--model", type=str, default="gpt-4o", help="OpenAI model to use")
    parser.add_argument("--max-tags", type=int, default=25, help="Number of tags to generate")
    parser.add_argument("--workers", type=int, default=os.cpu_count(), help="Thread pool size")
    parser.add_argument("--dry-run", action="store_true", help="Only simulate tagging without writing to Finder")
    parser.add_argument("--verbose", action="store_true", help="Enable debug output")
    parser.add_argument("--max-files", type=int, default=None, help="Limit the number of PDFs to process (for testing)")
    parser.add_argument("--no-filter", action="store_true", help="Skip TextBlob part-of-speech filtering")
    parser.add_argument("--retry-failed-only", action="store_true", help="Only retry tagging files that previously failed")
    parser.add_argument("--force-reprocess", action="store_true", help="Force reprocess all PDFs (ignores existing tags, failed cache, and dry-run)")
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--batch-size", type=int, default=100, help="Number of PDFs to process per batch (default: 100)")
    args = parser.parse_args()

    start_time = time.time()

    if args.force_reprocess:
        args.dry_run = False
        logging.info("⚠️ --force-reprocess is enabled. Overriding tag checks, cache, and dry-run.")

    failed_files = set() 
    log_file_path = configure_log(level=logging.DEBUG if args.verbose else logging.INFO)
    clear_console()

    logging.info(f"📂 Scanning current directory: {os.path.basename(args.dir)}")

    # Phase 1: Find untagged PDFs 
    if args.force_reprocess:
        logging.info("♻️ Forcing reprocess of all PDFs regardless of tags or cache.")
        untagged_pdfs = find_pdfs(args.dir, args.max_files)
    elif args.retry_failed_only:
        logging.info("🔁 Retrying previously failed files only...")
        failed_files = load_failed_tag_cache()
        if not failed_files:
            logging.info("✅ No failed files to retry.")
            return
        untagged_pdfs = list(failed_files)
    else:
        logging.info("🔎 Finding untagged PDFs...")
        if args.max_files is not None:
            logging.info(f"🔬 Capped file discovery to {args.max_files} PDFs.")
        untagged_pdfs = find_untagged_pdfs(args.dir, args.workers, args.max_files)
        if not untagged_pdfs:
            logging.info("✅ All PDFs are already tagged!")
            return

    tag_results = {}
    successful_files, new_failures = set(), set()

    for i in range(0, len(untagged_pdfs), args.batch_size):
        batch_paths = untagged_pdfs[i:i + args.batch_size]
        
        # Phase 2: Extracing and filtering text
        logging.info(f"\n🧩 Processing batch #{i//args.batch_size + 1} - 🔎 extracting and filtering text from {len(batch_paths)} PDFs...")
        filtered_texts, extraction_failures = extract_all_texts(batch_paths, args.dir, args.workers)
        logging.info(f"🧠 Filtered {len(filtered_texts)} documents in batch #{i//args.batch_size + 1}")
        new_failures |= extraction_failures
        tagging_queue = filtered_texts.keys() - failed_files
        logging.info(f"💬 Generating tags using ChatGPT for {len(tagging_queue)} documents (batch #{i//args.batch_size + 1})...")
        batch_results, success, fail = process_tagging_queue(
            filtered_texts, tagging_queue, args.model, args.max_tags
        )

        # Phase 3: First-pass tagging
        tag_results.update(batch_results)
        successful_files |= success
        new_failures |= fail
        logging.info(f"🍕 Batch #{i//args.batch_size + 1} - ✅ Tagged: {len(success)}, ❌ Failed: {len(fail)}")

    # Phase 5: Retry failed items once
    if not new_failures:
        logging.info("✅ No documents to retry — skipping retry phase.")
    else:
        logging.info(f"🔁 Retrying {len(new_failures)} failed documents...")
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            executor.map(lambda rel_path: strip_and_redo_ocr(os.path.join(args.dir, rel_path)), new_failures)

        filtered_retry_texts, retry_extraction_failures = extract_all_texts(
            [os.path.join(args.dir, path) for path in new_failures], args.dir, args.workers
        )
        retry_results, success, fail = process_tagging_queue(
            filtered_retry_texts, filtered_retry_texts.keys(), args.model, args.max_tags
        )
        tag_results.update(retry_results)
        successful_files |= success
        new_failures = fail

        # Log retry results
        logging.info(f"✅ Tagged on retry: {len(success)}")
        logging.info(f"❌ Still failed after retry: {len(fail)}")

        if success:
            logging.info("🟢 Successfully tagged on retry:\n" + "\n".join(sorted(success)))
        if fail:
            logging.info("🔴 Still failed on retry:\n" + "\n".join(sorted(fail)))

    # Phase 6: Save final failed cache
    logging.info("🛟 Saving failed cache...")
    all_failures = (failed_files - successful_files) | new_failures
    save_failed_tag_cache(all_failures)

    # Phase 7: Output
    def apply_wrapper(args):
        rel_path, full_path, all_tags = args
        apply_finder_tags(full_path, all_tags)
        return rel_path
    
    tagging_inputs = [
        (rel_path, os.path.join(args.dir, rel_path), tags + (["tagged"] if "tagged" not in tags else []))
        for rel_path, tags in tag_results.items()
    ]

    if not args.dry_run:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            list(tqdm(executor.map(apply_wrapper, tagging_inputs), total=len(tagging_inputs), desc="🏷️ Applying Tags"))
    else:
        logging.info(f"🌵 (dry-run) Tagging skipped for {rel_path}.")

    total_attempted = len(successful_files) + len(new_failures)
    duration = time.time() - start_time

    logging.info(f"📊 Summary:")
    logging.info(f"   🟢 Tagged: {len(successful_files)}")
    logging.info(f"   🔴 Failed: {len(new_failures)}")
    logging.info(f"   📄 Total processed: {total_attempted}")
    logging.info(f"   ⏱️ Duration: {round(duration/60, 3)} minutes.")
    logging.info(f"🗂️ Full log saved to: {log_file_path}")


if __name__ == "__main__":
    main()
