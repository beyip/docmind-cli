# 📖 DocMind CLI (`v1.1`) — Installation & Usage Guide

This guide explains how to install, configure, and use **DocMind CLI `v1.1`** across **Linux** (Arch Linux, Ubuntu/Debian, Fedora, etc.), **Windows 10/11**, and **macOS**.

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

> **Important:** Do **not** modify comments, headers, or code inside `DocMind.py`. DocMind verifies its embedded **SHA-256 + RSA-3072 cryptographic signature** (`OWNER: DEVRAN E. / BEYİP_`) on startup and refuses to run if the file has been altered.

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

1. **Language Selection (`[1-14]` — First-Time Setup Only):**  
   On your very first run (or when running `--setup`), DocMind asks for your preferred language before anything else and remembers it automatically on all future launches (switchable anytime via `/lang`):
   - `[1]` Türkçe (`TR`) · `[2]` English (`EN`) · `[3]` Azərbaycan (`AZ`) · `[4]` Deutsch (`DE`)
   - `[5]` Español (`ES`) · `[6]` Français (`FR`) · `[7]` Italiano (`IT`) · `[8]` Português (`PT`)
   - `[9]` Nederlands (`NL`) · `[10]` Русский (`RU`) · `[11]` العربية (`AR`) · `[12]` 中文 (`ZH`)
   - `[13]` 日本語 (`JA`) · `[14]` 한국어 (`KO`)
2. **Startup Authority Notice:**  
   DocMind displays its bright-red `OWNER: DEVRAN E. / BEYİP_` seal and a compact authority notice reminding you that the agent can inspect and manage files across your computer with your consent.
3. **AI Provider & Model Selection:**  
   Pick a provider (`Gemini`, `Anthropic`, `OpenAI`, `Groq`, `OpenRouter`, `DeepSeek`, or `Custom / Local`) and choose a model.
4. **API Key Verification:**  
   Paste your API key when prompted. DocMind tests the connection live and stores your configuration locally in:
   - **Linux / macOS:** `~/.docmind-single/config.json`
   - **Windows:** `%USERPROFILE%\.docmind-single\config.json`

---

## 4. Sending Images & Visual Debugging (`Vision` in `v1.1`)

Supported formats: **`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`** (BMP screenshots are automatically converted to lossless PNG in pure Python).

You can send screenshots or images in **5 easy ways**:

1. **Drag & Drop Directly into the Terminal:**  
   Drag an image from your Desktop/File Explorer into the `DocMind ❯` prompt (works with spaces in paths and `file://` URIs):
   ```text
   DocMind ❯ C:\Users\Devran\Desktop\Error Screenshot 1.png fix the bug shown here
   ```
2. **Paste Directly from Clipboard (`/paste`) — No File Needed:**  
   Take a screenshot (`Win + Shift + S`, `PrintScreen`, or macOS `Cmd + Ctrl + Shift + 4`) and run:
   ```text
   DocMind ❯ /paste explain and fix this error
   ```
3. **`/image` Slash Command:**
   ```text
   DocMind ❯ /image "screenshots/crash.png" why is this failing?
   ```
4. **`@` Inline Context Mentions (Combine Code + Screenshots):**
   ```text
   DocMind ❯ @src/server.py @crash.png fix the exception shown in the screenshot
   ```
5. **CLI `--image` / `-i` Flag:**
   ```bash
   python3 DocMind.py --image crash.png "Diagnose and fix this error"
   ```

> **Smart Vision Bridge:** Even if your active model is text-only (such as `openai/gpt-oss-120b` on Groq or `deepseek-chat`), DocMind automatically bridges the image through a Vision-capable model (`meta-llama/llama-4-scout-17b-16e-instruct` or another configured Vision provider) and enriches it with local OCR when available.

---

## 5. Live Internet Research, `@mentions` & Green `+` / Red `-` Approvals

- **Live Web Search & Fact Verification:**  
  Ask about current software releases, prices, documentation, or say *"research and verify this"* — or run **`/search <query>`** directly. DocMind queries DuckDuckGo, Wikipedia, and StackOverflow, then cross-checks top web pages before answering with source URLs.
