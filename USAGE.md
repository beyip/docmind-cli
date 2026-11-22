# 📖 DocMind CLI (`v1.3`) — Installation & Usage Guide

This guide explains how to install, configure, and use **DocMind CLI `v1.3`** across **Linux** (Arch Linux, Ubuntu/Debian, Fedora, etc.), **Windows 10/11**, and **macOS**.

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

## 4. Sending Images & Visual Debugging (`Vision`)

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

## 6. Token Saving & Aggressive Reasoning Mode

### 6.1 Token saving (default: **ON**)

Turn it off or on at any time:

```text
DocMind ❯ /token-save off
DocMind ❯ /token-save on
DocMind ❯ /token-save status
```

The choice is saved in `~/.docmind-single/config.json` and restored on the next launch.

**What it trims (and what it never touches)**

| Trimmed when saving | Never trimmed | Why the AI stays equally smart |
| :--- | :--- | :--- |
| Older bulky `read_file` / `grep` / `web_fetch` / command output | The system prompt and all tool schemas | Instructions and capabilities are unchanged |
| Large code/log blocks inside *earlier* turns (head + tail are kept) | Your current request and your own wording | Nothing you asked for is lost |
| Duplicate pasted blobs above ~12k characters | File paths, error lines, tool names | The model can re-read a file whenever it needs the full text — the inserted marker says so explicitly |
| Auto-compaction runs at 60% of the window instead of 78% | Tool-call / tool-result pairing | Compaction keeps every `(user → assistant → tool)` group atomic |

The only side effect is *fewer* tokens for the same answer: no reasoning level is lowered, no tool is removed, and no instruction changes. If you ever need the raw, untouched context (for example when the model must diff a very large file verbatim), run `/token-save off`.

### 6.2 Seeing the available levels (`/effort` with no argument)

```text
DocMind ❯ /effort
```

prints the option menu with the current level marked `◀` (real table output, columns aligned):

```text
No  Düzey       API         Token tasarrufu
---------------------------------------------
 1  agresif     aggressive  KAPALI
     -> en derin (maksimum)
     Tam güç: çok adımlı planlama, derin kod analizi, kendi kendini doğrulama.

 2  maksimum    max         yalnız düşük–orta
     -> max / xhigh
     Çok yüksek düşünme; uzun ve zor görevler için.

 3  yüksek      high        KAPALI             ◀
     -> high
     Dengeli yüksek düzey; günlük geliştirme için iyi varsayılan.

 4  zor         hard        KAPALI
 5  orta        medium      AÇIK / KAPALI
 6  düşük       low         AÇIK / KAPALI
 7  varsayılan  default     AÇIK / KAPALI
```

The table adapts to the terminal width, descriptions wrap under a fixed column, and the panel keeps a constant left
edge (no drifting/scattered rows). On a legacy console the symbols are folded automatically to ASCII
(`⚠` → `(!)`, `◀` → `<-`), so no line ever shows empty squares; set `DOCMIND_ASCII=1` to force that mode.

Right after the list DocMind asks for a choice:

- type a **number** (`1`–`7`) → that level is applied immediately (no need to remember its code name),
- type a **level name** (`medium`, `hard`, `agresif`, …) → same result,
- press **Enter** (or `q`) → nothing changes and DocMind tells you the level was kept.

Menu choice `1` (`aggressive`) still shows the `Y/N` warning first. `/effort <level>` keeps working exactly as
before if you prefer typing the level directly.

### 6.2.1 Terminal glyphs (`DOCMIND_ASCII`)

DocMind detects the encoding of your terminal at start-up. If the console cannot render `⚠ ✓ ◀ → • …` (Windows
`cp437`/`cp1254` consoles, `TERM=dumb`, `POSIX` locale, or a font missing those glyphs), the UI switches to ASCII
equivalents and transliterates Turkish/accented letters instead of printing empty boxes. Model replies are filtered
the same way, so a chat answer can never crash the screen.

```bash
DOCMIND_ASCII=1 docmind        # force ASCII (useful for old terminals or log files)
DOCMIND_GLYPHS=unicode docmind # force the Unicode glyphs
```

### 6.2.2 Automatic rollback after a bad write

When the agent writes or edits `.py`, `.pyi`, `.json`, `.toml`, `.xml`, `.svg`, `.sh`, `.bash`, `.js`, `.mjs` or
`.cjs`, DocMind runs a syntax check right away. If the file no longer parses, the previous working version is
restored from the undo snapshot, the fact is reported in your language and the model is told to re-read the file and
retry. You can still revert manually with `/undo`.

### 6.3 Reasoning levels

