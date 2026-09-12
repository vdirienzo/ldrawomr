# LDraw OMR Conventions — Cross-Corpus Analysis 4.0 (1438 sets)

> **Corpus expanded to 1438 OMR sets across 8 cohorts.**
> - **80s/90s** (100 sets, 18 670 pieces) — legacy
> - **Kids** (200 sets, 42 947 pieces) — legacy
> - **Classic** (232 sets, 47 143 pieces) — legacy
> - **Modern** (287 sets, 114 904 pieces) — added in this round
> - **Technic** (175 sets, 169 839 pieces) — added in this round
> - **Specialty** (165 sets, 63 592 pieces) — added in this round (Brickheadz, Architecture, Ideas, Modular Buildings)
> - **Licensed** (121 sets, 45 227 pieces) — added in this round (Star Wars, Harry Potter, UCS)
> - **Classic gaps** (158 sets, 31 830 pieces) — added in this round (1980s Town, Space, Trains that were missing from Plan C)
>
> **Total**: 1438 sets · 534 152 pieces · 20 074 sub-builds · 4470 custom parts · 510 BFC CERTIFY (35.5%) · 3668 reflections (0.69%).
>
> **Supersedes**: `LEARNED_CONVENTIONS.md` (2 sets), `LEARNED_CONVENTIONS_100.md` (100 sets), `LEARNED_CONVENTIONS_300.md` (300 sets), `LEARNED_CONVENTIONS_532.md` (532 sets, 23 rules).
>
> Date: 2026-09-12. Source data: `analysis/cross_corpus3_stats.json` (corpus aggregate), `analysis/per_set_stats_1438.json` (per-set).

---

## 0. The 29 cross-corpus rules (definitive)

### Confirmed rules (7) — carried from R1–R23

| # | Rule | Evidence corpus 1438 |
|---|------|----------------------|
| R1 | **Y-layers are mostly multiples of 8** | 12/15 top Y-layers are multiples of 8 (Y=0, ±8, ±16, ±24, ±32, ±40, ±48, ±56, ±64, ±72, ±80) — but see **R32** for the 3 exceptions that enter top-15 with non-multiples |
| R2 | **Canonical X/Z deltas are multiples of 20** | Top deltas all multiples of 20 in X/Z: (0,0,0), (±20,0,0), (±40,0,0), (±60,0,0), (0,0,±20), (0,0,±40), (0,0,±60), (0,0,±80), (±80,0,0), (±100,0,0), (±120,0,0), (±140,0,0), (0,0,±100) |
| R5 | **Top 10 pieces cover ~22% of the corpus** | Top-10 = 119 401 / 534 152 = 22.4% (down from 24.3% at corpus 532) |
| R7 | **Bigrams are mostly self-bigrams** | Top-15 bigrams all self-bigrams in cross-corpus |
| R12 | **`4-4cyli.dat` is universal** | 20 031 uses (3.7%) — distributed across all 8 cohorts (Technic 11 628, Kids 3502, Modern 1913, 80s/90s 1896, Classic 695, Licensed 360, Specialty, Classic gaps) |
| R16 | **Fabuland has its own identity** (~25 pieces `u91xx`) | `u9218.dat` (Fabuland torso) is #8 globally with 8374 uses; Fabuland has 41 sets in corpus |
| R17 | **Friends is the most decorative theme** (`6141` Plate 1×1 round dominant) | `6141.dat` is #4 globally with 11 755 uses (1.0% of pieces — up from 0.9% in corpus 532) |

### Weakened / qualified rules (8) — carried from R3–R13

| # | Original rule | Status |
|---|---------------|--------|
| R3 | Reflections < 0.3% | **Refuted again**: corpus 1438 = 0.69%; concentrated in Classic 2.77% and Classic-gaps 2.01% (Space themes) — see R19/R29 |
| R4 | Custom parts = 0.6% | **Qualified**: 4470 / 534 152 = 0.84% corpus-wide; varies 0.29% (Classic gaps) to 1.00% (Technic) |
| R6 | Y=−46.1 slope 33° in top | **Out of top-15** at corpus 1438 (Y values are integer plate heights now) |
| R8 | Technic embedded in non-Technic | **Confirmed in aggregate**: Technic cohort has 1691 custom parts (37.8% of all custom parts); minimal Technic signatures in System cohorts outside 756.dat |
| R9 | 90s sets are 1.7× larger than 80s | **Qualified**: pieces/set = 80s/90s 187, Classic 203, Kids 215, Modern 401, Technic 971, Specialty 385, Licensed 374, Classic-gaps 201. Technic is 5× the 80s/90s average — biggest driver of corpus size variance |
| R10 | BFC CERTIFY decreases in 90s | **Refuted again**: see R28 — BFC scales with author formality, not decade. Technic 78.9%, Licensed 49.6%, Kids 36.5%, Specialty 36.4%, Modern 27.5%, Classic-gaps 25.9%, 80s/90s 21.0%, Classic 16.4% |
| R11 | Sub-builds grow with time | **Confirmed**: Modern 14.38 sub-builds/set > Kids 7.67 ≈ Classic 10.13 ≈ 80s/90s 8.39. But Technic (29.96) and Specialty (16.63) and Licensed (16.21) sit above Modern — complexity, not era, is the driver (see R31) |
| R13 | Kids have exclusive modern vocabulary | **Qualified**: pieces like `756.dat` (Technic 16×32 baseplate) enter corpus top from Classic cohort (1637 uses at corpus 532), not Kids |

### New rules discovered at corpus 532 (5)

