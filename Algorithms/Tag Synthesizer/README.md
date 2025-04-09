# TagSynthesizer

**TagSynthesizer** is a fast Python utility that intelligently analyzes and tags PDF files using GPT-4o. It integrates tightly with macOS Finder tags, supports safe dry runs, and is structured for performance, clarity, and extendability.

---

## 🚀 Features

- 🔍 Scans PDFs and extracts context-aware keywords
- 🧠 GPT-powered tag generation using POS-filtered summaries
- 🏷️ Native macOS Finder tagging with fallback .tags.json sidecar support (Windows planned)
- 🚦 Handles API rate limits with exponential backoff
- 🧪 Supports dry-run testing and verbose debug logging
- 🧵 Multi-threaded PDF processing for speed
- 🕰️ Nanosecond-precision logging with separate log files per run
- 🔁 Optional retry of previously failed PDFs

---

## 🌐 Platform Support

| OS       | Tagging Method           | Supported |
|----------|---------------------------|-----------|
| macOS    | Native Finder Tags (`tag`) | ✅ Yes    |
| Windows  | `.tags.json` sidecar files | ⚠️ Partial (not yet implemented) |
| Linux    | Not officially supported  | ❌ No    |

---

## 📁 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/tagsynth.git
cd tagsynth
```

### 2. Create and activate a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key
```bash
export OPENAI_API_KEY=your-key-here  # or use .env
```

---

## 🔧 Usage

### Basic command
```bash
python tagsynth.py --dir "/path/to/pdf/files"
```

### Common options
| Flag | Description |
|------|-------------|
| `--model` | OpenAI model to use (`gpt-4o`, `gpt-3.5-turbo`, etc.) |
| `--max-tags` | Number of tags per document (default: 25) |
| `--workers` | Thread pool size (default: CPU cores) |
| `--dry-run` | Only simulate tagging without applying tags |
| `--verbose` | Enable debug-level logs |
| `--max-files` | Limit number of PDFs scanned (useful for testing) |
| `--retry-failed-only` | Only re-process previously failed documents |
| `--no-filter` | Skip POS filtering (faster, less smart) |

---

## 📊 Logging

- Logs are written to a `logs/` subdirectory.
- Timestamps include full nanosecond resolution.
- Two streams: console (info/debug based on `--verbose`) and log file (always debug).

Example:
```
[2025-04-08 23:51:24,081,112,064] [INFO] 🔎 Checking 10 PDFs for tags...
```

---

## 🛠 Dependencies

- PyMuPDF (fitz) — PDF text extraction
- TextBlob — POS tagging
- OpenAI API — GPT-based tag generation
- tqdm — Progress bars
- tag — macOS tag command (via Homebrew)

---

## 🚫 Known Limitations

- The macOS `tag` command must be installed via Homebrew:
  ```bash
  brew install tag
  ```
- Files with special characters or very long filenames may fail tagging.

---

## 🧑‍💻 Contributing

Pull requests, suggestions, and feedback are very welcome! For significant changes, open an issue first to discuss what you’d like to change.

---

## 🎓 Credits

- Built with ❤️ by [Norberto Sanchez-Dichi](https://github.com/your-username)
- Uses:
  - [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing
  - [TextBlob](https://textblob.readthedocs.io/) for POS tagging
  - [OpenAI API](https://platform.openai.com/) for GPT-based tag generation
  - [tqdm](https://tqdm.github.io/) for progress bars

---

## ⚖️ License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Norberto Sanchez-Dichi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Happy tagging! 🚀

