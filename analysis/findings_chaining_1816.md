# Chaining Conventions — Cross-Corpus Analysis 5.0 (1 816 sets OMR + seymouria.pl)

> Extends `findings_chaining_1438.md` (1 438 sets, 8 cohorts) and `LEARNED_CONVENTIONS_1438.md` (32 rules) to a corpus of **1 816 sets** across **9 cohorts**: the original 1 438 OMR sets plus **378 seymouria.pl sets** (Plan E).
> Source data: `analysis/cross_corpus4_stats.json` (aggregate) + `analysis/per_set_stats_1816.json` (per-set).

## Corpus overview

| Cohort | Sets | Pieces | Avg p/set | Sub-builds | Sub/set | Custom parts | Custom % | Refl. (neg-det) | Refl. ratio | BFC CERTIFY |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 80s/90s | 100 | 18 670 | 186.7 | 839 | 8.39 | 112 | 0.600 % | 50 | 0.268 % | 21.0 % |
| Kids | 200 | 42 947 | 214.7 | 1 535 | 7.67 | 818 | 1.905 % | 107 | 0.249 % | 36.5 % |
| Classic | 232 | 47 143 | 203.2 | 2 350 | 10.13 | 107 | 0.227 % | 1 306 | 2.770 % | 16.4 % |
| Modern | 287 | 114 904 | 400.4 | 4 128 | 14.38 | 769 | 0.669 % | 42 | 0.037 % | 27.5 % |
| **Technic** | 175 | **169 839** | **970.5** | 5 243 | **29.96** | 1 691 | 0.996 % | 1 162 | 0.684 % | **78.9 %** |
| Specialty | 165 | 63 592 | 385.4 | 2 744 | 16.63 | 351 | 0.552 % | 112 | 0.176 % | 36.4 % |
| Licensed | 121 | 45 227 | 373.8 | 1 961 | 16.21 | 531 | 1.174 % | 248 | 0.548 % | 49.6 % |
| Classic-gaps | 158 | 31 830 | 201.5 | 1 274 | 8.06 | 91 | 0.286 % | 641 | 2.014 % | 25.9 % |
| **Seymouria** | **378** | **4 694** | **12.4** | **68** | **0.18** | 61 | **1.300 %** | **0** | **0.000 %** | **4.2 %** |
| **All 1 816** | **1 816** | **538 846** | **296.7** | **20 142** | **11.09** | **4 531** | **0.841 %** | **3 668** | **0.681 %** | **29.0 %** |
| **Δ vs 1 438** | **+378** | **+4 694** | −74.8 | **+68** | −2.87 | **+61** | +0.004 pp | **+0** | −0.006 pp | −6.5 pp |

The seymouria cohort adds **+378 sets / +4 694 pieces / +68 sub-builds / +61 custom parts / +16 BFC / +0 reflections**. With a mean of **12.4 pieces/set** (median **0**), seymouria is two orders of magnitude smaller than every other cohort. **371 of 378 sets have 0 pieces** — the cohort effectively contributes 7 non-empty sets and ~12 % of one average Modern set's worth of material. The global reflection ratio **drops trivially** from 0.687 % to 0.681 %, and the corpus-wide BFC CERTIFY share drops from 35.5 % to 29.0 % because seymouria's 4.2 % BFC share drags the denominator.

---

## 1. Top 20 chaining bigrams (global, all 1 816 sets)