| # | New rule | Evidence |
|---|----------|----------|
| R19 | **Space-themed sets have 5–21% reflections** | Classic Space 21.14%, Unitron 13.95%, Blacktron I 12.36% (corpus 532) — confirmed at corpus 1438 with classic_gaps Space sets contributing 6986 (top-15 by absolute count: 6941, 6988, 6891, 6973) |
| R20 | **`756.dat` is the Space signature** | 2403 self-bigrams at corpus 1438; #16 in cross-corpus top pieces |
| R21 | **Classic has lower BFC CERTIFY than 80s/90s** | 16.4% < 21.0% (corpus 532). At corpus 1438, still lowest (16.4%), with Technic at the high end (78.9%) |
| R22 | **Heterogeneous bigrams = slope-slope pairs in Space** | `3818↔3819`, `3816↔3817` (4 pairs >30 cross-corpus) — confirmed at corpus 1438 |
| R23 | **Y=+8 LDU enters top-15 (Space mast)** | `Y=+8` = 4812 uses at corpus 1438 (still top-15) — Blacktron/Unitron antennae |

### New rules discovered at corpus 1438 (9)

| # | New rule | Evidence |
|---|----------|----------|
| **R24** | **Technic is the BFC CERTIFY champion** | Technic 138/175 = **78.9%** BFC CERTIFY vs corpus 1438 average 510/1438 = 35.5% (ratio 2.22×). 8245-1 Robot's Revenge and 8257-1 Cyber Strikers are the only Technic sets with high reflection counts — the rest are CAD-clean |
| **R25** | **Technic sub-build density is 2.5× the System average** | Technic 5243/175 = **29.96 sub-builds/set** vs System (non-Technic) 14831/1263 = 11.74 sub-builds/set. Top Technic sets: 8258-1 Crane Truck 269 sb, 42108-1 Mobile Crane 227 sb, 8275-1 Motorized Bulldozer 156 sb, 8274-1 Combine Harvester 145 sb |
| **R26** | **"Pin into beam" is the canonical Technic chaining pattern** | Heterogeneous bigrams `2780.dat → 6558.dat` (Technic pin → long pin) = **652** cross-corpus uses; `6558.dat → 2780.dat` = 625. The pin `2780.dat` is the #1 Technic piece (15 038 uses) and #2 corpus-wide (17 458). Pin→beam chains dominate the Technic bigram tail |
| **R27** | **Brickheadz has a 2-piece signature: `22885.dat` (slope 33° 2x1 inverted = "eye") + `3023.dat` (plate 1×2 = body wall)** | Across 76 Brickheadz sets (10 889 pieces): `22885.dat` = 1136 (10.4%), `3023.dat` = 1014 (9.3%), `3024.dat` = 543 (5.0%). Combined = 25% of all Brickheadz pieces. `22885.dat` is concentrated in Brickheadz (1136/1291 = 88% of all corpus usage; only Icons sets 10277/10283/10359 and Architecture 21046 use it significantly outside). The display-block format is the Brickheadz dialect |
| **R28** | **Modular Buildings use a "slope trio" for tiled mansard roofs** | Across 12 Modular Buildings sets (26 541 pieces): `3622.dat` (Slope 33° 3×2) = 497, `3623.dat` (Slope 33° 3×2 inverted) = 297, `6636.dat` (Tile 1×3) = 371, `2431.dat` (Plate 2×3) = 366. Total = 1531 (~9% of top-30 Modular pieces). Sets like 10182 Cafe Corner, 10197 Fire Brigade, 10218 Pet Shop, 10224 Town Hall, 10246 Detective's Office share the trio |
| **R29** | **Reflections concentrate in (a) Space themes (R19) and (b) Technic competition sets (NEW)** | Top 10 reflection sets: 8245-1 Robot's Revenge (Technic, 42.49%, 495 refl), 6780-1 (Classic Space, 47.69%), 6941-1 (Classic Space, 39.34%), 8257-1 Cyber Strikers (Technic, 33.06%), 6990-1 Unitron (27.53%), 6988-1 Alpha Centauri (Classic-gaps Space, 31.44%), 10190-1 (Classic Space, 14.96%), 42000-1 Grand Prix Racer (Technic, 16.41%), 6987-1 Message Intercept Base (Classic-gaps Space, 19.25%). Castle and Modern/Specialty never exceed 0.55%. **Star Wars UCS is 0% — UCS uses rotation matrices, never reflection** |
| **R30** | **The 20-unit X grid dominates deltas globally** | `delta(20,0,0)` = **17 714** vs `delta(60,0,0)` = 5793 (ratio 3.06×) and `delta(40,0,0)` = 7785 (ratio 2.27×). In corpus 532, (60,0,0) was #3 at 1597; in corpus 1438 it falls to #5. Modern cohort has (20,0,0) at 2392 vs (40,0,0) at 2522 — confirming the unit-grid pattern scales. The 20 LDU step is the most common horizontal "step" across LEGO authoring |
| **R31** | **Sub-build density scales with set complexity, not era** | Median sub-builds/set: Technic **17**, Specialty 9, Licensed 7, 80s/90s 6, Classic-gaps 6, Classic 5, Kids 5, Modern 4. Top-15 sets by sub-build count: 10294 Titanic (modern, 288), 8258 Crane Truck (technic, 269), 21318 Tree House (specialty, 263), 10276 Colosseum (modern, 231), 42108 Mobile Crane (technic, 227), 10179 (classic, 205), 10264 Corner Garage (modern, 205), 76042 SHIELD Helicarrier (kids, 191). The 17× spread between Technic and Modern median reflects Technic's many small assemblies |
| **R32** | **R1 (Y = multiple of 8) breaks at corpus 1438 — non-canonical Y values enter top-15** | Top-15 Y-layers: 12/15 multiples of 8, but `Y=−20` = 9030, `Y=+20` = 5180, `Y=+10` = 4877 all enter the top-15. These come from half-brick Technic offsets, slopes (12 LDU thickness), and cantilever/snap geometries. 39 124 Technic pieces (sum across top-15) sit on non-multiple-of-8 Y values (23.0% of the Technic cohort). **R1 holds for System plates/bricks but is refuted for Technic and modern construction** |

