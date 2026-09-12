# LDraw OMR — Analysis, Documentation, and Generator

Project to understand the LDraw file format (open standard for LEGO CAD) and
learn LEGO modeling conventions by analyzing official models in the OMR
(Official Model Repository).

**Corpus**: **532 OMR sets** (108,760 pieces) across three cohorts:
- 100 sets from 80s/90s (non-Technic).
- 200 "kids" sets (small/affordable, post-1985).
- 232 "classic" sets (Plan C: uniform distribution across 49 pre-2000 themes).

---

## ⚡ RESUME FROM HERE (next session)

If you want to continue the corpus, read first:
- **[NEXT_SESSION.md](./NEXT_SESSION.md)** — detailed continuation plan.
- **[STATE.json](./STATE.json)** — persistent project state (what's there, what's missing).

**TL;DR**: ~938 OMR sets still need downloading (out of 1,470 total).
Pipeline of 1-2 hours: generate URLs → download → re-parse → re-analyze →
synthesize new `LEARNED_CONVENTIONS_FINAL.md`.

**3 options for "what's missing"**:
- (A) **Plan D full**: complete the entire OMR (~938 new sets, 4 additional cohorts).
- (B) **Plan D focused**: only themes underrepresented in current cohorts.
- (C) **Plan D thematic**: user picks 3-5 specific themes.

---

## Quick start

```bash
# Generate demo models with the learned rules
cd generator/
python3 ldraw_gen.py

# Re-analyze the corpus if more MPDs are added
cd analysis/
python3 deep_parse.py    # 2 sets (10252, 10218) — legacy
python3 batch_parse.py   # 100 sets (mpds/*.mpd) — legacy
python3 batch_parse2.py  # 300 sets — legacy
python3 batch_parse3.py  # 532 sets (mpds/*.mpd + mpds_kids/*.mpd + mpds_classic/*.mpd)
```

---

## Project structure

```
.
├── README.md                       ← this file (English)
├── README.es.md                    ← Spanish version (legacy)
├── NEXT_SESSION.md                 ← continuation plan for next session
├── AGENTS.md                       ← agent instructions (English, language policy)
├── STATE.json                      ← persistent project state
├── LDRAW_GUIDE.md                  ← LDraw file format specification
│                                     (file format, primitives, BFC,
│                                     colors, headers, MPD, OMR)
│
├── LEARNED_CONVENTIONS.md          ← LEGACY: analysis of 2 sets
│                                     (10252 Beetle + 10218 Pet Shop).
│                                     Kept for traceability.
├── LEARNED_CONVENTIONS_100.md      ← analysis of 100 80s/90s sets.
├── LEARNED_CONVENTIONS_300.md      ← analysis of 300 sets (80s/90s + kids).
├── LEARNED_CONVENTIONS_532.md      ← CANONICAL: 23 rules (18 + 5 new)
│                                     learned from 532 OMR sets.
│
├── output/
│   └── dashboard.html              ← interactive HTML dashboard
│                                     (open in any browser, offline)
│
├── corpus/
│   ├── ldraw/                      ← full official Parts Library
│   │                                 (pybricks/ldraw mirror, ~28k files)
│   ├── 10252-1.mpd                 ← 2 sets analyzed initially
│   ├── 10218-1.mpd                   (Volkswagen Beetle + Pet Shop)
│   ├── mpds/                       ← 100 MPDs from 80s/90s (6.7 MB)
│   ├── mpds_kids/                  ← 200 MPDs kids (25 MB)
│   ├── mpds_classic/                ← 232 MPDs Plan C classic (8.5 MB)
│   ├── setlist_80s90s.{txt,json}   ← list of 100 sets from 80s/90s
│   ├── setlist_kids.{txt,json}      ← list of 200 kids sets
│   ├── setlist_classic.{txt,json}   ← list of 232 Plan C classic sets
│   ├── plan_c_distribution.json     ← Plan C plan + documented shortfalls
│   └── all_omr_themes.json          ← full catalog of 135 OMR themes
│
├── analysis/
│   ├── parse_omr.py                ← OMR parser level-1 (basic stats)
│   ├── deep_parse.py               ← parser level-2 (2 sets, bigrams,
│   │                                 matrices, deltas, Y-layers)
│   ├── batch_parse.py              ← batch parser (100 sets)
│   ├── batch_parse2.py             ← batch parser 2.0 (300 sets,
│   │                                 cross-cohort)
│   ├── batch_parse3.py             ← batch parser 3.0 (532 sets,
│   │                                 3 cohorts, per_set_stats_532)
│   ├── raw_stats.json              ← stats level-1 (2 sets)
│   ├── deep_stats.json             ← stats level-2 (2 sets)
│   ├── cross_corpus_stats.json     ← global stats (100 sets) [legacy]
│   ├── per_set_stats.json          ← per-set stats (100 sets) [legacy]
│   ├── cross_corpus2_stats.json    ← global stats (532 sets) — 4 cohorts
│   ├── per_set_stats_300.json      ← per-set stats (532 sets)
│   │
│   ├── findings_chaining.md        ← chaining 2 sets [legacy]
│   ├── findings_steps.md           ← STEP cadence (2 sets)
│   ├── findings_custom_parts.md    ← embedded custom parts (2 sets)
│   ├── findings_chaining_100.md    ← cross-corpus chaining (100 sets)
│   ├── findings_themes.md          ← theme conventions (100 sets)
│   ├── findings_evolution.md       ← 80s vs 90s (100 sets)
│   ├── findings_chaining_300.md    ← cross-corpus chaining (300 sets)
│   ├── findings_cohorts.md         ← 80s/90s vs kids (300 sets)
│   ├── findings_themes_300.md      ← theme conventions (300 sets)
│   ├── findings_cohorts_3.md       ← 3 cohorts 80s/90s vs kids vs classic
│   ├── findings_themes_532.md      ← theme conventions (532 sets)
│   │
│   └── findings_*.md               ← all English-doc-friendly analysis
│
└── generator/
    ├── ldraw_gen.py                ← Python model generator
    │                                 (class LdrBuilder, validations,
    │                                  templates per theme, demo)
    ├── demo_town.ldr               ← Town 80s style demo (29 pieces)
    ├── demo_kid.ldr                ← City Modern 2010s style demo (18 pieces)
    ├── demo_classic.ldr            ← sanity check brick 2x4 (1 piece)
    ├── demo_castle_lion_knights.ldr ← Castle demo with reflections (28 pieces)
    ├── demo_space_classic.ldr      ← Space Classic demo (18 pieces)
    └── demo_model.ldr              ← main demo (legacy, 52 pieces)
```

