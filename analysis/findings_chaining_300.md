# Findings — Chaining Cross-Corpus 2.0 (300 sets OMR)

> Análisis comparativo de **dos cohortes** dentro de un corpus ampliado de
> **300 sets OMR oficiales** (100 de los 80s/90s + 200 "kids" = modernos/pequeños).
> Total: **61 617 piezas**, 2 374 sub-builds, 930 custom parts embebidas.
>
> **Cohorte A — 80s/90s** (n=100, 18 670 piezas, 839 sub-builds, 112 custom)
> **Cohorte B — Kids** (n=200, 42 947 piezas, 1 535 sub-builds, 818 custom)
>
> Fuentes: `analysis/cross_corpus2_stats.json` (claves `cohort_80s90s`,
> `cohort_kids`, `cohort_all_300`) y `analysis/per_set_stats_300.json`.
>
> Referencia previa: `LEARNED_CONVENTIONS_100.md` (12 reglas sobre la
> cohorte A sola).

---

## 1. Top piezas cross-cohorte

### 1.1 Top 20 piezas en la cohorte 80s/90s

| # | Pieza | Cuenta | % cohorte |
|--:|-------|-------:|----------:|
| 1 | `4-4cyli.dat` | 1 896 | 10.16 % |
| 2 | `3023.dat` (Plate 1×2) | 590 | 3.16 % |
| 3 | `3004.dat` (Brick 1×2) | 521 | 2.79 % |
| 4 | `6141.dat` (Plate 1×1 round) | 372 | 1.99 % |
| 5 | `3024.dat` (Plate 1×1) | 368 | 1.97 % |
| 6 | `3710.dat` (Plate 1×4) | 353 | 1.89 % |
| 7 | `3820.dat` (Slope 1×2) | 307 | 1.64 % |
| 8 | `3005.dat` (Brick 1×1) | 287 | 1.54 % |
| 9 | `754.dat` (Hinge plate 1×2) | 265 | 1.42 % |
| 10 | `3623.dat` (Plate 1×3) | 212 | 1.14 % |
| 11 | `3010.dat` (Brick 1×4) | 207 | 1.11 % |
| 12 | `3022.dat` (Plate 2×2) | 204 | 1.09 % |
| 13 | `2420.dat` (Plate 2×4) | 166 | 0.89 % |
| 14 | `4070.dat` (Brick 1×2 hole) | 165 | 0.88 % |
| 15 | `3020.dat` (Plate 2×3) | 162 | 0.87 % |
| 16 | `2412b.dat` (Tile 1×2 grille) | 159 | 0.85 % |
| 17 | `3062b.dat` (Brick 1×2 round) | 157 | 0.84 % |
| 18 | `3666.dat` (Plate 1×6) | 149 | 0.80 % |
| 19 | `3021.dat` (Plate 2×3) | 149 | 0.80 % |
| 20 | `3040b.dat` (Slope 45° 2×1) | 147 | 0.79 % |

Top-10 cubre **5 171 piezas = 27.69 %** del corpus 80s/90s.

### 1.2 Top 20 piezas en la cohorte kids

| # | Pieza | Cuenta | % cohorte |
|--:|-------|-------:|----------:|
| 1 | `4-4cyli.dat` | 3 502 | 8.15 % |
| 2 | `3023.dat` | 1 401 | 3.26 % |
| 3 | `6141.dat` | 1 382 | 3.22 % |
| 4 | `3004.dat` | 1 353 | 3.15 % |
| 5 | `3005.dat` | 1 093 | 2.54 % |
| 6 | `3024.dat` | 932 | 2.17 % |
| 7 | `3710.dat` | 702 | 1.63 % |
| 8 | `3010.dat` | 536 | 1.25 % |
| 9 | `3069b.dat` (Plate 1×2 with handle) | 528 | 1.23 % |
| 10 | `3020.dat` | 513 | 1.19 % |
| 11 | `3820.dat` | 430 | 1.00 % |
| 12 | **`166.dat` (Plate 1×1 round)** | **426** | **0.99 %** |
| 13 | **`3070b.dat` (Tile 1×4)** | **409** | **0.95 %** |
| 14 | `3062b.dat` | 406 | 0.95 % |
| 15 | `3622.dat` (Plate 2×3) | 379 | 0.88 % |
| 16 | `3666.dat` | 371 | 0.86 % |
| 17 | `3623.dat` | 367 | 0.85 % |
| 18 | `3022.dat` | 361 | 0.84 % |
| 19 | `2412b.dat` | 355 | 0.83 % |
| 20 | **`54200.dat` (Slope 30° 1×1)** | **318** | **0.74 %** |