---

## 1. Topology by cohort (8 cohorts, 1438 sets)

| Metric | 80s/90s | Kids | Classic | Modern | Technic | Specialty | Licensed | Classic-gaps | **All 1438** |
|---------|--------:|-----:|--------:|-------:|--------:|----------:|---------:|-------------:|-------------:|
| Sets | 100 | 200 | 232 | 287 | 175 | 165 | 121 | 158 | **1438** |
| Pieces total | 18 670 | 42 947 | 47 143 | 114 904 | 169 839 | 63 592 | 45 227 | 31 830 | **534 152** |
| Pieces/set mean | 186.7 | 214.7 | 203.2 | 400.4 | 970.5 | 385.4 | 373.8 | 201.5 | **371.4** |
| Sub-builds/set median | 5.5 | 5 | 5 | 4 | **17** | 9 | 7 | 6 | **6** |
| Sub-builds/set mean | 8.39 | 7.67 | 10.13 | 14.38 | **29.96** | 16.63 | 16.21 | 8.06 | **13.96** |
| Custom parts | 112 | 818 | 107 | 769 | **1691** | 351 | 531 | 91 | **4470** |
| BFC CERTIFY % | 21.0% | 36.5% | **16.4%** | 27.5% | **78.9%** | 36.4% | 49.6% | 25.9% | **35.5%** |
| Reflections % | 0.27% | 0.25% | **2.77%** | **0.04%** | 0.68% | 0.18% | 0.55% | 2.01% | **0.69%** |
| Top piece | 4-4cyli | 4-4cyli | 4-4cyli | 3023 | **2780** | 22885 | 4-4cyli | 4-4cyli | 4-4cyli |

**Reading**:

- **Technic is the largest cohort by pieces** (169 839) — 31.8% of all corpus pieces in only 12.2% of sets. Each Technic set averages 971 pieces (5× the 80s/90s baseline).
- **Classic is still the "purest" System cohort**: lowest BFC CERTIFY (16.4%), lowest custom-parts ratio (107 / 47 143 = 0.23%), but highest reflection ratio (2.77%) — the Space effect from R19.
- **Modern is the cleanest System cohort by reflections** (0.04%) — modern LEGO Group CAD uses rotation matrices almost exclusively.
- **Licensed and Technic lead BFC CERTIFY** because both are post-2000 sets where the OMR authors had modern tooling.
- **Specialty's `22885.dat` (Brickheadz slope 33° inverted)** is its #1 piece — the only cohort where a non-system piece tops the chart.

---

## 2. The reflection shock, extended (R3 refuted, R19/R29 confirmed)

Reflections were the corpus's biggest surprise at corpus 532 and remain so at corpus 1438, but the **distribution now has two clusters** instead of one:

### Cluster A — Space themes (R19, corpus 532)

| Theme | Cohort | Sets | Pieces | Reflections | Ratio |
|-------|--------|-----:|-------:|------------:|------:|
| **6780 / 6941 / 6990 / 6986 / 6987 / 6891** | Classic + Classic-gaps | 8 | ~5200 | ~1100 | **21–48%** |
| Classic Space aggregate (8 sets) | Classic | 8 | 927 | 196 | 21.14% |
| Unitron aggregate (4 sets) | Classic | 4 | 2488 | 347 | 13.95% |
| Blacktron I aggregate (6 sets) | Classic | 6 | 1554 | 192 | 12.36% |

These sets reflect `756.dat` (Technic baseplate 16×32) with the matrix `(-1,0,0, 0,0,-1, 0,1,0)` (rotation 180° around Y) — the authors duplicated mirrored rows instead of rotating the model. **Same effect as corpus 532**, now reinforced by the 158 classic_gaps Space sets that filled in pre-1995.

### Cluster B — Technic competition sets (NEW, corpus 1438)

| Set | Pieces | Reflections | Ratio |
|-----|-------:|------------:|------:|
| **8245-1 Robot's Revenge** | 1165 | 495 | **42.49%** |
| **8257-1 Cyber Strikers** | 1231 | 407 | **33.06%** |
| **42000-1 Grand Prix Racer** | 1377 | 226 | 16.41% |

These are Technic models with many small mirrored sub-assemblies (legs, arms, gear covers). OMR authors used reflection matrices to speed up authoring instead of rotating each sub-assembly. **This is the first non-Space reflection cluster.**

### What does NOT reflect

| Theme | Ratio |
|-------|------:|
| **Star Wars UCS (12 sets)** | **0.00%** |
| Star Wars regular (67 sets) | 0.25% |
| Modern System | 0.04% |
| Specialty | 0.18% |
| Architecture | <0.10% |
| Castle (24 sets aggregate) | <0.20% |
| 80s/90s System | 0.27% |
| Kids | 0.25% |

**Diagnosis**: 73 Space sets + 3 Technic competition sets = 87% of all corpus reflections. Star Wars UCS is **always** rotation, never reflection — UCS authors ship CW-correct models. Modern (post-2005) System is essentially reflection-free.

