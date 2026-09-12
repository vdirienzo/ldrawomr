# AGENTS.md

Project: analyze LDraw OMR (Official Model Repository) MPDs and synthesize learned conventions into a generator.

## Language

**All new documentation, comments, docstrings, commit messages, and user-facing strings MUST be in English.** This applies to:

- Markdown files (`.md`)
- Python source code (docstrings, comments, log/error messages, `#` comments)
- HTML/CSS/JS strings
- JSON keys that are user-facing (data keys can stay English)
- Commit messages
- Output strings in print/log/UI text

**NO Spanish, NO mixed Spanish-English in any of these contexts.**

If historical content is in Spanish (legacy files like `LEARNED_CONVENTIONS_*.md`, `NEXT_SESSION.md`, `dashboard.html`, `findings_*.md`, `generator/ldraw_gen.py`), treat it as technical debt to be cleaned up. The canonical language is English.

## Project at a glance

- **Corpus**: 1,438 OMR sets across 8 cohorts, ~534k pieces analyzed.
- **Canonical doc**: `LEARNED_CONVENTIONS_532.md` (23 learned rules from the 532-set baseline corpus).
- **Generator**: `generator/ldraw_gen.py` produces `.ldr`/`.mpd` files.
- **State persistence**: `STATE.json` lists all setlist files, parser paths, cohort counts.

## Orientation

- **`AGENTS.md`** (this file) — agent instructions + strict English-only policy.
- **`STATE.json`** — load first to know corpus, cohorts, scripts, and what's done.
- **`README.md`** — quick-start guide (English).
- **`LEARNED_CONVENTIONS_532.md`** — canonical learned rules.
- **`NEXT_SESSION.md`** — plan for the next session to continue the corpus.
- **`analysis/`** — parsers, stats JSONs, findings MDs.
- **`generator/`** — code generator + 5 demos.
- **`corpus/`** — Parts Library mirror + MPDs + setlists.
- **`output/dashboard.html`** — interactive HTML dashboard.

## Resume protocol (when user says "download and analyze everything that's missing")

1. Read `STATE.json` and `NEXT_SESSION.md`.
2. Verify corpus: `python3 -c "import json; print(json.load(open('STATE.json'))['corpus']['total_sets'])"`.
3. Pick a strategy: Plan D complete (full OMR), focused (gaps only), or thematic (user-chosen).
4. Dispatch **one** subagent to scrape URLs from `corpus/all_omr_themes.json` (if available) or OMR pages. The OMR directory is at `https://library.ldraw.org/omr/sets`. Verify each with `curl -sI`. Output: `corpus/setlist_<cohort>.{txt,json}`.
5. Download in parallel: `cat setlist.txt | xargs -I {} -P 24 sh -c 'curl -sL --max-time 60 -o mpds_<cohort>/$(basename {}) {}'`.
6. Update parser (or copy `analysis/batch_parse4.py` to `batch_parse5.py`) to scan the new directory.
7. Re-run parser.
8. Dispatch 4 parallel analysis subagents:
   - (A) **chaining** → `analysis/findings_chaining_<N>.md`.
   - (B) **cohorts** → `analysis/findings_cohorts_<N>.md`.
   - (C) **themes** → `analysis/findings_themes_<N>.md`.
   - (D) **generator update** → modifies `generator/ldraw_gen.py` with new constants/templates, returns stats of new demos.
9. Synthesize new conventions doc (`LEARNED_CONVENTIONS_<N>.md` or update existing).
10. Update `README.md`, `STATE.json`, and commit.

Each subagent writes its own MD and cites numbers from the JSON. Do **NOT** have subagents write code that touches the parser or generator beyond the (D) task.

## Scripts and entrypoints

| Script | Purpose | Run as |
|--------|---------|--------|
| `analysis/parse_omr.py` | parser level-1 (basic stats) | `python3 analysis/parse_omr.py` |
| `analysis/deep_parse.py` | parser level-2 (bigrams, matrices, deltas, Y-layers) | `python3 analysis/deep_parse.py` |
| `analysis/batch_parse.py` | parser batch (100 sets) | `python3 analysis/batch_parse.py` |
| `analysis/batch_parse2.py` | parser batch 2.0 (300 sets, cross-cohort) | `python3 analysis/batch_parse2.py` |
| `analysis/batch_parse3.py` | parser batch 3.0 (532 sets, 3 cohorts) | `python3 analysis/batch_parse3.py` |
| `analysis/batch_parse4.py` | parser batch 4.0 (1,438 sets, 8 cohorts) | `python3 analysis/batch_parse4.py` |
| `generator/ldraw_gen.py` | CLI demo generator | `cd generator && python3 ldraw_gen.py` |

