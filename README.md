# ⚡ DocMind CLI (`v1.1`)

![Version](https://img.shields.io/badge/version-1.1-06b6d4?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-3776ab?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-zero%20(stdlib%20only)-22c55e?style=flat-square)
![Languages](https://img.shields.io/badge/languages-14-f97316?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-a855f7?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-eab308?style=flat-square)

**DocMind CLI** is a self-contained, **zero-dependency** (Python standard library only), cross-platform autonomous **Command-Line Interface (CLI) AI Agent** built for software engineering, high-precision screenshot & visual debugging, live internet research & fact verification, full-system file & document management, and transparent OS-aware terminal automation across **Windows**, **Linux** (**Arch Linux**, **Ubuntu/Debian**, **Fedora**, etc.), and **macOS**.

> **Creator / Owner:** `DEVRAN E. / BEYİP_`  
> **Full Installation & Usage Guide:** See [**USAGE.md**](./USAGE.md)

---

## 🆕 What's New in `v1.1`

- **🖼️ High-Precision Vision & Screenshot Debugging (`detail: "high"` + OCR + Smart Vision Bridge):**
  - Send screenshots, UI mockups, or error dialogs via **Drag & Drop**, **`/paste`** (directly from clipboard without saving a file!), **`/image <path>`**, **`@image.png`** mentions, **`--image`** CLI flags, or the autonomous **`inspect_image`** tool.
  - Supports `.png`, `.jpg`/`.jpeg`, `.webp`, `.gif`, and lossless pure-Python **`.bmp` -> `.png`** conversion.
  - Combines high-resolution pixel inspection (`detail: "high"`), optional built-in local OCR (**Windows 10/11 WinRT OCR** / `tesseract`), and an automatic **Smart Vision Bridge** so even text-only models can accurately read and solve visual errors.
- **🌐 Live Multi-Source Internet Research & Fact Verification (`web_search` + `/search`):**
  - Searches **DuckDuckGo**, **Wikipedia REST/Query API**, and **StackOverflow API** without requiring any search API key, then automatically fetches and cross-checks top web pages (`verify_top_pages=True`) to verify versions, releases, current facts, and error fixes with cited URLs.
- **🟢🔴 Clean Green `+` / Red `-` File Approval & Git Diff Boxes:**
  - Every file creation, edit, deletion, and `/diff` view displays exact **bright green `+` lines** for added/written code and **bright red `-` lines** for removed code (with ultra-fast `O(N)` prefix/suffix trimming for 20,000+ line files — zero raw JSON clutter).
- **🌍 Expanded 14-Language Support (`[1-14]`):**
  - Full interface, permission, activity, and strict AI response localization across **14 languages**: `TR`, `EN`, `AZ`, `DE`, `ES`, `FR`, `IT`, `PT`, `NL`, `RU`, `AR`, `ZH`, `JA`, `KO`.
- **⚡ Power-User Workflow Upgrades:**
  - **`@file`, `@folder`, and `@image` inline mentions** for instant context injection,
  - **`/paste`** (clipboard image/text capture) & **`/copy` / `/copy code`** (OS clipboard + OSC-52),
  - **`/diff`** (live Git status + green `+` / red `-` diff box),
  - **Multi-step `/undo [N]`**, **`/undo list`**, and **`/redo`** stack,
  - **`/export [file.md]`** Markdown conversation transcripts, **stdin pipe** support, and **fuzzy `/command` typo suggestions**.

---

## ✨ Core Highlights

- **Single-File, Zero External Packages:** Runs directly out of the box with Python's built-in standard library (`python DocMind.py` or `python3 DocMind.py`). No `pip install` or virtual environment required.
- **Full Computer-Wide Access & Rich Document Intelligence:** Inspect, search, create, edit, move, archive, or open files across any drive or directory (`C:\`, `D:\`, `/`, `Desktop`, `Downloads`, `Documents`, `Pictures`, etc.). Natively reads source code, `UTF-8` / `UTF-16` / `CP1254` text, **Word (`.docx`)**, **Excel (`.xlsx`)**, **PowerPoint (`.pptx`)**, **OpenDocument (`.odt`/`.ods`/`.odp`)**, **PDF (`.pdf`)**, **SQLite (`.sqlite`/`.db`)**, **Images (`.png`/`.jpg`/`.webp`/`.gif`/`.bmp`)**, and **Archives (`.zip`/`.tar.gz`)**.
- **Deep OS & Distro Awareness:** Automatically detects your exact operating system and Linux distribution (e.g., **Arch Linux** with `pacman`/`yay`/`paru`, **Ubuntu/Debian** with `apt`, **Fedora** with `dnf`, **Windows 11 / 10** with PowerShell/CMD/`winget`, **macOS** with `brew`) and asks whether generated scripts should target your exact OS or be cross-platform.
- **Interactive Explain-vs-Execute Terminal Mode:** When you ask for a runnable terminal/code task, DocMind lets you choose between **[1] Explain how to do it** and **[2] Execute it directly using the terminal**.
- **Mandatory Terminal Consent & Transparent Reporting:** Every `run_command` and `python_eval` displays the exact shell, working directory, and command to ask for your explicit approval **before** execution, followed by a detailed execution summary.
- **Self-Reflection, Error Triage & Rollback:** Automatically repairs fixable command/syntax errors while cleanly handing off interactive password/elevation (`sudo`/`root`/Administrator) commands without looping.
- **Multi-Provider Support:** Works with **Google Gemini**, **Anthropic (Claude)**, **OpenAI**, **Groq**, **OpenRouter**, **DeepSeek**, and **Custom / Local OpenAI-Compatible** endpoints (Ollama, LM Studio, vLLM).
- **Cryptographic Source Integrity:** Protected by **SHA-256 + 3072-bit RSA** signature verification (`OWNER: DEVRAN E. / BEYİP_`) to detect unauthorized tampering.

---

## 🚀 Quick Start

### 1. Clone the Repository (or Download `DocMind.py`)

```bash
git clone https://github.com/beyip/docmind-cli.git
cd docmind-cli
```

### 2. Run DocMind CLI

- **Linux / Arch Linux / macOS:**
  ```bash
  python3 DocMind.py
  ```

- **Windows (PowerShell or CMD):**
  ```powershell
  python DocMind.py
  ```

On first launch:
1. Pick your preferred language (`1`–`14`).
2. Select your AI provider and model.
3. Paste your API key (saved locally to `~/.docmind-single/config.json` with `0600` permissions on POSIX).
4. Start chatting, attach `@files` or screenshots, search the web, and build!

For complete setup instructions, all 5 ways to attach images, CLI flags, and slash commands, read [**USAGE.md**](./USAGE.md).

---

## 🛠️ Built-In Agent Tools (`24` Native Tools)

| Category | Tools |
| :--- | :--- |
| **Filesystem & Navigation** | `read_file`, `write_file`, `edit_file`, `multi_edit`, `delete_path`, `move_or_copy`, `list_directory`, `change_directory`, `list_system_drives`, `undo_file_change` |
| **Vision & Visual Debugging** | `inspect_image` (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp` + high-res detail & local OCR layer) |
| **Live Web Research & Verification** | `web_search` (DuckDuckGo + Wikipedia + StackOverflow + deep top-page cross-check), `web_fetch` (SSRF-protected) |
| **Search & Code Analysis** | `search_files`, `grep_search`, `project_overview`, `check_syntax` (Python, JSON, TOML, XML/SVG, Shell, JS) |
| **Archives** | `archive_tool` (create, list, and Zip-Slip-safe extract for `.zip` & `.tar.gz`) |
| **System & Terminal** | `run_command` (`bash`, `powershell`, `cmd`, `sh`), `python_eval`, `open_path`, `find_processes`, `system_info` |
| **User Interaction** | `ask_user` (interactive platform/preference selector) |

---

## ⚠️ Safety & Disclaimer

DocMind CLI operates as a full-system desktop/terminal assistant with broad filesystem visibility and user-approved command execution. Always review proposed green `+` / red `-` file diffs and terminal commands carefully before approving them. Provided **as-is** under the MIT License without warranty or liability of any kind.

---

## 📄 License & Credits

- **Author / Creator:** `DEVRAN E. / BEYİP_`
- **License:** [MIT License](./LICENSE)
