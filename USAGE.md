# 📖 DocMind CLI (`v1.0`) — Installation & Usage Guide

This guide explains how to install, configure, and use **DocMind CLI** across **Linux** (Arch Linux, Ubuntu/Debian, Fedora, etc.), **Windows 10/11**, and **macOS**.

---

## 1. Requirements

- **Python `3.9` or newer** (`3.11+` recommended).
- **Zero third-party Python packages** — DocMind relies strictly on the Python standard library.
- An API key from at least one supported LLM provider (**Google Gemini**, **Anthropic Claude**, **OpenAI**, **Groq**, **OpenRouter**, **DeepSeek**), **or** a local OpenAI-compatible server (**Ollama**, **LM Studio**, **vLLM**).

Check your Python version:

```bash
# Linux / macOS
python3 --version

# Windows (PowerShell / CMD)
python --version
```

If Python is not installed yet:
- **Arch Linux:** `sudo pacman -S python`
- **Ubuntu / Debian:** `sudo apt update && sudo apt install -y python3`
- **Fedora:** `sudo dnf install -y python3`
- **Windows:** `winget install Python.Python.3.12` (or download from [python.org](https://www.python.org/downloads/))
- **macOS:** `brew install python`

---

## 2. Installation

No build step or package installation is needed. Simply clone the repository (or download `DocMind.py` directly):

```bash
git clone https://github.com/beyip/docmind-cli.git
cd docmind-cli
```

> **Important:** Do **not** modify comments, headers, or code inside `DocMind.py`. DocMind verifies its embedded **SHA-256 + RSA-3072 cryptographic signature** on startup and refuses to run if the file has been altered.

---

## 3. Running DocMind CLI & First-Time Setup

### Launch Interactive Mode

```bash
# Linux / Arch Linux / macOS
python3 DocMind.py

# Windows
python DocMind.py
```

### Step-by-Step Onboarding Flow

1. **Language Selection (`[1-6]`):**  
   Immediately upon startup, select your preferred interface and assistant language:
   - `[1]` Türkçe (`TR`)
   - `[2]` English (`EN`)
   - `[3]` Deutsch (`DE`)
   - `[4]` Español (`ES`)
   - `[5]` Français (`FR`)
   - `[6]` Русский (`RU`)
2. **Startup Authority Notice:**  
   DocMind displays a compact red warning reminding you that the agent has full access to inspect and manage files across your computer.
3. **AI Provider & Model Selection:**  
   On first run, the Setup Wizard asks you to pick a provider (`Gemini`, `Anthropic`, `OpenAI`, `Groq`, `OpenRouter`, `DeepSeek`, or `Custom / Local`) and choose a model.
4. **API Key Verification:**  
   Paste your API key when prompted. DocMind tests the connection live and stores your configuration locally in:
   - **Linux / macOS:** `~/.docmind-single/config.json`
   - **Windows:** `%USERPROFILE%\.docmind-single\config.json`

---

## 4. Everyday Usage Examples

Once at the `DocMind ❯` prompt, type natural-language requests:

- **Explore Drives & Folders Anywhere on Your Machine:**
  - *"List all drives on my computer and check free disk space."*
  - *"Summarize the PDF or Word document on my Desktop."*
  - *"Find all `.zip` archives in my Downloads folder and extract the latest one."*
- **Software Development & Self-Healing Code Edits:**
  - *"Inspect this project, find why the script crashes, fix the bug, and verify syntax."*
  - *"Write a system cleanup utility."* *(DocMind automatically detects your exact OS — e.g., Arch Linux or Windows 11 — and asks whether you want the code tailored to your OS or written universally cross-platform.)*
- **Controlled Terminal & System Operations:**
  - *"Check which process is using the most memory."*
  - *"Run my test suite and fix any failing tests."*

### How Terminal Permission & Error Triage Work

1. **Pre-Execution Approval:**  
   Before executing any shell command (`run_command`) or Python snippet (`python_eval`) — even in `/auto` mode — DocMind shows a permission box containing:
   - Shell / Runtime (`bash`, `powershell`, `cmd`, or `python`)
   - Working Directory
   - Exact Command / Code to Execute  
   Approve with `y` / `yes` (or `e` / `evet` in Turkish) or decline with `n` / `no`.
2. **Execution Report:**  
   After running, DocMind prints a clear execution box showing the command used, exit code, duration, and output preview.
3. **Smart Self-Repair vs. Manual Password Commands:**  
   - If a command fails due to a fixable issue (wrong flag, path typo, syntax error), DocMind analyzes the error, corrects the command/code, asks for your approval again, and verifies the fix. Also, any broken file edit can be rolled back automatically via snapshots (`undo_file_change` or `/undo`).
   - If a command requires an interactive password or elevated privileges (`sudo`, `root`, `pkexec`, SSH passphrase, or Windows `Run as Administrator`), DocMind **will not** retry blindly — instead, it explains why elevation is needed and gives you the exact OS-specific command to run in your own terminal.

---

## 5. Interactive Slash Commands

Type any of these commands at the `DocMind ❯` prompt:

| Command | Description |
| :--- | :--- |
| `/help` | Show all available slash commands and shortcuts |
| `/setup` | Re-run the full interactive configuration wizard |
| `/api` | Switch AI provider or update your API key |
| `/model [name]` | Select or type a different model |
| `/lang [code]` | Change language (`tr`, `en`, `de`, `es`, `fr`, `ru`) |
| `/effort [level]` | Adjust reasoning effort (`low`, `medium`, `high`, `max`, `default`) |
| `/smart` | Enable **Smart Confirm** mode (prompts before file writes & commands) |
| `/auto` | Enable **Full Auto** mode for file edits (terminal commands still require approval) |
| `/os` | Display detected OS/Linux distribution, package managers, shells, and drives |
| `/doctor` | Run system & live API health diagnostics (`/doctor tools` tests tool calling; `/doctor all` checks all configured providers) |
| `/cd <path>` | Change active working directory (supports `~`, `Desktop`, `Downloads`, absolute paths) |
| `/tree [path]` | Render a visual directory tree |
| `/undo` | Revert the most recent file edit/write/deletion from snapshot history |
| `/tokens` | Show session token consumption and estimated API cost |
| `/context` | View active context window usage or compact history (`/context compact`) |
| `/history` | Browse and resume past conversation sessions |
| `/save [name]` | Export current conversation to `~/.docmind-single/sessions/` |
| `/load <name>` | Load a saved session |
| `/clear` | Clear terminal screen and start a fresh conversation |
| `/exit` | Exit DocMind CLI cleanly |

> **Multiline Input Tip:** End a line with `\` to continue writing on the next line, or type `"""` to enter a multi-line block and finish with `"""`.

---

## 6. Command-Line Flags (CLI Arguments)

```bash
# Show version
python3 DocMind.py --version

# Launch directly in a specific language (skips startup language prompt)
python3 DocMind.py --lang en

# Run system & API diagnostics and exit
python3 DocMind.py --doctor

# Launch setup wizard directly
python3 DocMind.py --setup

# Override provider / model / permission mode
python3 DocMind.py --provider gemini --model gemini-3.8-flash --smart

# One-shot task execution
python3 DocMind.py --lang en "Summarize README.md in 5 bullet points"
```

---

## 7. Resetting Configuration

To reset saved settings and trigger first-time onboarding again, delete `config.json`:

- **Linux / macOS:**
  ```bash
  rm -f ~/.docmind-single/config.json
  ```
- **Windows (PowerShell):**
  ```powershell
  Remove-Item -Force "$HOME\.docmind-single\config.json" -ErrorAction SilentlyContinue
  ```

---

## 8. Credits & License

- **Creator / Owner:** `DEVRAN E. / BEYİP_`
- **License:** Released under the [MIT License](./LICENSE).