---

## Main documents

| Document | Purpose |
|----------|---------|
| **[LDRAW_GUIDE.md](./LDRAW_GUIDE.md)** | Complete LDraw format spec. What you need to **read/write** `.dat`/`.ldr`/`.mpd` files. |
| **[LEARNED_CONVENTIONS_532.md](./LEARNED_CONVENTIONS_532.md)** | Conventions learned from **532 sets** (108,760 pieces). What you need to **build models the OMR way**. |
| **[LEARNED_CONVENTIONS_300.md](./LEARNED_CONVENTIONS_300.md)** | Previous analysis (300 sets). Kept for traceability. |
| **[LEARNED_CONVENTIONS_100.md](./LEARNED_CONVENTIONS_100.md)** | Previous analysis (100 sets 80s/90s). Kept for traceability. |
| **[LEARNED_CONVENTIONS.md](./LEARNED_CONVENTIONS.md)** | (Legacy) analysis of 2 sets. Kept for traceability. |
| **[NEXT_SESSION.md](./NEXT_SESSION.md)** | Continuation plan for next session. |
| **[analysis/findings_cohorts_3.md](./analysis/findings_cohorts_3.md)** | 3-cohort structural differences. |
| **[analysis/findings_themes_532.md](./analysis/findings_themes_532.md)** | Theme-specific conventions. |
| **[analysis/findings_chaining_300.md](./analysis/findings_chaining_300.md)** | Quantitative chaining detail. |
| **[output/dashboard.html](./output/dashboard.html)** | Interactive HTML dashboard with all stats (open in browser). |
| **[generator/ldraw_gen.py](./generator/ldraw_gen.py)** | Python generator that applies the learned rules. |

---

## The 23 canonical rules (corpus 532)

The 12 rules from the corpus 100 were re-evaluated with 532 sets (3 cohorts). Summary:

- **7 rules confirmed** (R1, R2, R5, R7, R12, R16, R17).
- **8 rules weakened or qualified** (R3 reflections, R4 custom parts, R6 slope signature, R8 Technic, R9 size, R10 BFC, R11 sub-builds, R13 vocabulary).
- **2 rules refuted** (R3 — Space-themed sets spike reflections to 5-21%, R10 — BFC is NOT monotonic with time).
- **5 new rules** (R19-R23) — focused on Space-themed patterns.

