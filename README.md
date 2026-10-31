# ⚡ DocMind CLI (`v1.0`)

![Version](https://img.shields.io/badge/version-1.0-06b6d4?style=flat-square)
![Python](https://img.shields.io/badge/python-3.9%2B-3776ab?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-zero%20(stdlib%20only)-22c55e?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-a855f7?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-eab308?style=flat-square)

**DocMind CLI** is a self-contained, **zero-dependency** (Python standard library only), cross-platform autonomous **Command-Line Interface (CLI) AI Agent** designed for software engineering, full-system file & document management, and transparent OS-aware terminal automation across **Windows**, **Linux** (including **Arch Linux**, **Ubuntu/Debian**, **Fedora**, etc.), and **macOS**.

> **Creator / Owner:** `DEVRAN E. / BEYİP_`  
> **Full Installation & Usage Guide:** See [**USAGE.md**](./USAGE.md)

---

## ✨ Key Highlights

- **Single-File, Zero External Packages:** Runs directly out of the box with Python's built-in standard library (`python DocMind.py` or `python3 DocMind.py`). No `pip install` or virtual environment required.
- **Instant Multi-Language Onboarding (`6` Languages):** Prompts for your preferred language (`TR`, `EN`, `DE`, `ES`, `FR`, `RU`) first thing during initial setup before displaying warnings or menus, and remembers your choice on future launches (switchable anytime via `/lang`).
- **Full Computer-Wide Access & Rich Document Intelligence:** Inspect, search, create, edit, move, archive, or open files across any drive or directory (`C:\`, `D:\`, `/`, `Desktop`, `Downloads`, `Documents`, etc.). Natively reads source code, `UTF-8` / `UTF-16` / `CP1254` text, **Word (`.docx`)**, **Excel (`.xlsx`)**, **PowerPoint (`.pptx`)**, **OpenDocument (`.odt`/`.ods`/`.odp`)**, **PDF (`.pdf`)**, **SQLite (`.sqlite`/`.db`)**, and **Archives (`.zip`/`.tar.gz`)**.
- **Deep OS & Distro Awareness:** Automatically detects your exact operating system and Linux distribution (e.g., **Arch Linux** with `pacman`/`yay`/`paru`, **Ubuntu/Debian** with `apt`, **Fedora** with `dnf`, **Windows 11 / 10** with PowerShell/CMD/`winget`, **macOS** with `brew`) and asks whether generated code/scripts should target your exact OS or be universal (cross-platform).
- **Mandatory Terminal Consent & Transparent Reporting:** Never runs shell commands or Python snippets behind your back. Every `run_command` and `python_eval` displays the exact shell, working directory, and code to ask for your explicit approval **before** execution, and prints a detailed execution summary immediately afterward.
- **Self-Reflection, Error Triage & Rollback:**
  - Automatically distinguishes between **errors the agent can fix itself** (syntax/flag mistakes, wrong file paths, code bugs — automatically repairing, re-validating syntax, or rolling back via snapshots) and **operations that require manual user execution** (`sudo` passwords, `root` privileges, SSH passphrases, or Windows UAC Administrator elevation), explaining the exact command for you to run in your own terminal instead of looping.
- **Resilient Keep-Alive Networking:** Thread-safe persistent HTTP/1.1 TLS Keep-Alive connection pool with OS-level TCP keep-alive probes, automatic mid-stream SSE disconnect recovery, and seamless fallback.
- **Multi-Provider Support:** Works with **Google Gemini**, **Anthropic (Claude)**, **OpenAI**, **Groq**, **OpenRouter**, **DeepSeek**, and **Custom / Local OpenAI-Compatible** endpoints (Ollama, LM Studio, vLLM).
- **Cryptographic Source Integrity:** Protected by SHA-256 + 3072-bit RSA signature verification to detect unauthorized tampering.

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
1. Pick your language (`1`–`6`).
2. Select your AI provider and model.
3. Paste your API key (saved locally to `~/.docmind-single/config.json` with `0600` permissions on POSIX).
4. Start chatting with natural-language instructions or `/slash` commands!

For complete setup instructions, CLI flags, slash commands, and examples, read [**USAGE.md**](./USAGE.md).

---

## 🛠️ Built-In Agent Tools (`22` Native Tools)

| Category | Tools |
| :--- | :--- |
| **Filesystem & Navigation** | `read_file`, `write_file`, `edit_file`, `multi_edit`, `delete_path`, `move_or_copy`, `list_directory`, `change_directory`, `list_system_drives`, `undo_file_change` |
| **Search & Code Analysis** | `search_files`, `grep_search`, `project_overview`, `check_syntax` (Python, JSON, TOML, XML/SVG, Shell, JS) |
| **Archives** | `archive_tool` (create, list, and Zip-Slip-safe extract for `.zip` & `.tar.gz`) |
| **System & Terminal** | `run_command` (`bash`, `powershell`, `cmd`, `sh`), `python_eval`, `open_path`, `find_processes`, `system_info` |
| **Interaction & Web** | `ask_user` (interactive platform/preference selector), `web_fetch` |

---

## ⚠️ Safety & Disclaimer

DocMind CLI operates as a full-system desktop/terminal assistant with broad filesystem visibility and user-approved command execution. Always review proposed file modifications and terminal commands carefully before approving them. Provided **as-is** under the MIT License without warranty or liability of any kind.

---

## 📄 License & Credits

- **Author / Creator:** `DEVRAN E. / BEYİP_`
- **License:** [MIT License](./LICENSE)
