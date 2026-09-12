# Findings — Cohorts & Themes (1 438 sets OMR)

> Scope: 1 438 sets · 534 152 pieces · 20 074 sub-builds · 4 470 embedded custom parts · 510 BFC CERTIFY · **0.687 % reflejos**.
> Corpus distribution across 8 cohorts: `80s90s` (100) + `kids` (200) + `classic` (232) + `modern` (287) + `technic` (175) + `specialty` (165) + `licensed` (121) + `classic_gaps` (158).
> Source: `analysis/per_set_stats_1438.json` + `analysis/cross_corpus3_stats.json` + `corpus/all_omr_themes.json`.
> Carry-over: rules R1-R23 from `LEARNED_CONVENTIONS_532.md` are preserved; this document **extends** with R24-R30 derived from the larger corpus.

---

## 1. Cohort overview (1 438 sets)

| Cohort | Sets | Pieces | Pps | Steps/set | Sub-builds/set | Custom + Sub + Hi | BFC CERTIFY | Neg-det | Top piece | Top delta |
|--------|----:|------:|----:|---------:|---------------:|------------------:|------------:|--------:|-----------|-----------|
| `80s90s` | 100 | 18 670 | **186.7** | 19.9 | 8.39 | 112 (0.60 %) | 21 / 21.0 % | 50 / 0.268 % | `4-4cyli.dat` | (0, 0, 0) |
| `kids` | 200 | 42 947 | **214.7** | 29.8 | 7.67 | 818 (1.90 %) | 73 / 36.5 % | 107 / 0.249 % | `4-4cyli.dat` | (0, 0, 0) |
| `classic` | 232 | 47 143 | **203.2** | 22.6 | 10.13 | 107 (0.23 %) | 38 / 16.4 % | 1 306 / **2.770 %** | `3023.dat` | (0, 0, 0) |
| `modern` | 287 | 114 904 | **400.4** | 70.5 | 14.38 | 769 (0.67 %) | 79 / 27.5 % | 42 / **0.037 %** | `3023.dat` | (0, **-8**, 0) |
| `technic` | 175 | 169 839 | **970.5** | 114.9 | **29.96** | 1 691 (1.00 %) | **138 / 78.9 %** | 1 162 / 0.684 % | `2780.dat` | (0, 0, 0) |
| `specialty` | 165 | 63 592 | **385.4** | 69.8 | 16.63 | 351 (0.55 %) | 60 / 36.4 % | 112 / 0.176 % | **`98138.dat`** | (**20**, 0, 0) |
| `licensed` | 121 | 45 227 | **373.8** | 82.0 | 16.21 | 531 (1.17 %) | 60 / 49.6 % | 248 / 0.548 % | `3023.dat` | (20, 0, 0) |
| `classic_gaps` | 158 | 31 830 | **201.5** | 19.3 | 8.06 | 91 (0.29 %) | 41 / 25.9 % | 641 / **2.014 %** | `3004.dat` | (0, 0, 0) |
| **All 1 438** | **1 438** | **534 152** | **371.5** | 54.2 | 13.96 | 4 470 (0.84 %) | **510 / 35.5 %** | **3 668 / 0.687 %** | `4-4cyli.dat` | (20, 0, 0) |

**Three outliers vs. corpus 532**:

1. **Technic (175 sets, 32 % of all pieces)** — pps 970.5 = **5× the 532-doc average (204)**; sub-builds 29.96 = **3.4× classic's 10.13**; BFC CERTIFY 78.9 % = **3× the 532-doc legacy rate (24.8 %)**.
2. **Specialty (165 sets)** — top piece is `98138.dat` (Tile 1×1 with groove, Brickheadz-style) at 7 622 units = 11.99 % of the cohort — a piece that did **not appear in the legacy top-30** and now sits at #9 globally (2.06 %).
3. **classic_gaps (158 sets)** — top piece is `3004.dat` (Brick 1×2), but `756.dat` (Baseplate 16×32 Technic) appears as a self-bigram with 624 counts, mirroring the Classic cohort Space-ship signature.

**Sub-builds ranking** (new in 1 438): `technic` 29.96 > `specialty` 16.63 > `licensed` 16.21 > `modern` 14.38 > `classic` 10.13 > `80s90s` 8.39 > `classic_gaps` 8.06 > `kids` 7.67.

**Neg-det ranking**: `classic` 2.77 % > `classic_gaps` 2.01 % > `technic` 0.68 % > `licensed` 0.55 % > `kids` 0.25 % > `80s90s` 0.27 % > `specialty` 0.18 % > `modern` 0.04 %. The classic_gaps result (2.01 %) **re-confirms R19** — pre-2000 Space-themed sets carry the reflection phenomenon beyond the legacy Plan C corpus.

---

## 2. Theme taxonomy (1 438 corpus vs. all_omr_themes.json)

