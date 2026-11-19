# 📜 Changelog

All notable changes to **DocMind CLI**. Version format: `MAJOR.MINOR`.

---

## `v1.2` — Token Saving, Aggressive Reasoning Mode & Stability

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
