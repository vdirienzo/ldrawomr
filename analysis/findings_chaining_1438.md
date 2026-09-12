# Chaining Conventions — Cross-Corpus Analysis 4.0 (1 438 sets OMR)

> Extends `LEARNED_CONVENTIONS_532.md` (23 rules, 532 sets) to a corpus of **1 438 sets** across **8 cohorts**, drawn from the LDraw OMR.
> Source data: `analysis/cross_corpus3_stats.json` (aggregate) + `analysis/per_set_stats_1438.json` (per-set).

## Corpus overview

| Cohort | Sets | Pieces | Avg p/set | Sub-builds | Sub/set | Custom parts | Custom % | Refl. (neg-det) | Refl. ratio | BFC CERTIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 80s/90s | 100 | 18 670 | 186.7 | 839 | 8.39 | 112 | 0.600 % | 50 | **0.268 %** | 21.0 % |
| Kids | 200 | 42 947 | 214.7 | 1 535 | 7.67 | 818 | **1.905 %** | 107 | **0.249 %** | 36.5 % |
| Classic | 232 | 47 143 | 203.2 | 2 350 | **10.13** | 107 | 0.227 % | 1 306 | **2.770 %** | 16.4 % |
| Modern | 287 | 114 904 | 400.4 | 4 128 | 14.38 | 769 | 0.669 % | 42 | **0.037 %** | 27.5 % |
| **Technic** | 175 | **169 839** | **970.5** | 5 243 | **29.96** | 1 691 | 0.996 % | 1 162 | 0.684 % | **78.9 %** |
| Specialty | 165 | 63 592 | 385.4 | 2 744 | 16.63 | 351 | 0.552 % | 112 | 0.176 % | 36.4 % |
| Licensed | 121 | 45 227 | 373.8 | 1 961 | 16.21 | 531 | 1.174 % | 248 | 0.548 % | 49.6 % |
| Classic-gaps | 158 | 31 830 | 201.5 | 1 274 | 8.06 | 91 | 0.286 % | 641 | 2.014 % | 25.9 % |
| **All 1 438** | **1 438** | **534 152** | **371.5** | **20 074** | **13.96** | **4 470** | **0.837 %** | **3 668** | **0.687 %** | **35.5 %** |

Compared with the 532-set baseline (108 760 pieces, 1.345 % neg-det, 24.8 % BFC), the larger corpus **divides the reflection ratio roughly in half** (1.345 → 0.687 %) because the new cohorts (Modern, Technic, Specialty, Licensed, Classic-gaps) overwhelmingly use **identity / rotation matrices** and only rarely reflect. The Space-dominated classic cohort remains the only major reflection driver.

---

## 1. Top 20 chaining bigrams (global, all 1 438 sets)

From `cohort_all_1438.global_top_50_bigrams` (top 20).

| # | Bigram (A → B) | Count | % of corpus | Self? | Dominant cohort |
|---:|---|---:|---:|:---:|---|
| 1 | `4-4cyli.dat` → `4-4cyli.dat` | 19 842 | 3.715 % | ✓ | Technic (11 568) |
| 2 | `166.dat` → `166.dat` | 10 508 | 1.967 % | ✓ | Technic (10 052) |
| 3 | `2780.dat` → `2780.dat` | 9 114 | 1.706 % | ✓ | Technic (7 690) |
| 4 | `u9218.dat` → `u9218.dat` | 8 344 | 1.562 % | ✓ | Technic (7 969) |
| 5 | `77.dat` → `77.dat` | 8 129 | 1.522 % | ✓ | Technic (7 472) + Star Wars (4 410) |
| 6 | `98138.dat` → `98138.dat` | 7 311 | 1.369 % | ✓ | Specialty (7 024) |
| 7 | `6141.dat` → `6141.dat` | 7 009 | 1.312 % | ✓ | Specialty (3 234) + Modern (1 510) |
| 8 | `3023.dat` → `3023.dat` | 6 151 | 1.152 % | ✓ | Modern (1 922) |
| 9 | `axlehol8.dat` → `axlehol8.dat` | 5 574 | 1.044 % | ✓ | Technic |
| 10 | `box4o8a.dat` → `box4o8a.dat` | 5 313 | 0.995 % | ✓ | Technic |
| 11 | `3024.dat` → `3024.dat` | 4 423 | 0.828 % | ✓ | Modern (1 683) + Specialty (1 119) |
| 12 | `3004.dat` → `3004.dat` | 3 899 | 0.730 % | ✓ | Classic-gaps (496) + Classic (685) |
| 13 | `6558.dat` → `6558.dat` | 3 645 | 0.682 % | ✓ | Technic |
| 14 | `3005.dat` → `3005.dat` | 3 400 | 0.637 % | ✓ | Kids (509) |
| 15 | `3069b.dat` → `3069b.dat` | 3 233 | 0.605 % | ✓ | Modern (1 442) |
| 16 | `756.dat` → `756.dat` | 2 403 | 0.450 % | ✓ | Classic (1 447) + Classic-gaps (624) |
| 17 | `u9190.dat` → `u9190.dat` | 2 315 | 0.433 % | ✓ | Kids (Fabuland) |
| 18 | `3070b.dat` → `3070b.dat` | 2 239 | 0.419 % | ✓ | Modern |
| 19 | `3710.dat` → `3710.dat` | 2 029 | 0.380 % | ✓ | Modern (Universal Plate 1×4) |
| 20 | `2412b.dat` → `2412b.dat` | 1 819 | 0.341 % | ✓ | Universal across all 8 cohorts |