The corpus covers **130 distinct `theme_full` values** (1 438 sets), against the **135 themes catalogued** in `corpus/all_omr_themes.json` (1 470 sets indexed by the OMR). Missing themes (5): `The LEGO Batman Movie`, `Ninjago > Spinjitzu`, `Collectible Minifigures`, `Dimensions` (partial), `Minecraft` (partial — only 4 of 60+ sets).

### Top-15 themes by piece count (1 438 corpus)

| # | Theme | Pieces | Sets | BFC CERTIFY | Neg-det | Cohorts | Years |
|--:|-------|------:|-----:|------------:|--------:|---------|-------|
| 1 | **Technic** | **152 331** | 155 | 127 (81.9 %) | 0.17 % | technic | 1983-2021 |
| 2 | Creator > Creator Expert | 30 948 | 20 | 17 (85 %) | 0.00 % | modern | 2003-2020 |
| 3 | Town > Classic Town | 21 096 | 124 | 25 | 0.34 % | kids / classic_gaps | 1978-1997 |
| 4 | Modular Buildings | 25 127 | 11 | 11 (100 %) | 0.17 % | modern | 2007-2022 |
| 5 | Icons | 18 786 | 8 | 8 (100 %) | 0.00 % | modern | 2020-2025 |
| 6 | Creator > Creator 3-in-1 | 16 726 | 50 | 11 | 0.00 % | kids/modern | 2006-2019 |
| 7 | Architecture | 15 943 | 36 | 8 | 0.00 % | specialty | 2008-2019 |
| 8 | Star Wars > UCS | 14 754 | 12 | 9 | 0.76 % | licensed | 2000-2018 |
| 9 | LEGO Ideas and CUUSOO | 13 880 | 12 | 8 | 0.76 % | specialty | 2015-2021 |
| 10 | Star Wars | 13 241 | 64 | 16 | 0.74 % | 80s90s/lic | 1999-2020 |
| 11 | Brickheadz | 10 889 | 76 | 27 (35.5 %) | **0.05 %** | specialty | 2016-2021 |
| 12 | Classic Town (Plan C tagged) | 10 002 | 73 | 16 | 0.34 % | classic | 1978-1997 |
| 13 | LEGO Art | 10 703 | 1 | 1 | 0.00 % | specialty | 2021 |
| 14 | Technic > Star Wars | 10 702 | 3 | 3 | 0.00 % | technic | 2000-2002 |
| 15 | Racers | 9 890 | 76 | 1 | 0.00 % | modern | 2004-2012 |

**Note on "Town > Classic Town"** — the corpus uses two near-identical theme strings: `Town > Classic Town` (124 sets, used by 80s90s/kids/classic_gaps cohorts) and `Classic Town` (73 sets, used by the Plan C `classic` cohort). Combined they form **197 sets, 31 098 pieces** — the second-largest theme by any measure. They are functionally the same theme but were tagged differently across parser versions.

**Top-10 (without dedup) = 322 832 pieces = 60.4 % of 534 152 corpus pieces.** The single Technic theme (155 sets) holds **28.5 % of the entire corpus piece count** by itself. After deduping Town variants, top-10 = 332 834 = 62.3 %.

### Top-15 themes by set count (1 438 corpus)

| # | Theme | Sets | Pieces |
|--:|-------|----:|------:|
| 1 | Town > Classic Town + Classic Town (combined) | **197** | 31 098 |
| 2 | Technic | 155 | 152 331 |
| 3 | Racers | 76 | 9 890 |
| 4 | Brickheadz | 76 | 10 889 |
| 5 | Star Wars | 64 | 13 241 |
| 6 | Creator > Creator 3-in-1 | 50 | 16 726 |
| 7 | Town (modern) | 42 | 7 947 |
| 8 | Fabuland | 41 | 1 346 |
| 9 | Architecture | 36 | 15 943 |
| 10 | Creator | 33 | 1 008 |
| 11 | Friends | 29 | 5 800 |
| 12 | Space > Classic Space | 27 | 4 319 |
| 13 | Train > 9V + 9V (combined) | **24** | 6 826 |
| 24 | Creator > Designer Sets | 22 | 1 162 |
| 15 | Creator > Creator Expert | 20 | 30 948 |

### Theme-category recap from `corpus/all_omr_themes.json` (1 470 sets indexed)

| Category | Themes | Sets | % of OMR |
|----------|------:|-----:|--------:|
| `official_classic` (pre-2000 System) | 49 | 545 | 37 % |
| `official_modern` (post-2000 non-franchise) | 37 | 408 | 28 % |
| `licensed` (franchise IPs) | ~25 | ~280 | 19 % |
| `technic` (Technic + Mindstorms) | 6 | 175 | 12 % |
| `specialty` (Brickheadz, Architecture, Ideas, Seasonal, etc.) | ~18 | ~62 | 4 % |