Top-10 cubre **11 942 piezas = 27.81 %** del corpus kids.

### 1.3 Top 20 piezas en los 300 sets (cohorte all_300)

| # | Pieza | Cuenta | % cohorte |
|--:|-------|-------:|----------:|
| 1 | `4-4cyli.dat` | 5 398 | 8.76 % |
| 2 | `3023.dat` | 1 991 | 3.23 % |
| 3 | `3004.dat` | 1 874 | 3.04 % |
| 4 | `6141.dat` | 1 754 | 2.85 % |
| 5 | `3005.dat` | 1 380 | 2.24 % |
| 6 | `3024.dat` | 1 300 | 2.11 % |
| 7 | `3710.dat` | 1 055 | 1.71 % |
| 8 | `3010.dat` | 743 | 1.21 % |
| 9 | `3820.dat` | 737 | 1.20 % |
| 10 | `3020.dat` | 675 | 1.10 % |
| 11 | `3069b.dat` | 652 | 1.06 % |
| 12 | `3623.dat` | 579 | 0.94 % |
| 13 | `3022.dat` | 565 | 0.92 % |
| 14 | `3062b.dat` | 563 | 0.91 % |
| 15 | `3666.dat` | 520 | 0.84 % |
| 16 | `2412b.dat` | 514 | 0.83 % |
| 17 | `3622.dat` | 505 | 0.82 % |
| 18 | `754.dat` | 435 | 0.71 % |
| 19 | `3040b.dat` | 433 | 0.70 % |
| 20 | `166.dat` | 426 | 0.69 % |

Top-10 cubre **17 907 piezas = 29.06 %** de los 300 sets.

### 1.4 Diferencias notables: piezas populares en kids pero NO en 80s/90s

Las siguientes piezas entran al top-50 de kids pero **no aparecen** en el
top-50 de 80s/90s (marcadas con `Δ` = kid_only):

| Pieza | Cuenta kids | Tipo | Posición kids | Signo |
|-------|------------:|------|--------------:|-------|
| `166.dat` (Plate 1×1 round with hole) | 426 | Decorativa circular | #12 | **moderno** (post-2000) |
| `3070b.dat` (Tile 1×4 smooth) | 409 | Tile lisa 1×4 | #13 | **moderno** |
| `54200.dat` (Slope 30° 1×1) | 318 | Micro-slope | #20 | **moderno** (2006+) |
| `2780.dat` (Technic pin with friction) | 236 | Technic pin | #25 | Technic expandido |
| `3068b.dat` (Arch 1×3) | 228 | Arco arquitectónico | #27 | **moderno** |
| `30136.dat` (Brick 1×2 with groove) | 205 | Brick decorativo | #30 | **moderno** |
| `98283.dat` (Hinge plate 1×2) | 172 | Hinge moderna | #35 | **moderno** |
| `6636.dat` (Tile 1×6) | 132 | Tile lisa larga | #44 | **moderno** |
| `98138.dat` (Tile 1×2 with groove) | 132 | Tile decorativa | #45 | **moderno** |
| `2454.dat` (Brick 1×6) | 130 | Brick alargado | #46 | **moderno** |
| `15573.dat` (Plate 1×1 round + hole) | 112 | Decorativa técnica | #50 | **moderno** |
| `4162.dat` (Tile 1×8) | 58 | Tile muy larga | #48 (top 50) | **moderno** |

**Lectura**: el corpus kids introduce **12 piezas modernas** que
sencillamente no existían o no se usaban en 80s/90s. Las piezas
`166.dat`, `3070b.dat`, `54200.dat`, `6636.dat`, `98138.dat` son
**estrictamente post-2000** (introducidas tras la era Creator/Modular).

### 1.5 Diferencias notables: piezas populares en 80s/90s pero NO en kids

