# Convenciones LDraw — Análisis cross-corpus 2.0 (300 sets OMR)

> Análisis ampliado: **300 sets oficiales del OMR**, dos cohortes:
> - **Cohorte 80s/90s** (100 sets, 18 670 piezas, 1980–1999): Town, Castle, Space, Pirates, Model Team, Star Wars, Western, etc.
> - **Cohorte kids** (200 sets, 42 947 piezas, 1985–2020): City, Creator, Friends, Fabuland, Harry Potter, Western, Castle Junior, etc.
>
> **Total**: 61 617 piezas, 1 794 sub-builds, 930 custom parts embebidas.
>
> Documentos relacionados:
> - `LEARNED_CONVENTIONS_100.md` — análisis previo (100 sets 80s/90s).
> - `LDRAW_GUIDE.md` — especificación del formato LDraw.

---

## 0. Reglas confirmadas / debilitadas / refutadas (vs las 12 reglas previas)

Las 12 reglas del corpus 100 sets se reevaluaron con los 300 sets:

| # | Regla previa (corpus 100) | Veredicto (corpus 300) |
|---|---------------------------|------------------------|
| R1 | 95 % Y-layers múltiplos de 8 | ✅ **Confirmada** (96.4 % top-15 canónicos) |
| R2 | 99 % deltas X/Z múltiplos de 20 | 🟡 **Debilitada**: en kids aparece una nueva firma `(2.8,-0.6,0.8)` del slope 30° post-2006 (no múltiplo de 20) |
| R3 | 0.27 % reflejos | ✅ **Confirmada** (0.25 % en corpus 300) |
| R4 | Custom parts = 0.6 % | ❌ **Refutada**: en kids son 1.9 % (triplica). Fabuland 9.3 %, Friends 4.1 % |
| R5 | Top 10 piezas cubren ~30 % | ✅ **Confirmada** (32.7 %) |
| R6 | Y-layers irregulares = Technic/slopes | ✅ **Confirmada** (slope 33° firma -46.1 LDU) |
| R7 | 91 % bigramas self-bigrams | ✅ **Confirmada** (90 %+) |
| R8 | Technic embebido en no-Technic | 🟡 **Debilitada**: 80s/90s ratio **mayor** (2.61 %) que kids (1.50 %) |
| R9 | 90s 1.7× más grandes que 80s | 🟡 **Invertida**: kids (mediana 2010s) son 2× más grandes que 80s/90s |
| R10 | BFC CERTIFY decrece en 90s | 🟡 **Invertida**: kids duplican BFC CERTIFY (36.5 % vs 21 %) |
| R11 | Sub-builds crecen con tiempo | 🟡 **Invertida**: 80s/90s tienen **más** sub-builds/set (8.39 vs 7.68) |
| R12 | `4-4cyli` es artefacto de outliers | ❌ **Refutada**: en corpus 300, está uniformemente distribuido (17.5 sets/uso en kids), no es outlier |

### 6 reglas NUEVAS descubiertas con los 300 sets

| # | Regla nueva | Evidencia |
|---|-------------|-----------|
| R13 | **Kids tiene vocabulario moderno** (12 piezas exclusivas del top-50) | `166`, `3070b`, `54200`, `6636`, `98138`, `30136`, `98283`, `15573`, `2780`, `3068b`, `2454`, `4162` |
| R14 | **Bigrama `3005 → 3004` (Brick 1×1 → Brick 1×2) es exclusivo de kids** | 70 ocurrencias, 0 en 80s/90s |
| R15 | **Kids llegan a Y=-168 LDU** (más profundos que 80s/90s que llegan a -128) | Por sets apilados (City skyscrapers, Castles) |
| R16 | **Piezas exclusivas de Fabuland** (~25 piezas `u91xx`) — theme con más identidad propia | 23 sets Fabuland, 9.3 % custom parts |
| R17 | **Friends es el theme más decorativo** (94 % de sets usan `6141` plate 1×1 round) | 17 sets, 208 custom parts (4.1 %) |
| R18 | **Train es el único theme con eje Z-dominante** | `(0, 0, -60) = 68 ocurrencias`, ningún `dx` significativo en top |

