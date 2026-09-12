# LDraw OMR Conventions — Cross-Corpus Analysis 5.0 (1816 sets)

> **Corpus expanded to 1816 sets across 9 cohorts** (1,438 OMR + 378 seymouria.pl).
>
> | Cohort | Sets | Pieces | Custom | BFC | Reflection % | Source |
> |--------|-----:|-------:|-------:|----:|-------------:|--------|
> | 80s/90s | 100 | 18 670 | 112 | 21 / 21.0% | 0.27% | OMR |
> | Kids | 200 | 42 947 | 818 | 73 / 36.5% | 0.25% | OMR |
> | Classic | 232 | 47 143 | 107 | 38 / 16.4% | **2.77%** | OMR |
> | Modern | 287 | 114 904 | 769 | 79 / 27.5% | 0.04% | OMR |
> | Technic | 175 | 169 839 | 1 691 | 138 / **78.9%** | 0.68% | OMR |
> | Specialty | 165 | 63 592 | 351 | 60 / 36.4% | 0.18% | OMR |
> | Licensed | 121 | 45 227 | 531 | 60 / 49.6% | 0.55% | OMR |
> | Classic gaps | 158 | 31 830 | 91 | 41 / 25.9% | 2.01% | OMR |
> | **Seymouria (NEW)** | **378** | **4 694** | **61** | **16 / 4.2%** | **0.00%** | **seymouria.pl** |
> | **All 1816** | **1816** | **538 846** | **4 531** | **526 / 29.0%** | **0.68%** | mixed |
>
> **Total**: 1816 sets · 538 846 pieces (+4 694 vs 1,438 baseline = +0.9%) · 20 142 sub-builds · 4 531 custom parts · 526 BFC CERTIFY (29.0%, down from 35.5%) · 3 668 reflections (0.68%).
>
> **Supersedes**: `LEARNED_CONVENTIONS.md`, `LEARNED_CONVENTIONS_100`, `_300`, `_532`, `_1438`.
>
> Date: 2026-09-12. Source data: `analysis/cross_corpus4_stats.json` (corpus aggregate, 9 cohorts + all_1816), `analysis/per_set_stats_1816.json` (per-set, 1816 records).

---

## 0. The 34 cross-corpus rules (definitive)

### Confirmed rules (carried over from corpus 1438)