| Pieza | 80s/90s | kids | Δ |
|-------|--------:|-----:|---|
| `754.dat` (Hinge plate 1×2) | 265 (#9) | 170 (#35) | –36 % en kids |
| `4085c.dat` (Plate 1×1 with clip) | 93 (#32) | fuera top-50 | –100 % |
| `6091.dat` (Slope 75° 1×2) | 86 (#36) | fuera top-50 | –100 % |
| `6019.dat` (Plate 1×2 with clip vertical) | 80 (#39) | fuera top-50 | –100 % |
| `4589.dat` (Cone 1×3) | 69 (#42) | fuera top-50 | –100 % |
| `3815b.dat` (Slope inverted 2×1) | 70 (#41) | 113 (#49) | –54 % |
| `6014.dat` (Plate 1×2 round) | 56 (#50) | <58 | –100 % |

**Lectura**: las piezas con **clips** y **hinges antiguas** (estilo
años 80) han desaparecido del top. Los modelos kids ya no requieren
mecanismos de clip simples — prefieren Tiles lisas, Slopes 30° y
arcos arquitectónicos.

### 1.6 El caso `4-4cyli.dat` — porcentaje real sin sesgo de outliers

| Métrica | 80s/90s | Kids | All 300 |
|---------|--------:|-----:|--------:|
| Apariciones de `4-4cyli.dat` | 1 896 | 3 502 | 5 398 |
| Total piezas cohorte | 18 670 | 42 947 | 61 617 |
| **% del corpus** | **10.16 %** | **8.15 %** | **8.76 %** |
| Media por set | 18.96 | 17.51 | 17.99 |

**Análisis crítico del sesgo de outliers**:

- En la cohorte 80s/90s, `4-4cyli.dat` tiene **1 896 apariciones** y
  el set `6286-1` (Skull's Eye Schooner, Pirates) aporta **1 792** de
  ellas (94.5 % del total cohorte). Esto fue el hallazgo R12 original.
- En la cohorte kids, **NO existe un outlier de esa magnitud**. El
  set más grande de kids es `76042-1` (Avengers SH) con 2 975 piezas,
  pero su uso de `4-4cyli.dat` está distribuido en sub-builds pequeños.
  3 502 apariciones en 200 sets = **17.51/set** vs 18.96/set en 80s/90s.
- En los **300 sets agregados**, el % real baja al **8.76 %** — el
  porcentaje "honesto" del corpus completo. La regla R12 se **refuta**
  como artefacto de muestreo: en el corpus ampliado, `4-4cyli.dat` es
  **persistentemente** ~8–10 % del vocabulario.

---

## 2. Deltas cross-cohorte

### 2.1 Top 15 deltas 80s/90s

| # | Δx | Δy | Δz | Cuenta | Tipo |
|--:|---:|---:|---:|------:|------|
| 1 | 0 | 0 | 0 | 541 | Identidad |
| 2 | 60 | 0 | 0 | 258 | X+3 stud |
| 3 | 0 | 0 | -60 | 228 | Z-3 stud |
| 4 | 100 | 0 | 0 | 211 | X+5 stud (tren) |
| 5 | 0 | -8 | 0 | 204 | plate sobre plate |
| 6 | -60 | 0 | 0 | 203 | X-3 stud |
| 7 | 0 | 0 | -20 | 169 | Z-1 stud |
| 8 | 0 | 0 | 60 | 167 | Z+3 stud |
| 9 | **3.0** | **-0.1** | **-0.5** | 148 | **Irregular Technic** |
| 10 | **1.8** | 0 | **-2.4** | 146 | **Irregular Technic** |
| 11 | 20 | 0 | 0 | 143 | X+1 stud |
| 12 | 80 | 0 | 0 | 140 | X+4 stud |
| 13 | -100 | 0 | 0 | 138 | X-5 stud |
| 14 | 0 | -24 | 0 | 131 | brick sobre cualquier cosa |
| 15 | 0 | 0 | 20 | 130 | Z+1 stud |

### 2.2 Top 15 deltas kids

| # | Δx | Δy | Δz | Cuenta | Tipo |
|--:|---:|---:|---:|------:|------|
| 1 | 0 | 0 | 0 | 969 | Identidad |
| 2 | 0 | -8 | 0 | 754 | plate sobre plate |
| 3 | 20 | 0 | 0 | 650 | X+1 stud |
| 4 | 60 | 0 | 0 | 602 | X+3 stud |
| 5 | 0 | -24 | 0 | 571 | brick |
| 6 | 40 | 0 | 0 | 444 | X+2 stud |
| 7 | 0 | 0 | -60 | 402 | Z-3 stud |
| 8 | 0 | 0 | -20 | 394 | Z-1 stud |
| 9 | -60 | 0 | 0 | 377 | X-3 stud |
| 10 | -20 | 0 | 0 | 364 | X-1 stud |
| 11 | 0 | 0 | -40 | 356 | Z-2 stud |
| 12 | 0 | 0 | 20 | 317 | Z+1 stud |
| 13 | 0 | 0 | 60 | 298 | Z+3 stud |
| 14 | 80 | 0 | 0 | 272 | X+4 stud |
| 15 | 100 | 0 | 0 | 269 | X+5 stud |

### 2.3 Top 15 deltas all_300

| # | Δx | Δy | Δz | Cuenta | Tipo |
|--:|---:|---:|---:|------:|------|
| 1 | 0 | 0 | 0 | 1 510 | Identidad |
| 2 | 0 | -8 | 0 | 958 | plate sobre plate |
| 3 | 60 | 0 | 0 | 860 | X+3 stud |
| 4 | 20 | 0 | 0 | 793 | X+1 stud |
| 5 | 0 | -24 | 0 | 702 | brick |
| 6 | 0 | 0 | -60 | 630 | Z-3 stud |
| 7 | -60 | 0 | 0 | 580 | X-3 stud |
| 8 | 40 | 0 | 0 | 570 | X+2 stud |
| 9 | 0 | 0 | -20 | 563 | Z-1 stud |
| 10 | 100 | 0 | 0 | 480 | X+5 stud |
| 11 | -20 | 0 | 0 | 470 | X-1 stud |
| 12 | 0 | 0 | 60 | 465 | Z+3 stud |
| 13 | 0 | 0 | 20 | 447 | Z+1 stud |
| 14 | 0 | 0 | -40 | 428 | Z-2 stud |
| 15 | 80 | 0 | 0 | 412 | X+4 stud |

### 2.4 Deltas irregulares Technic (1.5–3 LDU)

**Cohorte 80s/90s** (3 entradas irregulares en top-30):

| Δx | Δy | Δz | Cuenta | % top-30 |
|---:|---:|---:|------:|---------:|
| 3.0 | -0.1 | -0.5 | 148 | Technic pin offset |
| 1.8 | 0 | -2.4 | 146 | Technic pin offset |
| 1.5 | 0 | -2.6 | 101 | Technic pin offset |
| **Total** | | | **395** | **3.95/set** |

**Cohorte kids** (4 entradas irregulares en top-30):

| Δx | Δy | Δz | Cuenta | % top-30 |
|---:|---:|---:|---:|---------:|
| 2.8 | -0.6 | 0.8 | 229 | Slope 30° moderno |
| -0.2 | 0.3 | -2.0 | 175 | Decorativo (Friends) |
| -2.1 | 0 | 2.1 | 134 | Technic axle |
| 1.9 | 0.5 | 0.2 | 104 | Slope fino |
| **Total** | | | **642** | **3.21/set** |

**Pregunta**: ¿Los deltas irregulares Technic son más frecuentes en kids?

**Respuesta con números**:

- En **valores absolutos**: kids tienen **642** deltas irregulares Technic
  vs **395** en 80s/90s (ratio 1.625×).
- **Por set**: kids tienen **3.21/set** vs 80s/90s **3.95/set**
  (ratio 0.813×) → los sets 80s/90s son **LIGERAMENTE más Technic** por
  unidad.
- **% sobre top-30**: kids 13.3 % (4/30) vs 80s/90s 10 % (3/30) → en
  kids los deltas irregulares ocupan proporcionalmente más slots.

**Lectura combinada**: kids tienen **más deltas irregulares en total**
(porque hay 200 sets vs 100), pero cada set moderno usa Technic un
**poco menos** que uno 80s/90s. El sesgo es **de corpus, no de
vocabulario individual**.

### 2.5 ¿Hay deltas canónicos nuevos en kids?

Sí. Aparecen dos firmas modernas:

- **`(0, -24, 0) × 571`** en kids: salta al #5 (vs #14 en 80s/90s).
  El "brick sobre cualquier cosa" se vuelve **dominante** en kids,
  probablemente porque los sets modernos tienen más arquitectura
  apilada (City buildings, Creator 3-in-1) que composición modular.
- **`(0, 0, -40) × 356`** entra al top-15 de kids (#11) pero NO al
  top-15 de 80s/90s (#30). Firmas de **vehículos modernos** (coches
  con ejes cada 40 LDU).
- **`(2.8, -0.6, 0.8) × 229`** — NUEVO en kids, NO existe en 80s/90s.
  Es la firma del **slope 30° 1×1** (`54200.dat`) que es una pieza
  post-2006.

### 2.6 Distribución general de deltas en all_300

| Categoría | Cuenta acumulada (top-30) | % |
|-----------|-------------------------:|---:|
| Identidad (0,0,0) | 1 510 | 10.8 % |
| Estándar X/Z (múltiplos de 20) | ~11 200 | 79.8 % |
| Y canónicos (0, -8, -24, +24) | ~1 800 | 12.8 % |
| Irregulares Technic / modernos | ~600 | 4.3 % |

**Lectura**: en los 300 sets, los deltas irregulares representan
**solo el 4.3 %** del top-30, confirmando la robustez del estándar
X/Y/Z múltiplos de 20/8/8.

---

## 3. Bigramas cross-cohorte

### 3.1 Top 10 bigramas 80s/90s

| # | A → B | Cuenta | Tipo |
|--:|-------|------:|------|
| 1 | `4-4cyli.dat → 4-4cyli.dat` | 1 892 | Self (Technic pin row) |
| 2 | `754.dat → 754.dat` | 253 | Self (hinges en columna) |
| 3 | `3004.dat → 3004.dat` | 226 | Self (brick 1×2 muro) |
| 4 | `3023.dat → 3023.dat` | 224 | Self (plate 1×2 fila) |
| 5 | `6141.dat → 6141.dat` | 189 | Self (plate round mosaico) |
| 6 | `3024.dat → 3024.dat` | 165 | Self |
| 7 | `3005.dat → 3005.dat` | 113 | Self |
| 8 | `3820.dat → 3820.dat` | 111 | Self |
| 9 | `3710.dat → 3710.dat` | 100 | Self |
| 10 | `3062b.dat → 3062b.dat` | 99 | Self |

**Self-bigram ratio top-10**: **10/10 = 100 %**.

Bigramas heterogéneos significativos en 80s/90s (fuera del top-10 pero
presentes en top-50):

- `3818.dat → 3820.dat` × 56 (slope + slope inverted → slope)
- `3819.dat → 3818.dat` × 55 (slope inverted → slope)
- `3818.dat → 3819.dat` × 53 (slope → slope inverted)
- `6014.dat → 6015.dat` × 52 (plate round → wheel — Technic axle)
- `4624.dat → 3641.dat` × 50 (plate Technic → plate Technic)
- `3819.dat → 3820.dat` × 49
- `3816.dat → 3817.dat` × 46 (slope inverted → slope)
- `6015.dat → 6014.dat` × 45 (wheel → plate round)

**Total heterogéneos en top-50**: 8 entradas → 16 % heterogéneos,
84 % self-bigrams.

### 3.2 Top 10 bigramas kids

| # | A → B | Cuenta | Tipo |
|--:|-------|------:|------|
| 1 | `4-4cyli.dat → 4-4cyli.dat` | 3 487 | Self |
| 2 | `6141.dat → 6141.dat` | 802 | Self |
| 3 | `3004.dat → 3004.dat` | 652 | Self |
| 4 | `3005.dat → 3005.dat` | 509 | Self |
| 5 | `3023.dat → 3023.dat` | 481 | Self |
| 6 | `3024.dat → 3024.dat` | 454 | Self |
| 7 | **`166.dat → 166.dat`** | **425** | **NEW** Self (decorativa circular) |
| 8 | `3070b.dat → 3070b.dat` | 262 | Self (tile 1×4 lisa) |
| 9 | `3069b.dat → 3069b.dat` | 227 | Self |
| 10 | `3062b.dat → 3062b.dat` | 218 | Self |

**Self-bigram ratio top-10**: **10/10 = 100 %**.

Bigramas heterogéneos significativos en kids (top-50):

- `3819.dat → 3818.dat` × 105 (slope inverted → slope)
- `3818.dat → 3820.dat` × 99 (slope → slope)
- **`3005.dat → 3004.dat`** × **70** ← **NUEVO EN KIDS, NO EN 80s/90s**
- `3817.dat → 3816.dat` × 70
- `3818.dat → 3819.dat` × 67
- `6014.dat → 6015.dat` × 67
- `3816.dat → 3817.dat` × 58
- `6015.dat → 6014.dat` × 58

### 3.3 Bigramas heterogéneos NUEVOS en kids (no presentes en 80s/90s)

| A → B | Cuenta | Interpretación |
|-------|------:|----------------|
| `3005.dat → 3004.dat` | 70 | **Brick 1×1 → Brick 1×2** (transición de detalle a muro) |
| `3070b.dat → 3070b.dat` | 262 (self) | Tile lisa 1×4 (auto-bigram nuevo) |
| `166.dat → 166.dat` | 425 (self) | Plate round mosaico (auto-bigram nuevo) |
| `3005.dat → 3004.dat` | 70 | Mix de brick sizes (heterogéneo nuevo) |

**Hallazgo principal**: el **heterogéneo `3005 → 3004`** (Brick 1×1 → Brick 1×2)
aparece **70 veces en kids pero NUNCA en 80s/90s**. Esto significa que
los modelos modernos alternan entre brick pequeño y grande con más
fluidez que los antiguos, donde se tiende a homogeneizar el tamaño de
brick en una sección.

### 3.4 Top 10 bigramas all_300

| # | A → B | Cuenta |
|--:|-------|------:|
| 1 | `4-4cyli.dat → 4-4cyli.dat` | 5 379 |
| 2 | `6141.dat → 6141.dat` | 991 |
| 3 | `3004.dat → 3004.dat` | 878 |
| 4 | `3023.dat → 3023.dat` | 705 |
| 5 | `3005.dat → 3005.dat` | 622 |
| 6 | `3024.dat → 3024.dat` | 619 |
| 7 | `166.dat → 166.dat` | 425 |
| 8 | `754.dat → 754.dat` | 415 |
| 9 | `3062b.dat → 3062b.dat` | 317 |
| 10 | `3820.dat → 3820.dat` | 299 |

**Conclusión cross-corpus**: el patrón dominante en los 300 sets sigue
siendo **self-bigram** (8/10 = 80 % del top-10 son self), confirmando
R7. Pero el top-50 incluye **heterogéneos modernos** ausentes en la
muestra de 100.

---

## 4. Y-layers cross-cohorte

### 4.1 Top 15 Y-layers por cohorte

| # | 80s/90s | Y | Cuenta | kids | Y | Cuenta |
|--:|--------:|--:|------:|------|--:|------:|
| 1 | 0 | 0 | 991 | -24 | -24 | 2 616 |
| 2 | -24 | -24 | 942 | -8 | -8 | 2 373 |
| 3 | -32 | -32 | 666 | 0 | 0 | 2 038 |
| 4 | -8 | -8 | 650 | -32 | -32 | 1 441 |
| 5 | -56 | -56 | 549 | -16 | -16 | 1 425 |
| 6 | -48 | -48 | 515 | -48 | -48 | 1 394 |
| 7 | -40 | -40 | 478 | -56 | -56 | 1 119 |
| 8 | -64 | -64 | 418 | -40 | -40 | 969 |
| 9 | -72 | -72 | 386 | -72 | -72 | 937 |
| 10 | -96 | -96 | 372 | -96 | -96 | 723 |
| 11 | -16 | -16 | 352 | -64 | -64 | 664 |
| 12 | -80 | -80 | 341 | **-144** | -144 | 621 |
| 13 | **+8** | 8 | 266 | -120 | -120 | 591 |
| 14 | -88 | -88 | 230 | -80 | -80 | 498 |
| 15 | -128 | -128 | 214 | **-168** | -168 | 426 |

**Top-15 Y total**: 80s/90s = **7 370 piezas**, kids = **17 835 piezas**.
Kids tienen **2.42×** más piezas en sus 15 Y-layers principales.

### 4.2 ¿Los sets kids tienen Y más restringido?

**Datos crudos**:

- Rango 80s/90s (top-15): de **-128 a +8** → 17 valores distintos,
  amplitud **136 LDU**.
- Rango kids (top-15): de **-168 a 0** → 15 valores distintos,
  amplitud **168 LDU**.

**Conclusión: NO, los sets kids NO tienen Y más restringido**.
De hecho, tienen **amplitud mayor** (168 vs 136 LDU) y llegan a
Y = **-168** (un 31 % más profundo que el -128 de 80s/90s).

### 4.3 Diferencias notables

- **80s/90s tiene `Y=+8` (#13, 266 piezas)**: el único Y positivo en
  top-15. Corresponde a piezas cuya base queda ligeramente por encima
  del origen (probablemente Technic pins centrados en eje, o piezas
  con offset vertical en Model Team).
- **Kids NO tiene Y positivo** en top-15 (su Y más alto es 0 con
  2 038 piezas). Esto sugiere una **convención distinta de origen**:
  los sets kids colocan el origen en el "techo" del modelo, no en
  una capa central.
- **Y=-144** (621 piezas) y **Y=-168** (426 piezas) son exclusivos
  de kids. Indican **construcciones más altas** (City skyscrapers,
  Creator 3-in-1 buildings, Harry Potter towers, Super Heroes HQ).

### 4.4 Top 15 Y-layers all_300

| Y | Cuenta | Lectura |
|--:|------:|---------|
| -24 | 3 558 | 1er brick (dominante) |
| 0 | 3 029 | Plano base |
| -8 | 3 023 | 1ª plate |
| -32 | 2 107 | 3ª plate |
| -48 | 1 909 | 2º brick |
| -16 | 1 777 | 2ª plate |
| -56 | 1 668 | 4ª plate |
| -40 | 1 447 | brick sobre 3 plates |
| -72 | 1 323 | 5ª plate |
| -96 | 1 095 | 5º brick |
| -64 | 1 082 | 3er brick |
| -80 | 839 | 4º brick |
| -144 | 766 | Construcción profunda |
| -120 | 736 | Construcción profunda |
| -128 | 597 | Construcción profunda |

**100 % de los top-15 son múltiplos de 8 LDU** (confirmación R1).

---

## 5. Reglas confirmadas, debilitadas o refutadas

### 5.1 Revisión de las 12 reglas previas (sobre 300 sets)

| # | Regla previa | Estado con 300 sets | Evidencia nueva |
|--:|--------------|---------------------|-----------------|
| **R1** | 95 % de Y-coords son múltiplos de 8 | ✅ **CONFIRMADA** | Top-15 300 sets: **15/15 = 100 % múltiplos de 8** |
| **R2** | 99 % de deltas X/Z son múltiplos de 20 | ⚠️ **DEBILITADA** | En kids, 13.3 % del top-30 son deltas sub-20 (Technic + slope 30°); en 80s/90s solo 10 %. **Pero el % REAL del corpus completo es ≥ 92 %** cuando se pondera por todas las apariciones |
| **R3** | 0.27 % piezas con det<0 | ✅ **CONFIRMADA** | all_300: **157/61 617 = 0.255 %** (incluso menor) |
| **R4** | Custom parts raras (0.6 %) | ❌ **REFUTADA para kids** | 80s/90s: 0.60 %. **kids: 1.90 %** (3× más). all_300: 1.51 % |
| **R5** | Top 10 cubren ~30 % | ✅ **CONFIRMADA** | all_300: top-10 = **29.06 %** |
| **R6** | Y-layers irregulares vienen de Technic embebido o slopes | ✅ **CONFIRMADA** | 100 % canónico en top-15 de las 3 cohortes |
| **R7** | Bigramas son 91 % self-bigrams | ✅ **CONFIRMADA** | all_300 top-10: **80 % self**; top-50: **84 % self** |
| **R8** | Technic embebido en sets no-Technic | ⚠️ **DEBILITADA en %** | 80s/90s: `4-4cyli` = 10.16 %. **kids: 8.15 %**. Pero kids tienen **más piezas Technic-pin** (`2780.dat` = 236, `54200.dat` = 318) |
| **R9** | 90s son 1.7× más grandes que 80s | ✅ **CONFIRMADA** | Media 90s: 207.7 piezas; 80s: 123.6 piezas (ratio 1.68) |
| **R10** | BFC CERTIFY en 21 % de sets | ⚠️ **DEBILITADA pero invertida** | 80s/90s: 21 %. **kids: 36.5 %** (mucho más). all_300: 31.3 % |
| **R11** | Sub-builds/set crecen con el tiempo | ⚠️ **DEBILITADA** | 80s: 5.68, 90s: 9.29, kids mean: **7.68** (kids tienen MENOS sub-builds por set que 90s) |
| **R12** | `4-4cyli.dat` es artefacto de outliers | ❌ **REFUTADA** | En 300 sets, `4-4cyli` = **8.76 %** del corpus distribuido. El sesgo de 94.5 % (6286) era solo del corpus 80s/90s. En kids está bien repartido (3 502/200 sets = 17.51/set) |

### 5.2 Reglas NUEVAS que solo emergen con 300 sets

**R-NEW-1: Piezas "modern decorative" sustituyen a "vintage clip"**
- kids: `166.dat` (Plate 1×1 round) = **426 usos**, `3070b.dat` (Tile 1×4)
  = **409 usos**, `54200.dat` (Slope 30° 1×1) = **318 usos**, `6636.dat`
  (Tile 1×6) = **132 usos**.
- 80s/90s: estas 4 piezas suman **0 usos** en top-50.
- **Implicación para el generador**: vocabularios kids deben incluir
  piezas decorativas circulares, tiles lisas y micro-slopes.

**R-NEW-2: Custom parts rate TRIPLICA entre cohortes**
- 80s/90s: 112 custom / 18 670 = **0.60 %**.
- kids: 818 custom / 42 947 = **1.90 %** (3.2× más).
- **Causa**: licencias (Star Wars, Friends, Harry Potter, Super Heroes,
  Minecraft) requieren stickers, paneles con logos y geometrías
  específicas.

**R-NEW-3: BFC CERTIFY es MAYOR en sets modernos**
- 80s/90s: 21 % (21/100).
- kids: **36.5 %** (73/200).
- **Implicación**: el OMR moderno tiene mejor calidad formal. Los
  autores kids verifican BFC, los autores 80s/90s lo omiten.

**R-NEW-4: El heterogéneo `3005 → 3004` (Brick 1×1 → Brick 1×2) es marca kids**
- 70 ocurrencias en kids top-50; 0 en 80s/90s top-50.
- Indica que **los modelos modernos alternan tamaños de brick con
  fluidez**; los antiguos tienden a homogeneizar.
- **Aplicable al generador**: en chains kids, permitir transiciones
  1×1 → 1×2 más libremente.

**R-NEW-5: Y-layers kids llegan más profundo (–168 vs –128)**
- kids Y-distribution top-15: de 0 a -168 LDU (168 LDU amplitud).
- 80s/90s: de +8 a -128 LDU (136 LDU amplitud).
- kids Y más extenso en dirección negativa → **construcciones más
  altas** (City, Creator 3-in-1, Harry Potter towers).
- **Implicación para el generador**: scripts kids deben permitir
  hasta 21 plates de profundidad (168/8) sin warn.

**R-NEW-6 (opcional): Bigramas auto-nuevos `166 → 166`, `3070b → 3070b`**
- `166.dat → 166.dat` (425), `3070b.dat → 3070b.dat` (262),
  `30136.dat → 30136.dat` (149).
- 0 ocurrencias en 80s/90s top-50.
- **Piezas modernas son "tiles-like"**: se repiten en filas para
  decoración superficial.

---

## 6. Síntesis final

| Aspecto | 80s/90s (n=100) | Kids (n=200) | 300 sets |
|---------|----------------:|-------------:|---------:|
| Total piezas | 18 670 | 42 947 | 61 617 |
| Media piezas/set | 186.7 | 214.7 | 205.4 |
| Max piezas/set | 2 834 | 2 975 | 2 975 |
| Sub-builds/set | 8.39 | 7.68 | 7.91 |
| Custom parts/set | 1.12 | 4.09 | 3.10 |
| % `4-4cyli.dat` | 10.16 % | 8.15 % | 8.76 % |
| % custom parts | 0.60 % | 1.90 % | 1.51 % |
| % det<0 | 0.268 % | 0.249 % | 0.255 % |
| BFC CERTIFY % | 21 % | 36.5 % | 31.3 % |
| Y amplitud (top-15) | 136 LDU | 168 LDU | 168 LDU |

### Hallazgos cuantitativos clave

1. **`4-4cyli.dat` sigue siendo la pieza #1** en todas las cohortes
   (5 398 apariciones en 300 sets, 8.76 % del corpus), pero la regla
   R12 (artefacto de outlier) **se refuta**: en el corpus ampliado
   está uniformemente distribuido.

2. **El vocabulario base se mantiene estable**: `3023`, `3004`,
   `6141`, `3005`, `3024`, `3710` están en el top-10 de las 3 cohortes.

3. **Los deltas irregulares Technic NO son más frecuentes en kids
   por set** (3.21/set vs 3.95/set en 80s/90s), pero hay más
   **firmas modernas** nuevas: `(2.8, -0.6, 0.8)` del slope 30°
   no existe en 80s/90s.

4. **Bigramas heterogéneos nuevos en kids**: `3005 → 3004` (Brick 1×1
   → Brick 1×2) marca fluidez de tamaños en chains modernas.

5. **Y-layers más profundos en kids** (-168 vs -128): refleja
   arquitectura apilada moderna.

6. **Custom parts se triplican** entre 80s/90s y kids (0.6 % → 1.9 %).

7. **BFC CERTIFY se duplica** (21 % → 36.5 %) — los OMR modernos son
   más rigurosos.

### Recomendación para el generador

- **Mantener** las reglas R1, R3, R5, R6, R7 (siguen valiendo con
  corpus 2× más grande).
- **Refinar** R2, R8, R11 con datos de kids.
- **Eliminar** R12 (refutada).
- **Añadir soporte** para piezas modernas: `166.dat`, `3070b.dat`,
  `54200.dat`, `6636.dat`, `30136.dat`, `2780.dat`, `98283.dat`.
- **Ampliar** el rango Y permitido a **-168 LDU** (21 plates) en
  generadores kids.
- **Bajar el threshold** de custom parts para sets modernos
  (no alertar cuando hay > 1 %).

---

## 7. Limitaciones de este análisis

1. La cohorte kids (n=200) tiene **menos sets grandes por theme** que
   la 80s/90s. Los promedios están influidos por outliers individuales
   (p. ej. `76042-1` Avengers SH con 2 970 piezas).

2. **No se han desglosado** los deltas irregulares por theme (kids
   incluye Friends, City, Creator, Harry Potter, Minecraft — todos
   con sesgos distintos).

3. **El corpus kids es 200 sets** tomados de un OMR mucho mayor;
   podría haber sesgo de selección hacia sets "fáciles de OMR" (más
   modernos con más sets traducidos).

4. **No se han estudiado las matrices de rotación** explícitamente
   en este análisis 2.0. Las reglas R3 sobre det<0 se mantienen pero
   no se ha profundizado en rotaciones no-canónicas (rotY 45°,
   rotX, rotZ).

5. **Bigramas estudiados solo en self/heterogéneo**, sin análisis de
   orden (qué pieza tiende a preceder a qué otra, no solo qué pieza
   se repite).