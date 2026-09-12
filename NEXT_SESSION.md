# NEXT_SESSION.md — Plan to continue the corpus

> This file documents **exactly** what to do in the next session to continue the cross-corpus LDraw analysis.

**Current state (closed 2026-09-12)**:
- 1,438 OMR sets downloaded (534,152 pieces, 8 cohorts).
- 23 rules learned (`LEARNED_CONVENTIONS_532.md` → canonical: `LEARNED_CONVENTIONS_1438.md`).
- Generator `generator/ldraw_gen.py` with 7 demos validated.
- **What is missing**: ~32 OMR sets not yet downloaded (OMR has ~1,470 total).

---

## TL;DR — For the next session

If the user says "download all missing models and analyze", do:

```bash
# 1. Load current state
cat /home/user/Projects/ldraw/STATE.json

# 2. Generate setlist of missing sets (~32 OMR remaining)
# Strategy: Plan D — complete the OMR to the maximum (excluding what we already have)

# 3. Download the new MPDs
mkdir -p /home/user/Projects/ldraw/corpus/mpds_remaining
# (use xargs with P=24 to parallelize)

# 4. Re-parse everything (with updated parser)
python3 /home/user/Projects/ldraw/analysis/batch_parse4.py

# 5. Re-dispatch parallel subagents to update findings

# 6. Update LEARNED_CONVENTIONS_1438.md → or write FINAL version
# 7. Update the generator
```

---

## 1. What is ALREADY done (do not repeat)

### Current corpus: 1,438 sets in 8 cohorts

| Cohort | Sets | Pieces | Folder | Setlist JSON |
|--------|-----:|-------:|--------|--------------|
| 80s/90s | 100 | 18,670 | `corpus/mpds/` | `corpus/setlist_80s90s.json` |
| Kids | 200 | 42,947 | `corpus/mpds_kids/` | `corpus/setlist_kids.json` |
| Classic (Plan C) | 232 | 47,143 | `corpus/mpds_classic/` | `corpus/setlist_classic.json` |
| Classic gaps | 158 | 31,830 | `corpus/mpds_classic_gaps/` | `corpus/setlist_classic_gaps.json` |
| Technic | 175 | 169,839 | `corpus/mpds_technic/` | `corpus/setlist_technic.json` |
| Modern | 287 | 114,904 | `corpus/mpds_modern/` | `corpus/setlist_modern.json` |
| Specialty | 165 | 63,592 | `corpus/mpds_specialty/` | `corpus/setlist_specialty.json` |
| Licensed | 121 | 45,227 | `corpus/mpds_licensed/` | `corpus/setlist_licensed.json` |
| **Total** | **1,438** | **534,152** | — | — |

### Canonical documents (DO NOT overwrite)

- `LDRAW_GUIDE.md` — LDraw file format spec.
- `LEARNED_CONVENTIONS_1438.md` — **23 rules learned from 1,438 sets, canonical**.
- `LEARNED_CONVENTIONS_532.md` — 23 rules from 532-set baseline (canonical for the 532 corpus).
- `README.md` — project overview.
- `AGENTS.md` — agent instructions (English-only policy).

### Functional scripts

- `analysis/batch_parse4.py` — main parser (handles all 8 cohorts).
- `generator/ldraw_gen.py` — generator with 7 validated demos.

### Data

- `analysis/cross_corpus3_stats.json` — global stats (4 cohorts aggregated).
- `analysis/per_set_stats_1438.json` — per-set stats (1,438 entries).
- `corpus/all_omr_themes.json` — full catalog of 135 OMR themes.
- `corpus/plan_c_distribution.json` — Plan C plan + documented shortfalls.

---

## 2. What needs to be done (still missing)

### 2.1 Sets NOT downloaded

OMR has ~1,470 sets total. We have 1,438. **~32 sets still missing.**

URL pattern: `https://library.ldraw.org/library/omr/{SET}-{Q}.mpd`

### 2.2 Themes underrepresented (Plan C shortfall)

24 themes from the pre-2000 plan still have documented shortfalls. Some critical:

| Theme | Shortfall | Reason |
|-------|----------:|-------|
| Pirates > Pirates I | 8 | All were in previous cohorts |
| Castle > Forestmen | 5 | All were in previous cohorts |
| Castle > Black Knights | 3 | All were in previous cohorts |
| Castle > Dragon Knights | 2 | All were in previous cohorts |
| Castle > Knights Kingdom II | 1 | Already included |
| Castle (generic) | 1 | — |
| Universal Building Set > Basic | 5 | All were in previous cohorts |
| Sports > Soccer | 3 | All were in previous cohorts |
| Town Jr. | 2 | All were in previous cohorts |
| Town > World City | 2 | All were in previous cohorts |
| Adventurers > Desert | 2 | — |
| Adventurers > Orient Expedition | 1 | — |
| Town > Extreme Team | 1 | — |
| Town > Town Plan | 1 | — |
| Znap | 1 | — |

**Recommendation**: verify whether the sets these shortfalls mention are actually in previous cohorts. If not, add them manually.

### 2.3 Themes NOT downloaded (large opportunities)

| Theme | Sets in OMR | Downloaded? |
|-------|------------:|:------------:|
| Technic | 158 | ✅ (175 total) |
| Brickheadz | 76 | ✅ (76 total) |
| Racers | 76 | ✅ |
| Star Wars | 64 | ✅ |
| Architecture | 36 | ✅ |
| Modular Buildings | 14 | ✅ |
| Icons | 8 | ✅ |
| Ninjago | ~20 | ❌ NO (limited OMR) |

---

## 3. Pipeline (step by step for the next session)