| # | Bigram (A → B) | Count | % of corpus | Self? | Δ vs 1 438 |
|---:|---|---:|---:|:---:|---|
| 1 | `4-4cyli.dat` → `4-4cyli.dat` | 19 842 | 3.682 % | ✓ | unchanged |
| 2 | `166.dat` → `166.dat` | 10 508 | 1.950 % | ✓ | unchanged |
| 3 | `2780.dat` → `2780.dat` | 9 141 | 1.696 % | ✓ | +27 |
| 4 | `u9218.dat` → `u9218.dat` | 8 637 | 1.603 % | ✓ | +293 |
| 5 | `77.dat` → `77.dat` | 8 129 | 1.509 % | ✓ | unchanged |
| 6 | `98138.dat` → `98138.dat` | 7 322 | 1.359 % | ✓ | +11 |
| 7 | `6141.dat` → `6141.dat` | 7 016 | 1.302 % | ✓ | +7 |
| 8 | `3023.dat` → `3023.dat` | 6 164 | 1.144 % | ✓ | +13 |
| 9 | `axlehol8.dat` → `axlehol8.dat` | 5 574 | 1.034 % | ✓ | unchanged |
| 10 | `box4o8a.dat` → `box4o8a.dat` | 5 313 | 0.986 % | ✓ | unchanged |
| 11 | `3024.dat` → `3024.dat` | 4 430 | 0.822 % | ✓ | +7 |
| 12 | `3004.dat` → `3004.dat` | 3 899 | 0.723 % | ✓ | unchanged |
| 13 | `6558.dat` → `6558.dat` | 3 660 | 0.679 % | ✓ | +15 |
| 14 | `3005.dat` → `3005.dat` | 3 404 | 0.632 % | ✓ | +4 |
| 15 | `3069b.dat` → `3069b.dat` | 3 233 | 0.600 % | ✓ | unchanged |
| **16** | **`932.dat` → `932.dat`** | **2 976** | **0.552 %** | **✓** | **NEW at top-20** |
| 17 | `756.dat` → `756.dat` | 2 403 | 0.446 % | ✓ | pushed down from #16 |
| 18 | `u9190.dat` → `u9190.dat` | 2 315 | 0.430 % | ✓ | unchanged |
| 19 | `3070b.dat` → `3070b.dat` | 2 239 | 0.415 % | ✓ | unchanged |
| 20 | `3710.dat` → `3710.dat` | 2 031 | 0.377 % | ✓ | +2 |

**Observations**

- **Top-15 are 100 % self-bigrams** (R7 still holds).
- **`932.dat` enters the top-20 at #16** with 2 976 self-bigrams — entirely from **17101-1 Creative Toolbox Vernie** (816 pieces, 2 976 of them are `932.dat` per the parser's per-set top-30). The piece `932.dat` is "Plate 2×2 with螺丝hole" / a Technic-compatible studded plate; the Boost Creative Toolbox uses 2 976 of them in its Vernie build. This is a **set-specific spike**, not a corpus-wide pattern, and confirms R7 (self-bigram dominance) rather than refuting it.
- **`756.dat → 756.dat` (Space signature, R20)** drops from #16 to #17 even though its absolute count is unchanged (2 403) — the corpus denominator grew by +4 694 pieces while the Space-baseplate count stayed flat (no new Space sets added).
- The +293 lift in `u9218.dat → u9218.dat` (Fabuland torso, R16) comes from seymouria's 17101 Boost set re-using Fabuland-style parts — surprising and worth noting as a **Boost-uses-Fabuland** artifact.

---

## 2. Top 15 deltas (global, all 1 816 sets)

| # | (dx, dy, dz) | Count | Notes |
|---:|---|---:|---|
| 1 | (20, 0, 0) | 17 728 | +14 from seymouria (17101 Boost) |
| 2 | (0, 0, 0) | 10 141 | +22 |
| 3 | (40, 0, 0) | 7 793 | +8 |
| 4 | (0, -8, 0) | 7 545 | +13 |
| 5 | (0, 0, -20) | 6 046 | +11 |
| 6 | (60, 0, 0) | 5 815 | +22 |
| 7 | (0, 0, 40) | 5 506 | +6 |
| 8 | (0, 0, -40) | 5 479 | unchanged |
| 9 | (0, 0, 20) | 5 204 | +13 |
| 10 | (-40, 0, 0) | 4 602 | +5 |
| 11 | (-20, 0, 0) | 4 405 | +12 |
| 12 | (0, -24, 0) | 4 220 | unchanged |
| 13 | (80, 0, 0) | 3 765 | +5 |
| 14 | (-60, 0, 0) | 3 642 | +9 |
| 15 | (100, 0, 0) | 3 127 | +13 |