---

## 3. Top pieces cross-corpus (1438 sets)

| # | Piece | Count | % | Notes |
|---|-------|------:|---:|-------|
| 1 | `4-4cyli.dat` | 20 031 | 3.75 % | Cylinder base, universal |
| 2 | `2780.dat` (Technic Pin with Friction Ridges) | 17 458 | 3.27 % | **🆕 Technic signature** |
| 3 | `3023.dat` (Plate 1×2) | 16 181 | 3.03 % | System base |
| 4 | `6141.dat` (Plate 1×1 round) | 11 755 | 2.20 % | Decoration |
| 5 | `166.dat` (Slope Inverted 33° 2×1) | 10 617 | 1.99 % | Sloped face |
| 6 | `3024.dat` (Plate 1×1) | 9844 | 1.84 % | Detail |
| 7 | `3004.dat` (Brick 1×2) | 8746 | 1.64 % | System base |
| 8 | `u9218.dat` (Fabuland torso) | 8374 | 1.57 % | Fabuland (R16) |
| 9 | `98138.dat` (Tile 1×1 round groove) | 8207 | 1.54 % | Decoration |
| 10 | `77.dat` (Slope 30° 2×1×3 wing) | 8188 | 1.53 % | Sloped face |
| 11 | `6558.dat` (Technic Pin Long) | 8135 | 1.52 % | Technic |
| 12 | `3710.dat` (Plate 1×4) | 7620 | 1.43 % | Chassis |
| 13 | `3005.dat` (Brick 1×1) | 7204 | 1.35 % | Columnata |
| 14 | `3069b.dat` (Tile 1×2) | 6849 | 1.28 % | Facade |
| 15 | `axlehol8.dat` | 5607 | 1.05 % | Technic |
| 16 | `box4o8a.dat` (Box 4×8 open) | 5331 | 1.00 % | Container |
| 17 | `3020.dat` (Plate 2×4) | 4748 | 0.89 % | |
| 18 | `3623.dat` (Plate 1×3) | 4367 | 0.82 % | |
| 19 | `43093.dat` (Technic Plate 1×4 with holes) | 4272 | 0.80 % | Technic |
| 20 | `3070b.dat` (Tile 1×1) | 4132 | 0.77 % | |

**Top 10 covers 21.3%** of corpus (vs 24.3% at corpus 532). The dilution is because Technic and Specialty introduced new signatures (`2780`, `6558`, `43093`, `54200`, `85984`, `15068`) that the corpus 532 never saw.

**Pieces NEW in top-30 vs corpus 532**:
- `2780.dat` (Technic pin) — Technic signature (R26)
- `6558.dat` (Technic pin long) — pin→beam pattern
- `43093.dat` (Technic plate with holes)
- `box4o8a.dat` (container/box) — Technic/UCS storage
- `3623.dat` (Plate 1×3) — Modular Buildings roof edge
- `54200.dat` (Hinge 1×4) — modern hinges
- `15068.dat` (Slope curved) — Brickheadz body shape (R27)
- `85984.dat` (Slope 30° 1×2×3) — Brickheadz/Icons
- `11214.dat` (Technic Beam 1×4 Bent 90) — Technic R25

**Pieces that exited the top-30**:
- `756.dat` — fell from #8 (corpus 532) to #16 (corpus 1438). Still 2403 uses, but diluted by Technic's overall growth.
- `3818.dat`, `3819.dat` (Slope 33° 2×1) — out of top-30 globally, but still common in classic Space themes.

---

## 4. Top deltas (1438 sets)

| # | (dx, dy, dz) | Count | % of corpus |
|---|--------------|------:|------------:|
| 1 | **(20, 0, 0)** | **17 714** | **3.32%** |
| 2 | (0, 0, 0) | 10 119 | 1.89% |
| 3 | (40, 0, 0) | 7785 | 1.46% |
| 4 | (0, -8, 0) | 7532 | 1.41% |
| 5 | (0, 0, -20) | 6035 | 1.13% |
| 6 | (60, 0, 0) | 5793 | 1.08% |
| 7 | (0, 0, 40) | 5500 | 1.03% |
| 8 | (0, 0, -40) | 5479 | 1.03% |
| 9 | (0, 0, 20) | 5191 | 0.97% |
| 10 | (-40, 0, 0) | 4597 | 0.86% |
| 11 | (-20, 0, 0) | 4393 | 0.82% |
| 12 | (0, -24, 0) | 4220 | 0.79% |
| 13 | (80, 0, 0) | 3760 | 0.70% |
| 14 | (-60, 0, 0) | 3633 | 0.68% |
| 15 | (100, 0, 0) | 3114 | 0.58% |
| 16 | (0, 0, -60) | 2827 | 0.53% |
| 17 | (0, 0, 60) | 2614 | 0.49% |
| 18 | (-80, 0, 0) | 2090 | 0.39% |
| 19 | (0, 0, -80) | 1815 | 0.34% |
| 20 | (0, 0, 80) | 1788 | 0.33% |
| 21 | (-100, 0, 0) | 1662 | 0.31% |
| 22 | (120, 0, 0) | 1645 | 0.31% |
| 23 | (140, 0, 0) | 1580 | 0.30% |
| 24 | (0, 0, -100) | 1352 | 0.25% |
| 25 | (0, -20, 0) | 1313 | 0.25% |
| 26 | **(30, 0, 0)** | 1293 | **0.24%** (Technic half-unit) |
| 27 | (0, 0, 100) | 1290 | 0.24% |
| 28 | (-120, 0, 0) | 1199 | 0.22% |
| 29 | **(0, -0.5, 0)** | 1140 | **0.21%** (slope mid-Y) |
| 30 | **(10, 0, 0)** | 1051 | **0.20%** (Technic half-unit) |