---

## 1. Topología cross-cohorte

| Métrica | 80s/90s | kids | All 300 |
|---------|--------:|-----:|--------:|
| Sets | 100 | 200 | 300 |
| Piezas totales | 18 670 | 42 947 | 61 617 |
| Piezas/set media | 186.7 | 214.7 | 205.4 |
| Piezas/set mediana | ~101 | ~130 | ~120 |
| Sub-builds/set media | 8.39 | 7.68 | 7.91 |
| STEPs/set media | 19.85 | 29.78 | 26.47 |
| Piezas/STEP media | 9.41 | 7.21 | 7.76 |
| Custom parts | 112 | 818 | 930 |
| Custom parts ratio | 0.6 % | 1.9 % | 1.5 % |
| BFC CERTIFY | 21 % | 36.5 % | 31.3 % |
| Reflejos | 0.27 % | 0.25 % | 0.25 % |
| STEPs vacíos | 39 % | 28.5 % | 31.7 % |

---

## 2. Vocabulario cross-cohorte

### 2.1 Top 15 piezas en los 300 sets

| Pieza | Cuenta | % corpus |
|-------|-------:|---------:|
| `4-4cyli.dat` (cylinder) | 5 398 | 8.76 % |
| `3023.dat` (Plate 1×2) | 1 991 | 3.23 % |
| `3004.dat` (Brick 1×2) | 1 874 | 3.04 % |
| `6141.dat` (Plate 1×1 round) | 1 754 | 2.84 % |
| `3005.dat` (Brick 1×1) | 1 380 | 2.24 % |
| `3024.dat` (Plate 1×1) | 1 300 | 2.11 % |
| `3710.dat` (Plate 1×4) | 1 055 | 1.71 % |
| `3010.dat` (Brick 1×4) | 743 | 1.20 % |
| `3820.dat` (Slope 1×2) | 737 | 1.19 % |
| `3020.dat` (Plate 2×4) | 675 | 1.09 % |

**Lectura**: 6 piezas estables en top-10 de las 3 cohortes (`3023`, `3004`,
`6141`, `3005`, `3024`, `3710`). Estas son **el vocabulario base** del LEGO
System desde los 80s.

### 2.2 Top 15 deltas cross-corpus

| Δx | Δy | Δz | Cuenta | Lectura |
|----:|---:|----:|-------:|---------|
| 0 | 0 | 0 | 1 510 | Misma posición (sub-build concatenado) |
| 0 | -8 | 0 | 958 | **Plate sobre plate** (Δy=-8 LDU) |
| 60 | 0 | 0 | 860 | 3-stud X+ |
| 20 | 0 | 0 | 793 | 1-stud X+ |
| 0 | -24 | 0 | 702 | **Brick (encima de cualquier cosa)** |
| 0 | 0 | -60 | 630 | 3-stud Z- |
| -60 | 0 | 0 | 580 | 3-stud X- |
| 40 | 0 | 0 | 570 | 2-stud X+ |
| 0 | 0 | -20 | 563 | 1-stud Z- |
| 100 | 0 | 0 | 480 | 5-stud X+ (trenes) |

### 2.3 Bigramas cross-corpus

**Top-5** (todos self-bigrams):
1. `4-4cyli → 4-4cyli` × 5 168 (Technic pin-holes en fila).
2. `3023 → 3023` × 1 105 (plates 1×2 en fila).
3. `3004 → 3004` × 994 (bricks 1×2 en muro).
4. `6141 → 6141` × 870 (plates redondos decorativos).
5. `3005 → 3004` × 70 — **bigrama exclusivo de kids** (Brick 1×1 sobre Brick 1×2; decoración en pared).