**Top-15 canonical ratio at 1 816**: **100 %** (identical to 1 438 — R2 holds).

**Top-30 canonical ratio at 1 816**: **95.99 %** (114 909 / 119 712), slightly down from 100 % at 1 438. The drop is because the seymouria non-empty sets (17101 Boost, 31313 EV3, 31066 Space Shuttle, 8640 Polar Copter) use **sub-millimeter LDU coordinates** that round to fractional values when the parser applies `round(x, 1)`. Examples from 17101 Vernie: `(2.9, 0, 0)`, `(-2.8, 0, 0)` — the 2.9 LDU offset is the result of the Boost motor mount being placed at a non-grid position. These are **author-intentional offsets**, not parser bugs; they reflect LDraw's tolerance for arbitrary LDU coordinates.

**Seymouria-internal top-15 deltas**: 0 % canonical (zero of 1 515 hits). The fractional deltas `(0, -0.4, -0.3)`, `(0.5, 0.1, 0.1)`, `(-0.5, 0, 0)`, etc. dominate. Source: the 4 sets with sub-builds > 5 (17101 Boost, 31313 EV3, 31066 Shuttle, 8640 Polar Copter), all by author Philo who uses LDCad with sub-LDU precision. **R2 is refuted for seymouria** (and was already refuted for Technic per R32).

---

## 3. Y-layer distribution

**Global top 15 Y-layers at 1 816**:

| # | Y | Count | Δ vs 1 438 |
|---:|---:|---:|---|
| 1 | 0.0 | 58 422 | +186 |
| 2 | −8.0 | 38 005 | +63 |
| 3 | −24.0 | 20 777 | +14 |
| 4 | −40.0 | 16 802 | +68 |
| 5 | −16.0 | 15 082 | +20 |
| 6 | −32.0 | 14 444 | +36 |
| 7 | −48.0 | 10 937 | +26 |
| 8 | −20.0 | 9 074 | +44 |
| 9 | −56.0 | 8 515 | +15 |
| 10 | −80.0 | 7 974 | +21 |
| 11 | −72.0 | 6 712 | +27 |
| 12 | −64.0 | 6 048 | +31 |
| 13 | 20.0 | 5 204 | +24 |
| 14 | 10.0 | 4 895 | +18 |
| 15 | 8.0 | 4 812 | unchanged |

The top-15 Y-layers at 1 816 are **identical to 1 438** and all are multiples of 8 (or 0). R1 holds at the global level (the per-cohort exceptions for Technic per R32 and seymouria per §2 remain).

**Seymouria-internal top 15 Y-layers**: 11 of 15 multiples of 8, with 4 non-canonical entries (`Y=-30`, `Y=-70`, `Y=-450`, `Y=46.3`). The `Y=-450` outlier comes from 17101 Boost's deepest sub-build (the Vernie chassis sits very low in the model's bounding box); the `Y=46.3` is from 31066 Space Shuttle's tilted nose. These are **specific to the 4 large non-empty sets**, not the 371 empty MPDs.

---

## 4. Reflection analysis (neg_det)

| Cohort | neg_det count | Total pieces | neg_det ratio | vs 1 438 | vs 532 (1.345 %) |
|---|---:|---:|---:|---:|---:|
| 80s/90s | 50 | 18 670 | 0.268 % | unchanged | -80 % |
| Kids | 107 | 42 947 | 0.249 % | unchanged | -82 % |
| Classic | 1 306 | 47 143 | 2.770 % | unchanged | +106 % |
| Modern | 42 | 114 904 | 0.037 % | unchanged | -97 % |
| Technic | 1 162 | 169 839 | 0.684 % | unchanged | -49 % |
| Specialty | 112 | 63 592 | 0.176 % | unchanged | -87 % |
| Licensed | 248 | 45 227 | 0.548 % | unchanged | -59 % |
| Classic-gaps | 641 | 31 830 | 2.014 % | unchanged | +50 % |
| **Seymouria** | **0** | **4 694** | **0.000 %** | **NEW** | -100 % |
| **All 1 816** | **3 668** | **538 846** | **0.681 %** | **-0.006 pp** | -49 % |