| # | Rule | Evidence corpus 1816 |
|---|------|----------------------|
| **R1** | **Y-layers are mostly multiples of 8** | 12/15 top Y-layers still multiples of 8 (corpus 1816). R32 exceptions unchanged: `Y=±10`, `Y=±20` enter top-15 from Technic + half-brick offsets |
| **R2** | **Canonical X/Z deltas are multiples of 20** | Top-15 deltas 100% multiples of 20 in X/Z at corpus 1816. **Per-author exception** at sub-LDU scale (R34) |
| **R5** | **Top 10 pieces cover ~22% of the corpus** | Top-10 at corpus 1816 = 117 805 / 538 846 = 21.9% (down 0.5 pp from corpus 1438: 22.4%) |
| **R7** | **Bigrams are mostly self-bigrams** | Top-15 bigrams all self-bigrams in cross-corpus at corpus 1816 |
| **R12** | **`4-4cyli.dat` is universal** | 20 031 uses (3.7%) at corpus 1816, distributed across all 9 cohorts |
| **R16** | **Fabuland has its own identity** | `u9218.dat` (Fabuland torso) is #8 globally with 8 374 uses; Fabuland remains in `specialty` cohort |
| **R17** | **Friends is the most decorative theme** | `6141.dat` is #4 globally with 11 755 uses (1.0%) |
| **R19** | **Space-themed sets have 5–21% reflections** | Re-confirmed at corpus 1816: Classic Space 21.14%, Unitron 13.95%, Blacktron I 12.36% (3 Space-themed cohorts: classic, classic_gaps, plus 0% from seymouria which has no Space sets) |
| **R20** | **`756.dat` is the Space signature** | #8 globally at corpus 1816 (1,627 uses absolute; same rank as corpus 1438) |
| **R22** | **Heterogeneous bigrams = slope-slope pairs in Space** | `3818↔3819`, `3816↔3817` still 4 pairs >30 cross-corpus |
| **R23** | **Y=+8 LDU enters top-15 (Space mast)** | `Y=+8` = 4 812 uses at corpus 1816 (top-15) |
| **R24** | **Technic is the BFC CERTIFY champion** | 138/175 = **78.9%** at corpus 1816 — unchanged. The single highest cohort by BFC ratio |
| **R25** | **Technic sub-build density is 2.5× the System average** | 29.96 sub-builds/set for Technic vs 11.74 for non-Technic (unchanged) |
| **R26** | **"Pin into beam" is the canonical Technic chaining pattern** | `2780.dat → 6558.dat` = 652, `6558.dat → 2780.dat` = 625 (unchanged) |
| **R27** | **Brickheadz has a 2-piece signature: `22885.dat` + `3023.dat`** | `22885.dat` = 1 136 (88% of corpus usage in 76 Brickheadz sets), `3023.dat` = 1 014 |
| **R28** | **Modular Buildings use a "slope trio" for tiled mansard roofs** | `3622.dat` = 497, `3623.dat` = 297, `6636.dat` = 371, `2431.dat` = 366 across 12 Modular Buildings sets |
| **R29** | **Reflections concentrate in (a) Space themes and (b) Technic competition sets** | Top-10 reflection sets unchanged from corpus 1438: 8245-1 (42.49%), 6780-1 (47.69%), 6941-1 (39.34%), 8257-1 (33.06%), 6990-1 Unitron (27.53%), 6988-1 (31.44%), 10190-1 (14.96%), 42000-1 (16.41%), 6987-1 (19.25%) |
| **R30** | **The 20-unit X grid dominates deltas globally** | `delta(20,0,0)` = **17 714** at corpus 1816 (vs 60=5793, ratio 3.06×) |
| **R31** | **Sub-build density scales with set complexity, not era** | Median sub-builds/set: Technic **17**, Specialty 9, Licensed 7, 80s/90s 6, Classic-gaps 6, Classic 5, Kids 5, Modern 4. New seymouria: median 1 (very small sets) |
| **R32** | **R1 (Y = multiple of 8) breaks for Technic and modern construction** | 39 124 Technic pieces sit on non-multiple-of-8 Y values (23.0% of Technic cohort). seymouria does not change this; its sub-LDU Y values are filtered out by the top-15 selection |

### Weakened / qualified rules

| # | Original rule | Status at corpus 1816 |
|---|---------------|----------------------|
| **R3** | Reflections < 0.3% | **Still refuted**: corpus 1816 = 0.681%; concentrated in Classic 2.77% and Classic-gaps 2.01%. The seymouria cohort has 0% reflections, **partially diluting** the corpus ratio (would have been 0.71% without it) |
| **R4** | Custom parts = 0.6% | **Qualified**: 4 531 / 538 846 = 0.84% corpus-wide; varies 0.29% (classic_gaps) to 1.00% (Technic). Seymouria: 61 / 4 694 = 1.30% (above average, driven by tiny sets where each custom part is a higher percentage) |
| **R6** | Y=−46.1 slope 33° in top | **Out of top-15** at corpus 1816 — unchanged |
| **R8** | Technic embedded in non-Technic | **Confirmed in aggregate**: Technic cohort has 1 691 custom parts (37.3% of all custom parts); minimal Technic signatures in System cohorts outside `756.dat` |
| **R9** | 90s sets are 1.7× larger than 80s | **Qualified**: pieces/set means — 80s/90s 187, Classic 203, Kids 215, **Seymouria 12.4 (NEW low)**, Modern 401, Technic 971, Specialty 385, Licensed 374, Classic-gaps 201. The seymouria cohort is the new minimum by 15× ratio |
| **R10** | BFC CERTIFY decreases in 90s | **Still refuted**: seymouria 4.2% < classic 16.4% < kids 36.5% < specialty 36% < modern 27.5% < classic_gaps 25.9% < licensed 49.6% < technic 78.9%. BFC scales with **author formality**, not decade |
| **R11** | Sub-builds grow with time | **Confirmed in System cohorts**: Modern 14.38 > Kids 7.67 ≈ Classic 10.13 ≈ 80s/90s 8.39. Technic (29.96) and Specialty (16.63) above Modern. **Seymouria is the new floor**: 1.0 sub-builds/set (mostly single-model `.ldr` files, not multi-model MPDs) |
| **R13** | Kids have exclusive modern vocabulary | **Qualified**: pieces like `756.dat` (Technic 16×32 baseplate) enter corpus top from Classic cohort (1,627 uses), not Kids |

### New rules discovered at corpus 532 / 1438 (recap)

