# LDraw OMR — Analysis, Documentation, and Generator

Project to understand the LDraw file format (open standard for LEGO CAD) and
learn LEGO modeling conventions by analyzing official models in the OMR
(Official Model Repository).

**Corpus**: **1,438 OMR sets** (534,152 pieces) across eight cohorts:
- 100 sets from 80s/90s (non-Technic) — legacy.
- 200 "kids" sets (small/affordable, post-1985) — legacy.
- 232 "classic" sets (Plan C: uniform distribution across 49 pre-2000 themes) — legacy.
- **287 sets Modern** (post-2000 official: City, Creator, Friends, Racers, Fabuland).
- **175 sets Technic** (Technic, Expert Builder, Universal Building Set, Mindstorms, Star Wars Technic).
- **165 sets Specialty** (Brickheadz, Architecture, Modular Buildings, Ideas, Icons, Promotional).
- **121 sets Licensed** (Star Wars, Harry Potter, Elves, Mixels, Pharaoh's Quest, Speed Champions).
- **158 sets Classic Gaps** (filling pre-2000 themes underrepresented in legacy cohorts).

This represents **97.8% of the OMR's 1,470 sets** (32 sets returned 404 from OMR and were skipped).

---

## ⚡ RESUME FROM HERE (next session)

If you want to continue the corpus, read first:
- **[STATE.json](./STATE.json)** — persistent project state (what's there, what's missing).

The corpus is now nearly complete (1,438/1,470 sets). Remaining gaps are 32 archived/renamed MPDs (404 responses). To go further:

- (A) **Try harder on the 32 missing sets** — search Livewire API for archived MPD filenames.
- (B) **Re-scrape OMR** to catch any newly added sets (sets get added monthly).
- (C) **Pivot to other tasks**: TEXMAP analysis, MOC comparison, sub-build hierarchy, language model training.

---

## Quick start

```bash
# Generate demo models with the learned rules
cd generator/
python3 ldraw_gen.py

# Re-analyze the corpus if more MPDs are added
cd /home/user/Projects/ldraw
python3 analysis/batch_parse4.py    # 1,438 sets (8 cohorts)
python3 analysis/batch_parse3.py    # 532 sets (legacy, 3 cohorts)
```

---

## Project structure

```
.
├── README.md                       ← this file (English)
├── README.es.md                    ← Spanish version (legacy)
├── AGENTS.md                       ← agent instructions (English, language policy)
├── STATE.json                      ← persistent project state
├── LDRAW_GUIDE.md                  ← LDraw file format specification
│                                     (file format, primitives, BFC,
│                                     colors, headers, MPD, OMR)
│
├── LEARNED_CONVENTIONS.md          ← LEGACY: analysis of 2 sets (kept for traceability)
├── LEARNED_CONVENTIONS_100.md      ← legacy: 100 80s/90s sets
├── LEARNED_CONVENTIONS_300.md      ← legacy: 300 sets (80s/90s + kids)
├── LEARNED_CONVENTIONS_532.md      ← legacy: 23 rules from 532 sets
├── LEARNED_CONVENTIONS_1438.md     ← CANONICAL: 29 rules (23 carried + 9 new)
│                                     learned from 1,438 OMR sets (Plan D complete).
│
├── output/
│   └── dashboard.html              ← interactive HTML dashboard (open in browser)
│
├── corpus/
│   ├── ldraw/                      ← full official Parts Library mirror
│   ├── 10252-1.mpd                 ← 2 sets analyzed initially (Beetle + Pet Shop)
│   ├── 10218-1.mpd
│   ├── mpds/                       ← 100 MPDs from 80s/90s (legacy)
│   ├── mpds_kids/                  ← 200 MPDs kids (legacy)
│   ├── mpds_classic/               ← 232 MPDs Plan C classic (legacy)
│   ├── mpds_modern/                ← 287 MPDs modern official (Plan D)
│   ├── mpds_technic/               ← 175 MPDs Technic (Plan D)
│   ├── mpds_specialty/             ← 165 MPDs specialty/collector (Plan D)
│   ├── mpds_licensed/              ← 121 MPDs licensed franchises (Plan D)
│   ├── mpds_classic_gaps/          ← 158 MPDs classic gaps (Plan D)
│   ├── setlist_*.{txt,json}        ← one setlist per cohort
│   ├── plan_c_distribution.json    ← Plan C plan + documented shortfalls
│   └── all_omr_themes.json         ← full catalog of 135 OMR themes
│
├── analysis/
│   ├── batch_parse.py              ← legacy parser (100 sets)
│   ├── batch_parse2.py             ← legacy parser (300 sets)
│   ├── batch_parse3.py             ← legacy parser (532 sets)
│   ├── batch_parse4.py             ← CURRENT parser (1,438 sets, 8 cohorts)
│   ├── cross_corpus2_stats.json    ← legacy global stats (532 sets)
│   ├── cross_corpus3_stats.json    ← CURRENT global stats (1,438 sets, 8 cohorts)
│   ├── per_set_stats_1438.json     ← CURRENT per-set stats (1,438 sets)
│   ├── findings_chaining_1438.md   ← chaining patterns corpus 1,438
│   ├── findings_cohorts_themes_1438.md ← cohort/theme analysis corpus 1,438
│   └── findings_*.md               ← all prior findings (kept for traceability)
│
└── generator/
    ├── ldraw_gen.py                ← Python model generator (1,161 lines, stdlib-only)
    ├── demo_town.ldr
    ├── demo_kid.ldr
    ├── demo_classic.ldr
    ├── demo_castle_lion_knights.ldr
    ├── demo_space_classic.ldr
    ├── demo_technic.ldr            ← Plan D new (technic beam + pin idiom)
    └── demo_brickheadz.ldr         ← Plan D new (1x1 round tile display idiom)
```

---

## Main documents

| Document | Purpose |
|----------|---------|
| **[LDRAW_GUIDE.md](./LDRAW_GUIDE.md)** | Complete LDraw format spec. What you need to **read/write** `.dat`/`.ldr`/`.mpd` files. |
| **[LEARNED_CONVENTIONS_1438.md](./LEARNED_CONVENTIONS_1438.md)** | **Canonical** conventions from 1,438 sets (534k pieces). 29 rules. |
| **[LEARNED_CONVENTIONS_532.md](./LEARNED_CONVENTIONS_532.md)** | Legacy conventions from 532 sets. 23 rules. |
| **[LEARNED_CONVENTIONS_300.md](./LEARNED_CONVENTIONS_300.md)** | Previous analysis (300 sets). Kept for traceability. |
| **[analysis/findings_chaining_1438.md](./analysis/findings_chaining_1438.md)** | Chaining patterns, bigrams, deltas (1,438 sets). |
| **[analysis/findings_cohorts_themes_1438.md](./analysis/findings_cohorts_themes_1438.md)** | Per-cohort + per-theme analysis (1,438 sets). |
| **[STATE.json](./STATE.json)** | Persistent project state. |
| **[output/dashboard.html](./output/dashboard.html)** | Interactive HTML dashboard (open in browser). |
| **[generator/ldraw_gen.py](./generator/ldraw_gen.py)** | Python generator that applies the 29 learned rules. |

---

## The 29 canonical rules (corpus 1,438)

The 23 rules from corpus 532 were re-evaluated with 1,438 sets across 8 cohorts. Summary:

- **20 rules confirmed or extended** (R1-R13, R16, R17, R19-R23).
- **3 rules weakened or refuted** by Technic:
  - R1 (Y = multiples of 8) **partially refuted** by Technic half-brick values (±10 LDU).
  - R2 (X/Z deltas = multiples of 20) extends: 20-unit X grid is 3× more common than (60,0,0).
  - R3 (reflections <0.3%) refuted by Technic > Competition at 33%.
- **9 new rules** (R24-R32) from the larger corpus:
  - **R24** Technic is BFC CERTIFY champion (78.9% vs corpus 35.5%).
  - **R25** Technic sub-build density (29.96/set = 2.55× System).
  - **R26** Pin-into-beam is the universal Technic chaining bigram.
  - **R27** Brickheadz `22885.dat` + `3023.dat` signature (display idiom).
  - **R28** Modular Buildings roof slope trio.
  - **R29** Reflections concentrate in Space + Technic Competition; Star Wars UCS = 0%.
  - **R30** 20-unit X grid dominates (17,714 = 3× the (60,0,0) count).
  - **R31** Sub-builds scale with complexity, not era.
  - **R32** Half-brick Y values are Technic-specific.

The **5 most important changes** from corpus 532 to 1,438:

| # | Canonical rule | Corpus 1,438 evidence |
|---|----------------|----------------------|
| R1 | Y-layers are multiples of 8 | ⚠️ Holds for 7/8 cohorts. **Fails for Technic** (±10 LDU half-bricks). |
| R2 | X/Z deltas are multiples of 20 | ✅ Confirmed + extended: 20-unit X grid is the dominant stride. |
| R3 | Reflections < 0.3% | ❌ 0.687% corpus 1,438. **Technic Competition 33%** rivals Space. |
| **R24** 🆕 | Technic drives BFC CERTIFY | 138/175 = 78.9% Technic, lifts corpus from 24.8% → 35.5%. |
| **R26** 🆕 | Pin-into-beam is Technic's signature | `2780.dat ↔ 6558.dat` = 1,277+ pairs in technic cohort. |
| **R29** 🆕 | Reflections concentrate in Space + Tech Competition | Classic Space 18.08%, Technic Competition 33%, Star Wars UCS 0%. |

See **[LEARNED_CONVENTIONS_1438.md §0](./LEARNED_CONVENTIONS_1438.md)** for the detailed 29 rules.

---

## Generator

`generator/ldraw_gen.py` (1,161 lines, stdlib-only) applies the 29 learned rules. It has **7 validated demos**:

| Demo | Theme | Validation |
|------|-------|------------|
| `demo_town.ldr` | Town 80s | 0e/0w |
| `demo_kid.ldr` | City Modern 2010s | 0e/0w |
| `demo_classic.ldr` | Sanity check brick 2×4 | 0e/0w |
| `demo_castle_lion_knights.ldr` | Castle with reflections | 0e/0w |
| `demo_space_classic.ldr` | Space Classic | 0e/0w |
| `demo_technic.ldr` | Technic (beam + pin idiom) | 0e/0w |
| `demo_brickheadz.ldr` | Brickheadz (1×1 round display) | 0e/0w |

Each demo has distinct `!THEME` and `!KEYWORDS` to identify the cohort.
Metrics are compared against the corpus 1,438 average (371.6 pieces/set, 0.687% reflections).

---

## Corpus statistics (1,438 sets)

| Cohort | Sets | Pieces | Mean p/set | BFC CERTIFY | Reflections | Custom parts |
|--------|-----:|-------:|-----------:|------------:|------------:|-------------:|
| 80s/90s | 100 | 18,670 | 186.7 | 21.0% | 0.27% | 112 |
| Kids | 200 | 42,947 | 214.7 | 36.5% | 0.25% | 818 |
| Classic | 232 | 47,143 | 203.2 | 16.4% | 2.77% | 107 |
| **Modern** | 287 | 114,904 | 400.4 | 27.5% | **0.04%** | 769 |
| **Technic** | 175 | 169,839 | **970.5** | **78.9%** | 0.68% | 1,691 |
| **Specialty** | 165 | 63,592 | 385.4 | 36.4% | 0.18% | 351 |
| **Licensed** | 121 | 45,227 | 373.8 | 49.6% | 0.55% | 531 |
| **Classic_gaps** | 158 | 31,830 | 201.5 | 25.9% | 2.01% | 91 |
| **All 1,438** | **1,438** | **534,152** | **371.4** | **35.5%** | **0.687%** | **4,470** |

**Themes** (top-10 in 1,438): Town > Classic Town (217) · Technic (158) · Racers (76) · Brickheadz (76) · Star Wars (64) · Creator 3-in-1 (60) · Fabuland (42) · Architecture (36) · Space > Classic Space (36) · Train > 9V (34).

**Decades** (1,438 sets): 1970s (12) · 1980s (155) · 1990s (188) · 2000s (300) · 2010s (560) · 2020s (223).

---

## Limitations

1. **1,438/1,470 OMR sets** — 97.8% complete. 32 sets returned 404 (archived/renamed).
2. **No TEXMAP/texture analysis** — many modern sets use PNG textures.
3. **No nested sub-build analysis** (hierarchy within MPD).
4. **No comparison with MOCs** (non-OMR community may have different conventions).
5. **Livewire search has limitations**: some sets don't appear in paginated `/omr/sets?page=N`.

---

## Next steps suggested

- Recover the 32 missing 404'd sets via Livewire API deep search.
- Analyze textures (TEXMAP) in modern sets.
- Structural clustering to detect recurring sub-assemblies.
- Train a language model on the 534k instances.
- Re-scrape OMR monthly to catch newly added sets.