### 2.4 Y-layers cross-corpus (top-15)

| Y | Cuenta | Significado |
|---:|-------:|-------------|
| 0 | 6 023 | Plano base |
| -8 | 4 916 | 1ª plate apilada |
| -16 | 3 098 | 2ª plate |
| -24 | 2 580 | 1er brick |
| -32 | 1 974 | 3ª plate |
| -40 | 1 523 | brick sobre 3 plates |
| -46.1 | 1 156 | **Slope 33°** (firma absoluta) |
| -48 | 1 080 | 2º brick |
| -56 | 838 | 4ª plate |
| -64 | 712 | 3er brick |
| -72 | 597 | 5ª plate |
| -80 | 498 | 4º brick |
| -88 | 421 | 6ª plate |
| -96 | 364 | 5º brick |
| -104 | 312 | pieza alta |

---

## 3. Diferencias estructurales entre cohortes

### 3.1 Tamaño y cadencia

- **Kids son +15 % más grandes en piezas/set** (214.7 vs 186.7).
- **Kids tienen +50 % más STEPs/set** (29.78 vs 19.85) → manuales digitales más granulares.
- **Piezas/STEP**: kids 7.21 (más granular), 80s/90s 9.41 (más agregado).
- **Sub-builds**: 80s/90s **descomponen más** (8.39 vs 7.68) — probablemente porque los 80s/90s son piezas más grandes (más necesidad de modular).

### 3.2 STEPs vacíos

- **80s/90s: 39 %** STEPs vacíos — cierres de sección.
- **Kids: 28.5 %** — los sets modernos no cierran secciones con STEP vacío tanto.

### 3.3 BFC CERTIFY

- **80s/90s: 21 %** — menor conformidad formal.
- **Kids: 36.5 %** — casi duplica. Los autores modernos son más formales.

### 3.4 Custom parts

- **80s/90s: 0.6 %** (112 custom en 18 670 piezas).
- **Kids: 1.9 %** (818 custom en 42 947 piezas) — **triplica**.

Los kids contienen muchos más custom parts porque hay más sets con
licencias (Friends, Harry Potter, Disney, etc.) que requieren piezas
específicas.

### 3.5 Technic embebido (ratio deltas irregulares)

Contrariamente a la intuición, los 80s/90s tienen **mayor ratio** de
Technic embebido:
- 80s/90s: 2.61 % (395 irregulares / total).
- Kids: 1.50 % (642 irregulares / total).

Los 80s/90s integraban Technic para dar "funcionalidad" (puertas, ruedas);
los kids son más "estáticos" (decorativos).

---

## 4. Distribución por década

| Década | Sets | Piezas | Media piezas/set |
|--------|-----:|-------:|-----------------:|
| 1980s | 72 | 11 506 | 159.8 |
| 1990s | 116 | 22 052 | 190.0 |
| 2000s | 44 | 9 541 | 216.8 |
| 2010s | 66 | 18 355 | 278.1 |
| 2020s | 2 | 163 | 81.5 |

**Lectura**: los sets crecen monótonamente desde los 80s hasta los 2010s.
Los 2010s tienen la media más alta (278 piezas/set) — Modern City, Star Wars
coleccionable, Friends elaborados.

---

## 5. Convenciones por theme (top-10 con más sets en el corpus 300)

| Theme | Sets | Piezas | Media | Top pieza | Custom |
|-------|-----:|-------:|------:|-----------|-------:|
| Town > Classic Town | 36 | 5 848 | 162.4 | 3023 | 12 |
| Town | 40 | 4 394 | 109.9 | 3023 | 23 |
| Friends | 17 | 5 046 | 296.8 | 6141 | 208 |
| Pirates (inc. Pirates I) | 5+2 | 6 319 | 901.3 | 4-4cyli | 95 |
| Model Team | 5 | 3 215 | 643.0 | 754 (hinge) | 14 |
| Creator 3-in-1 | 14 | 3 143 | 224.5 | 3004 | 83 |
| Train | 9 | 2 592 | 288.0 | 3710 | 17 |
| Castle | 10 | 1 537 | 153.7 | 3004 | 7 |
| Fabuland | 23 | 1 145 | 49.8 | piezas exclusivas | 95 |
| Harry Potter | 4 | 2 407 | 601.8 | 3023 | 35 |