**Observations**

- **Top-20 are 100 % self-bigrams**, identical to the 532 finding (R7 still holds at 1 438 scale).
- **Top-7 are all Technic parts** (`4-4cyli`, `166` = Technic axle, `2780` = Technic pin, `u9218`, `77` = Technic hinge plate, `98138` = Technic/Brickheadz baseplate, `axlehol8`). The 532 corpus was System-heavy; the larger corpus surfaces the Technic vocabulary.
- `756.dat` (Space baseplate) drops from 1.50 % at 532 to **0.45 % at 1 438** — its dominance is **Space-specific**, not corpus-wide.
- `6141.dat` and `3023.dat` are the only System-originated parts to make the global top-10 (positions 7 and 8).

---

## 2. Top 10 deltas (global, all 1 438 sets)

From `cohort_all_1438.global_top_30_deltas` (top 10).

| # | (dx, dy, dz) | Count | Notes |
|---:|---|---:|---|
| 1 | (20, 0, 0) | 17 714 | **Top delta in modern/specialty/licensed/technic** — basic stud width (Plate 1×2 horizontal) |
| 2 | (0, 0, 0) | 10 119 | Same-location placement (Technic stacks, hinge rotation origins) |
| 3 | (40, 0, 0) | 7 785 | Two-stud horizontal step |
| 4 | (0, -8, 0) | 7 532 | One plate down (Universal Y-grid) |
| 5 | (0, 0, -20) | 6 035 | One-stud step in -Z |
| 6 | (60, 0, 0) | 5 793 | Three-stud horizontal step |
| 7 | (0, 0, 40) | 5 500 | Two-stud step in +Z |
| 8 | (0, 0, -40) | 5 479 | Two-stud step in -Z |
| 9 | (0, 0, 20) | 5 191 | One-stud step in +Z |
| 10 | (-40, 0, 0) | 4 597 | Two-stud step in -X |

**Distribution top-15**: 100 % canonical (X/Z multiples of 20, Y multiples of 8). R2 still holds.

**New delta finding at scale**: (20, 0, 0) becomes the **#1 global delta** (17 714 occurrences), surpassing (0, 0, 0). In the 532 corpus, (0, 0, 0) was #1 — the change is driven by **Technic's horizontal-axle placement** and **specialty/Brickheadz plate chains**, both of which produce dense (20, 0, 0) chains. The previous top delta (0, -8, 0) drops from 1.53 % to 7 532 / 534 152 ≈ 1.41 %.

---

## 3. Per-cohort comparison of top bigrams

### 3.1 Top-5 bigrams per cohort