| Level | Sent to the API | Token saving |
| :--- | :--- | :--- |
| `low` | `low` | allowed (`on`/`off`) |
| `medium` | `medium` (DeepSeek: `high`) | allowed (`on`/`off`) |
| `default` | provider default (nothing sent) | allowed (`on`/`off`) |
| `high` | `high` | **always off** |
| `hard` | `high` (kept as its own level) | **always off** |
| `max` | `max` / `xhigh` on OpenAI | **always off** |
| `aggressive` | deepest level the model documents (`max` / `xhigh` / top `thinking`) | **always off** |

### 6.4 `Aggressive` mode — the Aggressive Engine

`/effort aggressive` (or menu item `1`) is not just the deepest reasoning value. After the `Y/N` warning it arms the
**Aggressive Engine**, a quality contract applied to every turn:

| Layer | What it does |
| --- | --- |
| Prompt protocol | clarify once → plan → read the code → implement → verify → fix → report. No unverified "done". |
| Perfection audit | after a turn that wrote code, an audit of the working folder runs (pruned walk, size/file-count bounded). **Blocking** = real syntax errors anywhere, or findings in files this turn touched → the turn cannot end until they are fixed. Pre-existing markers elsewhere are reported as advisory and never block |
| Tool | read-only `aggressive_audit` (model can call it any time; nothing is executed) |
| Snapshots | previous revision of every rewritten file is kept in `.docmind_backups/` (newest 20 per file) |
| Project memory | `AGGRESSIVE_PLAN.md` (plan/assumptions) and `AGGRESSIVE_JOURNAL.md` (decisions, open work) |

```text
DocMind ❯ /effort aggressive
[!] AGGRESSIVE MODE WARNING ... (Y/N) ❯ y
[OK] 🔴 AGGRESSIVE MODE ACTIVE: token saving disabled, deepest reasoning enabled.
```

Turn the engine off while keeping the deepest reasoning (it behaves like the plain deep mode):

```text
DocMind ❯ /effort engine off
[!] Aggressive engine is off for this session; only the deepest reasoning level is applied.
DocMind ❯ /effort engine
[..] Aggressive engine: off  (/effort engine on|off)
```

### 6.4 `Aggressive` mode

```text
DocMind ❯ /effort aggressive
```

The **first time** you select it, DocMind shows this warning and waits for `Y` or `N`:

- token saving is turned **off by default**,
- it **may consume more tokens** (higher API cost),
- very deep reasoning and full tool access are enabled.

Press **`Y`** to activate it — every other system keeps working normally, and the model runs at full power. Press **`N`** (or just Enter) and nothing changes; your previous level is kept and reported back to you.

If the provider rejects the deepest level, DocMind automatically retries one step lower (`high`) instead of dropping the reasoning parameter, and tells you about it.

### 6.5 Mode compatibility guard

```text
DocMind ❯ /effort hard
DocMind ❯ /token-save on
[!] Token saving cannot be enabled in 'hard' mode. Aggressive, High and Hard modes
    always keep it off; choose /effort medium or low first.
```

Switching to `aggressive`, `high`, `hard` or `max` forces token saving off (and persists that), while `low`, `medium` and `default` let you flip it freely.

## 7. Interactive Slash Commands

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
| `/effort [level]` | Show the level menu when used alone; adjust reasoning effort (`low`, `medium`, `high`, `hard`, `max`, `aggressive`, `default`). Turkish aliases: `/zeka dusuk/orta/yuksek/zor/maksimum/agresif`. `/effort engine on\|off` toggles the Aggressive Engine |
| `/token-save [on\|off\|status]` | Toggle token saving (ON by default). Refused in `aggressive`/`high`/`hard` modes |
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

## 8. Command-Line Flags & Piped Input

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

## 9. Resetting Configuration

Inside DocMind CLI, run `/reset` and confirm to automatically delete your saved `.json` configuration file and close the terminal, or delete `~/.docmind-single/config.json` (`%USERPROFILE%\.docmind-single\config.json` on Windows) manually.

---

## 10. Credits & License

- **Creator / Owner:** `DEVRAN E. / BEYİP_`
- **License:** Released under the [MIT License](./LICENSE).


## New in v1.3 — commands
| `/squad` | Team mode: `status`, `on`, `off`, `auto`, `agents <2-8>`, `parallel on\|off` — split complex work into named sub-agents |
| `/mobile` | Mobile/Termux profile: `on`, `off`, `ascii`, `unicode`, `status` |


## Squad Engine at a glance

Ask for something complex and DocMind offers a choice:

```
[1] Görev parçalama: küçük ajanlar oluşturayım (plan + isimler + paralel iş)
[2] Tek ajan: parçalamadan DocMind kendisi yapsın
```

Pick **[1]** and the terminal streams the team live:

```
  * DocMind planning the work
  * DocMind plan ready: 3 agents (Nova/planner, Pixel/ui_builder, Atlas/tester)
  > Nova     map the folder and write SQUAD_PLAN.md
     ... Nova is thinking
  [OK] Nova     finished
  > Pixel    build src/ui.py
     - Pixel writing src/ui.py
  [OK] Pixel    finished
  > Atlas    run the tests
     - Atlas running pytest -q
  [OK] Atlas    finished
```

Everything lands in `SQUAD_PLAN.md` plus `SQUAD_LOG_<timestamp>.json`; DocMind reviews the result and the
perfection audit still has the last word.

**Mobile (Termux):** `pkg install python`, then `python DocMind.py`. Run `termux-setup-storage` once so the
agent can see `~/storage/shared`; `/mobile` confirms what it detected.


### Parallel by default

```
~ running 3 agents in parallel, 1 wave(s)
▶ wave 1/1: Atlas, Nova, Pixel
   ... Pixel is thinking
   • Nova writing src/api.py
   • Atlas running pytest -q
[OK] Nova     finished
[OK] Pixel    finished
[OK] Atlas    finished
```

Agents that write **different** files share a wave and run at the same time. Agents that write the **same**
file are pushed into separate waves, so a file is never written by two threads at once. Every agent gets its
own copy of the conversation state, its own tool whitelist and its own round cap.

`/squad parallel off` returns to one-at-a-time execution.

Two agents that want the same file are not serialised silently: the first one **claims** the file, the second
gets `app.py is being edited by Nova right now; left it alone` and reports it as deferred. After the team
finishes, DocMind runs the **review pass** itself (join the pieces, verify, report) — you never have to
merge the agents' work by hand.

The single-agent/team question is printed in **one language only** (the interface language) in all 14
locales: `Bu işi nasıl yapayım?` · `How should I build this?` · `Wie soll ich das umsetzen?` · `¿Cómo quieres
que lo haga?` · `Как это сделать?` · `どのように進めますか？` …

### Phone or tablet? use `/mobil`

Every start prints exactly one line about this, in your language, on any device — the device is
detected automatically, you never choose it:

```
[i] 📱 Cihazınız otomatik algılandı: telefon/tablet · mobil mod AÇIK. DocMind kendini cihazınıza göre ayarlar.
[i] 📱 Device detected automatically: computer · mobile mode OFF. DocMind adjusts itself to your device.
[i] 📱 Gerät automatisch erkannt: Handy/Tablet · Mobilmodus AN. DocMind passt sich Ihrem Gerät an.
```

`/mobil` and `/mobile` are the same command, and on a phone it is a **switch**:

| Command | Phone / tablet | Computer |
|---|---|---|
| `/mobil` | turns mobile mode **on**; again turns it **off** | says mobile mode only applies to a phone/tablet, changes nothing |
| `/mobil on` · `/mobil off` | forces the state | still nothing |
| `/mobil status` | panel: device, mode, glyphs, storage, width | same panel, mode always OFF |
| `/mobil ascii` · `/mobil unicode` | plain glyphs · fancy glyphs | glyph preference only |

Mobile mode is remembered between starts. While it is on: the layout stays inside phone width, glyphs
are plain ASCII unless you chose otherwise, the full-screen footer is off, the prompt is short and the
model is told to keep answers narrow. A terminal narrower than 46 columns is treated the same way even
without the switch, because a full-screen footer there hides half of every answer.

### The status row on a narrow screen

With the footer off (mobile mode, or any terminal narrower than 46 columns) DocMind shows the session
status as **one row under the message** and keeps it there:

```
  T:12.4k C:31% ~$0.045
```

- unchanged numbers are not printed again, so the row never stacks;
- a changed row is rewritten in place, not appended;
- if the terminal is too narrow for one row, the three facts go on two or three short rows instead of
  one line that would be wrapped over the one above it;
- the full `Tokens … | Context … | Cost …` sentence is used only on a terminal wide enough to hold it.

### Streaming that cannot end up half printed

DocMind wraps every streamed line itself, to the terminal width it actually has, before the text reaches
the terminal. That matters most on a phone: a terminal that wraps a long line by itself can drop the rest
of it when the screen is narrow. What the patch guarantees:

- long answers break at a space (or, for a word wider than the screen, mid-word) and never run past the
  right edge;
- the first streamed line starts where the `DocMind: ` prompt ends, so the prompt never pushes it out;
- emoji and CJK characters are counted as **two** columns, so boxes, bars and labels stay aligned;
- a bare carriage return, NUL or any other control byte from the model is neutralised (colours are kept);
- the answer always finishes on its own line — after `Ctrl+C`, after an empty answer, after a closed
  pipe (`docmind | head`);
- at `Ctrl+D` or on a closed stdin the prompt ends the turn instead of printing a traceback.

Tested on 24, 40, 80, 100 and 120-column terminals: the widest printed row always stays inside the
terminal, and no word of the answer is lost.