### 5.1 Hallazgos clave por theme

- **Pirates** dominado por 6286 Skull's Eye Schooner (86 % del theme).
  Su bigrama `4-4cyli → 4-4cyli = 1 789` es el más alto del corpus.
- **Friends** = theme más decorativo (94 % usan `6141` plate 1×1 round;
  208 custom parts = 4.1 %).
- **Fabuland** = theme con más identidad propia (~25 piezas `u91xx`
  exclusivas), 9.3 % custom parts (el más alto del corpus).
- **Creator 3-in-1** = vocabulario modular: `54200` hinge, `2780` technic pin.
- **Western** = caballo `30136 → 30136 = 137` (5/13 sets).
- **Train** = único theme con eje Z-dominante (`dz=-60` = 68, ningún
  `dx` significativo en top).
- **Castle** perdió identidad exclusiva al fragmentarse: las piezas
  signature (`2541`, etc.) están en sub-themes (Lion Knights, Black Falcons,
  Forestmen) que cuentan aparte.

---

## 6. Themes exclusivos (no aparecían en corpus 100)

Estos themes solo aparecen en la cohorte kids:

- **Friends** (17 sets): decoración pastel, plate 1×1 round masivo.
- **Creator 3-in-1** (14 sets): módulos intercambiables.
- **Designer Sets** (6 sets): sets premium de Creator.
- **Promotional Bricktober** (5 sets): sets temáticos Halloween.

---

## 7. Reglas cross-corpus definitivas (corpus 300)

### 7.1 Reglas geométricas (universales)

- **Y-layers canónicos múltiplos de 8**: 96.4 % del top-15. Slope 33° tiene
  firma absoluta en y=-46.1 LDU.
- **Deltas X/Z canónicos múltiplos de 20**: 90 %+. Excepción: Technic
  embebido (1.5-3 LDU) en 1.5-2.5 % del corpus.
- **Δy=-8** y **Δy=-24** son los deltas verticales más frecuentes
  (plate y brick respectivamente).
- **Reflejos < 0.3 %** — casi todo se construye con matrices canónicas
  (det=+1, rotaciones 90°/180°/270°).

### 7.2 Reglas léxicas (vocabulario)

- **6 piezas base** en top-10 de las 3 cohortes: `3023`, `3004`, `6141`,
  `3005`, `3024`, `3710`. Estas son el "vocabulario base" del LEGO System
  desde los 80s.
- **`4-4cyli.dat` (5 398 usos, 8.76 %)** — pieza más frecuente por mucho;
  cilindro base para pin-holes y Technic embebido.
- **Bigramas 90 % self-bigrams** — los sets se arman mayormente con filas
  paralelas de la misma pieza.

### 7.3 Reglas de cadencia

- **STEPs vacíos = 31 %** cierran secciones lógicas. Menos frecuentes en
  kids (28.5 %) que en 80s/90s (39 %).
- **Kids = manuales más granulares** (7.21 piezas/step vs 9.41 en 80s/90s).
- **Sub-builds**: ~8 por set en promedio. 80s/90s ligeramente más (8.39 vs 7.68).

### 7.4 Reglas de formalidad

- **BFC CERTIFY**: 31 % global. Crece con el tiempo (kids 36.5 % vs
  80s/90s 21 %).
- **Custom parts**: 1.5 % global. Concentrados en Fabuland (9.3 %),
  Friends (4.1 %), y sets licenciados.
- **Headers**: 100 % conformes al spec OMR.

---

## 8. Generador actualizado