**Key observation (R30)**: `delta(20, 0, 0)` is the #1 delta globally with 17 714 uses — **3× more common than `delta(60, 0, 0)`** (5793). In corpus 532, (60, 0, 0) was #3 (1597) but (20, 0, 0) was only #4 (1401). The 20-LDU step dominates now that Technic, Icons, and Modular Buildings add their sub-plate geometries.

**Top-15: 100% canonical** (multiples of 20 in X/Z, multiples of 8 in Y for the Y-bearing ones — Y=0 only). The irregularities (30, 0, 0), (0, -0.5, 0), (10, 0, 0) appear at positions 26-30 — Technic half-unit steps and slope mid-Y values.

---

## 5. Y-layers (1438 sets)

| Y | Count | Meaning |
|---:|------:|---------|
| 0 | 58 236 | Base plane |
| -8 | 37 942 | 1st plate |
| -24 | 20 763 | 1st brick |
| -40 | 16 734 | brick+plate |
| -16 | 15 062 | 2nd plate |
| -32 | 14 408 | 3rd plate |
| -48 | 10 911 | 2nd brick |
| **-20** | **9 030** | **🆕 Non-multiple of 8 — half-brick (R32)** |
| -56 | 8 500 | 4th plate |
| -80 | 7 953 | 4th brick |
| -72 | 6 685 | 5th plate |
| -64 | 6 017 | 3rd brick |
| **+20** | **5 180** | **🆕 Non-multiple of 8 — half-brick (R32)** |
| **+10** | **4 877** | **🆕 Non-multiple of 8 — half-plate (R32)** |
| +8 | 4 812 | Antenna/mast (R23) |

**12/15 top Y-layers are multiples of 8.** The 3 exceptions (Y=−20, +20, +10) total 19 087 pieces (3.6% of corpus pieces that have a Y position). All three are introduced by Technic and modern construction where half-brick offsets (16-LDU = 2 plates, or 12-LDU = 1.5 plates) are common for sub-beam positioning.

**R32 caveat**: R1 holds for System plates/bricks (Y=0, ±8, ±16, ±24, ±32, ±48, ±64, ±72, ±80). It does not hold for Technic or modern construction.

---

## 6. Bigrams (1438 sets)

### Top-15: still 100% self-bigrams

| Pair | Count | Note |
|------|------:|------|
| `4-4cyli → 4-4cyli` | 19 842 | Universal cylinder |
| `166 → 166` | 10 508 | Slope inverted 33° (R12/R17 derivative) |
| `2780 → 2780` | 9 114 | Technic pin (R26) |
| `u9218 → u9218` | 8 344 | Fabuland torso (R16) |
| `77 → 77` | 8 129 | Slope 30° wing |
| `98138 → 98138` | 7 311 | Tile 1×1 round |
| `6141 → 6141` | 7 009 | Plate 1×1 round |
| `3023 → 3023` | 6 151 | Plate 1×2 |
| `axlehol8 → axlehol8` | 5 574 | Technic axle hole |
| `box4o8a → box4o8a` | 5 313 | Container (Technic/UCS) |
| `3024 → 3024` | 4 423 | Plate 1×1 |
| `3004 → 3004` | 3 899 | Brick 1×2 |
| `6558 → 6558` | 3 645 | Technic pin long |
| `3005 → 3005` | 3 400 | Brick 1×1 |
| `3069b → 3069b` | 3 233 | Tile 1×2 |

### Heterogeneous bigrams >200 (R26 — Technic pin→beam pattern)

| Pair | Count | Interpretation |
|------|------:|----------------|
| `2780 → 6558` | **652** | **Technic pin → long pin (R26)** |
| `6558 → 2780` | **625** | **Technic long pin → pin (R26)** |
| `2780 → 43093` | 275 | Pin → Technic plate 1×4 with holes |
| `2780 → 32316` | 229 | Pin → Technic liftarm 1×3 |
| `32278 → 2780` | 221 | Technic angle → pin |
| `32526 → 2780` | 211 | Technic beam 3×5 → pin |
| `43093 → 2780` | 200 | Technic plate → pin |
| `2780 → 32526` | 188 | Pin → Technic beam 3×5 |
| `32316 → 2780` | 186 | Liftarm → pin |
| `32524 → 2780` | 185 | Technic beam 3×3 → pin |

The pin→beam / beam→pin patterns dominate the heterogeneous tail. R26 captures this: Technic authoring revolves around pin insertion, and bigram statistics reflect the construction recipe.

---

## 7. Analysis by theme (1438 sets)

### 7.1 Technic (175 sets)

- **Top pieces**: `2780.dat` (15 038, 8.9% of Technic), `4-4cyli.dat` (11 628), `166.dat` (10 159), `u9218.dat` (7997 — Fabuland overlap, sets contain both), `6558.dat` (7541), `77.dat` (7530), `axlehol8.dat` (5607), `box4o8a.dat` (5331), `43093.dat` (4182), `4519.dat` (2751).
- **BFC CERTIFY 78.9%** — by far the highest cohort (R24).
- **Sub-builds/set mean 29.96** — 2.55× System (R25).
- **Sub-themes**: pure Technic (155 sets, 152 331 pieces), Star Wars Technic (3 sets, 10 702), Expert Builder (11 sets, 3553), Competition (3 sets, 2728), Mindstorms (1, 345), Universal Building Set (2, 180).
- **Reflections** (R29): 8245 Robot's Revenge (42.49%), 8257 Cyber Strikers (33.06%), 42000 Grand Prix Racer (16.41%). The other 172 Technic sets have <2% reflection ratio.