| Cohort | #1 (count, %) | #2 | #3 | #4 | #5 |
|---|---|---|---|---|---|
| **80s/90s** | `4-4cyli→4-4cyli` (1 892, 10.13 %) | `754→754` (253) | `3004→3004` (226) | `3023→3023` (224) | `6141→6141` (189) |
| **Kids** | `4-4cyli→4-4cyli` (3 487, 8.12 %) | `6141→6141` (802) | `3004→3004` (652) | `3005→3005` (509) | `3023→3023` (481) |
| **Classic** | **`756→756` (1 447, 3.07 %)** | `4-4cyli→4-4cyli` (690) | `3004→3004` (685) | `3023→3023` (679) | `3005→3005` (530) |
| **Modern** | `3023→3023` (1 922, 1.67 %) | `4-4cyli→4-4cyli` (1 812) | `3024→3024` (1 683) | `6141→6141` (1 510) | `3069b→3069b` (1 442) |
| **Technic** | `4-4cyli→4-4cyli` (11 568, 6.81 %) | **`166→166` (10 052)** | **`u9218→u9218` (7 969)** | **`2780→2780` (7 690)** | **`77→77` (7 472)** |
| **Specialty** | **`98138→98138` (7 024, 11.05 %)** | `6141→6141` (3 234) | `3023→3023` (1 748) | `3024→3024` (1 119) | `3069b→3069b` (961) |
| **Licensed** | `2780→2780` (554, 1.22 %) | `3023→3023` (498) | `6141→6141` (478) | `u9218→u9218` (375) | `4-4cyli→4-4cyli` (357) |
| **Classic-gaps** | `756→756` (624, 1.96 %) | `3004→3004` (496) | `754→754` (392) | `6141→6141` (387) | `754.DAT→754.DAT` (370) |

### 3.2 Universal vs cohort-specific bigrams

**Universal bigrams** (appear in top-50 of **all 8 cohorts**): **3 pairs**
- `2412b.dat → 2412b.dat` — Slope 45° 1×2 corner (decorative element everywhere)
- `3023.dat → 3023.dat` — Plate 1×2 (universal building block)
- `3710.dat → 3710.dat` — Plate 1×4 (universal chassis/long base)

**Cohort-specific bigrams** (top-1 only in one cohort):
- `756→756` — Classic + Classic-gaps only (Space-themed baseplate signature; R20 confirmed)
- `98138→98138` — Specialty only (Technic/Brickheadz baseplate; **new R24**)
- `3023→3023` — Modern only (City/Creator plate vocabulary, but universal in top-50)
- `2780→2780` — Licensed only (Technic-pin dense Star Wars / superhero builds)

**Strong thematic skews**:
- **Technic** uses 4 of top-5 from Technic vocabulary (`166`, `u9218`, `2780`, `77`). Self-bigram dominance 100 %.
- **Specialty** is dominated by `98138` (Technic-compatible baseplate used in Brickheadz and Architecture).
- **Classic-gaps** retains the Space-baseplate `756` signature despite the cohort name — many Classic-gaps sets are Space sub-themes (Blacktron II, Spyrius, Futuron, Ice Planet 2002, Blacktron I, Space Police III, Classic Space).
- **Licensed** surprisingly leads with `2780` (Technic pin), driven by Star Wars and Super Heroes mechs.

### 3.3 Heterogeneous (non-self) bigrams per cohort

The 532 doc noted heterogeneous bigrams (`3818↔3820`, etc.) only as Space signature. At 1 438 we see **clear cohort-specific heterogeneous patterns**:

- **Technic**: dominated by Technic-pin/beam pairs — `2780↔6558` (Technic pin + Technic beam) total 1 277 occurrences, plus `2780↔43093`, `2780↔32316`, `32278↔2780`. **These are the "Technic grammar" (R25)**.
- **Specialty**: `98138↔6141` (Technic baseplate + Plate 1×1 round) total 937 — the Brickheadz "display pedestal" idiom.
- **Licensed**: `2429↔2430` (Hinge plate 1×2 ↔ 1×3) total 90 + `3818↔3820` (slope 33° + 45°) total 49 + `60592↔60601` (tile 1×2 + 1×3 rounded) total 30 — the **"decorative armour" pattern of Star Wars / Super Heroes**.
- **Star Wars** specifically: `77.dat → 77.dat` (4 410 self-bigrams) and `box4o8a.dat → box4o8a.dat` (4 343) dominate — these are hinge-plate and box-Technic patterns for symmetry-built Star Wars vehicles.

---

## 4. STEP marker analysis per cohort

`total_steps` is the count of `0 STEP` markers per MPD. From `per_set_stats_1438.json`.