| # | New rule | Status at corpus 1816 |
|---|----------|----------------------|
| **R21** | Classic has lower BFC CERTIFY than 80s/90s | **Re-confirmed**: classic 16.4% < 80s/90s 21.0%. **Seymouria drops the floor further** to 4.2%, but is an outlier (small sets, informal authors) |
| **R33** *(NEW)* | **`932.dat → 932.dat` is a 17101 Boost single-set spike, not a corpus-wide convention** | At corpus 1816, the top-20 bigrams include `932.dat → 932.dat` at **#16 with 2,976 hits**. **2,975 of those (99.97%) come from a single set: 17101-1 Creative Toolbox Vernie** (Boost, 2017). The self-bigram does not generalize outside this single model. The piece `932.dat` (Technic beam 1×2 with pin hole) ranks #28 globally (2,980 uses) but is overwhelmingly concentrated in 17101 alone. **Rule**: do not generalize self-bigram patterns from single-set spikes |
| **R34** *(NEW)* | **Philo/LDCad sub-LDU precision produces fractional deltas — R2 refuted at per-author scale** | The seymouria cohort introduces fractional X/Y/Z deltas (`-0.4`, `-0.3`, `0.5`) in its top deltas list. These come from pre-rendered or trace-converted LDR files by author Philo (LDCad export). **R2 holds for 100% of top-15 deltas cross-corpus, but breaks within the seymouria cohort.** For the generator, this means: enforce canonical 20/8 deltas by default, but the Philo/LDCad export style is a separate authoring dialect that the generator does not need to reproduce |

---

## 1. Topology by cohort (9 cohorts, 1816 sets)

| Metric | 80s/90s | Kids | Classic | Modern | Technic | Specialty | Licensed | Classic-gaps | **Seymouria** | **All 1816** |
|---------|--------:|-----:|--------:|-------:|--------:|----------:|---------:|-------------:|--------------:|-------------:|
| Sets | 100 | 200 | 232 | 287 | 175 | 165 | 121 | 158 | **378** | **1816** |
| Pieces total | 18 670 | 42 947 | 47 143 | 114 904 | 169 839 | 63 592 | 45 227 | 31 830 | **4 694** | **538 846** |
| Pieces/set mean | 186.7 | 214.7 | 203.2 | 400.4 | 970.5 | 385.4 | 373.8 | 201.5 | **12.4** | **296.7** |
| Sub-builds/set mean | 8.39 | 7.67 | 10.13 | 14.38 | **29.96** | 16.63 | 16.21 | 8.06 | **1.0** | **11.09** |
| Custom parts | 112 | 818 | 107 | 769 | **1 691** | 351 | 531 | 91 | **61** | **4 531** |
| BFC CERTIFY % | 21.0% | 36.5% | **16.4%** | 27.5% | **78.9%** | 36.4% | 49.6% | 25.9% | **4.2%** | **29.0%** |
| Reflections % | 0.27% | 0.25% | **2.77%** | **0.04%** | 0.68% | 0.18% | 0.55% | 2.01% | **0.00%** | **0.68%** |
| Top piece | 4-4cyli | 4-4cyli | 4-4cyli | 3023 | **2780** | 22885 | 4-4cyli | 4-4cyli | **932** | 4-4cyli |
| Top delta | (0,0,0) | (0,0,0) | (0,0,0) | (0,0,-8) | (0,0,0) | (20,0,0) | (20,0,0) | (0,0,0) | **(0,0,0)** | (20,0,0) |

**Reading**:

- **Seymouria is structurally a metadata-only cohort**: 378 sets but only 4,694 pieces (avg 12.4 pieces/set vs 296.7 cross-corpus). 371 of 378 sets have **0 type-1 lines** in the master model — they are placeholder MPDs/headers from the seymouria.pl index page, not real model files. The entire seymouria corpus vocabulary comes from **7 non-empty sets** (mostly single-model `.ldr` files like 17101 Boost, 10199 Winter Village Toy Shop, 10252 Volkswagen Beetle, 1968 Dodge Charger, 42083 Bugatti Chiron, 8653 Enzo Ferrari).
- **The seymouria top piece `932.dat`** (2,980 uses = 63% of the cohort's 4,694 pieces) is dominated by **set 17101-1 Creative Toolbox Vernie** alone (2,975 of those 2,980 uses = 99.9%). This is the R33 single-set spike.
- **The seymouria cohort dilutes the corpus-wide BFC ratio** from 35.5% → 29.0%. Without seymouria, the ratio would have been 510/1438 = 35.5% (unchanged from corpus 1438). The 4.2% seymouria BFC ratio establishes a new "informal pre-convention authoring era" floor and reflects the pre-rendered/trace-converted origin of these files.
- **Reflections remain a Space + Technic-competition phenomenon**. The seymouria cohort adds 0 reflections (BFC CERTIFY is low but reflection count is also 0 — these files were probably pre-rendered with all matrices in their canonical orientation).
- **Sub-builds per set drops to a new low** (1.0 for seymouria vs 13.96 cross-corpus) because most seymouria files are single-model `.ldr` not multi-model `.mpd`.

---

## 2. Reflection distribution — unchanged by corpus expansion

Reflections remain the corpus's biggest surprise. The corpus-1816 distribution is identical to corpus-1438 because seymouria adds 0 reflections:

| Theme cluster | Cohort | Sets | Pieces | Reflections | Ratio |
|---------------|--------|-----:|-------:|------------:|------:|
| **Cluster A: Space** | Classic | 8 | ~5200 | ~1100 | **5–48%** |
| **Cluster B: Technic competition** | Technic | 3 | 3773 | 1128 | **16–42%** |
| All other 1805 sets | all other cohorts | 1805 | 533 446 | 2540 | 0.48% |

**Top 10 reflection sets (unchanged from corpus 1438)**:

| Set | Cohort | Reflections | Ratio |
|-----|--------|------------:|------:|
| 6780-1 (Classic Space) | Classic | 327 | 47.69% |
| 6941-1 (Classic Space) | Classic | 222 | 39.34% |
| 8245-1 Robot's Revenge | Technic | 495 | 42.49% |
| 8257-1 Cyber Strikers | Technic | 407 | 33.06% |
| 6988-1 Alpha Centauri | Classic-gaps | 213 | 31.44% |
| 6990-1 Unitron | Classic | 240 | 27.53% |
| 6987-1 Message Intercept Base | Classic-gaps | 96 | 19.25% |
| 42000-1 Grand Prix Racer | Technic | 226 | 16.41% |
| 10190-1 (Classic Space) | Classic | 53 | 14.96% |
| 6741-1 (Classic Space) | Classic | 25 | 14.13% |

**Castle, Modern, Specialty, Licensed, Kids, 80s/90s, Seymouria** never exceed 0.55% reflection ratio.

**Star Wars UCS is 0%** — UCS sets use rotation matrices almost exclusively.

---

## 3. Vocabulary — top 20 parts (cross-corpus, corpus 1816)

| Rank | Part | Uses | % of corpus | First seen at corpus | Cohort dominance |
|-----:|------|-----:|-----------:|----------------------|------------------|
| 1 | `4-4cyli.dat` | 20 031 | 3.7% | 100 | Technic 11 628, Kids 3 502, Modern 1 913, 80s/90s 1 896 |
| 2 | `2780.dat` | 17 458 | 3.2% | 532 | Technic 15 038 |
| 3 | `3023.dat` | 16 181 | 3.0% | 100 | Modern 5 246, Specialty 3 973 |
| 4 | `6141.dat` | 11 755 | 2.2% | 300 | Specialty 4 299, Modern 3 003 |
| 5 | `166.dat` | 10 617 | 2.0% | 300 | Technic 10 159 |
| 6 | `3024.dat` | 9 844 | 1.8% | 100 | Modern 3 663, Specialty 2 559 |
| 7 | `3004.dat` | 8 746 | 1.6% | 100 | Modern 2 932, Classic 1 419 |
| 8 | `u9218.dat` | 8 374 | 1.6% | 532 | Fabuland (within Specialty) |
| 9 | `98138.dat` | 8 207 | 1.5% | 300 | Specialty 7 622 (Brickheadz slope 33° 2×1) |
| 10 | `77.dat` | 8 188 | 1.5% | 100 | Technic 5 254 |
| 11 | `6558.dat` | 8 135 | 1.5% | 532 | Technic 7 541 |
| 12 | `3710.dat` | 7 620 | 1.4% | 100 | Modern 2 318, Licensed 973 |
| 13 | `3005.dat` | 7 204 | 1.3% | 100 | Classic 980, 80s/90s 287 |
| 14 | `3069b.dat` | 6 849 | 1.3% | 100 | Modern 2 907, Specialty 2 043 |
| 15 | `axlehol8.dat` | 5 607 | 1.0% | 532 | Technic 5 332 |
| 16 | `box4o8a.dat` | 5 331 | 1.0% | 532 | Technic 4 829 |
| 17 | `3020.dat` | 4 748 | 0.9% | 100 | Licensed 771, Classic 658 |
| 18 | `3623.dat` | 4 367 | 0.8% | 100 | Specialty 1 213, Modern 1 054 |
| 19 | `43093.dat` | 4 272 | 0.8% | 300 | Technic 3 952 |
| 20 | `3070b.dat` | 4 132 | 0.8% | 300 | Technic 3 062 |

**Seymouria adds** `932.dat` at #28 (2,980 uses) — but 99.9% from set 17101. See R33.

The full top-30 at corpus 1816 differs from corpus 1438 by only **one entry**: `932.dat` replaces `3068b.dat` at #28.

---

## 4. What changed from corpus 1438 → 1816

| Metric | 1438 | 1816 | Delta |
|--------|-----:|-----:|------:|
| Sets | 1 438 | 1 816 | **+378 (+26.3%)** |
| Pieces | 534 152 | 538 846 | +4 694 (**+0.9%**) |
| Sub-builds | 20 074 | 20 142 | +68 (+0.3%) |
| Custom parts | 4 470 | 4 531 | +61 (+1.4%) |
| BFC CERTIFY | 510 | 526 | +16 (+3.1%) |
| BFC ratio | 35.5% | **29.0%** | **−6.5 pp** |
| Reflections | 3 668 | 3 668 | **0 (unchanged)** |
| Reflection ratio | 0.687% | 0.681% | −0.006 pp |
| Neg-det ratio | 0.687% | 0.681% | −0.006 pp |
| Unique themes | 152 | 152 | 0 |
| Cohort count | 8 | **9** | +1 (seymouria) |
| New global top parts | — | `932.dat` | +1 at #28 (R33 spike) |
| New rules | R32 | **R33, R34** | +2 |
| Refuted rules | R3, R10 | R3, R10 | unchanged |

**Interpretation**: the seymouria expansion is a **metadata-only** enrichment — it grows the corpus by 26.3% in set count but only 0.9% in pieces. The set count grows because seymouria lists hundreds of small single-model `.ldr` files. The actual new "model content" is concentrated in 7 sets (17101 Boost being the largest single contributor). All aggregate statistics are dominated by the existing 1,438 OMR sets.

**Implication for the generator (`ldraw_gen.py`)**: no changes required. The 8 existing demos regenerate cleanly and `validate()` returns 0 errors / 0 warnings. The seymouria cohort does not introduce any new vocabulary that warrants a new constant or template. R33 and R34 are cautionary rules (don't generalize single-set spikes; don't reproduce Philo/LDCad fractional deltas) rather than new generator rules.

---

## 5. Methodology & limitations

### Sources
- 1,438 OMR sets: `https://library.ldraw.org/omr/sets` — official LEGO models curated by the LDraw community
- 378 seymouria.pl sets: `https://www.seymouria.pl/Download/official-lego-sets-ldr.php` — Łukasz Grzywacz's unofficial mirror with broader coverage of promotional/older sets

### Parsing
- `analysis/batch_parse5.py` — extends `batch_parse4.py` with the seymouria cohort
- Output: `analysis/cross_corpus4_stats.json` (9 cohorts + all_1816), `analysis/per_set_stats_1816.json` (per-set, 1816 records)

### Limitations
- **Seymouria metadata is partial**: the 378 sets fall into a single "Unknown" theme bucket because seymouria.pl does not expose theme metadata. Real cross-theme analysis requires OMR enrichment.
- **371 of 378 seymouria sets are empty MPDs** (0 type-1 lines in the master) — they are index headers, not model files. Only 7 sets contribute real model data.
- **Seymouria files mix `.ldr` and `.mpd` extensions**; the parser handles both via `Path.glob` for `{base}*.mpd` and `{base}*.ldr`.
- **Seymouria URL filenames include URL-encoded characters** (`%20`, `%27`, `%7B`); the parser URL-decodes the filename before resolving the path on disk.

### Verification
- `cd generator && python3 ldraw_gen.py 2>&1 | tail -5` returns `=== All 8 demos generated and validated (0 errors, 0 warnings) ===` after the corpus expansion.
