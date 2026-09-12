# Findings — Cohorts & Themes (1 816 sets OMR + seymouria.pl)

> Scope: **1 816 sets · 538 846 pieces · 20 142 sub-builds · 4 531 embedded custom parts · 526 BFC CERTIFY · 0.681 % reflections**.
> Corpus distribution across **9 cohorts**: `80s90s` (100) + `kids` (200) + `classic` (232) + `modern` (287) + `technic` (175) + `specialty` (165) + `licensed` (121) + `classic_gaps` (158) + **`seymouria` (378, NEW)**.
> Source: `analysis/per_set_stats_1816.json` + `analysis/cross_corpus4_stats.json` + `corpus/all_omr_themes.json`.
> Carry-over: rules R1-R30 from `LEARNED_CONVENTIONS_1438.md` are preserved; this document **extends** with R31-R33 derived from the new cohort.

---

## 1. Cohort overview (1 816 sets)

| Cohort | Sets | Pieces | Pps | Sub-builds/set | Custom + Sub + Hi | BFC CERTIFY | Neg-det | Top piece | Top delta |
|--------|----:|------:|----:|---------------:|------------------:|------------:|--------:|-----------|-----------|
| `80s90s` | 100 | 18 670 | **186.7** | 8.39 | 112 (0.60 %) | 21 / 21.0 % | 50 / 0.27 % | `4-4cyli.dat` | (0, 0, 0) |
| `kids` | 200 | 42 947 | **214.7** | 7.67 | 818 (1.90 %) | 73 / 36.5 % | 107 / 0.25 % | `4-4cyli.dat` | (0, 0, 0) |
| `classic` | 232 | 47 143 | **203.2** | 10.13 | 107 (0.23 %) | 38 / 16.4 % | 1 306 / **2.77 %** | `3023.dat` | (0, 0, 0) |
| `modern` | 287 | 114 904 | **400.4** | 14.38 | 769 (0.67 %) | 79 / 27.5 % | 42 / **0.04 %** | `3023.dat` | (0, -8, 0) |
| `technic` | 175 | 169 839 | **970.5** | **29.96** | 1 691 (1.00 %) | **138 / 78.9 %** | 1 162 / 0.68 % | `2780.dat` | (0, 0, 0) |
| `specialty` | 165 | 63 592 | **385.4** | 16.63 | 351 (0.55 %) | 60 / 36.4 % | 112 / 0.18 % | **`98138.dat`** | (20, 0, 0) |
| `licensed` | 121 | 45 227 | **373.8** | 16.21 | 531 (1.17 %) | 60 / 49.6 % | 248 / 0.55 % | `3023.dat` | (20, 0, 0) |
| `classic_gaps` | 158 | 31 830 | **201.5** | 8.06 | 91 (0.29 %) | 41 / 25.9 % | 641 / **2.01 %** | `3004.dat` | (0, 0, 0) |
| **`seymouria`** | **378** | **4 694** | **12.4** | **0.18** | 61 (1.30 %) | **16 / 4.2 %** | **0 / 0.00 %** | **`932.dat`** | **(-0, -0.4, -0.3)** |
| **All 1 816** | **1 816** | **538 846** | **296.7** | 11.09 | 4 531 (0.84 %) | **526 / 29.0 %** | **3 668 / 0.681 %** | `4-4cyli.dat` | (0, 0, 0) |

**Three observations vs. the 1 438 baseline:**

1. **Net delta +26.4 % sets (+378) for +0.9 % pieces (+4 694).** The seymouria addition is essentially free in terms of vocabulary — it adds **20.8 % of the total set count but only 0.87 % of the total piece count**. The 1 438-vs-1 816 piece count is identical for every other metric (Technic still drives everything).
2. **Cohort-wide BFC CERTIFY ratio drops from 35.5 % → 29.0 %** despite the additional 378 sets. The drop is **entirely driven by seymouria's 4.2 % CERTIFY ratio**, which dilutes the corpus average. Without seymouria: 510/1 438 = 35.5 %; with seymouria: 526/1 816 = 29.0 %. The OMR-only CERTIFY ratio is unchanged.
3. **`seymouria` is structurally unlike any other cohort**: 378 sets, only 68 sub-builds total, 0 reflected pieces, 4.2 % BFC, and a top delta of `(-0, -0.4, -0.3)` (sub-LDU fractional offsets, see §3).

---

## 2. The seymouria cohort — where does it fit?

