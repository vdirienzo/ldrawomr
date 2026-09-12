# AGENTS.md

Project: analyze LDraw OMR (Official Model Repository) MPDs and synthesize learned conventions into a generator.

## Language

**All new documentation, comments, commit messages, and user-facing strings MUST be in English.** Historical docs written in Spanish (LEARNED_CONVENTIONS_*.md, README.md, NEXT_SESSION.md, dashboard.html, findings/*.md) are kept for traceability — do not delete them, but **do not add new Spanish content**. Add English versions alongside them when needed (e.g. `README.en.md`).

The Spanish-tinted docs reflect an early-session convention when the user was speaking Spanish. The user has since clarified that English is the canonical language for this project. Going forward: English only.

Spanish-only entry points and key Spanish→English mappings for reading historical docs:
- "reflejos" / "matrices con det<0" → "reflections" / "matrices with det < 0" / "mirrored geometry"
- "aprendidas" / "reglas aprendidas" → "learned rules"
- "piezas" → "parts" / "pieces"
- "encadenamiento" → "chaining" (chaining conventions)
- "delimitadores STEP" → "STEP markers"
- "custom parts embebidas" → "embedded custom parts"
- "validar" → "validate"
- "omr" → OMR (Official Model Repository)
- "sub-modelos" / "sub-builds" → "sub-models" / "sub-builds"

The analysis JSONs use English keys (`meta`, `total_pieces`, `neg_det_count`, `sub_build_count`, etc.) so the JSON-based tooling is language-agnostic.

## Orientation

- **State is persisted in `STATE.json`** — load it first to know corpus, cohorts, and what's done.
- **`NEXT_SESSION.md`** is the canonical "what to do next" doc when the user asks for continuation.
- **`LEARNED_CONVENTIONS_532.md`** is the current canonical rules doc (23 rules from 532 sets).
- **Project root**: `/home/user/Projects/ldraw`. No git, no `package.json`, no build system — pure Python scripts.

## Resume protocol (when user says "continue with everything that's missing")

1. Read `STATE.json` and `NEXT_SESSION.md`.
2. Verify corpus: `python3 -c "import json; print(json.load(open('STATE.json'))['corpus']['total_sets'])"`.
3. Pick a strategy: Plan D completo (full OMR), enfocado (gaps only), or temático (user-chosen).
4. Dispatch **one** subagent to scrape URLs from `corpus/all_omr_themes.json` (135 themes) and verify each with `curl -sI`. Output: `corpus/setlist_<cohort>.{txt,json}`.
5. Download in parallel: `cat setlist.txt | xargs -I {} -P 24 sh -c 'curl -sL --max-time 60 -o mpds_<cohort>/$(basename {}) {}'`.
6. Update parser (or copy `analysis/batch_parse3.py` to `batch_parse4.py`) to scan the new directory.
7. Re-run parser, dispatch 4 parallel analysis subagents (chaining / themes / cohorts / generator-update).
8. Synthesize new conventions doc, update `STATE.json`, update `README.md`.

## Scripts and entrypoints

| Script | Type | Run as | Output |
|--------|------|-------|--------|
| `analysis/parse_omr.py` | parser level-1 | `python3 analysis/parse_omr.py` | `analysis/raw_stats.json` |
| `analysis/deep_parse.py` | parser level-2 | `python3 analysis/deep_parse.py` | `analysis/deep_stats.json` |
| `analysis/batch_parse.py` | parser 100 sets | `python3 analysis/batch_parse.py` | legacy |
| `analysis/batch_parse2.py` | parser 300 sets | `python3 analysis/batch_parse2.py` | legacy |
| `analysis/batch_parse3.py` | parser 532 sets, 3 cohorts | `python3 analysis/batch_parse3.py` | `analysis/cross_corpus2_stats.json`, `analysis/per_set_stats_532.json` |
| `generator/ldraw_gen.py` | CLI demo generator | `python3 generator/ldraw_gen.py` | 5 `demo_*.ldr` files |

To add a new cohort, **copy `batch_parse3.py` → `batch_parse4.py`** and add the cohort loop. Do not edit `batch_parse3.py` in place — older scripts must remain runnable for legacy corpora.

## Cohort directories and setlists

| Cohort | Dir | Setlist JSON | Sets |
|--------|-----|--------------|-----|
| 80s/90s | `corpus/mpds/` | `corpus/setlist_80s90s.json` | 100 |
| Kids | `corpus/mpds_kids/` | `corpus/setlist_kids.json` | 200 |
| Classic | `corpus/mpds_classic/` | `corpus/setlist_classic.json` | 232 |

Add new cohorts as `corpus/mpds_<name>/` + `corpus/setlist_<name>.json`.

## OMR download protocol

- URL pattern: `https://library.ldraw.org/library/omr/{SET}-{QUALIFIER}.mpd`
- No auth required despite session cookies being set.
- Some classic MPDs use multi-model suffix: `XXX-1_Helicopter.mpd`. The parser handles this via `glob("XXX-1*.mpd")`; download script must too.
- Always HEAD-verify before bulk download: `curl -sI URL | head -1`.
- 24 parallel downloads is safe; >32 may trigger rate limits.

## MPD format gotchas (will trip the parser)

- **CRLF line endings**: MPDs from OMR use `\r\n`. The parser normalizes via `read_bytes().replace(b'\r\n', b'\n')`. Don't skip this.
- **`set_number` in metadata can include the qualifier**: e.g. `"1591-1"`, `"6712-1-1"`, `"3101-1"`. Always split on the **last** `-` to get `(num, qualifier)`: `num, q = full.rsplit('-', 1)`.
- **`0 FILE` lines contain the full `<set> - <name>` filename** (e.g. `0 FILE 10252 - subModel-1.ldr`). The regex must use `.+?` not `\S+` (greedy `\S+` truncates at the space).
- **Custom parts use prefix paths**: `s\10252 - 24599s01.dat` or `48\10252 - t08o2500.dat`. The parser detects these but the directory layout inside MPDs does not match disk.
- **First MPD block is the "master"**: a sub-model may have 0 type-1 lines and only reference other sub-builds. Always concatenate all sub-builds for corpus-level stats.
- **Reflections are real**: `4-4cyli.dat` reflections in Space-themed sets are 5-21% (not the 0.27% cross-corpus average). Do NOT treat reflections as parser errors.

## Generator conventions (`generator/ldraw_gen.py`)

- The file is **1161 lines, single-file, stdlib-only**. Don't split it into a package.
- **Constants are global module-level**: `BLACK=0`, `IDENTITY=(1,0,0,...)`, `BRICK_2X2="3004.dat"`. Adding more? Keep alphabetical within section.
- **Demos are checked-in artifacts**: when modifying `ldraw_gen.py`, re-run to refresh `generator/demo_*.ldr`. Don't delete demos.
- **`validate()` is the contract**: every demo must return `0 errors, 0 warnings`. Warnings are emitted for non-canonical Y (not multiple of 8) or X/Z (not multiple of 20), and for `det<0` matrices.
- **Reflections require `allow_mirrors=True`**: Castle Lion Knights and Black Falcons demos use this. Without it, `place_mirrored()` still places but `validate()` warns.
- **New themes get a `build_<theme>()` method on `LdrBuilder`** and a corresponding `build_demo_<theme>()` module-level function. Wire it into `main()` alongside the existing demos.

## Theme taxonomy (`corpus/all_omr_themes.json`)

135 OMR themes are pre-categorized:
- `official_classic` — pre-2000 System (49 themes, 545 sets). Target corpus for 80s/90s + classic cohorts.
- `official_modern` — post-2000 non-franchise (37 themes, 408 sets). Target for kids cohort.
- `licensed` — franchise IPs (Star Wars, Harry Potter, etc.). User often excludes these.
- `technic` — Technic + Mindstorms. User excludes by default but `756.dat` reflections show up in no-Technic sets too.
- `specialty` — Brickheadz, Architecture, Ideas, Seasonal, etc.

User has signaled preference for `official_classic` (City/Town/Castle/Space focus), excluding Technic and licensed franchises.

## Subagent dispatch patterns

When the user asks for corpus analysis, dispatch subagents in parallel:
- (A) **chaining**: reads `analysis/cross_corpus2_stats.json` (or successor), produces `analysis/findings_chaining_*.md`.
- (B) **cohorts**: reads same, produces `analysis/findings_cohorts_*.md`.
- (C) **themes**: reads `analysis/per_set_stats_*.json`, produces `analysis/findings_themes_*.md`.
- (D) **generator update**: reads `analysis/cross_corpus2_stats.json` + `generator/ldraw_gen.py`, updates the generator with new constants/templates, returns stats of new demos.

Each subagent writes its own MD and is told to cite numbers from the JSON. Do NOT have subagents write code that touches the parser or generator beyond the (D) task.

## Validation invariant

After any change to `generator/ldraw_gen.py`:

```bash
cd generator && python3 ldraw_gen.py 2>&1 | tail -5
```

Expected: `=== All N demos generated and validated (0 errors, 0 warnings) ===` where N matches the number of demos wired in `main()`.

After any parser change, re-run the corresponding `batch_parse*.py` and confirm the per-cohort print lines match expected counts.

## When the user says "download and analyze everything that's missing"

This is the canonical resume trigger. The user will phrase this in Spanish (typical phrases below). **Do not stop until the full pipeline is complete.**

### Trigger phrases (Spanish, any of these means "do everything missing")

- "descargá todos los modelos que faltan y seguí hasta el final para el análisis"
- "descargá todo lo que falta y analizalo"
- "completá el corpus"
- "seguí con todo lo que falta"
- "download and analyze everything that's missing"
- "plan D completo"

When any of these (or similar) is detected, follow `NEXT_SESSION.md` §3 (Plan D) end-to-end. The user has done this 4 times already (2 sets → 100 → 200 → 232 → ???) with the same intent. **The full pipeline must run:**

1. Find URLs for missing sets (subagent).
2. Download in parallel.
3. Update parser (`batch_parse4.py`).
4. Run parser.
5. Dispatch 4 parallel analysis subagents (chaining, cohorts, themes, generator).
6. Synthesize new canonical doc (`LEARNED_CONVENTIONS_FINAL.md` or update `_532.md`).
7. Update `README.md`.
8. Update `STATE.json` with new totals.
9. Run `python3 generator/ldraw_gen.py` and confirm all demos validate.

**If a stage fails, retry it before stopping.** Do not pause mid-pipeline to ask "should I continue?" — the user has already said yes.