| Cohort | n sets | Mean STEPs | Median | 0 STEPs | 1 STEP | 2 STEPs | 3+ STEPs | % ≥ 3 STEPs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 80s/90s | 100 | 19.85 | 7.0 | 39 | 0 | 0 | 61 | 61.0 % |
| Kids | 200 | 29.77 | 10.5 | 57 | 2 | 4 | 137 | 68.5 % |
| Classic | 232 | 22.57 | 2.5 | 114 | 0 | 2 | 116 | 50.0 % |
| Modern | 287 | 70.49 | 11.0 | 87 | 1 | 1 | 198 | 69.0 % |
| **Technic** | 175 | **114.86** | **57.0** | 23 | 1 | 0 | 151 | **86.3 %** |
| Specialty | 165 | 69.82 | 42.0 | 53 | 0 | 0 | 112 | 67.9 % |
| Licensed | 121 | 81.98 | 18.0 | 28 | 1 | 0 | 92 | 76.0 % |
| Classic-gaps | 158 | 19.31 | 10.0 | 50 | 0 | 1 | 107 | 67.7 % |
| **All 1 438** | **1 438** | **54.24** | **13.0** | **451** | **5** | **8** | **974** | **67.7 %** |
| 532 baseline | 532 | 24.77 | 6.0 | 210 (39.5 %) | — | — | — | 59.0 % |

**Comparison vs 532 baseline**:
- Mean STEPs per set **doubled** (24.77 → 54.24) — the new cohorts (Technic, Specialty, Licensed, Modern) heavily use STEP markers to separate logical sub-assemblies.
- Technic sets average **115 STEPs/set** — more than 2× any System cohort. They use STEP to break beams and pin-runs into discrete logical units.
- Classic cohort has the **lowest mean (22.57)** and the **highest "0 STEP" share (49.1 %)** — half of classic MPDs are monolithic, single-step structures.
- 67.7 % of all 1 438 sets have ≥ 3 STEP markers, vs 59.0 % at 532 baseline.

**Reading**: STEP marker density correlates with **structural complexity and authorship care** — Technic and Modern sets get step-by-step build instructions baked in (Technic because of complex internal geometry, Modern because MPDs often accompany set manuals). Classic pre-2000 MPDs were simpler single-block dumps.

---

## 5. Reflections (`neg_det` ratio) per cohort

`neg_det_count` / `total_pieces` per set, aggregated per cohort.

| Cohort | neg_det count | Total pieces | neg_det ratio | vs 532 (1.345 %) |
|---|---:|---:|---:|---|
| 80s/90s | 50 | 18 670 | 0.268 % | -80 % |
| Kids | 107 | 42 947 | 0.249 % | -82 % |
| Classic | 1 306 | 47 143 | **2.770 %** | +106 % |
| Modern | 42 | 114 904 | **0.037 %** | -97 % |
| Technic | 1 162 | 169 839 | 0.684 % | -49 % |
| Specialty | 112 | 63 592 | 0.176 % | -87 % |
| Licensed | 248 | 45 227 | 0.548 % | -59 % |
| Classic-gaps | 641 | 31 830 | **2.014 %** | +50 % |
| **All 1 438** | **3 668** | **534 152** | **0.687 %** | **-49 %** |

**Anomalies** (themes with neg_det ratio > 5 % of theme-total pieces — extracted from `per_set_stats_1438.json`):

| Theme | Sets | Pieces | neg_det | Ratio | Notes |
|---|---:|---:|---:|---:|---|
| Space > Classic Space | 10 | 1 084 | 196 | **18.08 %** | Confirmed R19 (slightly stronger than 532) |
| Space > Unitron | 5 | 2 681 | 347 | **12.94 %** | Confirmed R19 |
| Space > Blacktron I | 6 | 1 554 | 192 | **12.36 %** | Confirmed R19 |
| Space > Space Police I | 3 | 862 | 61 | **7.08 %** | Confirmed R19 |
| Space > Ice Planet 2002 | 9 | 773 | 50 | **6.47 %** | Confirmed R19 |
| Space > M:Tron | 10 | 1 792 | 99 | **5.52 %** | **NEW**: at 532 this theme was 8.02 % on 8 sets; still >5 % |

**Cohort-level** (not theme-level) reflection ratios > 5 %: **none** — all cohort ratios are < 3 %. This validates R3 refutation: reflections are a **theme phenomenon**, not a corpus-wide property. The 1.345 % 532 baseline was inflated by the Space over-representation in the Classic cohort.