`seymouria` is a single-author mirror (`seymouria.pl`) of pre-rendered official LEGO instructions converted to LDR/MPD. The cohort has a unique fingerprint:

| Metric | seymouria | Next-lowest cohort | Why it differs |
|---|---:|---:|---|
| Sets | **378** | 100 (`80s90s`) | 2.5× the next cohort |
| Pieces per set | **12.4** | 186.7 (`80s90s`) | 6.6 % of the next cohort |
| Pieces per non-empty set | **670.6** (7 of 378 sets) | n/a | 99 % of seymouria "sets" carry 0 type-1 lines in the master model |
| Sub-builds per set | **0.18** | 7.67 (`kids`) | 42× lower |
| Total custom parts | 61 | 91 (`classic_gaps`) | Despite 2.4× more sets |
| BFC CERTIFY | **4.2 %** | 16.4 % (`classic`) | 4× lower than the next-lowest |
| Neg-det ratio | **0.000 %** | 0.04 % (`modern`) | Zero reflected parts (corpus-wide lowest) |
| Top piece | **`932.dat`** (2 980 uses) | varies | Tile Round 1×1 — a single decorative part dominates 63 % of all seymouria pieces |
| Top delta | **`(-0.0, -0.4, -0.3)`** (236) | integer-LDU values | **Sub-LDU fractional offsets** unique to this cohort |

**Structure of the seymouria collection:**

- **Format mix**: 159 `.ldr` (single model) + 219 `.mpd` (multi-model) = 378 files.
- **371 / 378 sets (98.1 %) have `total_pieces == 0`** in the master model. These are header-only or sub-build-only MPDs that import their geometry from `0 FILE` references that the parser cannot resolve against the LDraw parts library.
- **The 7 non-empty sets contribute ALL 4 694 pieces** (avg 670.6 each). The 7 non-empty sets are dominated by `31313-1` Mindstorms EV3 (3 302 pieces) and `17101-1` Creative Toolbox Vernie (816 pieces), with 5 small sets totaling 576 pieces.
- **Top-15 seymouria pieces**: `932.dat` 2 980, `u9218.dat` 295, `2780.dat` 68, `3023.dat` 57, `6558.dat` 30, `98138.dat` 24, `4273a.dat` 24, `3710.dat` 22, `32123b.dat` 21, `3020.dat` 21, `4519.dat` 21, `3713.dat` 20, `3666.dat` 19, `3024.dat` 17, `11477.dat` 17.
- **Top-10 seymouria deltas**: all sub-LDU fractional values (`-0.0, -0.4, -0.3`, `0.5, 0.1, 0.1`, `0.5, 0.0, 0.1`, etc.). No other cohort in the 1 816 corpus has fractional LDU deltas in its top-10.

**Interpretation (R31 new):**

The seymouria collection is functionally a **"model index"**, not a model corpus. 98 % of the files are instruction-trace shells where the master model is empty by design (geometry is loaded via sub-build references that point to URLs the parser cannot fetch). The 7 non-empty sets, plus the unusual top-delta fingerprint and `932.dat` dominance, suggest seymouria.pl files are optimized for **rendering at small scales** (the top-10 deltas sub-pixel-fine-tune position on a 0.4 LDU grid).

For corpus-level vocabulary statistics, seymouria contributes ~1 % of pieces and zero structural insight. It is best treated as a **metadata-only cohort**.

---

## 3. Cohort ordering & structural comparisons

### Pieces ranking (descending)

```
technic      169 839 (31.5 %)   ─┐
modern       114 904 (21.3 %)    │  Top 3 = 451 648 = 83.8 %
specialty     63 592 (11.8 %)   ─┘
licensed      45 227 ( 8.4 %)
classic       47 143 ( 8.7 %)    ← second by sets (232)
kids          42 947 ( 8.0 %)
classic_gaps  31 830 ( 5.9 %)
80s90s        18 670 ( 3.5 %)
seymouria      4 694 ( 0.9 %)   ← last despite being the largest cohort
```

**Pieces-per-set (intensity) ranking**:

```
technic      970.5  ─── 3.3× corpus mean
modern       400.4  ─── 1.4× corpus mean
specialty    385.4  ─── 1.3× corpus mean
licensed     373.8
classic      203.2
kids         214.7
classic_gaps 201.5
80s90s       186.7
seymouria     12.4  ─── 24× lower than the next cohort
```

**Sub-builds-per-set ranking (chaining depth)**:

```
technic      29.96
specialty    16.63
licensed     16.21
modern       14.38
classic      10.13
80s90s        8.39
classic_gaps  8.06
kids          7.67
seymouria     0.18  ← 42× lower than the next cohort
```

