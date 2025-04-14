# 🏷️ TagSynthesizer

**TagSynthesizer** is a blazing-fast, GPT-powered command-line utility that automatically tags technical PDFs based on their content. Designed for macOS Finder tagging, it's built for reliability, clarity, and high-performance workflows.

## 🚀 Features

- 📂 Recursively scans directories for `.pdf` files
- 🧠 GPT-4o/3.5-based tag generation using cleaned and POS-filtered summaries
- 🔁 **Dynamic chunking and batch merging** using `tiktoken`
- 🧠 **Recursive tag merging** from multiple GPT calls
- 🏷️ macOS-native Finder tag integration (`tag` CLI)
- 🧪 Dry-run mode with verbose logs
- 🔁 **Intelligent retry of failed OCR extractions**
- 🧽 **Automatic OCR reprocessing** for broken PDFs (`--redo-ocr`)
- ⏱️ Nanosecond-precision logging for each run
- 🧵 Multi-threaded processing across:
  - Tag generation
  - Tag application
  - Retry OCR fallback
- 🧲 `--force-reprocess` bypasses all caches and dry-run
- ⚡ Configurable batch size for efficient processing
- 🔕 Suppresses noisy MuPDF/Ghostscript errors

## ⚙️ Installation

```bash
git clone https://github.com/your-username/tagsynth.git
cd tagsynth
python3 -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY=your-key-here
```

## 💻 Usage

```bash
python tagsynth.py --dir "/path/to/pdf/folder"
```

### 🔧 Common Flags

| Flag | Description |
|------|-------------|
| `--model` | OpenAI model to use (`gpt-4o`, `gpt-3.5-turbo`, etc.) |
| `--max-tags` | Maximum number of tags per PDF |
| `--workers` | Thread pool size (defaults to all cores) |
| `--batch-size` | Number of PDFs to process per batch (default: 100) |
| `--dry-run` | Simulate tagging without modifying files |
| `--force-reprocess` | Reprocess all PDFs (ignores cache & dry-run) |
| `--retry-failed-only` | Retry only previously failed PDFs |
| `--verbose` | Enable detailed debug logging |
| `--no-filter` | Disable POS filtering via TextBlob |
| `--max-files` | Cap number of PDFs to process (for testing) |

## 🧠 Smart Processing Highlights

- ✅ Batches GPT calls based on token size using `tiktoken`
- ✅ Merges tags recursively when GPT output exceeds size limits
- ✅ Redoes broken OCR using `ocrmypdf --redo-ocr`
- ✅ Skips retry phase entirely when no documents failed
- ✅ All subprocess noise is silenced to keep logs clean

## 📊 Logging

All logs are saved in `logs/` with nanosecond-level timestamp resolution.

Example:
```
[2025-04-08 23:51:24,081,112,064] [INFO] 🔎 Checking 10 PDFs for tags...
```

## 🧪 Known Issues

- Windows `.tags.json` sidecar support is not yet implemented
- Extremely long or malformed PDFs may still fail GPT/OCR
- `ocrmypdf` may silently fail if Ghostscript/PyMuPDF isn't properly installed

## 🧑‍💻 Contributing

Pull requests are welcome! Feel free to open an issue to propose improvements or report bugs.

## 🪪 License

MIT License  
© 2025 Norberto Sanchez-Dichi