The 1 438 corpus covers **1 350 of 1 470 sets (91.8 %)** in `official_classic` + `official_modern` + `technic` + most of `licensed` and `specialty`. Shortfalls: most Ninjago (5 of ~50), Minecraft (4 of 60+), Ideas pre-2015, and Modular Buildings pre-2007.

---

## 3. Decade distribution per cohort

| Cohort | 1960s | 1970s | 1980s | 1990s | 2000s | 2010s | 2020s | Span |
|--------|----:|----:|----:|----:|----:|----:|----:|------|
| `80s90s` | — | — | 25 (25 %) | 75 (75 %) | — | — | — | **1980-1999** |
| `kids` | — | — | 47 (24 %) | 41 (21 %) | 44 (22 %) | 66 (33 %) | 2 (1 %) | **1985-2020** |
| `classic` | 15 (6 %) | 68 (29 %) | 84 (36 %) | 63 (27 %) | 2 (1 %) | — | — | **1966-2004** |
| `modern` | 2 (1 %) | 13 (5 %) | 15 (5 %) | — | 125 (44 %) | 118 (41 %) | 14 (5 %) | **1969-2025** |
| `technic` | — | 7 (4 %) | 14 (8 %) | 28 (16 %) | 23 (13 %) | 81 (46 %) | 22 (13 %) | **1977-2021** |
| `specialty` | — | 4 (2 %) | — | — | 6 (4 %) | 125 (76 %) | 30 (18 %) | **1975-2025** |
| `licensed` | — | — | — | 5 (4 %) | 41 (34 %) | 66 (55 %) | 9 (7 %) | **1999-2020** |
| `classic_gaps` | — | 9 (6 %) | 80 (51 %) | 60 (38 %) | 4 (3 %) | 5 (3 %) | — | **1979-2010** |
| **All** | 17 (1 %) | 101 (7 %) | 265 (18 %) | 272 (19 %) | 245 (17 %) | 461 (32 %) | 77 (5 %) | **1966-2025** |

**Era coverage matrix**:

- `80s90s` — narrow 20-year window, only pre-2000 (Plan A legacy).
- `kids` — broadest pre-2000 + modern span (4 decades).
- `classic` — Plan C, 1966-2004 (39-year window, intentional).
- `modern` — concentrated 2000s-2020s (43.6 % + 41.1 % + 4.9 % = 89.6 %).
- `technic` — heaviest in 2010s (46.3 %), but reaches back to 1977 (early Expert Builder).
- `specialty` — overwhelmingly 2010s+ (76 % + 18 % = 94 %). **No 1980s-1990s coverage** because Brickheadz (2016-), Architecture (2008-), and Ideas (2008-) are post-2007.
- `licensed` — entirely post-1999 (no Star Wars pre-Episode I).
- `classic_gaps` — fixes the Space/Boat/Train/Launch Command shortfall from Plan C; 89 % pre-2000.

**Decade-mode finding (R24 new)**: Specialty is the only cohort whose **mode is 2010s** (125/165 sets). All other cohorts have mode in 1980s/1990s/2000s. This is structural, not an artifact of corpus selection.

---

## 4. BFC CERTIFY: 132/532 → 510/1 438 (24.8 % → 35.5 %)

### Per-cohort BFC CERTIFY

| Cohort | Sets | BFC | Ratio | vs legacy 532 (24.8 %) |
|--------|----:|----:|------:|------------------------|
| `technic` | 175 | **138** | **78.9 %** | **+54.1 pp** (driver) |
| `licensed` | 121 | 60 | 49.6 % | +24.8 pp |
| `kids` | 200 | 73 | 36.5 % | +11.7 pp |
| `specialty` | 165 | 60 | 36.4 % | +11.6 pp |
| `modern` | 287 | 79 | 27.5 % | +2.7 pp |
| `classic_gaps` | 158 | 41 | 25.9 % | +1.1 pp |
| `80s90s` | 100 | 21 | 21.0 % | -3.8 pp |
| `classic` | 232 | 38 | 16.4 % | **-8.4 pp** |

**Diagnosis**: the +10.7-pp jump (24.8 → 35.5 %) is **driven by Technic**, which alone contributes 138/510 = 27.1 % of all BFC CERTIFY sets in the 1 438 corpus. Without Technic, the corpus-wide BFC ratio would be 372/1 263 = 29.4 % — only +4.6 pp above the legacy 24.8 %.

### BFC CERTIFY by theme (top reflectors)

