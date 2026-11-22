# 📜 Changelog

All notable changes to **DocMind CLI**. Version format: `MAJOR.MINOR`.

---

## `v1.3` — Squad Engine (task decomposition, parallel agents), mobile/Termux, sealed owner row

### Added — Squad Engine: DocMind splits the work into named agents
- **Task decomposition with a human in the loop.** For a complex request (site, app, game, API, refactor…)
  DocMind now asks one question first: **[1] split the work into small agents** or **[2] do it alone**.
  `/squad auto` skips the question, `/squad off` disables teams entirely.
- **DocMind is always the lead.** It writes the plan (`SQUAD_PLAN.md`), gives every agent a job, runs the
  steps, performs the final review and only closes the turn after the perfection audit passes.
- **Agents get names, not numbers.** `Nova`, `Pixel`, `Atlas`, `Vector`, `Lyra`, `Orion` … The planner
  proposes them, `squad_assign_names()` guarantees unique, terminal-safe handles (duplicates and long
  names are repaired automatically).
- **Live stream in the terminal** while the team works:
  `Nova is thinking` · `Pixel writing src/ui.py` · `Atlas running tests` · `✓ Nova finished (3 files)`.
  Every event is also written to `SQUAD_LOG_<timestamp>.json`.
- **Per-agent limits:** own context slot, own tool whitelist (an agent can only call the tools it was
  given), 10 rounds per agent, 45 child rounds and a 15-minute wall-clock budget per team run.
  An agent that repeats the same tool call is closed instantly instead of burning tokens.
- **`/squad` command:** `status` (live dashboard), `on`, `off`, `auto`, `agents <2-8>`.
- **The team question is localised.** The "split the work or do it alone?" prompt used to print Turkish
  and English together; it now speaks **one language only** — the interface language — in all 14 locales
  (tr, en, az, de, es, fr, it, pt, nl, ru, ar, zh, ja, ko), with localised answer words.
- **The lead always closes the job.** After the agents finish, DocMind runs its own review pass (join the
  pieces, verify, report) instead of handing the integration work back to you.
- **True parallelism.** Sub-agents run on their own worker copy of the agent (own context, own stream
  buffers, own permission scope) and never stop to ask a question mid-flight; the API calls overlap for
  real (3 agents = 3 concurrent calls, one wave). A file that two agents want is **claimed** by the first
  one and the second gets a clear note instead of silently overwriting it.
- **Cheaper children.** Sub-agents no longer repeat the whole system prompt per step and skip context
  trimming while siblings are running.