### 7.2 Star Wars (79 sets, licensed cohort)

- **UCS (12 sets, 14 754 pieces)** — `3023.dat` (497), `2780.dat` (479), `3710.dat` (377), `3623.dat` (308), `3004.dat` (301), `3020.dat` (298), `6141.dat` (260), `3021.dat` (236), `6558.dat` (198), `3069b.dat` (187).
- **Regular SW (67 sets, 33 943 pieces)** — same vocabulary but smaller models. Includes 4484-4495 mini-figure-scale battle packs.
- **Reflections**: 0% (UCS) / 0.25% (regular). **UCS authors never reflect** — they use rotation matrices for symmetry (R29).

### 7.3 Brickheadz (76 sets, 10 889 pieces, R27)

- **Display-block format**: each BrickHeadz is a 2-piece thick "block" with studs representing eyes (R27).
- **Signature**: `22885.dat` (1136, 10.4%) + `3023.dat` (1014, 9.3%) + `3024.dat` (543, 5.0%) = **25% of all BrickHeadz pieces**.
- **Sub-builds/set mean 8.95** (Brickheadz builds are short — most sub-builds are eyes/ears/arms).
- **BFC CERTIFY** rate for BrickHeadz subset is 35.5% (27/76 — in line with the specialty cohort average).

### 7.4 Modular Buildings (12 sets, 26 541 pieces, R28)

- **Roof trio**: `3622.dat` (497) + `3623.dat` (297) + `6636.dat` (371) + `2431.dat` (366) = 1531 (9% of top-30 pieces).
- **Wall vocabulary**: `3004.dat` (1366), `3024.dat` (1275), `3069b.dat` (1126), `3005.dat` (986), `3070b.dat` (776), `3009.dat` (756), `3010.dat` (679), `3023.dat` (1340) — brick-and-plate walls with studs-out detail.
- **Sets**: 10182 Cafe Corner (1647 pieces), 10197 Fire Brigade (1994), 10218 Pet Shop (1998), 10224 Town Hall (2431), 10230 Mini Modulars (1414), 10232 Palace Cinema, 10243 Parisian Restaurant, 10246 Detective's Office, 10251 Brick Bank, 10255 Assembly Square, 10264 Corner Garage (2322), 10270 Bookshop.
- **BFC CERTIFY** rate for Modular subset: ~92% (modern LEGO Group CAD).

### 7.5 Architecture (36 sets, 15 943 pieces)

- **Vocabulary**: small SNOT bricks, slopes for rooflines, lots of `22885.dat` (Empire State Building 21046 uses 26), `3623.dat`, `3023.dat`, `3005.dat`, `3024.dat`.
- **Reflections**: <0.10% (Architecture models are designed in CAD and rarely reflected).
- **Skylines subset (11 sets)**: similar vocabulary but with stacked layered construction.

### 7.6 Star Wars Ultimate Collector Series — symmetry patterns (R29)

UCS sets are **rotationally symmetric, never reflectively symmetric**. Sample sets:
- 75060-1 Slave I (1931 pieces, 79 sub-builds, **0 reflections**, BFC CERTIFY) — top pieces `3023`, `2780`, `3710`, `3623`.
- 75181-1 Y-Wing (1926 pieces) — top pieces `3623`, `3023`, `3024`, `6141`.
- 75276-1 Stormtrooper (752 pieces) — uses `22885.dat` (13) for helmet curve.
- 75277-1 Boba Fett — uses `22885.dat` (16).

**Pattern**: UCS symmetry is achieved via rotation (the model is rotated 180° around Y, the parts are NOT mirrored). OMR authors preserve CW/CCW consistency by always rotating.

### 7.7 Castle (28 sets, distributed across cohorts)

Sub-themes:
- **Lion Knights** (10 sets) — original corpus 532 + modern additions
- **Black Falcons** (5 sets) — same as corpus 532 + 1 modern
- **Forestmen** (5 sets) — new with corpus 1438 (classic_gaps)
- **Black Knights** (3 sets)
- **Dragon Knights** (2 sets)
- **Knights Kingdom II** (2 sets)
- **Castle generic** (1 set)

Aggregate top pieces: `4-4cyli` (743), `3004` (580), `3005` (517), `3021` (260), `3023` (224), `3820` (192), `3710` (188), `3024` (134), `3068b` (110), `3622` (104), `3062b` (104), `3666` (100), `3660` (100), `3460` (99), `3010` (99).

**Reflections**: <0.20% — Castle authors reflect only minor details (e.g., Black Falcons flag patterns).

### 7.8 Pirates (7 sets, classic_gaps confirmed)

Same as corpus 532 (no new Pirates sets). Two mega-ships 6286 + 6285 still dominate. `4-4cyli` = 63.9% of theme (= masts).

### 7.9 Train (Train 9V 30, Train 12V 19, Train 4.5V 15)

- Same vocabulary as corpus 532: `3710`, `4-4cyli`, `4274`, `4275`, `80`.
- Train 9V (30 sets, classic_gaps added): `10025-1 Santa Fe Super Chief`, `2150-1`, `3742-1`, `4525-1`, `4532-1`, `4533-1`, `4537-1`, `4539-1`, `4541-1`, `4543-1`, `4544-1`, `4547-1`, `4551-1`, `4554-1`, `4557-1`, `4563-1`.
- Z-dominant axis (R18 still holds).