### Step 1: Verify state (30 seconds)

```bash
cat /home/user/Projects/ldraw/STATE.json | head -30
ls /home/user/Projects/ldraw/corpus/mpds*/ 2>/dev/null | head
python3 -c "import json; s=json.load(open('/home/user/Projects/ldraw/STATE.json')); print(f\"Corpus: {s['corpus']['total_sets']}/{s['omr_metadata']['total_sets_in_omr_canonical']} sets, missing {s['omr_metadata']['total_sets_in_omr_canonical']-s['corpus']['total_sets']}\")"
```

### Step 2: Identify themes to expand (only if user didn't specify)

- If the user doesn't specify, ask briefly with 3 options:
  - (A) **Plan D complete**: complete entire OMR (~32 new sets).
  - (B) **Plan D gaps**: only themes underrepresented in current cohorts.
  - (C) **Plan D thematic**: user picks 3-5 specific themes.
- If the user says "whatever you decide" / "everything" / "all", go with (A) by default.

### Step 3: Generate URLs (subagent, ~5 min)

Dispatch a subagent to:
- Read `corpus/all_omr_themes.json`.
- For each target theme, generate setlist with URLs from OMR.
- Verify each URL with HEAD.
- Return JSON with full metadata.

### Step 4: Download

```bash
mkdir -p corpus/mpds_remaining
cd corpus
cat setlist_remaining.txt | xargs -I {} -P 24 sh -c '
  url="$1"
  fname=$(basename "$url")
  curl -sL --max-time 60 -o "mpds_remaining/$fname" "$url" 2>/dev/null
' _ {}
```

### Step 5: Update parser

Modify `analysis/batch_parse4.py` to scan the new directory. Or create `batch_parse5.py`.

Add:
```python
newcohort = []
for meta in setlist_remaining:
    path = Path('corpus/mpds_remaining') / f"{num}-{q}.mpd"
    if path.exists():
        try:
            r = analyze_one(path, meta, cohort='remaining')
            newcohort.append(r)
        except: pass
```

### Step 6: Re-run analysis

```bash
python3 analysis/batch_parse4.py  # or 5.py
```

### Step 7: Dispatch 4 parallel subagents

- (a) chaining cross-corpus with new cohort.
- (b) cohort comparison (include new).
- (c) themes specific to new cohort.
- (d) generator update.

### Step 8: Synthesize document

- `LEARNED_CONVENTIONS_FINAL.md` (replaces `_1438.md`).
- Or update `LEARNED_CONVENTIONS_1438.md` directly.

### Step 9: Validate

- All demos of the generator pass `validate()` with 0 errors / 0 warnings.
- Updated corpus appears in `STATE.json`.

---

## 4. Naming conventions

| Concept | Convention |
|---------|------------|
| Cohorts | `<era>_<style>` e.g. `80s90s`, `kids`, `classic`, `modern`, `technic` |
| Folders | `corpus/mpds_<cohort>/` |
| Setlists | `corpus/setlist_<cohort>.{txt,json}` |
| Parser scripts | `analysis/batch_parse<N>.py` (N=1, 2, 3, 4, ...) |
| Stats JSON | `analysis/cross_corpus<N>_stats.json` |
| Findings | `analysis/findings_<topic>.md` |
| Conventions doc | `LEARNED_CONVENTIONS_<N>.md` where N is the set count |

---

## 5. Persistent state

`STATE.json` contains:
- List of all downloaded sets (1,438 numbers).
- URLs for each setlist.
- Per-cohort statistics.
- Paths to scripts and outputs.

**Rule**: update `STATE.json` after each successful session.

---

## 6. Known risks

1. **OMR has rate limits**: downloading ~32 files in parallel may trigger. If so, add `--max-time 60` (already present) and reduce to `-P 8`.

2. **Sets with `sub_model` suffix**: `XXX-1_Helicopter.mpd` (not `XXX-1.mpd`). The parser handles this via `glob("XXX-1*.mpd")`; download script must too.

3. **OMR may have added new sets** since the previous session. Re-verify against `all_omr_themes.json`.

4. **BFC CERTIFY ratio may change** with new sets. If it drops below 20%, the corpus is becoming less formal.

5. **Generator may break** with new constants. Maintain backwards-compat with existing demos.

---

## 7. Full resume command (copy-paste)

```bash
# Verify state
cat /home/user/Projects/ldraw/STATE.json | python3 -c "import json,sys; d=json.load(sys.stdin); print('Sets:', len(d['corpus']['unique_set_numbers']), 'Pieces:', d['corpus']['total_pieces'])"

# Identify gaps
python3 -c "
import json
themes = json.load(open('/home/user/Projects/ldraw/corpus/all_omr_themes.json'))
state = json.load(open('/home/user/Projects/ldraw/STATE.json'))
downloaded = set(state['corpus']['unique_set_numbers'])
# Show themes not yet downloaded
print('Themes available in OMR not yet covered:')
for t in themes['themes']:
    print(f'  {t[\"theme_full\"]}: {t[\"set_count\"]} sets, category={t.get(\"category\")}')"
```

---

## 8. Final TL;DR

**For the next session**:
1. Read `STATE.json` and `NEXT_SESSION.md` (this file).
2. Ask the user: Plan D complete, focused on gaps, or thematic?
3. Dispatch subagent for URLs of the target themes.
4. Download in parallel.
5. Update parser.
6. Re-analyze with 4 parallel subagents.
7. Synthesize new canonical document.
8. Update `STATE.json`.

**Expected output**: corpus of ~1,470 sets, 28-30 learned rules (with refinements), generator with new templates.

**Time**: 1-2 hours wall-clock.