### Added — Search works without `/search`
- The model now searches on its own whenever a request needs live facts ("search the web and then build
  X", versions, prices, docs): read sources first, then do the work.
- `/search <topic>` still exists, unchanged, as the manual verified-research command.

### Added — Mobile / Termux support
- Automatic detection (`TERMUX_VERSION`, `ANDROID_ROOT`, tiny terminals < 46 columns) plus manual
  overrides `DOCMIND_MOBILE=1|0` and `DOCMIND_DESKTOP=1`.
- **Shared storage is exposed to the agent** on phones: `~/storage/shared`, `~/storage/downloads`,
  `~/storage/dcim`, `/sdcard`, `/storage/emulated/0` — the same file access as on a desktop.
- **Terminal text is no longer broken on phones:** mobile defaults to the plain ASCII glyph set,
  stdout/stderr are reconfigured to `utf-8` with `errors="replace"` and line buffering, and the system
  prompt tells the model to keep output inside ~44 columns and use short paths.
- `/mobile` command shows the device profile and switches `on|off|ascii|unicode`.
- **Startup note for phones and tablets:** every start prints one localised line —
  *"Telefondan veya tabletten kullanıyorsanız /mobil yazarak mobil modu açın"* /
  *"On a phone or tablet, type /mobile (or /mobil)…"* — and `/mobil` works as an alias of `/mobile`
  (router, `/help`, tab-completion).

### Fixed — messages can no longer stay half printed (patch #3)
- **The half message is gone.** Streamed text used to be handed to the terminal as one long unfinished
  line; the terminal then wrapped it itself, and on a narrow phone screen the rest of the answer was
  lost. Every chunk is now wrapped to the real terminal width (`_wrap_ansi_line`, `_last_wrap_point`)
  *before* it is written, so a line is never cut by the terminal and the message always ends where it
  was meant to end.
- **The first streamed line knows about the `DocMind:` prompt.** It used to start at column 0 and push
  the prompt line past the right edge; the stream now starts with the remaining budget of that line
  (measured: 24/40/80/100/120-column terminals, widest row always inside the terminal).
- **Streamed bytes are sanitised.** A bare `\r` (the thing that made lines repaint themselves), NUL and
  other control bytes are neutralised, zero-width spaces dropped — while the colour codes DocMind
  itself emits are kept intact instead of leaking as literal `[31m` text.
- **No more frozen or duplicated output.** A single owner writes the stream (locked), the queue is not
  appended to from several threads, and the stream always finishes on its own line — even when the
  answer ends mid-sentence, when the turn is interrupted with `Ctrl+C`, or when the model returns
  nothing.
- **Everything is measured in terminal cells, not characters.** Emoji and CJK characters count as two
  columns (`_display_width`, `_char_width`), so boxes, bars, panels, tool results and the info/success/
  warn lines stay inside narrow Termux columns (verified at 40 columns: widest row 38).
- **Long single words and code are handled.** A token wider than the terminal is split hard rather than
  overflowing, and fenced code is wrapped without breaking the colouring.

### Fixed — general runtime errors found in the same sweep
- **`ask()` at end of input.** EOF (`Ctrl+D`), `Ctrl+C` and a closed stdin no longer raise out of the
  prompt: the turn ends cleanly instead of printing a traceback.
- **`BrokenPipeError` / `OSError` on a closed terminal.** Writing to a closed pipe (`docmind | head`)
  now stops the stream instead of crashing the agent.
- **Path handling.** A pasted NUL byte gives a clear `ValueError` message instead of pathlib's cryptic
  `lstat` error, and a path the OS cannot resolve falls back safely.
- **File writes.** Atomic writes and `/export` used to raise `UnicodeEncodeError` on characters the
  target encoding has no mapping for; they now replace instead of crashing.
- **Localisation completeness.** The 10 `aggressive_*` strings that only existed in `tr`/`en`/`de` are
  now present in **all 14 locales** — every locale has the same 337 keys, and every `{}` template was
  format-checked.
- **Squad failure messages** now interpolate the error correctly instead of printing the literal
  `{err}` placeholder.

### Fixed — the context / cost row no longer piles up or overlaps on a phone
- The status line that replaces the full-screen footer (`Tokens … | Context … | Cost …`) was re-printed
  after **every** turn and its compact form was measured with `len()` instead of terminal cells. On a
  phone the same numbers stacked under every message, and rows longer than the screen were wrapped by
  the terminal **on top of the line above** — the "context and cost overlap" you saw.
- Now the status is **one row per turn**: unchanged numbers print nothing, changed numbers rewrite the
  same row in place (cursor up + clear line) instead of appending a new one.
- The row is shaped for the real width and measured in cells (emoji/CJK = 2): one compact row
  (`T:12.4k C:31% ~$0.045`), then two rows, and only on a very narrow screen three short rows — always
  inside the terminal, never wrapped over itself.
- Every caller passes its width now (the repl, `/tokens`, the live footer), so the long sentence only
  appears on terminals wide enough to hold it.
- Panels stopped assuming 80 columns: the `=== title` head wraps and the closing rule follows the screen
  (the Turkish token report used to draw a 41-cell rule on a 40-cell phone).

### Changed — `/mobil` is now a real switch, and only on a phone
- **On a phone / tablet** `/mobil` toggles mobile mode: first use turns it on (compact layout, plain
  glyphs, no full-screen footer, mobile rules in the system prompt), using it again turns it off. The
  saved choice survives a restart, `DOCMIND_MOBILE_MODE` reports it, `/mobil on|off` still forces a state
  and `/mobil status` prints the panel.
- **On a computer** `/mobil` no longer pretends to do something: it says mobile mode only applies to a
  phone or tablet, changes nothing, and even a narrow desktop window is not treated as a phone.
- **One startup line, in every language.** Instead of advice ("if you are on a phone, type /mobil"),
  DocMind now prints a single sentence that states what it detected and what it did —
  `[i] 📱 Cihazınız otomatik algılandı: telefon/tablet · mobil mod AÇIK. DocMind kendini cihazınıza göre
  ayarlar.` — localised in all 14 languages, one language only, exactly once per start. The user does
  not have to know or choose the device: detection is automatic and the layout follows it.
- Narrow terminals (fewer than 46 columns) no longer get the full-screen footer: it used to eat half of
  every message on a phone.
- Piped input (`printf "/mobil\n" | docmind`) now ends the prompt line before printing the reply instead
  of gluing the answer onto `DocMind ❯`.

### Changed
- Warning and permission text now says **"your device"** instead of "your computer" (English, German,
  Italian, Dutch), so it reads correctly on a phone, tablet or desktop.
- The system prompt reports the device type, the shared storage root and mobile layout rules.

### Security — the owner row is now the program's signature
- Deleting, blanking, duplicating or moving the `_DM_OWNER` row, removing the printed owner banner or
  editing the MIT/owner header now makes DocMind refuse to start (**exit 90**) on any machine:
  exactly one `_DM_OWNER = 'OWNER: DEVRAN E. / BEYİP_'` line at column 0, seal verified against
  `_DM_OWNER_SEAL`, header verified as the first bytes of the file. `DOCMIND_NO_OWNER_CHECK` is treated
  as tampering, not as an escape hatch.

### Added — parallel agent execution
- **Parallel execution (default ON).** Independent sub-agents run **at the same time** (threads), so a team
  finishes as fast as its slowest wave instead of adding up — measured: three 0.3 s agents in **0.30 s**
  instead of 0.90 s. Agents that declare the same file are pushed into *separate waves*, so no file is ever
  written by two threads at once; independent agents share one wave.
- **Per-agent isolation:** each sub-agent runs in its own shallow clone of the agent object (own context slot,
  own stream buffers, own tool whitelist) and skips the spinner, so parallel threads never fight over the
  terminal. Parent context is untouched. A crashing agent is marked failed and the rest of the wave finishes.
- **`/squad parallel on|off`** (default on) and the `squad_parallel` config field.
- **"computer" is now "device" in every language** — the Turkish startup warning reads
  **AGENT CİHAZINIZA TAM YETKİLİDİR** and the permission prompt says *cihazınızda*; Spanish, French,
  Portuguese, Russian, Azerbaijani, Chinese, Japanese and Korean prompts were fixed too, along with every
  English tool description and system-prompt heading. Source scan confirms **0** occurrences left.
- The planner no longer drops a step that only carries a `role`/`notes` (a 3-agent plan could collapse to
  "0 usable steps"). `/squad` and `/mobile` were added to the slash-command autocomplete.

---

## `v1.2` — Token Saving, Aggressive Reasoning Mode & Stability

### Fixed — `NameError` inside the Aggressive Engine
- **Root cause:** the modules are assembled from factories, so functions defined *inside* a factory resolve names
  against the root (`__main__`) globals, not the module they end up in. The engine helpers
  (`aggressive_directive`, `aggressive_audit_folder`, `tool_aggressive_audit`, `aggressive_snapshot`,
  `AGGRESSIVE_*`) were therefore invisible to the agent / tool-registry / filesystem code and the program died with
  `NameError: name 'aggressive_directive' is not defined` as soon as an Aggressive turn started.
- **Fix:** a top-level `_dm_aggressive_bridge()` now collects the helpers from the modules that own them and binds
  them into the real `__globals__` of every function in `docmind.core.agent`, `docmind.tools.registry`,
  `docmind.tools.filesystem`, `docmind.ui.commands` and friends. The old bridge lived *inside* the agent factory
  (where those names never existed) and was removed.
- **Regression guard:** an AST scan of the whole file now reports **0** cross-module bare-name references, and the
  prompt builder, the `aggressive_audit` tool dispatch and the perfection gate are exercised directly in tests.

### Added — Aggressive Engine (makes Aggressive genuinely aggressive)
- **`Aggressive` is now a full quality contract, not just a reasoning number.** With `/effort aggressive` the agent
  receives a mandatory engineering protocol in its system prompt: clarify once then commit, plan before touching files,
  read the code instead of guessing, never ship unverified work, hunt bugs to the root cause, keep the project folder
  coherent, protect user data, and close every turn with what changed / what was verified / what is left.
- **Perfection audit before a turn can end.** After a turn that actually wrote/edited something, DocMind scans the
  working folder (syntax via `check_syntax`, `TODO/FIXME/XXX/HACK/WIP/STUB` markers, swallowed exceptions and
  unimplemented stubs). Only **blocking** findings — a real syntax error anywhere, or a problem inside a file the
  turn touched — are fed back and force another round; pre-existing markers in legacy files are reported once and
  never trap the conversation in a loop. The walk is pruned (`.git`, `node_modules`, virtualenvs, build dirs), size
  and file-count bounded, and never follows symlink loops.
- **New tool `aggressive_audit`** (read-only) exposes that audit to the model on demand; it never executes project code.
- **Automatic write snapshots:** every file the agent rewrites keeps its previous revision in `.docmind_backups/`
  (newest 20 revisions per file are kept, older ones rotate out).
- **Project memory files:** `AGGRESSIVE_PLAN.md` (plan, assumptions, verification steps) and `AGGRESSIVE_JOURNAL.md`
  (decisions, changed files, open work) are created on the first aggressive run of a folder and kept up to date.
- **`/effort engine on|off`** toggles the engine itself (persisted as `aggressive_mode`); `/effort engine` shows the state.
- Strings for the new messages in Turkish, English and German (the rest fall back through the normal i18n chain).

### Added
- **Token saving (`/token-save on|off|status`, ON by default).**
  - Persisted in `~/.docmind-single/config.json`; restored on every launch.
  - Trims only *older, bulky* tool output / code / pasted blobs (head + tail kept, with an explicit
    `[... characters omitted by DocMind token saving; re-read the file if you need the full text]` marker).
  - Never touches the system prompt, the tool schemas, the active user request, file paths or error lines,
    so answer quality and reasoning power stay the same — only redundant context is removed.
  - Auto-compaction now triggers at 60 % of the context window while saving is on (78 % when off).
  - The model is additionally told to avoid duplicate listings/re-reads and to re-read a file when a trimmed
    section is actually needed.
- **`Aggressive` reasoning level (`/effort aggressive`, alias `/zeka agresif`)
  - Forces token saving off and sends the deepest reasoning level the active model documents
    (`max` on Anthropic/DeepSeek/GPT-5.6, `xhigh` on other OpenAI reasoning models, top `thinking` level on Gemini/Groq).
  - **First activation shows a warning with `Y` / `N`**: it disables token saving by default and may consume more
    tokens. `N` (or Enter) keeps the previous level untouched and reports it back.
  - If the provider rejects the level, DocMind now retries one step lower (`high`) instead of dropping the
    reasoning parameter entirely.
- **`Hard` reasoning level (`/effort hard`)** — first-class level sent to the API as `high`.
- **Mode compatibility guard** — token saving is refused (with a clear explanation) in `aggressive`, `high`,
  `hard` and `max`; allowed in `low`, `medium` and `default`.
- `tools/sign_docmind.py` — digest + RSA-3072 signature helper for maintainers who legitimately modify the file.

### Fixed — rendering, alignment & general bugs
- **No more "square boxes" instead of letters.** DocMind now probes the active terminal encoding at start-up and
  folds every symbol it cannot render into a readable ASCII form (`⚠` → `(!)`, `✓` → `[OK]`, `◀` → `<-`,
  `→` → `->`, `•` → `*`), transliterates non-Latin letters (`ş ğ ı İ ç ö ü`, `–`, `—`, smart quotes, `₺`) and
  drops emoji/pictographs on legacy consoles. `sys.stdout`/`stderr` are wrapped so *model output* is folded too,
  and lone UTF-16 surrogates are repaired instead of crashing the print with `UnicodeEncodeError`.
  New module: `docmind/core/sanitize.py` (`sanitize_text`, `ascii_fold`, `glyph`, `install_output_sanitizer`,
  `SanitizingWriter`). Force it with `DOCMIND_ASCII=1` (or `DOCMIND_GLYPHS=ascii`) when a font is stubborn.
- **`/effort` menu is now a real table.** Columns (`No | Level | API | Token saving`) are aligned, every row keeps
  the same indent, descriptions wrap under a fixed column with `textwrap` (`break_on_hyphens=False`), the active
  row is marked on the header line, the layout adapts to terminals under ~100 columns, and the panel keeps a
  constant left edge instead of drifting right (new `print_panel(..., center=...)` + `_center_block`).
- **`_visible_controls` no longer corrupts normal output.** It used to rewrite *every* ESC byte as the literal text
  `\x1b`, which broke colour codes and multi-part writes; it now preserves DocMind's own ANSI colour sequences and
  only neutralises genuinely dangerous cursor-moving bytes.
- `_validate_arguments` no longer raises `TypeError`/`AttributeError` when the model sends a list, a JSON string or
  `null`; a new `_coerce_tool_args` normalises the payload and reports a clean "invalid arguments" result.
- `/model` rejects garbage arguments (only letters, digits and `. _ : / @ + -`) instead of storing them, and an
  empty `/model` no longer overwrites the model with an empty string after a cancelled picker.
- `ToolRegistry.execute` now pre-seeds `ok/out`, so a tool branch that returns nothing can no longer raise
  `UnboundLocalError` and kill the turn.
- `write_file` refuses to overwrite a directory or a FIFO/socket, creates missing parent folders itself and reports
  `OSError` cleanly instead of crashing; `read_text_resilient` refuses devices/FIFOs, dangling symlinks and files
  larger than 2 MB (new `MAX_READ_BYTES`) instead of loading them blindly.
- **Automatic rollback on syntax errors:** after `write_file`/`edit_file`/`multi_edit` the changed file is checked;
  if the check fails, DocMind restores the previous version from the undo snapshot and tells the model exactly what
  to retry (`auto_syntax_rolled_back` in all 14 languages). New `UndoManager.peek_last_path()`.
- `ask_user` no longer crashes on a non-numeric `default_index`; `read_file` clamps absurd `start_line`/`end_line`
  values.

### Security
- **SSRF hardening:** `_is_public_url` and `sensitive_tool_action` now block abbreviated/obfuscated IPv4
  (`http://127.1`, `http://2130706433`, `http://0x7f.1`), scoped IPv6 zone IDs (`[fe80::1%25eth0]`), trailing-dot
  `localhost.`, `.internal` / `.home.arpa` hosts and multicast/reserved ranges.
- **Decompression-bomb guard:** HTTP bodies are inflated with a hard 12 MB cap (`_bounded_decompress`) instead of
  unbounded `gzip.decompress`/`zlib.decompress`.
- **Archive extraction:** ZIP/TAR members with absolute paths, `..` segments, symlinks/hardlinks, devices and FIFOs
  are rejected; TAR uses `filter="data"` on Python 3.12+.
- **Credential-vault detection is symlink-aware** (`os.path.realpath`) and covers more vaults: `.docker`,
  `.password-store`, `.gcloud`, `.oci`, `.pki`, `.terraform.d`, `~/.config/{gh,glab,gcloud,docker,vercel,...}`,
  `kubeconfig`, `.pgpass`, `.npmrc`, `.pypirc`, `.s3cfg`, `_netrc`, `.env*`, `authorized_keys`,
  `service-account.json`, tokens and the `.pem/.key/.p12/.pfx/.kdbx/.jks/.keystore/.ppk/.asc/.gpg` suffixes —
  applied consistently to read/write/edit/delete/move/copy/archive tools.
- **Secret masking** now covers GitHub (`ghp_`, `github_pat_`), Slack (`xox?-`), Google OAuth, Hugging Face,
  Stripe (`sk_live_`/`rk_test_`), JWTs, `Bearer`/`Basic` headers, `?api_key=`/`token=`/`password=` style
  credentials and `-----BEGIN … PRIVATE KEY-----` blocks.
- `~/.docmind-single/config.json` (and its backup/logs) is forced to `0600`, directories to `0700`, and Windows
  config files get an owner-only ACL via `icacls`; a typed API key is never persisted to shell history
  (prompt-toolkit uses `InMemoryHistory`, readline length is capped).
- Files written by the agent lose group/world execute and write bits (`_harden_new_file_permissions`).
- Catastrophic-command detection normalises quotes, backslashes and `$IFS` before matching, so `r''m -rf /` and
  `rm -rf $IFS/` are still recognised (the interactive approval prompt remains the real gate).
- Non-interactive mode now honours the permission manager as well, so approval cannot be skipped by a config flag.

### Changed
- Token-saving state and the active level are printed on start-up and after every `/effort` / `/token-save`.
- **🎚️ `/effort` option menu:** running `/effort` with no argument prints every level with a number, its
  alias, the value sent to the API, whether token saving is allowed and a one-line explanation (active level
  marked `◀`), then accepts the printed number (`1`–`7`) or any level name; `Enter`/`q` cancels and keeps the
  current level. Choosing `aggressive` from the menu still asks for `Y/N`. An unknown `/effort` argument now
  shows the usage line together with the menu.

- `/help` gained the `/token-save` entry in all 14 languages; `/effort` usage text lists the new levels.
- Old `v1.1` configs are migrated automatically (new `token_save` field defaults according to the saved level).

### Fixed
- Entering an empty line at the prompt now just redraws the prompt instead of sending an empty message to the API.
- `/help` in **DE / ES / FR / RU** no longer leaks English option text (`Token / context / cost`, `USD per million
  tokens`, `Context limit`).
- Anthropic dated model IDs (e.g. `claude-sonnet-4-5-20250929`) are now recognised by the reasoning-control
  whitelist instead of silently falling back to provider defaults.
- Restored the missing `Tuple` / `Optional` typing imports that made the Rich UI panels, the `/diff` preview and
  the `/paste` clipboard helpers raise `NameError`.
- Removed a placeholder-less f-string in the `/export` header and an unused import that shadowed the new policy helper.

---

## `v1.1` — High-Precision Vision, Live Web Search & Diff Approvals

- High-resolution vision analysis (`detail: "high"`), local OCR and the Smart Vision Bridge for text-only models.
- Live multi-source web search & fact verification (DuckDuckGo + Wikipedia + StackOverflow + top-page cross-check).
- Green `+` / red `-` file approval previews and `/diff`.
- 14-language interface and strict language lock.
- `/paste`, `/copy`, `/undo`/`/redo` stack, `/export`, stdin piping, fuzzy command suggestions.

## `v1.0` — Initial Release

- Single-file, zero-dependency autonomous terminal agent with 24 native tools, multi-provider support and
  SHA-256 + RSA-3072 source integrity verification.