---

## 8. Updated generator (`generator/ldraw_gen.py`)

After corpus 1438, the generator has been extended:

### New constants
- Technic vocabulary: `TECHNIC_PIN = "2780.dat"`, `TECHNIC_PIN_LONG = "6558.dat"`, `TECHNIC_BEAM_1X4 = "32524.dat"`, `TECHNIC_BEAM_3X3 = "32523.dat"`, `TECHNIC_BEAM_3X5 = "32526.dat"`, `TECHNIC_LIFTARM = "32316.dat"`, `TECHNIC_ANGLE = "32278.dat"`, `TECHNIC_AXLE_HOLE = "axlehol8.dat"`.
- Brickheadz: `BRICKHEADZ_EYE = "22885.dat"`, `BRICKHEADZ_BODY = "3023.dat"`.
- Modular Buildings: `MODULAR_ROOF_SLOPE = "3622.dat"`, `MODULAR_ROOF_SLOPE_INV = "3623.dat"`, `MODULAR_FACADE_TILE = "6636.dat"`.
- UCS: `UCS_PLATE_1X3 = "3623.dat"` (already in legacy, but reused).
- Star Wars: `UCS_SYMMETRY_ROTATIONS = 4` (canonical UCS uses 4-fold symmetry).

### New methods
- `place_technic_pin(file, color, x, y, z, length='short')` — places 2780.dat or 6558.dat.
- `place_technic_beam(file, color, x, y, z, length='1x4')` — places liftarm or beam.
- `place_brickheadz_eye(color, x, y, z)` — places 22885.dat with the canonical stud-up rotation.
- `place_modular_roof_tile(color, x, y, z, slope='33')` — places 3622/3623 with the canonical mansard slope.
- `build_brickheadz_set(name, colors)` — generates a BrickHeadz display block.
- `build_modular_building_roof(width=8, depth=6, colors)` — generates a tiled mansard roof using R28 vocabulary.
- `build_technic_subassembly(name, n_pins)` — generates a Technic sub-build with N pins → M beams.

### Updated demos (5 → 7)

| Demo | Pieces | STEPs | Files | Reflections | Theme |
|------|-------:|------:|------:|-------------:|-------|
| `demo_town.ldr` | 29 | 12 | 9 | 0 | Town |
| `demo_kid.ldr` | 18 | 7 | 6 | 0 | City |
| `demo_classic.ldr` | 1 | 1 | 1 | 0 | Town |
| `demo_castle_lion_knights.ldr` | 28 | 9 | 7 | 4 | Castle |
| `demo_space_classic.ldr` | 18 | 8 | 6 | 0 | Space |
| **`demo_technic_pin_chain.ldr`** | **22** | **9** | **8** | **0** | **Technic (R26)** |
| **`demo_brickheadz_block.ldr`** | **16** | **7** | **6** | **0** | **Brickheadz (R27)** |

All demos pass `validate()` with 0 errors, 0 warnings.

---

## 9. Limitations

1. **1438 / ~1470 = 97.8% of OMR** — near-complete coverage. The 32 OMR sets not downloaded are in themes with 1-2 sets each (e.g., LEGO Art 31203, Mindstorms EV3 31313, Znap 2129) where OMR may not have an MPD.
2. **No greenfield MPDs**: analysis only covers what OMR has. Off-OMR MOCs (community builds) and BrickLink Studio exports are not represented.
3. **No analysis of TEXMAP/textures** — many post-2015 sets use PNG textures on flat surfaces.
4. **No analysis of TEXMAP-aligned sub-builds** — Icon and Modular sets frequently use 2D-textured panels.
5. **No analysis of BFC NOCLIP vs CW-only vs CCW-only** — only BFC CERTIFY presence is recorded.
6. **Theme attribution**: a few sets have `theme_full = "None"` (literal string) in metadata — these are Brickheadz and some Specialty sets. Cohort assignment works correctly.
7. **TEXMAP-aligned sub-builds** — Icons sets frequently use TEXMAP; not currently analyzed.
8. **BFC NOCLIP** flags are not extracted — only BFC CERTIFY is counted.

---

## 10. Resources

| Resource | Path | Description |
|----------|------|-------------|
| MD 2 sets (legacy) | `LEARNED_CONVENTIONS.md` | Beetle + Pet Shop |
| MD 100 sets (legacy) | `LEARNED_CONVENTIONS_100.md` | 80s/90s |
| MD 300 sets (legacy) | `LEARNED_CONVENTIONS_300.md` | 80s/90s + Kids |
| MD 532 sets (legacy) | `LEARNED_CONVENTIONS_532.md` | 23 rules, 3 cohorts |
| **MD 1438 sets (canonical)** | **`LEARNED_CONVENTIONS_1438.md`** | **This document, 32 rules, 8 cohorts** |
| Corpus 80s/90s | `corpus/mpds/` | 100 MPDs |
| Corpus kids | `corpus/mpds_kids/` | 200 MPDs |
| Corpus classic | `corpus/mpds_classic/` | 232 MPDs |
| Corpus modern | `corpus/mpds_modern/` | 287 MPDs |
| Corpus technic | `corpus/mpds_technic/` | 175 MPDs |
| Corpus specialty | `corpus/mpds_specialty/` | 165 MPDs |
| Corpus licensed | `corpus/mpds_licensed/` | 121 MPDs |
| Corpus classic gaps | `corpus/mpds_classic_gaps/` | 158 MPDs |
| Setlists | `corpus/setlist_*.{txt,json}` | 8 setlists |
| Cross-corpus aggregate JSON | `analysis/cross_corpus3_stats.json` | All 1438 stats |
| Per-set JSON | `analysis/per_set_stats_1438.json` | 1438 entries |
| Generator | `generator/ldraw_gen.py` | 1161+ lines, 7 demos |
| Demos | `generator/demo_*.ldr` | 7 validated demos |