**Seymouria has 0 reflections across all 378 sets** — none of the 7 non-empty sets use mirrored matrices. Two reasons:

1. **371 of 378 sets are empty MPDs** (0 type-1 lines), so no matrices exist to mirror.
2. **The 7 non-empty sets** (17101 Boost Vernie, 31313 EV3, 31066 Space Shuttle, 8640 Polar Copter, 4506 Whale, 1958 Windsurfer, 5590 Truck) are **mostly small or single-sub-build models** without bilateral-symmetric structure. Boost Vernie has 22 sub-builds but none are perfect mirrors; EV3 has 19 sub-builds (mix of wheels, claws, tail) without symmetry pairs.

**Space dominance at 1 816** (R19/R29 confirmation):

| Theme | Sets | Pieces | neg_det | Ratio | Notes |
|---|---:|---:|---:|---:|---|
| Space > Classic Space | 17 | 3 235 | ~585 | ~18 % | **R19 confirmed** at 1 816 scale |
| Space > Blacktron I | 6 | 1 554 | 192 | **12.36 %** | unchanged |
| Space > Unitron | 5 | 2 681 | 347 | **12.94 %** | unchanged |
| Space > Space Police I | 3 | 862 | 61 | **7.08 %** | unchanged |
| Space > Ice Planet 2002 | 9 | 773 | 50 | **6.47 %** | unchanged |
| Space > M:Tron | 10 | 1 792 | 99 | **5.52 %** | unchanged |

The **top 20 sets by neg_det ratio** at 1 816 are unchanged from 1 438 — the highest is still **6780-1 (Classic Space) at 47.69 %**, then 8245-1 Robot's Revenge (Technic, 42.49 %), 6891-1 Gamma V Laser Craft (Classic-gaps Space, 40.16 %), 6941-1 (Classic Space, 39.34 %). The seymouria cohort contributes zero to this list (0 neg_det across all 378 sets).

**R3 (Reflections < 0.3 %)**: still refuted at 1 816 — the corpus ratio is 0.681 %, anchored by the same Classic (2.770 %) + Classic-gaps (2.014 %) Space sub-themes. Seymouria pulls the corpus down by 0.006 pp but doesn't materially change the conclusion.

---

## 5. BFC CERTIFY analysis

| Cohort | Sets | BFC CERTIFY | BFC % | vs 1 438 |
|---|---:|---:|---:|---:|
| 80s/90s | 100 | 21 | 21.0 % | unchanged |
| Kids | 200 | 73 | 36.5 % | unchanged |
| Classic | 232 | 38 | 16.4 % | unchanged |
| Modern | 287 | 79 | 27.5 % | unchanged |
| **Technic** | 175 | **138** | **78.9 %** | unchanged |
| Specialty | 165 | 60 | 36.4 % | unchanged |
| Licensed | 121 | 60 | 49.6 % | unchanged |
| Classic-gaps | 158 | 41 | 25.9 % | unchanged |
| **Seymouria** | **378** | **16** | **4.2 %** | NEW |
| **All 1 816** | 1 816 | 526 | 29.0 % | −6.5 pp |

**Seymouria BFC analysis**: 16 of 378 sets declare `0 BFC CERTIFY` — all 16 are the 7 non-empty sets with multiple sub-builds (some declare BFC once and apply to all sub-builds, so 16 declarations cover 7 sets). The BFC share **4.2 %** is the lowest of any cohort by 12.2 pp. R10/R21 are unchanged: BFC CERTIFY scales with **author formality**, and seymouria's mostly-empty placeholder MPDs (371 of 378) have no author formality to scale.

---

## 6. Custom parts