To add a new cohort, **copy `batch_parseN.py` → `batch_parse(N+1).py`** and add the cohort loop. Do not edit `batch_parseN.py` in place — older scripts must remain runnable for legacy corpora.

## Cohort directories and setlists

| Cohort | Dir | Setlist JSON | Sets |
|--------|-----|--------------|-----:|
| 80s/90s | `corpus/mpds/` | `corpus/setlist_80s90s.json` | 100 |
| Kids | `corpus/mpds_kids/` | `corpus/setlist_kids.json` | 200 |
| Classic (Plan C) | `corpus/mpds_classic/` | `corpus/setlist_classic.json` | 232 |
| Classic gaps | `corpus/mpds_classic_gaps/` | `corpus/setlist_classic_gaps.json` | 158 |
| Technic | `corpus/mpds_technic/` | `corpus/setlist_technic.json` | 175 |
| Modern | `corpus/mpds_modern/` | `corpus/setlist_modern.json` | 287 |
| Specialty | `corpus/mpds_specialty/` | `corpus/setlist_specialty.json` | 165 |
| Licensed | `corpus/mpds_licensed/` | `corpus/setlist_licensed.json` | 121 |

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

- The file is **~1,200 lines, single-file, stdlib-only**. Don't split it into a package.
- **Constants are global module-level**: `BLACK=0`, `IDENTITY=(1,0,0,...)`, `BRICK_2X2="3004.dat"`. Adding more? Keep alphabetical within section.
- **Demos are checked-in artifacts**: when modifying `ldraw_gen.py`, re-run to refresh `generator/demo_*.ldr`. Don't delete demos.
- **`validate()` is the contract**: every demo must return `0 errors, 0 warnings`. Warnings are emitted for non-canonical Y (not multiple of 8) or X/Z (not multiple of 20), and for `det<0` matrices.
- **Reflections require `allow_mirrors=True`**: Castle Lion Knights and Black Falcons demos use this. Without it, `place_mirrored()` still places but `validate()` warns.
- **New themes get a `build_<theme>()` method on `LdrBuilder`** and a corresponding `build_demo_<theme>()` module-level function. Wire it into `main()` alongside the existing demos.

## Theme taxonomy (`corpus/all_omr_themes.json`)

135 OMR themes are pre-categorized:
- `official_classic` — pre-2000 System (49 themes, ~545 sets). Target for 80s/90s + classic cohorts.
- `official_modern` — post-2000 non-franchise (37 themes, ~408 sets). Target for kids cohort.
- `licensed` — franchise IPs (Star Wars, Harry Potter, etc.). User often excludes these.
- `technic` — Technic + Mindstorms. User excludes by default but `756.dat` reflections show up in no-Technic sets too.
- `specialty` — Brickheadz, Architecture, Ideas, Seasonal, etc.

User has signaled preference for `official_classic` (City/Town/Castle/Space focus), excluding Technic and licensed franchises.

## Validation invariant

After any change to `generator/ldraw_gen.py`:

```bash
cd generator && python3 ldraw_gen.py 2>&1 | tail -5
```

Expected: `=== All N demos generated and validated (0 errors, 0 warnings) ===` where N matches the number of demos wired in `main()`.

After any parser change, re-run the corresponding `batch_parse*.py` and confirm the per-cohort print lines match expected counts.

## When the user says "download and analyze everything that's missing"

This is the canonical resume trigger. Trigger phrases (any of these means "do everything missing"):

- "download and analyze everything that's missing"
- "complete the corpus"
- "follow up with everything that's missing"
- "Plan D complete"
- (Spanish equivalents, but aim to write in English going forward)

When any of these is detected, follow the **Resume protocol** above end-to-end. The user has done this multiple times (2 sets → 100 → 200 → 232 → 906 more sets → 1,438 total). **The full pipeline must run**: do not pause mid-pipeline to ask "should I continue?" — the user has already said yes. If a stage fails, retry it before stopping.

## Code style

- All Python code: docstrings in English, comments in English (`#`).
- All identifiers: English only. No Spanish variable names.
- All error messages and log lines: English.
- String literals that might be printed: English.
- Type hints preferred (the project uses `from __future__ import annotations`).