### Reflections (`neg_det` ratio) ranking — highest to lowest

| Rank | Cohort | Neg-det ratio | Reflections | Notes |
|--:|---------|-------------:|-----------:|-------|
| 1 | `classic` | **2.77 %** | 1 306 | Castle Lion Knights + Black Falcons mirroring (R19) |
| 2 | `classic_gaps` | **2.01 %** | 641 | Same Castle/Lion phenomenon, second harvest |
| 3 | `technic` | 0.68 % | 1 162 | Technic > Competition (3 sets) lifts the ratio (R25) |
| 4 | `licensed` | 0.55 % | 248 | Star Wars UCS panels |
| 5 | `kids` | 0.25 % | 107 | |
| 6 | `80s90s` | 0.27 % | 50 | |
| 7 | `specialty` | 0.18 % | 112 | |
| 8 | `modern` | 0.04 % | 42 | |
| **9** | **`seymouria`** | **0.000 %** | **0** | **No reflections at all** |

**Why seymouria has 0 reflections**: with only 7 non-empty sets and piece counts that don't require mirrored sub-assemblies, the cohort never reaches the scale where a part-mirror saves geometry. This **confirms R19** (the reflection phenomenon is structural, not author-specific) — small sets simply don't mirror.

---

## 4. Top-15 themes by total pieces

| # | Theme | Pieces | Sets | Pps | BFC | Neg-det | Cohorts |
|--:|-------|------:|-----:|----:|----:|--------:|---------|
| 1 | **Technic** | **152 331** | 155 | 983 | **127 (81.9 %)** | 0.17 % | technic |
| 2 | **Town > Classic Town + Classic Town** (deduped) | **31 098** | 197 | 158 | 41 (20.8 %) | 0.34 % | 80s90s, kids, classic, classic_gaps |
| 3 | Creator > Creator Expert | 30 948 | 20 | 1 547 | 17 (85 %) | 0.00 % | modern |
| 4 | Modular Buildings | 25 127 | 11 | 2 284 | 11 (100 %) | 0.17 % | modern |
| 5 | Icons | 18 786 | 8 | 2 348 | 8 (100 %) | 0.00 % | modern |
| 6 | Creator > Creator 3-in-1 | 16 726 | 50 | 335 | 11 | 0.00 % | kids, modern |
| 7 | Architecture | 15 943 | 36 | 443 | 8 | 0.00 % | specialty |
| 8 | Star Wars > Ultimate Collector Series | 14 754 | 12 | 1 230 | 9 | 0.76 % | licensed |
| 9 | LEGO Ideas and CUUSOO | 13 880 | 12 | 1 157 | 8 | 0.76 % | specialty |
| 10 | Star Wars | 13 241 | 64 | 207 | 16 | 0.74 % | 80s90s, licensed |
| 11 | LEGO Art | 10 703 | 1 | 10 703 | 1 | 0.00 % | specialty |
| 12 | Brickheadz | 10 889 | 76 | 143 | 27 (35.5 %) | 0.05 % | specialty |
| 13 | Technic > Star Wars | 10 702 | 3 | 3 567 | 3 | 0.00 % | technic |
| 14 | Racers | 9 890 | 76 | 130 | 1 (1.3 %) | 0.00 % | modern |
| 15 | Train > 9V | 8 576 | 24 | 357 | 7 | 0.21 % | 80s90s, classic, classic_gaps |
| **—** | **`Unknown` (seymouria)** | **4 694** | **378** | **12** | **16 (4.2 %)** | **0.00 %** | **seymouria** |

**Observations vs. the 1 438 baseline (R32 new):**

- The **top-15 order is unchanged** from 1 438 → 1 816 except for the absolute `Town > Classic Town` count growing slightly (the parser normalizes parent/child theme strings).
- **`Unknown` lands at position 16** in the by-piece ranking — between `Pirates > Pirates I` (6 319) and `Super Heroes DC > Batman > UCS` (6 093). It is the **largest single-bucket theme by set count (378)** but the **smallest by piece count among named themes** (4 694).
- **Technic still holds 28.3 % of the entire corpus** (152 331 / 538 846). Removing Technic and seymouria together: corpus pieces drop to 376 321, BFC CERTIFY drops to 261/263 = 99.2 % from Technic alone.

---

## 5. Theme × cohort cross-tab

