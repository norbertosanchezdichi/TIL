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
from openai import OpenAI
from openai._exceptions import RateLimitError
from textblob import TextBlob
from tqdm import tqdm

VERSION = "1.0.0"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
FAILED_TAGS_CACHE = "TagSynth_failed_tags.json"
LOG_FILE_PREFIX = "TagSynth_"

def generate_log_filename(prefix=LOG_FILE_PREFIX, folder="logs"):
    # Ensure logs/ exists
    os.makedirs(folder, exist_ok=True)

    # Generate high-precision timestamp
    ns = time.time_ns()
    dt = datetime.fromtimestamp(ns / 1e9)
    date_str = dt.strftime("%Y-%m-%d_%H-%M-%S")
    ms = (ns // 1_000_000) % 1000
    us = (ns // 1_000) % 1000
    ns_only = ns % 1000

    timestamp = f"{date_str}_{ms:03}_{us:03}_{ns_only:03}"
    filename = f"{prefix}_{timestamp}.log"

    return os.path.join(folder, filename)


def configure_log(level=logging.INFO):
    filename = generate_log_filename()

    class HighPrecisionFormatter(logging.Formatter):
        def formatTime(self, record, datefmt=None):
            base = datetime.fromtimestamp(record.created)
            date_str = base.strftime("%Y-%m-%d %H:%M:%S")
            total_ns = int(record.created * 1_000_000_000)

            ms = (total_ns // 1_000_000) % 1000
            us = (total_ns // 1_000) % 1000
            ns_only = total_ns % 1000

            return f"{date_str},{ms:03},{us:03},{ns_only:03}"

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
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        return "tagged" in output.lower()
    except subprocess.CalledProcessError:
        return False

def find_untagged_pdfs(root_dir, max_workers, max_files=None):
    all_pdfs = find_pdfs(root_dir, max_files)
    untagged_pdfs = []
    logging.info(f"🔎 Checking {len(all_pdfs)} PDFs for tags...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_path = {executor.submit(has_tagged_finder_tag, path): path for path in all_pdfs}
        for future in tqdm(as_completed(future_to_path), total=len(future_to_path), desc="📄 Scanning"):
            path = future_to_path[future]
            try:
                if not future.result():
                    untagged_pdfs.append(path)
                    # logging.debug(f"Append {path}")
            except Exception:
                continue
    return untagged_pdfs

def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as doc:
            text_parts = []
            for page in doc:
                text_parts.append(page.get_text())
            return " ".join(text_parts).strip()
    except Exception as e:
        logging.error(f"❌ Failed to extract from {pdf_path}: {e}")
        return ""

def filter_by_pos(text):
    blob = TextBlob(text)
    allowed = ("NN", "VB", "JJ")  # Noun, Verb, Adjective
    filtered_words = [word for word, pos in blob.tags if pos.startswith(allowed)]
    logging.debug(f"Text length percent change: {round((-len(filtered_words)/len(text))*100, 3)}%")
    return " ".join(filtered_words)

def extract_and_filter(pdf_path, skip_filter=False):
    text = extract_text_from_pdf(pdf_path)
    if skip_filter:
        return text
    return filter_by_pos(text)

def clean_tags(tag_list):
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

def generate_tags_from_text(relative_path, text, model, num_tags=25, max_retries=3, backoff=5):
    prompt = f"""
            You are an expert technical assistant helping categorize academic and engineering documents.

            Your task is to read the following text and generate **exactly {num_tags} concise, relevant tags** that best summarize and capture the key themes, topics, and technical focus of the content.

            **Instructions:**
            - Tags should be **specific**, not generic (e.g., use "flyback converter" not just "electronics")
            - Tags must reflect **core concepts, technologies, design methods, or components** discussed
            - **Do not include full sentences**, explanations, or commentary
            - Use **lowercase** only
            - Format output as a simple list (one tag per line, no numbering)

            Text:
            {text}

            Return only the {num_tags} tags.
            """
    logging.debug(f"Generating tags for {relative_path}.")

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
    logging.info(f"🚫 Max retries reached. Skipping "{relative_path}".\n")
    return []

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
        subprocess.run(["tag", "--set", tag_string, file_path], check=True)

    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Failed to apply tags to {file_path}: {e}")

def process_tagging_queue(filtered_texts, queue, model, max_tags):
    tag_results = {}
    successful, failed = set(), set()
    for rel_path in tqdm(queue, desc="🤖 Tagging"):
        text = filtered_texts.get(rel_path)
        if not text:
            failed.add(rel_path)
            continue
        tags = generate_tags_from_text(rel_path, text, model, max_tags)
        tags = clean_tags(tags)
        logging.debug(f"Cleaned tags: {tags}")
        if tags:
            tag_results[rel_path] = tags
            successful.add(rel_path)
        else:
            failed.add(rel_path)
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
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args()

    BATCH_SIZE = 100
    failed_files = set() 

    configure_log(level=logging.DEBUG if args.verbose else logging.INFO)
    clear_console()

    logging.info(f"📂 Scanning current directory: {args.dir}")

    # Phase 1: Find untagged PDFs 
    if args.retry_failed_only:
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

    for i in range(0, len(untagged_pdfs), BATCH_SIZE):
        batch_paths = untagged_pdfs[i:i + BATCH_SIZE]
        
        # Phase 2: Extracing and filtering text
        logging.info(f"\n🧩 Processing batch #{i//BATCH_SIZE + 1} - 🔎 extracting and filtering text from {len(batch_paths)} PDFs...")
        filtered_texts, extraction_failures = extract_all_texts(batch_paths, args.dir, args.workers)
        new_failures |= extraction_failures
        batch_results, success, fail = process_tagging_queue(
            filtered_texts, filtered_texts.keys() - failed_files, args.model, args.max_tags
        )

        # Phase 3: First-pass tagging
        logging.info(f"💬 Generating tags using ChatGPT for {len(batch_paths)} PDFs...")
        tag_results.update(batch_results)
        successful_files |= success
        new_failures |= fail

    # Phase 5: Retry failed items once
    logging.info("\n🔁 Retrying failed files once more...")
    retry_results, success, fail = process_tagging_queue(filtered_texts, new_failures, args.model, args.max_tags)
    tag_results.update(retry_results)
    successful_files |= success
    new_failures = fail 

    # Phase 6: Save final failed cache
    logging.info("🛟 Saving failed cache...")
    all_failures = (failed_files - successful_files) | new_failures
    save_failed_tag_cache(all_failures)

    # Phase 7: Output
    for rel_path, tags in tag_results.items():
        logging.debug(f"\n📄 {rel_path}\n🏷️ Tags: {', '.join(tags)}")
        full_path = os.path.join(args.dir, rel_path)
        all_tags = tags + (["tagged"] if "tagged" not in tags else [])
        if not args.dry_run:
            apply_finder_tags(full_path, all_tags)
        else:
            logging.info(f"🌵 (dry-run) Tagging skipped for {rel_path}.")

    logging.info(f"\n✅ {len(successful_files)} successfully tagged")
    logging.info(f"🚫 {len(all_failures)} still failed (saved to failed_tags.json)")

if __name__ == "__main__":
    main()
