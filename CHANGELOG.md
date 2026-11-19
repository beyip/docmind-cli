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