| Theme | Sets | BFC | Ratio |
|-------|----:|----:|------:|
| **Modular Buildings** | 11 | 11 | **100.0 %** |
| **Icons** | 8 | 8 | 100.0 % |
| **LEGO Art** | 1 | 1 | 100.0 % |
| **Technic** | 155 | 127 | **81.9 %** |
| **Technic > Star Wars** | 3 | 3 | 100.0 % |
| **Technic > Competition** | 3 | 3 | 100.0 % |
| **LEGO Ideas and CUUSOO** | 12 | 8 | 66.7 % |
| **Star Wars > UCS** | 12 | 9 | 75.0 % |
| Mindstorms | 1 | 1 | 100.0 % |
| **Racers** | 76 | 1 | **1.3 %** (anomaly — explained below) |
| **Brickheadz** | 76 | 27 | **35.5 %** |
| **Architecture** | 36 | 8 | **22.2 %** |
| Friends | 29 | (n/a in this slice) | — |

**Anomaly (R25 new)**: Racers (76 sets, all `modern` cohort, 2004-2012) has **only 1 / 76 BFC CERTIFY (1.3 %)** despite being a modern post-2000 theme. Diagnosis: OMR contributors in the late 2000s were not yet following BFC convention. Brickheadz (76 sets, 2016+) at 35.5 % reflects the OMR cleanup around 2018.

### BFC CERTIFY by decade

| Decade | Sets | BFC | Ratio |
|--------|----:|----:|------:|
| 1960s | 17 | 8 | **47.1 %** |
| 1970s | 101 | 18 | 17.8 % |
| 1980s | 265 | 87 | **32.8 %** |
| 1990s | 272 | 74 | 27.2 % |
| 2000s | 245 | 45 | **18.4 %** |
| 2010s | 461 | 219 | 47.5 % |
| 2020s | 77 | 59 | **76.6 %** |

**Diagnosis**: BFC CERTIFY ratio is **NOT monotonic with time** across the full corpus. It is:
- High in 1960s (47.1 %) — small N (17 sets), but Technic-era pioneer contributors did use BFC.
- **Dips to 18.4 % in 2000s** — Racers + Friends + Harry Potter era where BFC was not yet community-wide convention.
- Recovers to 47.5 % in 2010s and 76.6 % in 2020s.

**R10 reaffirmed**: BFC CERTIFY is **NOT** simply "more recent = more certified". It tracks **community authoring culture** of the era, not the era itself.

---

## 5. Custom parts / subparts / hi-res embeds

| Cohort | Custom parts | Subparts | Hi-res | Total custom+sub+hires | Pct of cohort | Notes |
|--------|----:|----:|----:|----:|----:|-------|
| `80s90s` | 78 | 34 | 0 | 112 | 0.60 % | Mostly Fabuland + Castle minifigs |
| `kids` | 519 | 292 | 7 | 818 | **1.90 %** | Highest ratio of legacy cohorts |
| `classic` | 76 | 30 | 1 | 107 | **0.23 %** | Lowest — pure classic vocabulary |
| `modern` | 529 | 224 | 16 | 769 | 0.67 % | Stickered tiles, modern minifigs |
| `technic` | **1 080** | **580** | **31** | **1 691** | 1.00 % | Largest absolute custom geometry |
| `specialty` | 239 | 107 | 5 | 351 | 0.55 % | Stickers + Brickheadz prints |
| `licensed` | 354 | 176 | 1 | 531 | 1.17 % | Minifigs, weapons, decorations |
| `classic_gaps` | 89 | 1 | 1 | 91 | 0.29 % | Some Classic-Town minifigs |
| **All 1 438** | **2 964** | **1 444** | **62** | **4 470** | **0.84 %** | (was 1 037 / 0.95 % in 532 doc) |

**Notable (R26 new)**:

- **Technic has 1 691 custom embeds** — 4.7× more than any other cohort in absolute count. This is **Technic > Expert Builder + Technic sub-build stickers** (e.g. `42043-1` has 20 custom parts, `42053-1` has 30).
- **Kids is the highest in ratio (1.90 %)** — Friends + City decorated pieces.
- **classic_gaps subparts are only 1** — these 158 sets are pure System, almost no embedded geometry.
- **Hi-res embeds (62 total)** are concentrated in `modern` (16), `technic` (31), `specialty` (5) — i.e. post-2010 sets use hi-res LDraw parts more often.

---

## 6. Sub-builds (chaining depth) per cohort

| Cohort | Sets | Mean sub-builds/set | Median | Max | Total |
|--------|----:|-------------------:|-------:|----:|------:|
| `technic` | 175 | **29.96** | 14 | (large) | 5 243 |
| `specialty` | 165 | 16.63 | 10 | (large) | 2 744 |
| `licensed` | 121 | 16.21 | 8 | (large) | 1 961 |
| `modern` | 287 | 14.38 | 8 | (large) | 4 128 |
| `classic` | 232 | 10.13 | 5 | (large) | 2 350 |
| `80s90s` | 100 | 8.39 | 4 | (large) | 839 |
| `classic_gaps` | 158 | 8.06 | 4 | (large) | 1 274 |
| `kids` | 200 | 7.67 | 4 | (large) | 1 535 |
| **All 1 438** | — | **13.96** | 6 | — | **20 074** |