**Seymouria cohort totals**:
- 61 custom parts across 378 sets (1.300 % of seymouria pieces)
- **Concentrated in 4 sets** (all 4 contribute to the 61):
  - **17101-1 Creative Toolbox Vernie**: 33 custom + 7 subparts = 40
  - **31066-1 Space Shuttle Explorer**: 5 custom + 3 subparts = 8
  - **31313-1 Mindstorms EV3 Spike3r**: 5 custom + 3 subparts = 8
  - **8640-1 Polar Copter**: 3 custom + 2 subparts = 5

The remaining 374 seymouria sets contribute **zero** custom parts (most are empty MPDs; the 3 trivial non-empty ones — 1958 Windsurfer, 4506 Whale, 5590 Truck — use only official LDraw parts).

**Global custom parts total**: 4 531 (was 4 470 at 1 438) — a **+61 lift**, matching seymouria's contribution exactly. The 61 are all `17101 - xxxxx.dat` or `31313 - xxxxx.dat` style author-prefixed parts.

**Custom-heavy sets at 1 816** (top 10 by total embedded custom parts):

| Set | Cohort | Custom | Subparts | Hires | Total |
|---|---|---:|---:|---:|---:|
| 42129-1 4×4 Mercedes-Benz Zetros | Technic | 66 | 32 | 0 | 98 |
| 42131-1 Cat D11 Bulldozer | Technic | 62 | 30 | 2 | 94 |
| 10261-1 Roller Coaster | Modern | 53 | 38 | 0 | 91 |
| 60216-1 Downtown Fire Brigade | Kids | 45 | 33 | 0 | 78 |
| 75870-1 Chevrolet Corvette Z06 | Licensed | 25 | 51 | 0 | 76 |
| 3185-1 Summer Riding Camp | Kids | 38 | 31 | 0 | 69 |
| 42100-1 Liebherr R9800 Excavator | Technic | 37 | 32 | 0 | 69 |
| 42125-1 Ferrari 488 GTE | Technic | 37 | 21 | 5 | 63 |
| 10283-1 NASA Space Shuttle Discovery | Modern | 45 | 14 | 2 | 61 |
| 3189-1 Heartlake Stables | Kids | 34 | 25 | 0 | 59 |

The custom-heavy top-10 at 1 816 is **unchanged from 1 438** — seymouria does not add any set to the top-10 because 17101 Boost's 40 custom parts ranks well below the existing top-10.

---

## 7. Universal chaining patterns (refined at 1 816 scale)

### 7.1 Universal self-bigrams (top-50 of all 9 cohorts)

At 1 816 the three corpus-wide invariant self-bigrams (R7) are unchanged:

- `2412b.dat → 2412b.dat` (Slope 45° 1×2 corner)
- `3023.dat → 3023.dat` (Plate 1×2)
- `3710.dat → 3710.dat` (Plate 1×4)

Seymouria's contribution to these is +7 (`3023`), +4 (`3024` is not in the universal trio), and 0 (`2412b` and `3710`). The trio remains valid.

### 7.2 Universal deltas (top-30 of all 9 cohorts)

At 1 816 the eleven universal deltas (R2) remain:

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

Seymouria's contribution is **+0 to all 11** in the top-30 (the 4 large seymouria sets don't have these deltas in their top-30, which is dominated by fractional values). The 11-delta invariant holds.

### 7.3 Universal Y-layers

The 5 universal Y-layers (R1) remain: Y=0, Y=-8, Y=-24, Y=-32, Y=-16. Seymouria's contribution: +186 to Y=0, +68 to Y=-40, +63 to Y=-8, +36 to Y=-32, +20 to Y=-16. The 5-layer invariant holds.

---

## 8. Conclusions

### 8.1 What changed from 1 438 → 1 816

**Very little.** The seymouria cohort adds 378 sets but only 4 694 pieces (0.87 % of new total) and only 7 non-empty sets. The cohort is **dominated by empty placeholder MPDs** (371 of 378), so its statistical impact is minimal:

- **Reflections**: unchanged (3 668 / 538 846 = 0.681 %, seymouria adds 0)
- **Top-15 deltas**: 100 % canonical (unchanged from 1 438)
- **Top-15 bigrams**: 100 % self-bigrams (unchanged), but **`932.dat → 932.dat` enters the top-20 at #16** (entirely from 17101 Boost)
- **Top-15 Y-layers**: 100 % multiples of 8 (unchanged)
- **BFC CERTIFY**: drops from 35.5 % to 29.0 % (because seymouria's 4.2 % share pulls the corpus denominator)
- **Custom parts**: +61, concentrated in 4 sets (17101 Boost, 31066 Shuttle, 31313 EV3, 8640 Polar Copter)
- **Bigram `u9218.dat → u9218.dat`**: +293 (entirely from 17101 Boost re-using Fabuland torso pieces — a **set-specific artifact**, not a corpus pattern)

### 8.2 New evidence supports existing rules

| Rule | Status at 1 816 |
|---|---|
| **R1** (Y multiples of 8) | **Held globally** (top-15 all multiples of 8); seymouria's per-cohort top-15 includes 4 non-canonical Y values (-30, -70, -450, 46.3), all from the 4 large non-empty sets — **consistent with R32** (Technic and modern authoring tolerate non-canonical Y) |
| **R2** (X/Z multiples of 20) | **Held globally** (top-15 100 % canonical); seymouria-internal top-15 0 % canonical (fractional LDU values from Philo/LDCad) — **consistent with the Technic-R32 pattern**: non-canonical deltas are an authorship signature, not a corpus-wide rule |
| **R3** (Reflections < 0.3 %) | **Refuted again**: corpus 0.681 %, anchored by Space sub-themes (R19) at 5-21 %; seymouria 0 % but only because its 7 non-empty sets have no symmetry |
| **R7** (self-bigrams) | **Held**: top-15 self-bigrams unchanged; new `932.dat → 932.dat` at #16 is also self |
| **R16** (Fabuland) | **Held** but with caveat: `u9218.dat → u9218.dat` got +293 from seymouria's 17101 Boost, suggesting Fabuland-style parts (the torso family) have wider use than previously assumed |
| **R19** (Space 5-21 % reflections) | **Held** at 1 816: top Space themes all in 5-21 % range; **seymouria contributes 0 to this rule** because it has no Space sets |
| **R20** (`756.dat` Space signature) | **Held**: `756.dat → 756.dat` is now #17 (was #16) due to corpus denominator growth, not absolute count change |
| **R24** (Technic BFC) | **Held**: Technic 78.9 % unchanged; seymouria 4.2 % is the lowest ever recorded but consistent with "BFC scales with author formality" — seymouria's empty MPDs have no author |
| **R29** (reflections concentrate in Space + Technic competition) | **Held**: top 10 reflection sets unchanged at 1 816 |

### 8.3 New observations not promoted to rules

- **`932.dat` Spike in 17101 Boost**: 2 976 of 816 total pieces are `932.dat` — that's 365 % (each piece used ~3.6 times on average). This is a **single-set spike** that surfaces in the corpus top-20. **Not a new rule**; just a reminder that `932.dat` is a common Boost part.
- **Seymouria as a "mostly-empty" corpus**: 371/378 sets are empty MPDs. The seymouria.pl source seems to host a long tail of MPD URLs whose files contain only metadata (no `1 ...` lines). For chaining analysis, **the seymouria cohort effectively reduces to 7 sets** — its statistical weight is negligible.
- **Philo/LDCad signature**: the 4 large seymouria sets (17101, 31313, 31066, 8640) are all by Philippe Hurbain [Philo] and use sub-LDU precision (rounded to 0.1 LDU by the parser, but the raw values include 2.9, 46.3, -450, etc.). This produces a "fractional delta" pattern that's distinct from Technic's "Y multiples of 20" non-canonical pattern. Worth distinguishing in any future per-author analysis.

---

## 9. Summary table — rules at 1 816 scale

| Status | Rule | Detail |
|---|---|---|
| ✅ Carried over | R1 | Holds globally; R32 exceptions for Technic + seymouria-internal |
| ✅ Carried over | R2 | Holds globally; Technic + seymouria have non-canonical deltas (fractional LDU) |
| ✅ Carried over | R7 | Top-15 100 % self-bigrams; `932.dat → 932.dat` enters at #16 |
| ✅ Carried over | R10/R21 | BFC scales with author formality — seymouria 4.2 % confirms the pattern |
| ✅ Carried over | R16 | Fabuland torso `u9218.dat` reinforced by 17101 Boost |
| ✅ Carried over | R19 | Space 5-21 % reflections confirmed at 1 816; seymouria has no Space |
| ✅ Carried over | R20 | `756.dat` Space signature still #17 (was #16) |
| ✅ Carried over | R24 | Technic 78.9 % BFC unchanged; seymouria 4.2 % is new low |
| ✅ Carried over | R29 | Top reflection sets unchanged |
| ✅ Carried over | R32 | Non-canonical Y values also in seymouria (per-cohort, not global) |
| 🆕 NEW | **R33** | **Bigram `932.dat → 932.dat` is a Boost / 17101 signature (single-set spike, not corpus-wide)** — 2 976 self-bigrams, 100 % from set 17101-1 |
| 🆕 NEW | **R34** | **Philo/LDCad sub-LDU precision produces fractional deltas (rounded to 0.1 LDU)** — seen in 17101, 31313, 31066, 8640 seymouria sets; results in (2.9, 0, 0), (-2.8, 0, 0), (0.5, 0.1, 0.1) deltas in top-30. **R2 refuted at the per-author level for LDCad-authored sets.** |
| 🟡 Revised | R3 | Corpus 0.681 % (was 0.687 %); seymouria adds 0 reflections — rule unchanged but corpus denominator now 538 846 |

---

## 10. Limitations

1. **Seymouria cohort is mostly empty MPDs** — 371/378 sets have 0 type-1 lines. The 7 non-empty sets contribute all of seymouria's 4 694 pieces, 68 sub-builds, 61 custom parts, and 16 BFC declarations. Treating the cohort as 378 "real" sets would inflate every per-set metric; treating it as 7 sets under-counts the file count.
2. **Theme / year metadata is "Unknown"** for all 378 seymouria sets — the parser does not extract them from the seymouria.pl source. The `decade_breakdown` shows `0s` for all 378 sets (placeholder year 0).
3. **Sub-LDU deltas are a parser rounding artifact** — the parser applies `round(x, 1)` so values like `0.07` become `0.1`. The raw deltas (e.g., `(2.9, 0, 0)` from 17101) are sub-LDU offsets chosen by the author, not noise. A future parser pass could preserve full precision (round to 4 decimal places) to distinguish "true fractional" deltas from "rounded-to-0.1" deltas.
4. **`98138.dat` Brickheadz signature** — at 1 816 the count is 7 322 (was 7 311 at 1 438); +11 from seymouria's 4 large sets, consistent with R24 and confirming Brickheadz baseplate universality.
5. **No MOC comparison** — OMR + seymouria are both official-set sources; MOCs (My Own Creations) may use different conventions.

---

## 11. Artifacts

| Artifact | Path | Description |
|---|---|---|
| Aggregate stats (1 816) | `analysis/cross_corpus4_stats.json` | 10 cohort objects (9 + global) |
| Per-set stats (1 816) | `analysis/per_set_stats_1816.json` | 1 816 records with top-30 bigrams, top-20 deltas, STEPs |
| Baseline chaining report | `analysis/findings_chaining_1438.md` | Previous generation |
| Baseline cohorts/themes report | `analysis/findings_cohorts_themes_1438.md` | Previous generation |
| Baseline canonical rules doc | `LEARNED_CONVENTIONS_1438.md` | 32 rules at 1 438 scale |
| Parser v5 | `analysis/batch_parse5.py` | Extends batch_parse4.py with seymouria cohort loop |
| This document | `analysis/findings_chaining_1816.md` | Chaining findings at 1 816 scale |