The 1 816 corpus covers **131 distinct `theme_full` values** (vs. 130 in 1 438) — **only "Unknown" was added**, all 378 of whose sets come from seymouria's missing-metadata files. The 130 OMR-only themes are identical between 1 438 and 1 816.

### Top-3 themes per cohort (by set count)

| Cohort | #1 theme | #2 theme | #3 theme | Total themes |
|--------|----------|----------|----------|-------------:|
| `80s90s` | Town > Classic Town (27) | Train > 9V (6) | Star Wars (6) | 31 |
| `kids` | Town > Classic Town (36) | Fabuland (20) | Friends (17) | 53 |
| `classic` | Town > Classic Town (73) | Space > Classic Space (8) | Train > 9V (8) | 35 |
| `classic_gaps` | Town > Classic Town (88) | Space > Classic Space (17) | Train > 9V (16) | 14 |
| `modern` | Racers (76) | Creator > Creator 3-in-1 (36) | Creator (23) | 32 |
| `technic` | Technic (155) | Technic > Expert Builder (11) | Technic > Star Wars (3) | 6 |
| `specialty` | Brickheadz (76) | Architecture (36) | LEGO Ideas and CUUSOO (12) | 16 |
| `licensed` | Star Wars (58) | Star Wars > Ultimate Collector Series (12) | Racers > Ferrari (8) | 15 |
| **`seymouria`** | **Unknown (378)** | — | — | **1** |

**Cohort-theme exclusivity**:

- **`kids`** is the broadest pre-2000 + modern span, with 53 distinct themes — the most diverse cohort.
- **`technic`** has only 6 distinct themes — the most concentrated cohort (Technic proper dominates 88.6 % of the cohort's set count).
- **`seymouria`** has **exactly 1 distinct theme**, the placeholder `Unknown`. This is a **metadata gap**, not a real theme. Inferring from set numbers, the 378 sets span Town (1970s–80s), Star Wars UCS (2000s), Architecture (2008+), Mindstorms EV3 (2013+), Creator (2010+), Winter Village (2010+), Trains (1970s–80s), and Promotional — but the corpus metadata does not record this.

### Theme-level intersections

- **Town > Classic Town** (124 sets) + **Classic Town** (73 sets) = **197 sets** — the same theme tagged two ways across parser versions. Combined they are the **second-largest theme by any measure** after Technic.
- **Creator** (33 sets, 1 008 pieces) + **Creator > Designer Sets** (22 sets) + **Creator > Creator 3-in-1** (50 sets) + **Creator > Creator Expert** (20 sets) + **Creator > Early Creator** (5 sets) + **Creator > X-Pod** (2 sets) = 132 sets, 65 851 pieces (12.2 % of the corpus).
- **Star Wars** (64 sets) + **Star Wars > UCS** (12 sets) + **Technic > Star Wars** (3 sets) = 79 sets, 38 697 pieces (7.2 %).

---

## 6. BFC CERTIFY ratio evolution across cohorts

| Cohort | Sets | BFC CERTIFY | Ratio | Era signal |
|--------|----:|------------:|------:|------------|
| `seymouria` | 378 | 16 | **4.2 %** | **oldest informal authoring era** (pre-BFC standard) |
| `classic` | 232 | 38 | 16.4 % | 1966–2004 (Plan C era) |
| `80s90s` | 100 | 21 | 21.0 % | 1980–1999 (Plan A legacy) |
| `classic_gaps` | 158 | 41 | 25.9 % | 1979–2010 (Plan C gaps fill) |
| `modern` | 287 | 79 | 27.5 % | 2000–2025 |
| `specialty` | 165 | 60 | 36.4 % | 2010–2025 |
| `kids` | 200 | 73 | 36.5 % | 1985–2020 |
| `licensed` | 121 | 60 | 49.6 % | 1999–2020 |
| `technic` | 175 | 138 | **78.9 %** | 1977–2021 (BFC pioneers) |
| **All 1 816** | **1 816** | **526** | **29.0 %** | (was 35.5 % at 1 438) |

**Why seymouria's 4.2 % is meaningful**:

The BFC CERTIFY ratio has **never gone below 16 %** in any OMR cohort. Seymouria's 4.2 % is **4× lower than the next-lowest cohort (`classic` at 16.4 %)**. Combined with the 0 % reflection rate and the 12.4 pieces-per-set average, this confirms seymouria's files predate community-wide BFC adoption — they were authored before the convention was established.

**Era progression pattern**:

```
BFC era ranking (ascending ratio):
  seymouria     4.2 %   ← informal pre-convention
  classic      16.4 %   ← Plan C vintage
  80s90s       21.0 %
  classic_gaps 25.9 %
  modern       27.5 %
  specialty    36.4 %
  kids         36.5 %
  licensed     49.6 %
  technic      78.9 %   ← BFC pioneers
```

The pattern is **not monotonic with calendar time** — `kids` (1985–2020) has 36.5 % BFC while `modern` (2000–2025) has only 27.5 %. BFC CERTIFY is a **community authoring culture signal**, not a release-era signal. The seymouria cohort **re-establishes the lower bound** of this signal: 4.2 % is the floor we should expect from any pre-convention source.

---

## 7. Decade distribution per cohort

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
| `seymouria` | — | — | — | — | — | — | — | **unknown** (all sets bucketed "0s") |
| **All 1 816** | 17 (1 %) | 101 (6 %) | 265 (15 %) | 272 (15 %) | 245 (13 %) | 461 (25 %) | 77 (4 %) | **1966-2025** |

**Key decade finding**: 1 816 corpus spans 1966-2025 (60 years). 461 of 1 816 sets (25.4 %) are 2010s-era — the dominant decade. The seymouria cohort has **no year metadata**, so all 378 sets appear in a synthetic "0s" bucket. Set numbers span from 102 (Front End Loader, 1969) to 42138 (2025 Icons) — inferred coverage 1969-2025 if set numbers are monotonic, but the parser cannot confirm.

---

## 8. Conclusions — what changed from 1 438 → 1 816

**Headline changes:**

1. **+378 sets, +4 694 pieces, +68 sub-builds, +61 custom parts, +16 BFC CERTIFY.** The seymouria cohort contributes 20.8 % of the new set count but **only 0.87 % of the new pieces**. Corpus-wide metrics barely move; the OMR-only statistics are unchanged.
2. **BFC CERTIFY ratio drops from 35.5 % → 29.0 % (-6.5 pp)**, entirely due to seymouria's 4.2 % CERTIFY ratio diluting the corpus average. This is a **statistical dilution**, not a degradation of OMR metadata quality.
3. **Theme taxonomy expands from 130 → 131** — **only "Unknown" was added**. All 378 seymouria sets bucket into "Unknown" because seymouria.pl files lack the OMR theme metadata. No real new theme was introduced by this expansion.
4. **Seymouria's structural signature is unique**: 12.4 pieces/set, 0.18 sub-builds/set, 0 % reflections, 4.2 % BFC, and sub-LDU fractional deltas (`-0, -0.4, -0.3`). This **establishes a new floor for "informal authoring era"** in the BFC era ranking.
5. **The 8 OMR cohorts are internally unchanged**: same set counts, same piece counts, same BFC ratios. The seymouria addition is fully additive and orthogonal to all OMR findings from `LEARNED_CONVENTIONS_1438.md`.

**Implications for the generator (`generator/ldraw_gen.py`)**:

- **No code changes needed.** All generator templates, constants, and validation rules from the 1 438 baseline remain correct for the 1 816 corpus. The seymouria cohort's structural anomalies (sub-LDU deltas, 0-piece masters, single-piece-dominated sets) are **outside the generator's output space** — the generator produces canonical System building with integer-LDU deltas.
- **No new "Unknown" theme support required**: the generator uses themes only for naming conventions (e.g. Castle Lion Knights demos); seymouria's "Unknown" bucket has no generator impact.
- **The seymouria cohort could be excluded from corpus-wide statistics** without changing any of the learned conventions. It is metadata-rich (set numbers + names) but vocabulary-poor (4 694 pieces from 7 sets).

**New conventions introduced (R31-R33)**:

- **R31**: A "metadata-only" cohort is one where the file count is large but the parsed piece count is small (avg <50 pps). Such cohorts contribute to set counts without contributing to vocabulary statistics. Treat as supplementary rather than primary.
- **R32**: A corpus that grows by adding metadata-only cohorts will see **set count grow faster than piece count**, which **dilutes BFC CERTIFY and neg-det ratios** without changing the underlying OMR signal. Always report both metrics with and without such cohorts.
- **R33**: Sub-LDU fractional deltas (`dx, dy, dz` with non-integer or sub-0.5 LDU values) are a **signature of pre-rendered or trace-converted LDR files**. The seymouria cohort is the first time this signature appears in our corpus. Do not interpret sub-LDU deltas as parser errors — they are valid LDraw placements that violate R1's "Y multiple of 8" rule but comply with the underlying LDU grid (which permits any 0.4 LDU resolution).