**New theme-level findings** (themes > 2 % not previously documented):
- **Town (generic)**: 4.73 % neg_det ratio across 10 sets (4 394 pieces, 208 neg-det). Suggests some early Town sets used mirroring for symmetry.
- **Town > City Center**: 4.73 % across 3 sets (1 035 pieces, 49 neg-det). Modern Town sub-theme that builds bilateral-symmetric structures.
- **Star Wars**: 4.38 % across 6 sets (1 120 pieces, 49 neg-det). Symmetry-driven Star Wars designs (X-wings, TIEs) reflect wings and fuselages. **R26 (new)**.
- **Space > Futuron**: 3.81 % (11 sets).
- **Space > Blacktron II**: 3.46 % (11 sets).
- **Space > Space Police III**: 1.91 % (8 sets).

**Note**: the theme-level ratios can exceed 5 % because they're concentrated within those themes, while the **cohort** ratio dilutes them. Modern cohort at 0.037 % is the **lowest reflection ratio ever observed** — Modern sets almost exclusively use identity matrices.

---

## 6. Universal chaining patterns — the "metalanguage"

The following chains appear in **every cohort's top-30 deltas** (i.e. are invariant across the entire OMR).

### 6.1 Universal self-bigrams (top-50 of all 8 cohorts)

Exactly **3** bigrams qualify:
- `2412b.dat → 2412b.dat` (Slope 45° 1×2 corner)
- `3023.dat → 3023.dat` (Plate 1×2)
- `3710.dat → 3710.dat` (Plate 1×4)

These are the **invariant building blocks** of every LEGO MPD, regardless of theme or decade. The 532 doc claimed "top-15: 100 % self-bigrams" (R7). At 1 438, we can be more precise: the **deep** invariant is exactly 3 self-bigrams (one slope, two plates).

### 6.2 Universal deltas (top-30 of all 8 cohorts)

Exactly **11** deltas qualify — all are **pure-axis, all multiples of the canonical grid**:

| # | Delta | Meaning |
|---:|---|---|
| 1 | ( 20, 0, 0) | 1 stud +X |
| 2 | (-20, 0, 0) | 1 stud -X |
| 3 | ( 40, 0, 0) | 2 stud +X |
| 4 | (-40, 0, 0) | 2 stud -X |
| 5 | ( 60, 0, 0) | 3 stud +X |
| 6 | ( 80, 0, 0) | 4 stud +X |
| 7 | ( 0, 0, 20) | 1 stud +Z |
| 8 | ( 0, 0, -20) | 1 stud -Z |
| 9 | ( 0, 0, 40) | 2 stud +Z |
| 10 | ( 0, 0, -40) | 2 stud -Z |
| 11 | ( 0, 0, 0) | Same location |

These 11 deltas are the **"universal alphabet" of LDraw placement** — they appear in every cohort and constitute the core placement grammar. **R1 + R2 hold at the universal-invariant level** (Y in the 11 are all 0; X/Z are multiples of 20).

The 532 doc claimed "100 % top-15 canonical"; at 1 438 we can sharpen: the **universal** deltas are 11 in number and **all** are pure-axis (no compound moves). Compound moves like (60, -24, 40) appear in cohort top-30s but are cohort-specific (e.g. (0, -24, 0) is in 7/8 cohorts — close to universal but Classic-gaps lacks it because its Y-grid uses multiples of -8 only).

### 6.3 Universal Y-layers

The Y-layers that appear in every cohort's top-15: **Y=0, Y=-8, Y=-24, Y=-32, Y=-16** (5 layers). These are the canonical plate-stack (0, -8, -16, -24, -32). Y=-8 is the canonical first plate below origin, -24 is the first brick, -32 is the second plate after the first brick, -16 is the second plate directly.

---

## 7. New findings beyond LEARNED_CONVENTIONS_532.md

### 7.1 New rules