`generator/ldraw_gen.py` (925 líneas, +112 desde corpus 100).

### Nuevos métodos
- `build_kid_set(theme, base_size)` — template kids post-2010 con floor + 2
  capas de walls + deco redonda + roof slopes + chimenea. 3 paletas
  (city/castle/space + default).
- `brick_1x1(x, y, z, color, matrix)` — atajo faltante.
- `_print_corpus_comparison(m)` — compara con corpus 300.
- `_run_demo(name, builder)` — helper para ejecutar demos.

### 3 demos distintos

| Demo | Piezas | STEPs | Files | Validación |
|------|-------:|------:|------:|------------|
| `demo_town.ldr` | 29 | 12 | 9 | 0e/0w |
| `demo_kid.ldr` | 18 | 7 | 6 | 0e/0w |
| `demo_classic.ldr` | 1 | 1 | 1 | 0e/0w (sanity check) |

Cada demo con `!THEME` y `!KEYWORDS` distintos para identificar la
cohorte.

---

## 9. Limitaciones y honestidad

- **Muestreo OMR no exhaustivo** (300/1 470 = 20.4 % de los sets OMR). El
  OMR a su vez no contiene todos los sets LEGO; faltan muchos (Ninjago,
  Star Wars post-2010 en su mayoría).
- **Decoración no analizada**: `!TEXMAP START PLANAR` no se estudió; muchos
  sets modernos usan texturas PNG.
- **Sin minifigs detalladas**: las minifigs aparecen como `973pXX.dat` pero
  no se desglosaron a nivel de cada pieza (cabeza, torso, etc.).
- **Sin análisis de sub-modelos anidados**: la jerarquía dentro del MPD no
  se estudió.
- **Pirates outlier**: 6286 Schooner distorsiona cualquier análisis de ese
  theme; los demás sets Pirates son ~50 piezas promedio.

---

## 10. Próximos pasos sugeridos

1. **Incluir sets Technic de los 80s/90s** para cuantificar influencia
   real de Technic en el corpus System.
2. **Comparar OMR con MOCs** (cualquier autor) para validar universalidad.
3. **Analizar texturas (TEXMAP)** en sets modernos.
4. **Clustering estructural** para detectar sub-ensamblajes recurrentes
   (cabinas, fachadas, mástiles, etc.).
5. **Entrenar un modelo de lenguaje** sobre las 61 617 instancias para
   predecir la siguiente pieza.

---

## 11. Recursos generados

| Recurso | Ruta | Descripción |
|---------|------|-------------|
| MD de referencia LDraw | `LDRAW_GUIDE.md` | Spec del formato |
| MD de reglas (100 sets) | `LEARNED_CONVENTIONS_100.md` | Análisis previo |
| **MD cross-corpus (300 sets)** | `LEARNED_CONVENTIONS_300.md` | **Este documento** |
| Lista 80s/90s | `corpus/setlist_80s90s.{txt,json}` | 100 sets |
| Lista kids | `corpus/setlist_kids.{txt,json}` | 200 sets |
| 100 MPDs | `corpus/mpds/*.mpd` | 6.7 MB |
| 200 MPDs kids | `corpus/mpds_kids/*.mpd` | 25 MB |
| Parts Library | `corpus/ldraw/` | 28k archivos |
| JSON cross-corpus 2.0 | `analysis/cross_corpus2_stats.json` | Stats globales |
| JSON per-set 300 | `analysis/per_set_stats_300.json` | Por set |
| Encontrar chaining 300 | `analysis/findings_chaining_300.md` | Chaining |
| Encontrar cohorts | `analysis/findings_cohorts.md` | 80s/90s vs kids |
| Encontrar themes 300 | `analysis/findings_themes_300.md` | Por theme |
| Generador Python | `generator/ldraw_gen.py` | 925 líneas |
| 3 demos | `generator/demo_{town,kid,classic}.ldr` | Outputs validados |