The **3 most important rules** that changed with corpus 532:

| # | Canonical rule | Corpus 532 evidence |
|---|----------------|---------------------|
| R1 | Y-layers are multiples of 8 | ✅ 100% top-15 canonical |
| R2 | X/Z deltas are multiples of 20 | ✅ 100% top-15 canonical |
| R3 | Reflections < 0.3% | ❌ 1.345% in corpus 532 — **Space-themed spike to 5-21%** |
| **R19** 🆕 | Space-themed sets have 5-21% reflections | Classic Space 21.14%, Unitron 13.95% |
| **R20** 🆕 | `756.dat` (Technic 16×32 baseplate) is Space signature | 1,627 uses, enters top-8 global |
| **R23** 🆕 | Y = +8 LDU = antennas/masts | 1,389 pieces (signed by Space-themed) |

See **[LEARNED_CONVENTIONS_532.md §0](./LEARNED_CONVENTIONS_532.md)** for the detailed 23 rules.

---

## Generator

`generator/ldraw_gen.py` (1,161 lines, stdlib-only) applies the 23 learned rules. It has 5 validated demos:

| Demo | Theme | Pieces | STEPs | Files | Reflections | Validation |
|------|------|-------:|------:|------:|-----------:|------------|
| `demo_town.ldr` | Town 80s | 29 | 12 | 9 | 0 | 0e/0w |
| `demo_kid.ldr` | City Modern 2010s | 18 | 7 | 6 | 0 | 0e/0w |
| `demo_classic.ldr` | Sanity check brick 2×4 | 1 | 1 | 1 | 0 | 0e/0w |
| `demo_castle_lion_knights.ldr` | Castle with reflections | 28 | 9 | 7 | 4 | 0e/0w |
| `demo_space_classic.ldr` | Space Classic | 18 | 8 | 6 | 0 | 0e/0w |

Each demo has distinct `!THEME` and `!KEYWORDS` to identify the cohort.
Metrics are compared against the corpus 532 average (204 pieces/set, 1.34% reflections).

---

## Corpus statistics (532 sets)

| Metric | 80s/90s | Kids | Classic | **All 532** |
|--------|--------:|-----:|--------:|-----------:|
| Sets | 100 | 200 | 232 | **532** |
| Total pieces | 18,670 | 42,947 | 47,143 | **108,760** |
| Pieces/set (mean) | 186.7 | 214.7 | 203.2 | **204.4** |
| Sub-builds/set | 8.39 | 7.68 | **10.13** | 8.88 |
| Custom parts | 112 | 818 | 107 | **1,037** |
| Custom ratio | 0.6% | 1.9% | **0.2%** | 0.95% |
| BFC CERTIFY | 21% | 36.5% | **16.4%** | 24.8% |
| **Reflections (det<0)** | 0.27% | 0.25% | **2.77%** | **1.35%** |

**Themes** (top-10 in 532): Town > Classic Town (109 sets combined) · Train > 9V (14) · Castle Lion Knights (10) · Friends (17) · Pirates (7) · Model Team (5) · Creator 3-in-1 (14) · Train 12V (8) · M:Tron (8) · Castle (1).

**Decades** (532 sets): 1980s (140) · 1990s (165) · 2000s (84) · 2010s (126) · 2020s (17).

---

## Limitations

1. **532 sets** out of 1,470 in OMR — diverse sample but not exhaustive (36.2% of OMR).
2. **OMR incomplete**: missing many sets (Ninjago, Star Wars post-2010, etc.); this skews analyzed themes.
3. **Plan C shortfall**: 24 themes kept documented shortfall in `corpus/plan_c_distribution.json`.
4. **Pirates outlier**: 6286 Skull's Eye Schooner (2,834 pieces) + 6285 Black Seas Barracuda (2,975 pieces) = 91.9% of Pirates theme.
5. **BFC CERTIFY** still low (24.8%) — OMR editorial bias.
6. **No TEXMAP/texture analysis** — many modern sets use PNG textures.
7. **No nested sub-build analysis** (hierarchy within MPD).
8. **No comparison with MOCs** (non-OMR community may have different conventions).

---

## Next steps suggested

- Include Technic sets from 80s/90s to quantify Technic influence (would be a 4th cohort).
- Compare OMR vs MOCs to validate universality.
- Analyze textures (TEXMAP) in modern sets.
- Structural clustering to detect recurring sub-assemblies.
- Train a language model on the 108,760 instances.