**Findings**:

- **Technic's 29.96 sub-builds/set is 4× classic's 10.13** — Technic sets are decomposed into many small mechanical sub-assemblies (axle groups, gear groups, beam sub-frames).
- **Kids is the lowest (7.67)** — City/Friends/Castle modern sets are flat compositions, fewer intermediates.
- **R11 refuted again**: sub-builds do **not** grow monotonically with time. `kids` (mostly post-2000) < `80s90s` (mostly pre-2000). The driver is **theme/genre**, not era.
- **Sub-builds correlate with BFC CERTIFY**: cohorts with more sub-builds also have higher BFC CERTIFY (Technic 29.96 → 78.9 %, kids 7.67 → 36.5 %). Likely a side-effect of contributors who decompose sub-assemblies also adding BFC metadata.

---

## 7. Per-theme standout piece (top-15 themes by sets)

For each top theme, the most over-represented piece = `theme-frequency / corpus-frequency` (lift).

| Theme | Standout piece | Theme-fraction | Corpus-fraction | Lift | Notes |
|-------|----------------|---------------:|----------------:|-----:|-------|
| Town > Classic Town | **`754.DAT`** (Baseplate 16×16) | 2.04 % | 0.11 % | **18.8×** | 302 uses in 124 sets — Classic-Town signature |
| Technic | **`u9190.dat`** (Beam 1×2 Technic) | 1.90 % | 0.58 % | 3.3× | Beam vocabulary |
| Racers | **`51719.dat`** (Wheel base) | 4.64 % | 0.09 % | **49.8×** | Racers wheels dominate |
| Brickheadz | **`22885.dat`** (Brickheadz eye tile) | 11.70 % | 0.32 % | **36.1×** | Brickheadz stand |
| Classic Town | **`3005.DAT`** (Brick 1×1) | 0.96 % | 0.08 % | 12.5× | (Legacy "Town" sub-theme) |
| Star Wars | **`2654.dat`** (Dish 4×4) | 0.98 % | 0.08 % | 12.5× | Death Star dish |
| Creator 3-in-1 | **`3037.dat`** (Slope 45° 2×2) | 1.55 % | 0.12 % | 12.8× | Modern building slope |
| Town | **`4216.dat`** (Baseplate 8×16) | 0.88 % | 0.06 % | 13.6× | (Modern Town) |
| Fabuland | **`6264.dat`** (Fabuland roof) | 1.52 % | 0.00 % | **319.1×** | Fabuland-specific |
| Architecture | **`50746.dat`** (Ribbed tile) | 1.35 % | 0.11 % | 12.6× | Skyline ribbing |
| Creator | **`2436b.dat`** (Bracket 1×2-1×4) | 0.80 % | 0.01 % | 54.7× | Vintage Creator |
| Friends | **`6191.dat`** (Friends slope) | 1.05 % | 0.02 % | **66.7×** | R17 confirmed |
| Creator Designer Sets | **`44567.dat`** (Windscreen 4×4) | 0.94 % | 0.01 % | **169.9×** | Café Modular style |
| Creator Expert | **`3711.dat`** (Plate 1×4 Technic) | 1.65 % | 0.13 % | 12.5× | Modular chassis |
| Western | **`30136.dat`** (Brick 1×2 with studs) | 7.04 % | 0.18 % | **38.3×** | Western-specific wall |
| Star Wars > UCS | **`72504.dat`** (UCS plate) | 0.2 % | 0.00 % | 47.9× | UCS stand tile |
| LEGO Ideas / CUUSOO | **`92411.dat`** (WALL-E panel) | 0.1 % | 0.00 % | 48.2× | WALL-E-specific |

**Three signature discoveries (R27-R29 new)**:

- **R27**: `22885.dat` (Brickheadz eye tile) is the strongest **theme-specific piece** of any modern theme — 11.70 % of all Brickheadz pieces, 36× the corpus rate.
- **R28**: `51719.dat` (Racers wheel base) at **49.8× lift** — Racers almost exclusively uses this wheel.
- **R29**: `6264.dat` (Fabuland roof) at **319.1× lift** is the single most theme-distinctive piece — Fabuland uses almost no shared vocabulary with System.

---

## 8. New findings beyond the 532 doc

### R24: Technic dominates the corpus (28.5 % of all pieces from a single theme)

