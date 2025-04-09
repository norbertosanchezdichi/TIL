# 🏷️ TagSynthesizer

**TagSynthesizer** is a blazing-fast, GPT-powered command-line utility that automatically tags technical PDFs based on their content. Designed for macOS Finder tagging, it's built for reliability, clarity, and high-performance workflows.

## 🚀 Features

- 📂 Scans entire directories recursively for PDFs
- 🧠 GPT-4o/3.5-based tag generation using cleaned and POS-filtered summaries
- 🔁 Intelligent chunking for large documents, with tag merging
- 🏷️ macOS-native Finder tag integration (`tag` CLI)
- 🧪 Dry-run support and detailed debug logging
- 🧵 Multi-threaded processing
- ⏱️ Nanosecond-precision logs per run
- 🔁 Retry failed PDFs
- 🧲 `--force-reprocess` bypasses all caches and retries
- ⚡ Configurable batch size for scalability

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

### Common Flags

| Flag | Description |
|------|-------------|
| `--model` | OpenAI model (`gpt-4o`, `gpt-3.5-turbo`, etc.) |
| `--max-tags` | Max number of tags per PDF |
| `--workers` | Max concurrent threads |
| `--batch-size` | PDFs per batch (default: 100) |
| `--dry-run` | Simulate without tagging |
| `--force-reprocess` | Ignore all caches and dry-run |
| `--retry-failed-only` | Retry only failed PDFs |
| `--verbose` | Enable debug logs |
| `--no-filter` | Skip part-of-speech filtering |

## 📊 Logging

Logs are saved in `logs/` with nanosecond-precision timestamps.
Example:
```
[2025-04-08 23:51:24,081,112,064] [INFO] 🔎 Checking 10 PDFs for tags...
```

## 🧠 Dependencies

- `fitz` (PyMuPDF)
- `textblob`
- `openai`
- `tqdm`
- `tag` (macOS-only via `brew install tag`)

## 🧪 Known Issues

- Windows `.tags.json` sidecar support is not yet implemented
- Extremely long filenames or corrupted PDFs may fail

## 🧑‍💻 Contributing

Pull requests are welcome! Open an issue to propose features or changes.

## 🪪 License

MIT License  
© 2025 Norberto Sanchez-Dichi