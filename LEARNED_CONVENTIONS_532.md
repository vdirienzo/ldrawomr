# LDraw Conventions — Cross-corpus 3.0 Analysis (532 OMR sets)

> **Historical note**: This document was originally written in Spanish. The English version of the canonical document (corpus 1,438 sets) is `LEARNED_CONVENTIONS_1438.md`. The Spanish original of this 532-set version is preserved as `LEARNED_CONVENTIONS_532.es.md` for traceability.

---

## 0. The 23 cross-corpus rules (definitive)

See the canonical document at [`LEARNED_CONVENTIONS_1438.md`](./LEARNED_CONVENTIONS_1438.md).

## 1. Topology of the corpus

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
| Empty STEPs | 39% | 28.5% | **49.1%** | ? |

## 2. The reflections shock (R3 refuted, R19 new)

The corpus 532 ratio of 1.345% reflections is **NOT** a corpus-wide bias — it is hyperconcentrated in Space-themed sets:

- **73 Space sets** = **87.8%** of all reflections in the corpus.
- Classic Space: **21.14%**, Unitron: **13.95%**, Blacktron I: **12.36%**.
- Classic Town (109 sets, the largest theme): ratio **0.40%** — identical to kids modern.

The bias is in the **Space theme**, not in the classic corpus. This refutes rule R3.

## 3. Top pieces cross-corpus (532 sets)

| # | Part | Count | % | Notes |
|---|------|------:|---:|-------|
| 1 | `4-4cyli.dat` | 6,093 | 5.60% | Cylinder base, universal |
| 2 | `3023.dat` (Plate 1×2) | 3,670 | 3.37% | Base vocabulary |
| 3 | `3004.dat` (Brick 1×2) | 3,293 | 3.03% | Base vocabulary |
| 4 | `6141.dat` (Plate 1×1 round) | 2,519 | 2.32% | Decoration |
| 5 | `3005.dat` (Brick 1×1) | 2,360 | 2.17% | Colonnade |
| 6 | `3024.dat` (Plate 1×1) | 2,091 | 1.92% | Detail |
| 7 | `3710.dat` (Plate 1×4) | 2,036 | 1.87% | Long chassis |
| **8** | **`756.dat` (Baseplate 16×32 Technic)** | **1,627** | **1.50%** | **🆕 NEW — Space signature** |
| 9 | `3010.dat` (Brick 1×4) | 1,500 | 1.38% | |
| 10 | `3820.dat` (Slope 1×2) | 1,229 | 1.13% | |

## 4. Top deltas (532 sets)

| # | (dx, dy, dz) | Count | % of corpus |
|---|---|---:|---:|
| 1 | (0, 0, 0) | 2,660 | 2.45% |
| 2 | (0, -8, 0) | 1,669 | 1.53% |
| 3 | (60, 0, 0) | 1,597 | 1.47% |
| 4 | (20, 0, 0) | 1,401 | 1.29% |
| 5 | (-60, 0, 0) | 1,104 | 1.02% |
| 6 | (0, -24, 0) | 1,068 | 0.98% |
| 7 | (0, 0, -60) | 1,057 | 0.97% |
| 8 | (100, 0, 0) | 1,027 | 0.94% |
| 9 | (40, 0, 0) | 1,011 | 0.93% |
| 10 | (0, 0, -20) | 968 | 0.89% |

## 5. Y-layers (532 sets)

| Y | Count | Meaning |
|---:|------:|---------|
| 0 | 6,436 | base plane |
| -8 | 6,041 | 1st plate |
| -24 | 5,976 | 1st brick |
| -32 | 3,754 | 3rd plate |
| -16 | 3,439 | 2nd plate |
| -48 | 3,164 | 2nd brick |
| -40 | 2,742 | brick+plate |
| -56 | 2,723 | 4th plate |
| -72 | 2,098 | 5th plate |
| -64 | 1,905 | 3rd brick |
| -96 | 1,738 | 5th brick |
| **+8** | **1,389** | **🆕 antenna/mast (R23)** |
| -80 | 1,345 | 4th brick |
| -144 | 1,102 | 10th brick (classic deep) |
| -120 | 1,101 | 7th brick |

## 6. Resources

For the complete canonical document with all 23 rules, see:
- `LEARNED_CONVENTIONS_1438.md` — the canonical 1,438-set document.

For per-section detail:
- `analysis/findings_chaining_300.md` — chaining detail.
- `analysis/findings_cohorts_3.md` — 3-cohort structural differences.
- `analysis/findings_themes_532.md` — theme-specific conventions.
- `analysis/findings_chaining_300.md` — chaining patterns.
- `output/dashboard.html` — interactive HTML dashboard with all stats.