155 Technic sets contribute 152 331 pieces = 28.5 % of the entire 1 438 corpus. This **biases every corpus-wide statistic** toward Technic vocabulary. Removing Technic:
- pps drops from 371.5 to **288.5**.
- Top-10 coverage shifts from 29.96 % to **33.74 %** (Technic's `2780`, `166`, `u9218`, `77`, `6558`, `axlehol8` are heavy in the top-10; without them System pieces concentrate).
- BFC CERTIFY drops from 35.5 % to **29.45 %** (372/1 263).
- Top-10 without Technic: `3023`, `6141`, `3024`, `3004`, `4-4cyli`, `98138`, `3710`, `3005`, `3069b`, `3020` — pure System vocabulary.

### R25: Technic > Competition has 33 % reflections (sub-theme with massive mirroring)

3 sets (8202-1, 8245-1, 8257-1) — all 1998 Mindstorms-vs-Robots competitor sets. `8245-1` Robot's Revenge alone has 495 reflections; `8257-1` Cyber Strikers has 407. Combined: 902 / 2 728 = **33.06 % neg-det ratio**, lifting the entire Technic cohort's neg-det ratio from 0.17 % (Technic proper) to 0.68 % (Technic cohort average).

This **doubles the known reflection phenomenon** beyond R19 (Classic Space Unitron/Blacktron). The Technic > Competition mirror pattern is **physical part-mirroring**, not matrix mirroring — competitors' brick shapes are structurally symmetrical.

### R26: Technic Y-layers use non-canonical values (-20, -10, +20, +10)

Top Technic Y-layers:
- `Y=0` 32 606 (base plane)
- `Y=-20` 8 239 — half-plate LDU (8 LDU plate + 12 LDU stud offset)
- `Y=-40` 6 466 — full beam height (20 LDU)
- `Y=+20` 5 045 — beam-above-base
- `Y=-60` 3 844 — 3 beams stacked
- **`Y=-10`** 2 204 — half-beam sub-LDU offset
- **`Y=+10`** 1 987 — same on positive axis

Y-layers **-10 and +10 are Technic-specific** and account for ~13 % of all Technic Y-positions. The classic System "R1" rule (Y multiple of 8) **does not hold** for Technic.

### R27: Technic > Star Wars (3 sets) is 100 % BFC + 0 reflections + 10 702 pieces

3 sets (8001-1 Battle Droid, 8002-1 Destroyer Droid, 8007-1 AT-AT) at **10 702 pieces**. Top piece `6141.dat` (Plate 1×1 round), then `3710.dat` (Plate 1×4). These are large System-with-Technic-connections hybrids.

### R28: Specialty's top piece `98138.dat` (Tile 1×1 round groove) is 12 % of all specialty pieces

7 622 uses out of 63 592 (11.99 %). This is **Brickheadz + Architecture + LEGO Art** almost exclusively. The piece **enters the global top-10 at #9** (2.06 %) — it did not exist in the 532-doc top-30.

### R29: Technic top piece `2780.dat` (Technic Pin) is **8.85 %** of Technic cohort (15 038 uses)

15 038 / 169 839 = 8.85 % — by far the highest single-piece ratio of any cohort. This is the connector vocabulary that defines Technic. Globally `2780.dat` is #2 (4.38 % of 1 438 corpus).

### R30: Neg-det by theme — 12 themes account for ~75 % of all 3 668 reflections

| Theme | Reflections | % corpus |
|-------|-----------:|--------:|
| **Technic > Competition** | **902** | **24.6 %** |
| Unitron | 347 | 9.5 % |
| Technic (non-Competition) | 260 | 7.1 % |
| Town (modern, incl. 10190-1 Modular Town Hall) | 208 | 5.7 % |
| The LEGO Movie | 198 | 5.4 % |
| Classic Space | 196 | 5.3 % |
| Blacktron I (legacy + cohort modern) | 194 + 192 = 386 | 10.5 % combined |
| Space > Blacktron II | 183 | 5.0 % |
| Town > Classic Town | 111 | 3.0 % |
| LEGO Ideas and CUUSOO | 105 | 2.9 % |
| M:Tron | 99 | 2.7 % |
| Star Wars | 98 | 2.7 % |
| Space > Classic Space (modern) | 98 | 2.7 % |
| Space Police I | 61 | 1.7 % |
| **Top 14 themes sum** | **3 246** | **88.5 %** |

**R30 conclusion**: reflections cluster in **Technic > Competition** (24.6 %), **pre-2000 Space sub-themes** (Unitron, Blacktron, Classic Space, M:Tron = ~35 % combined), and **specific outliers** (LEGO Movie 5.4 %, LEGO Ideas 2.9 %, 10190-1 Modular Town Hall in modern Town 5.7 %). Modern System themes (City, Friends, Creator) almost never use reflections.

### R31: Technic deltas include `(0, -0.5, 0)` and other sub-LDU values

Top Technic deltas:
- `(0, 0, 0)` 4 266 (anchor)
- `(40, 0, 0)` 2 049 (beam length)
- `(20, 0, 0)` 1 759
- `(0, 0, 40)` 1 672 (beam length Z)
- `(0, 0, -40)` 1 541
- `(0, 0, 20)` 1 455
- `(0, 0, -20)` 1 449
- `(-40, 0, 0)` 1 336
- `(-20, 0, 0)` 1 298
- **`(0, -0.5, 0)` 1 139** — sub-LDU vertical alignment (0.5 LDU = stud-snug tolerance)
- `(80, 0, 0)` 1 066
- `(10, 0, 0)` 994 (half-beam)
- `(-80, 0, 0)` 863
- `(0, -20, 0)` 831
- `(-10, 0, 0)` 790

The `(0, -0.5, 0)` delta is Technic-specific — used to "snap" Technic pin alignments. This **violates R2** (canonical deltas) for Technic.

### R32: classic_gaps cohort extends R19 confirmation

The 158-set classic_gaps cohort was specifically constructed to fill Plan C shortfalls (Boat, Train, 9V, Launch Command, Divers, additional Space sub-themes). It produced **641 reflections (2.014 %)** — confirming that pre-2000 Space sub-themes (Blacktron II 183, Blacktron I 144 + 192, Space Police III, etc.) carry the same phenomenon as the original Plan C Space subset.

### R33: LEGO Ideas / CUUSOO is the **highest BFC ratio specialty theme** (66.7 %)

12 sets, 8 BFC CERTIFY. Most Ideas sets follow modern BFC convention because they are peer-reviewed through LEGO Ideas platform and often rewritten by OMR contributors.

### R34: Racers (76 sets) has the lowest BFC ratio (1.3 %) of any modern theme

1 / 76. Despite being post-2000, Racers was authored before BFC became convention. **R25 confirms**: legacy authoring era dominates BFC ratio more than release year.

### R35: Decade-cohort matrix reveals 2 uncovered eras

- **`specialty` 1980s-1990s** = 0 sets. Specialty = Brickheadz + Architecture + Ideas + Seasonal + Promotional — all post-2007 themes.
- **`licensed` pre-1999** = 0 sets. The first licensed theme (Star Wars) launched 1999.

### R36: Top-10 piece coverage grows with corpus diversity (24.3 % → 30.0 %)

In the 532 corpus, top-10 = 24.3 % of all pieces. In the 1 438 corpus, top-10 = **29.96 %**. The increase comes from Technic-heavy pieces (`2780.dat`, `166.dat`, `u9218.dat`, `77.dat`, `6558.dat`) and Brickheadz (`98138.dat`) entering the top-10. **R5 ("top 10 covers ~24 %") is qualified: 24.3 % held for 532; with Technic it climbs to ~30 %**.

### R37: The "fabuland has identity" rule (R16) is now measurable

Fabuland (41 sets, 1 346 pieces) has pieces with 319× lift (`6264.dat`, `4222a.dat`, `787c02.dat`). The R16 estimate of "25 pieces u91xx" is consistent with the 0.93 % custom-parts-of-system ratio for Fabuland.

---

## 9. Top-10 pieces (1 438 corpus) and what they reveal

| # | Piece | Count | % corpus | Source cohort |
|--:|-------|------:|--------:|---------------|
| 1 | `4-4cyli.dat` | 20 031 | 5.03 % | Universal — cylinder base |
| 2 | `2780.dat` (Technic Pin) | **17 458** | **4.38 %** | **Technic only** |
| 3 | `3023.dat` (Plate 1×2) | 16 181 | 4.06 % | System |
| 4 | `6141.dat` (Plate 1×1 round) | 11 755 | 2.95 % | Friends + decorative |
| 5 | `166.dat` (Technic Pin) | **10 617** | **2.66 %** | **Technic only** |
| 6 | `3024.dat` (Plate 1×1) | 9 844 | 2.47 % | System |
| 7 | `3004.dat` (Brick 1×2) | 8 746 | 2.19 % | System |
| 8 | `u9218.dat` (Technic pin) | **8 374** | **2.10 %** | **Technic only** |
| 9 | `98138.dat` (Tile 1×1 groove) | **8 207** | **2.06 %** | **🆕 Brickheadz + Architecture** |
| 10 | `77.dat` (Technic pin) | **8 188** | **2.05 %** | **Technic only** |

**Five of the top-10 pieces are Technic-dominated** (positions 2, 5, 8, 10 — `2780.dat` 86 % Technic, `166.dat` 96 % Technic, `u9218.dat` 96 % Technic, `77.dat` 92 % Technic). This is a **regime shift** vs the 532 corpus, where the top-10 was dominated by System plates/bricks. The corpus-level "vocabulary" is now Technic-leaning even though only 12 % of OMR sets are Technic.

Top-30 sum = **53.00 %** of all 398 599 piece-uses.

---

## 10. Carry-over: which 532 rules survive in 1 438?

| Rule | Status at 1 438 |
|------|-----------------|
| R1 Y múltiplos de 8 | ✅ Holds for System (`modern` top Y-layers are all ±8 multiples) |
| R2 Deltas X/Z múltiplos de 20 | ✅ Holds for System; ❌ breaks for Technic (R31) |
| R3 Reflejos < 0.3 % | ❌ Refuted again — corpus-wide 0.687 % |
| R4 Custom parts = 0.6 % | 🟡 Recalibrated to 0.84 % corpus-wide |
| R5 Top 10 ≈ 24 % | 🟡 Qualified — Technic pushes it to ~30 % |
| R7 Bigramas self | ✅ Holds for top-15 |
| R12 `4-4cyli.dat` universal | ✅ 5.03 % of corpus, still #1 |
| R16 Fabuland identidad propia | ✅ Confirmed (319× lift for Fabuland pieces) |
| R17 Friends decorativo | ✅ Confirmed (66.7× lift for `6191.dat`) |
| R19 Space-themed reflejos | ✅ Confirmed + extended (R25, R32) |
| R20 `756.dat` Space signature | ✅ Confirmed (in classic + classic_gaps top-3) |
| R21 Clásicos BFC bajo | 🟡 Qualified — modern Specialty + Licensed + Technic also have varied BFC |
| R22 Bigramas heterogéneos Space | ✅ Holds |
| R23 Y = +8 mástil Space | ✅ Holds; Technic adds ±10 (R26) |

**Net new rules from 1 438 corpus: R24-R37 (14 new rules)**.

---

## 11. Implications for the generator

### Add a Technic sub-mode
- New constants: `TECHNIC_PIN = "2780.dat"`, `TECHNIC_AXLE_2 = "32184.dat"`, `TECHNIC_BEAM_3 = "32523.dat"`, `TECHNIC_BEAM_5 = "32316.dat"`, `TECHNIC_BUSH = "4265c.dat"`, `TECHNIC_ANGLE = "32062.dat"`.
- New helper: `place_technic_pin(file, color, x, y, z)` that allows **non-canonical Y** (multiples of 20 only — but 0.5 LDU tolerance OK).
- New color for Technic: `DARK_GRAY = 10`, `LIGHT_GRAY = 9`.

### Add a Brickheadz sub-mode
- New constants: `BRICKHEADZ_EYE = "22885.dat"`, `BRICKHEADZ_TILE = "98138.dat"`.
- Default body color: `BRICKHEADZ_BODY_COLOR = 0` (black) or `WHITE`.
- 2-stud wide builds only — no plate stacking beyond 6 plates.

### Add Architecture sub-mode
- `ARCH_TILE = "3070b.dat"`, `ARCH_RIBBED = "50746.dat"`.
- `SNAP_TOLERANCE = 0.5` (LDU).
- Color palette: dark gray, light gray, white, transparent.

### Reflection helper evolution
- `place_mirrored()` already exists (R19 era). Add `place_mirrored_with_axis(file, color, axis='y')` to handle the 33 % Technic > Competition sub-theme pattern.

---

## 12. Limitations

1. **Sample still skewed toward OMR availability**: 1 438 / 1 470 = 97.8 % of OMR. We are **saturated** on what OMR has indexed.
2. **Themes like Ninjago, Minecraft, Collectible Minifigures** are under-represented because the OMR itself has few MPDs for those themes (community-contributed LDraw libraries have more).
3. **BFC CERTIFY may not reflect LEGO's intent**: OMR contributors add BFC independently of LEGO authoring; high-BFC Technic reflects contributor culture, not LEGO convention.
4. **Neg-det ratio varies 50× across cohorts** (modern 0.037 % vs classic 2.770 %): aggregating to "0.687 %" hides the bimodal distribution.
5. **Custom-part detection is regex-based**; some embedded parts may be classified as "subparts" instead of "custom_parts" depending on naming.

---

## 13. Suggested follow-up corpus expansions

| Theme | Sets in OMR | Corpus coverage | Suggestion |
|-------|------------:|----------------:|-----------|
| Ninjago | ~50 | < 10 | Add `cohort_ninjago` |
| Minecraft | ~60 | < 10 | Add `cohort_minecraft` |
| Collectible Minifigures | ~20 | 0 | Add `cohort_minifigs` |
| The LEGO Batman Movie | ~30 | 0 | Add `cohort_batman` |
| Dimensions | ~40 | 5 | Add `cohort_dimensions` |
| **Total remaining** | **~200** | — | Would bring corpus to ~1 638 sets |

---

## 14. References

- `analysis/per_set_stats_1438.json` (1 438 records, top-30 pieces + top-20 deltas + top-30 bigrams per set)
- `analysis/cross_corpus3_stats.json` (8 cohort aggregates + all-1 438 aggregate)
- `corpus/all_omr_themes.json` (135-theme catalog + 1 470-set index)
- `LEARNED_CONVENTIONS_532.md` (R1-R23 carry-over)
- `analysis/findings_cohorts_3.md` (legacy 3-cohort analysis)
- `analysis/findings_themes_532.md` (legacy 532 themes analysis)
- `analysis/batch_parse4.py` (parser that produced these JSONs)