- **Inline `@file` & `@folder` Mentions:**  
  Reference existing files or folders directly in chat (`@app.py`, `@"my notes.docx"`, `@src/`) to attach their content or directory tree immediately.
- **Green `+` / Red `-` File Approval System:**  
  Before creating, editing, or deleting a file in Smart Confirm mode, DocMind renders a clean preview box showing **bright green `+` lines** for added/written code and **bright red `-` lines** for removed code.
- **Interactive Explain-vs-Execute & Mandatory Terminal Consent:**  
  For runnable tasks, choose between `[1] Explain` and `[2] Run in Terminal`. Every shell/Python execution requires explicit pre-execution approval and prints a full summary afterward.

---

## 6. Interactive Slash Commands

Type any of these commands at the `DocMind ❯` prompt (includes Tab completion and fuzzy typo suggestions):

| Command | Description |
| :--- | :--- |
| `/help` | Show all available slash commands and shortcuts |
| `/search <query>` | Search the live internet & cross-verify facts across multiple sources |
| `/image <path> [prompt]` | Attach an image/screenshot and analyze or fix errors |
| `/paste [prompt]` | Capture screenshot or text directly from your OS clipboard |
| `/copy [code]` | Copy the last assistant reply (`/copy code` copies code blocks only) |
| `/diff [path]` | Show Git status and uncommitted changes in green `+` / red `-` lines |
| `/undo [N \| list]` | Revert the last `N` file modifications or inspect snapshot history (`/undo list`) |
| `/redo` | Re-apply the most recently undone file modification |
| `/export [file.md]` | Export the current conversation transcript to a clean Markdown file |
| `/setup` | Re-run the full interactive configuration wizard |
| `/api` | Switch AI provider or update your API key |
| `/model [name]` | Select or type a different model |
| `/lang [code]` | Switch interface & AI language (`tr`, `en`, `az`, `de`, `es`, `fr`, `it`, `pt`, `nl`, `ru`, `ar`, `zh`, `ja`, `ko`) |
| `/effort [level]` | Adjust reasoning effort (`low`, `medium`, `high`, `max`, `default`) |
| `/smart` | Enable **Smart Confirm** mode (green `+` / red `-` approval before file edits & commands) |
| `/auto` | Enable **Full Auto** mode for file edits (terminal commands still require approval) |
| `/os` | Display detected OS/Linux distribution, package managers, shells, and drives |
| `/doctor` | Run system & live API diagnostics (`/doctor tools` tests tool schemas; `/doctor all` checks all configured providers) |
| `/cd <path>` | Change active working directory |
| `/tree [path]` | Render a visual directory tree |
| `/tokens` | Show session token consumption and estimated API cost |
| `/price` | Configure custom USD token pricing for the active model |
| `/context` | View active context window usage or compact history (`/context compact`) |
| `/history` | Browse and resume past conversation sessions |
| `/delete` | Delete a saved conversation from history |
| `/save [name]` | Save current conversation to `~/.docmind-single/sessions/` |
| `/load <name>` | Load a saved session |
| `/clear` | Clear terminal screen and start a fresh conversation |
| `/reset` | Delete saved `.json` configuration after confirmation and close the terminal |
| `/exit` | Exit DocMind CLI cleanly |

---

## 7. Command-Line Flags & Piped Input

```bash
# Show version
python3 DocMind.py --version

# Launch directly in a specific language (14 languages supported)
python3 DocMind.py --lang tr

# Analyze a screenshot directly from the terminal
python3 DocMind.py --image error.png "Fix the bug shown in this screenshot"

# Pipe logs or git diffs directly into DocMind
cat build.log | python3 DocMind.py "Diagnose why the build failed"

# Run system & API diagnostics and exit
python3 DocMind.py --doctor

# One-shot task execution
python3 DocMind.py --lang en "Summarize @README.md in 5 bullet points"
```

---

## 8. Resetting Configuration

Inside DocMind CLI, run `/reset` and confirm to automatically delete your saved `.json` configuration file and close the terminal, or delete `~/.docmind-single/config.json` (`%USERPROFILE%\.docmind-single\config.json` on Windows) manually.

---

## 9. Credits & License

- **Creator / Owner:** `DEVRAN E. / BEYİP_`
- **License:** Released under the [MIT License](./LICENSE).