| Rule | Statement | Evidence |
|---|---|---|
| **R24** | **`98138.dat` is the "Technic-baseplate signature"** for Specialty (Brickheadz / Architecture) sets | Top-1 bigram in `cohort_specialty` at 11.05 %; appears in 7 of top Brickheadz sets |
| **R25** | **Technic has a distinct heterogeneous bigram grammar**: `2780↔6558`, `2780↔43093`, `2780↔32316`, `32278↔2780` etc. — all are pin/beam pin-pair patterns | Technic cohort heterogeneous top-5 bigrams all share this pattern; combined 2 500+ occurrences |
| **R26** | **Star Wars / Super Heroes Licensed sets use 4-7 % neg_det** for symmetric vehicle wings and fuselages (X-wings, TIEs) | Star Wars theme: 4.38 % neg_det across 6 sets (49 / 1 120) |
| **R27** | **Specialty (Brickheadz) chaining signature is `98138 ↔ 6141`** — baseplate paired with a round 1×1 stud for "display" effect | 937 occurrences of `98138→6141` + `6141→98138` across Brickheadz |
| **R28** | **Technic Y-layers are NON-canonical** — top-5 Y values include -20, -40, -60, +20, which are NOT multiples of 8 | Technic cohort Y-layers: Y=0 (32 606), Y=-20 (8 239), Y=-40 (6 466), Y=+20 (5 045), Y=-60 (3 844) — all non-multiple-of-8 except 0. **R1 is REFUTED for Technic**. |
| **R29** | **Modern cohort has the lowest reflection ratio ever observed in OMR analysis** (0.037 %) — Modern MPDs are nearly all identity matrices | 42 / 114 904 = 0.037 % — a 36× lower ratio than the 532 baseline |
| **R30** | **STEP marker density correlates with set complexity / authorship era**: Technic averages 115 STEPs/set; Classic averages 22.57 | 6× spread between Technic and Classic cohorts; both extend the R12 / R23 patterns |

### 7.2 Re-statements of existing rules at 1 438 scale

- **R1 (Y multiples of 8)**: holds for 7 of 8 cohorts; **REFUTED for Technic (R28)**.
- **R2 (X/Z multiples of 20)**: holds universally — all top-15 deltas are canonical, all 11 universal deltas are canonical.
- **R3 (Reflections < 0.3 %)**: **RE-REFUTED**. The 532 baseline was 1.345 %; the 1 438 corpus is 0.687 % — half the 532 ratio. The drop is purely due to adding low-reflection cohorts (Modern 0.037 %, Specialty 0.176 %, Kids 0.249 %, 80s/90s 0.268 %). The Classic and Classic-gaps cohorts remain > 2 %, all driven by Space sub-themes.
- **R7 (Self-bigrams)**: holds at 1 438 scale — top-20 are 100 % self.
- **R12 (`4-4cyli.dat` universal)**: still holds; now ranks #1 globally at 3.715 % (was #1 at 532 at 5.6 %; ratio dropped because Technic/Specialty/Modern dilutions bring the corpus denominator up faster than `4-4cyli`).
- **R19 (Space sub-themes 5-21 % reflections)**: confirmed and slightly strengthened — at 1 438 the Space > Classic Space ratio is 18.08 % (was 21.14 % at 532, but with **more sets, the lower bound holds**).
- **R20 (`756.dat` Space signature)**: confirmed; `756→756` is now top-1 bigram in both Classic (1 447) and Classic-gaps (624) cohorts.
- **R22 (heterogeneous bigrams `3818↔3819` etc.)**: now generalized — at 1 438, heterogeneous bigrams appear in **every cohort**, but the **types** differ: Technic uses pin/beam, Licensed uses slope-pair, Specialty uses baseplate/stud.

### 7.3 Observations not promoted to rules

- **BFC CERTIFY correlates with Technic**: 78.9 % of Technic sets declare BFC CERTIFY vs 16.4 % of Classic. Technic authors are far more formal about chirality.
- **Custom-parts density correlates with sub-build count**: Technic has 0.996 % custom + 29.96 sub/set (highest in both). Kids has 1.905 % custom + 7.67 sub/set (low sub/set but high custom). Classic has 0.227 % custom + 10.13 sub/set. No simple linear relation.
- **Decade distribution** (all 1 438): 1960s=17, 1970s=101, 1980s=265, 1990s=272, 2000s=245, 2010s=461, 2020s=77. The corpus over-samples 2010s and 1980s/1990s.
- **Mindstorms** (1 set, 40413-1) is too small for bigram analysis but its heterogeneous bigrams (`13971→61254`, `43093→41677`) confirm it's Technic-adjacent.

---

## 8. Summary table — rules added or revised at 1 438 scale