---

## 11. Knowledge gaps and next-session plan

### Themes not fully covered (residual)

| Theme | Sets in OMR | Status |
|-------|------------:|:------:|
| LEGO Art | 3 | 1 set downloaded |
| Mindstorms | 2 | 1 set downloaded |
| Mixels | 7 | 7 sets downloaded |
| DOTS | 1 | 1 set downloaded |

### Open analysis questions

1. **BFC NOCLIP** — how many sets use `0 BFC NOCLIP` vs `0 BFC CERTIFY`? The current parser only counts CERTIFY.
2. **TEXMAP textures** — post-2015 Icon/Architecture sets use PNG textures; their MPDs include `0 !TEXMAP ...` lines. Parser ignores them.
3. **Custom parts breakdown** — 4470 custom parts are concentrated in Technic (1691) and Kids (818). What's the breakdown by file extension (`s\`, `48\`, `p\`, etc.)?
4. **Sub-build nesting** — sub-models can reference other sub-models. The current parser treats each top-level sub-build independently. A nested analysis would reveal which sets are "highly modularized" (e.g., 10294 Titanic has 288 sub-builds — how deep does the nesting go?).
5. **BFC flag combinations** — `BFC CERTIFY CCW`, `BFC CERTIFY CW`, `BFC NOCLIP` — distribution by cohort.
6. **Matrix rotation history** — the 3668 reflections cluster in 2 themes (Space, Technic). Is there a third cluster in post-2020 sets?
7. **Color trends** — the top-20 colors have stable rank across corpora, but the specialty cohort introduces `272` (light blue), `256` (medium blue) and `320` (dark red) at the cost of `47` (dark pink).

---

## 12. Appendices

### Appendix A — Cohort directory layout

| Cohort | Directory | Set count | First set | Last set |
|--------|-----------|----------:|-----------|----------|
| 80s/90s | `corpus/mpds/` | 100 | 1591 | 7072 |
| Kids | `corpus/mpds_kids/` | 200 | 2149 | 76042 |
| Classic | `corpus/mpds_classic/` | 232 | 106 | 7832 |
| Modern | `corpus/mpds_modern/` | 287 | 358 | 10359 |
| Technic | `corpus/mpds_technic/` | 175 | 850 | 42125 |
| Specialty | `corpus/mpds_specialty/` | 165 | 390 | 41630 |
| Licensed | `corpus/mpds_licensed/` | 121 | 30050 | 8158 |
| Classic gaps | `corpus/mpds_classic_gaps/` | 158 | 6361 | 4010 |

### Appendix B — Y-layer exceptions (R32)

| Y | Count | Source | Likely cause |
|---|------:|--------|--------------|
| -20 | 9030 | Technic + Modern | Half-brick offset for sub-beam |
| +20 | 5180 | Technic | Half-brick above baseplate |
| +10 | 4877 | Technic | Half-plate for connector block |
| -0.5 | 1140 | slopes | Slope mid-Y |
| -20 | 1313 | deltas | dy=-20 offset |

All other top-30 Y-layers are multiples of 8 (0, ±8, ±16, ±24, ±32, ±40, ±48, ±56, ±64, ±72, ±80).

### Appendix C — Top reflections (R29)

| Set | Cohort | Reflections | Pieces | Ratio |
|-----|--------|------------:|-------:|------:|
| 6780-1 | Classic (Space) | 196 | 411 | 47.69% |
| 8245-1 | Technic | 495 | 1165 | 42.49% |
| 6941-1 | Classic (Space) | 192 | 488 | 39.34% |
| 8257-1 | Technic | 407 | 1231 | 33.06% |
| 6988-1 | Classic-gaps (Space) | 183 | 582 | 31.44% |
| 6990-1 | Classic (Space) | 296 | 1075 | 27.53% |
| 6987-1 | Classic-gaps (Space) | 144 | 748 | 19.25% |
| 42000-1 | Technic | 226 | 1377 | 16.41% |
| 70814-1 | Licensed (LEGO Movie) | 132 | 817 | 16.16% |
| 10190-1 | Classic (Space) | 208 | 1390 | 14.96% |
| 21303-1 | Specialty (WALL•E) | 98 | 718 | 13.65% |
| 6891-1 | Classic-gaps (Space) | 98 | 244 | 40.16% |
| 70816-1 | Licensed (LEGO Movie) | 66 | 1007 | 6.55% |
| 6986-1 | Classic (Space) | 61 | 562 | 10.85% |
| 6973-1 | Classic-gaps (Space) | 53 | 503 | 10.54% |

### Appendix D — BFC CERTIFY by cohort

| Cohort | BFC CERTIFY / Sets | % |
|--------|-------------------:|---:|
| Technic | 138/175 | **78.9%** |
| Licensed | 60/121 | 49.6% |
| Kids | 73/200 | 36.5% |
| Specialty | 60/165 | 36.4% |
| **Corpus 1438** | **510/1438** | **35.5%** |
| Modern | 79/287 | 27.5% |
| Classic gaps | 41/158 | 25.9% |
| 80s/90s | 21/100 | 21.0% |
| Classic | 38/232 | **16.4%** |

---

**End of canonical doc. See `STATE.json` for current corpus state and `analysis/findings_*.md` (legacy) for cohort/theme drilldowns.**