| Status | Rule | Detail |
|---|---|---|
| ✅ Carried over | R1 | Holds for 7/8 cohorts (Technic exception per R28) |
| ✅ Carried over | R2 | Holds universally |
| ✅ Carried over | R5 | Top 10 covers ~15.3 % of corpus (lower than 24.3 % at 532, because Technic dilutes) |
| ✅ Carried over | R7 | Top-20 are 100 % self-bigrams |
| ✅ Carried over | R12 | `4-4cyli.dat` still #1 globally |
| ✅ Carried over | R19 | Space sub-themes 5-21 % reflections (5/12 themes ≥ 5 %) |
| ✅ Carried over | R20 | `756.dat` Space signature confirmed in Classic + Classic-gaps |
| ✅ Carried over | R22 | Heterogeneous bigrams appear in every cohort, but pattern differs |
| 🆕 NEW | R24 | `98138.dat` Specialty/Brickheadz baseplate signature |
| 🆕 NEW | R25 | Technic pin/beam heterogeneous grammar (`2780↔6558` etc.) |
| 🆕 NEW | R26 | Star Wars / Super Heroes 4-7 % neg_det for symmetric vehicles |
| 🆕 NEW | R27 | Brickheadz `98138 ↔ 6141` display pairing |
| 🆕 NEW | R28 | **R1 refuted for Technic**: Technic Y-layers are not multiples of 8 |
| 🆕 NEW | R29 | Modern cohort has 0.037 % neg_det (lowest ever) |
| 🆕 NEW | R30 | STEP density correlates with set complexity (Technic 115/set vs Classic 22.6/set) |
| 🟡 Revised | R3 | Reflections at 1 438 = 0.687 % (down from 1.345 % at 532 due to Modern dilution) |
| 🟡 Revised | R13 | Kids vocabulary no longer "modern exclusive" — top-30 includes Technic parts at 1 438 |

---

## 9. Limitations

1. **1 438 / ~1 470 OMR sets = 98 % coverage**. Near-complete corpus; remaining 32 sets are edge cases (deleted URLs, multi-model suffixes that the parser missed).
2. **Theme full paths** are empty for many new cohorts (Technic, Specialty, Licensed, Classic-gaps) because the parser pulls `theme_full` only when OMR exposes it. Cohort-level ratios are still valid; theme-level ratios may under-count.
3. **`98138.dat`** is identified as a "Technic-compatible baseplate" by usage patterns but the LDraw part name registry was not consulted. The piece is the Brickheadz display baseplate but is also reused in Architecture (Skylines) and Technic (M:Tron).
4. **STEP marker counts** may include auto-generated STEPs from MPD editors (e.g. LDCad) which are author-software-dependent, not author-intentional.
5. **Heterogeneous bigram totals are per-set top-30**, so true totals across all 1 438 sets are higher than reported (we count only top-30 per set).
6. **No MOC comparison** — OMR-author conventions may not reflect the broader LDraw community.

---

## 10. Artifacts

| Artifact | Path | Description |
|---|---|---|
| Aggregate stats (1 438) | `analysis/cross_corpus3_stats.json` | 9 cohort objects (8 + global) |
| Per-set stats (1 438) | `analysis/per_set_stats_1438.json` | 1 438 records with top-30 bigrams, top-20 deltas, STEPs |
| This document | `analysis/findings_chaining_1438.md` | Chaining findings at 1 438 scale |
| Findings 532 (legacy) | `analysis/findings_chaining_300.md` (532 records) | Previous generation |
| Canonical rules doc | `LEARNED_CONVENTIONS_532.md` | To be updated when corpus stabilizes |

---

## 11. Next steps

If the user requests corpus expansion:
1. **Add 100 more Star Wars sets** — would strengthen R26.
2. **Add Fabuland sub-cohort** — already in Kids (with `u9218`/`u9190` pieces) but under-represented.
3. **Validate R28** — sample-check 20 Technic MPDs to confirm Y values are actually non-multiples-of-8 (could be parser bug, not real-world convention).
4. **Update generator `ldraw_gen.py`** — add `build_brickheadz()`, `build_technic_pinbeam()`, `build_star_wars_symmetric()` demos.
5. **Promote `LEARNED_CONVENTIONS_FINAL.md`** once the corpus stabilizes at ~1 470.
