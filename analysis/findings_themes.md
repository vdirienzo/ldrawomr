# Convenciones de construcción por THEME LEGO

Análisis del corpus **OMR 1980–1999 no-Technic** (100 sets, 18 670 piezas, 1 985 steps, 839 sub-builds, 112 custom parts) agrupado por `meta.theme`. Datos extraídos con `jq` desde `cross_corpus_stats.json` y `per_set_stats.json` (sin código Python).

> **Nota metodológica:** los top-pieces por tema se obtienen sumando las frecuencias de las piezas que aparecen en el `top_30_pieces` de cada set. Esto captura el "vocabulario" típico, no la cola larga de piezas únicas. Los bigramas y deltas agregan lo mismo. Donde una sola pieza domina fuertemente, se anota.

---

## Resumen 1-línea por tema

| Theme | Sets | Piezas | Piezas/set | Subbuilds/set | Pasos/set | Piezas/paso (mediana) | Custom | Pieza-signatura |
|---|---|---|---|---|---|---|---|---|
| Town | 32 | 3 553 | 111 | 4.6 | 19.4 | 6.8 | 12 | baseplate `754`, ventanas `4084`/`4485`, parabrisas `3788` |
| Pirates | 5 | 3 314 | 663 | 11.4 | 10.8 | 32.2 (skew) | 23 | cylinder primitivo `4-4cyli`, baseplate `754`, bandera `2335p30` |
| Model Team | 5 | 3 215 | 643 | 23.8 | 62.2 | 10.0 | 14 | arco `3063b`, clip-plates `6019`, paneles `3665`/`3941` |
| Train | 9 | 2 592 | 288 | 11.4 | 24.2 | 6.2 | 8 | panel `4166b` 1×6, base-plate train `2653`, wheel-tile `2867` |
| Space | 15 | 2 088 | 139 | 12.6 | 2.6 | 3.9 | 1 | round plate `6141`, tyre/wheel `3641`+`4624`, slope `3838` |
| Castle | 9 | 1 549 | 172 | 8.1 | 23.8 | 7.2 | 5 | plate decorada `3626ap01`, slope `3847`/`4444`/`4489a` |
| Star Wars | 6 | 1 120 | 187 | 12.0 | 62.0 | 2.9 | 1 | baseplate `756` 32×32, slope 33° `4286`, printed plate `2877` |
| Western | 5 | 664 | 133 | 7.6 | 21.6 | 6.8 | 11 | saddle `30141`, brick 1×2 `3004` en pared |
| Sports | 1 | 165 | 165 | 10 | 22 | 7.5 | 0 | `30027a`+`30028` (grada/stadium) |
| Fabuland | 3 | 56 | 19 | 2 | 1 | 11.3 | 1 | piezas `u91xx` (custom Fabuland) |
| Boat | 2 | 135 | 68 | 3.5 | 0 | — | 2 | keel/hull `2349a`/`2348b` |
| Adventurers | 2 | 53 | 27 | 3 | 0 | — | 0 | wheel `4624`, tyre `3641` |
| Universal B.S. | 4 | 29 | 7 | 1.5 | 0 | — | 0 | `3003pe2` printed 2×2 |
| Promotional | 1 | 111 | 111 | 4 | 20 | 5.5 | 0 | mixto Town |
| Znap | 1 | 26 | 26 | 1 | 3 | 8.7 | 0 | `32207`–`32219` (familia Znap propia) |

---

## Town (32 sets, 3553 piezas)

- **Sets en corpus:** 32 (el corpus entero: 32 %)
- **Piezas totales:** 3 553
- **Piezas/set media:** **111** (rango 23–550). Distribución bimodal: vehículos pequeños (~30–100 p) y playsets grandes (~150–550 p).
- **Sub-builds/set media:** **4.6** (Town descompone moderadamente; los sets grandes como 6541 Intercoastal Seaport llegan a 19 sub-builds).
- **Pasos/set media:** 19.4 (Town instruye mucho paso a paso).
- **Piezas/paso mediana:** **6.8** — chunk moderado, un step ≈ 7 piezas.
- **Custom parts:** 12 en todo el tema (concentrados en 6541 Seaport = 5 y 6348 Surveillance Squad = 5: piezas específicas para grúas/puentes).
- **Subparts embebidos:** 0.

**Top 15 piezas (frecuencia ponderada):**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `754.dat` | **92** | baseplate 24×24 — duplicada en wall-stackings |
| 2 | `3008.dat` | 11 | brick 1×8 |
| 3 | `3070a.dat` | 10 | tile 1×1 |
| 4 | `2989.dat` | 10 | slope 45° 1×1 |
| 5 | `70961.dat` | 10 | wheel cover / hub |
| 6 | `4862.dat` | 9 | baseplate 6×12 (vehículos) |
| 7 | `3023.dat` | 8 | plate 1×2 |
| 8 | `3024.dat` | 8 | plate 1×1 |
| 9 | `6141.dat` | 8 | plate 1×1 round |
| 10 | `4084.dat` | 8 | windscreen 2×4×1⅔ — parabrisas |
| 11 | `4865a.dat` | 8 | panel 1×2×1 |
| 12 | `6091.dat` | 8 | slope 45° 1×1 inverted |
| 13 | `3037.dat` | 7 | slope 45° 2×4 |
| 14 | `4175.dat` | 7 | hinge plate 1×2 |
| 15 | `4162.dat` | 7 | tile 1×8 |

**Bigrama canónico:** `754 → 754` = **88** (repite baseplate como sub-modelo apilado).

**Piezas exclusivas de Town (en top-30 de ≥3 sets Town, ausentes en otros temas):**
`3788` (boat hull, 7 sets), `2437` (4), `3139` (4), `4855` (4), `6157` (4), `3680c01` printed plate (3), `3823` (3), `4084` parabrisas (3), `4485` bus windshield (3), `4592c01` propeller (3), `2415` (2), `2441` (2) → **vocabulario de vehículos y minifig-habs** muy marcado.

**Deltas dominantes (top 5):**
- `(0,0,0)` apilado: 26
- `dz=-60` (1 stud depth): 21
- `dx=-80` (módulos adyacentes): 19
- `dz=-180` (3 studs en Z): 12
- `dx=140` (panel largo), `dz=-200` (4 studs): 10–12 cada uno

→ Construcción **modular de pared**: piezas de 2×4 y 1×4 apiladas en muros lineales con deltas múltiplos de 20 LDU (= 1 stud).

**Ejemplo representativo:** **6541-1 Intercoastal Seaport** (550 p, 19 sub-builds, 76 steps, 5 custom parts) — el mayor set Town del corpus, wall + crane + boat + truck construidos como sub-modelos.

**Patrón:**
- Construcción de **muros planos** con bricks 1×2 / 1×4 (`3004`, `3005`, `3009`).
- **Parabrisas y ventanas impresos** (`4084`, `4871`, `4485`) — vocabulary de vehículos.
- **Baseplates repetidos** (`754` bigrama=88) — Town hace muchas casas modulares sobre la misma base.
- Sets pequeños (~30 p) tienen **0 steps** en muchos casos (modelos tan simples que se entregan como un único sub-model).

---

## Pirates (5 sets, 3314 piezas)

- **Sets en corpus:** 5 (gigantescada uno)
- **Piezas totales:** 3 314
- **Piezas/set media:** **663** (rango 29–2 834). El corpus está dominado por **6286-1 Skull's Eye Schooner (2 834 piezas)** — un único set representa el 85 % de las piezas del tema.
- **Sub-builds/set media:** 11.4 (Schiff descompone en casco + mástiles + velas + cañones).
- **Pasos/set media:** 10.8 (sólo 6235 Buried Treasure y 6286 tienen steps; el resto son "instrucciones mínimas").
- **Piezas/paso mediana:** **32.2** — muy alta, skew por 6286 (56.7 p/step). Sin contar el schooner, ~7.8 p/step.
- **Custom parts:** **23** (la mayor cantidad absoluta del corpus) — concentrated en 6286 (21) y 6279 Skull Island (2): velas custom, mástiles tallados, cañones.
- **Subparts embebidos:** **26** (la mayor cantidad absoluta) — mismos sets, para piezas complejas (velas, mascarones).

**Top 15 piezas:**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `4-4cyli.dat` | **1 792** | cilindro primitivo (1.792 de un set) — mástiles, cañones, remos |
| 2 | `754.dat` | **173** | baseplate 24×24 |
| 3 | `2431.dat` | 25 | plate 2×2 with side studs — anclaje de velas |
| 4 | `3062b.dat` | 25 | round brick 1×1 |
| 5 | `3005.dat` | 22 | brick 1×1 |
| 6 | `3623.dat` | 20 | plate 1×3 |
| 7 | `4477.dat` | 20 | plate 1×10 — cubiertas largas |
| 8 | `4085c.dat` | 18 | plate 1×1 con clip — bandera/cuerda |
| 9 | `3659.dat` | 17 | brick 1×3 arch |
| 10 | `4286.dat` | 17 | slope 33° 3×1 |
| 11 | `3040b.dat` | 16 | slope 45° 2×1 (barril) |
| 12 | `3665a.dat` | 16 | slope 45° 1×2 inverted |
| 13 | `6091.dat` | 14 | slope 45° 1×1 inverted |
| 14 | `3001.dat` | 12 | brick 2×4 |
| 15 | `4589.dat` | 11 | cone 1×1 |

**Bigramas canónicos:**
- `4-4cyli → 4-4cyli` = **1 789** (cilindro encadenado = mástil completo con varios segmentos)
- `754 → 754` = 165
- `2431 → 2431` = 15 (placa con studs laterales para velas)

**Deltas dominantes (signature única en el corpus):**
- `(3.0, -0.1, -0.5)` = **148** — micro-rotación de vela/bandera
- `(1.8, 0.0, -2.4)` = **146**
- `(1.5, 0.0, -2.6)` = **101**
- `(2.2, 0.1, 2.0)` = **93**
- deltas fraccionarios < 3 LDU en X/Y/Z dominantes — **rotación fina de elementos curvos** (velas, telas, cuerdas)

→ **NO comparte el sistema de deltas múltiplos-de-20** con Town/Castle/Train. Las velas de los barcos se modelan con orientaciones sub-stud.

**Ejemplo representativo:** **6286-1 Skull's Eye Schooner** (2 834 p, 33 sub-builds, 50 steps, 21 custom, 25 subparts). Es el set más complejo del corpus entero y el único que dispara todas las métricas de Pirates.

**Patrón:**
- **Cilindros primitivos masivos** (4-4cyli = 1 792) — mástiles, cañones, remos, barandilla.
- **Velas como sub-parts custom** (subparts=26) — no se renderizan con primitives estándar.
- **Plates con studs laterales** (`2431` = 25) — patrón de anclaje de velas a los mástiles.
- **Plate 1×10** (`4477` = 20) — cubiertas de barcos largos.
- **Bigrama 4-4cyli→4-4cyli** — patrón "mástil multi-segmento".

---

## Model Team (5 sets, 3215 piezas)

- **Sets en corpus:** 5
- **Piezas totales:** 3 215
- **Piezas/set media:** **643** (rango 283–1 703). Gigantes: 5571 Giant Truck = 1 703 p.
- **Sub-builds/set media:** **23.8** — el más alto del corpus. Los Model Team desmenuzan cada vehículo en subsistemas (chasis, motor, transmisión, ruedas, body, interior).
- **Pasos/set media:** **62.2** — segundo más alto.
- **Piezas/paso mediana:** **10.0** — chunk medio-grande (montaje por módulos).
- **Master steps totales:** 34 — ratio de pasos-macro = 34/311 = 11 % (mucho ensamble principal, no sólo sub-modelos).
- **Custom parts:** 14 (5510 Off-Road = 4, 5542 Black Thunder = 10: piezas detalladas como grúas, defensas, interiores).
- **Subparts embebidos:** 6.

**Top 15 piezas:**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `6019.dat` | **45** | plate 1×1 con clip — detalle fino |
| 2 | `3063b.dat` | **40** | brick arch 1×2 — pasos de rueda |
| 3 | `3069b.dat` | **35** | plate 1×2 |
| 4 | `3665.dat` | **28** | slope 45° 1×2 inverted — paneles curvos |
| 5 | `3941.dat` | **27** | brick 2×2 round — cuerpo curvo |
| 6 | `3021.DAT` | 25 | plate 2×3 |
| 7 | `3010.dat` | 25 | brick 1×1 |
| 8 | `3023.DAT` | 24 | plate 1×2 |
| 9 | `3023.dat` | 22 | plate 1×2 |
| 10 | `3005.dat` | 22 | brick 1×1 |
| 11 | `4070.dat` | 22 | brick 1×1 con studs laterales |
| 12 | `3622.dat` | 20 | plate 3×3 |
| 13 | `3024.DAT` | 20 | plate 1×1 |
| 14 | `28653.dat` | 20 | technic beam 1×2 (chasis reforzado) |
| 15 | `3062b.dat` | 18 | round brick 1×1 — faros |

**Bigramas canónicos (todos self-pairs):**
- `6019 → 6019` = **29**
- `3063b → 3063b` = **28**
- `3069b → 3069b` = **19**
- `3665 → 3665` = **19**
- `3021 → 3021` = **19**
- `3941 → 3941` = **16**

→ Model Team **compone paneles repitiendo la misma pieza** en filas.

**Deltas dominantes — signature "vehículos grandes":**
- `dx=180` = **47** (3 studs — paneles de capó)
- `dx=220` = 41
- `dx=-220` = 40
- `dx=140` = 34
- `dx=80` = 27
- `dx=260` = 23 (5 studs — panel más largo)
- `dx=240` = 17 (chasis doble)
- `dx=20` = 29 (incrementos finos)

→ **Deltas en X grandes (140–260 LDU = 3–5 studs) y simétricos** = piezas grandes tipo capó, lateral, parachoques.

**Ejemplo representativo:** **5571-1 Giant Truck** (1 703 p, 40 sub-builds, 152 steps, master=1) — camión articulado con chasis + container + detalles.

**Patrón:**
- **Subdivisión extrema** (40 sub-builds en 5571; 32 en 5533 Red Fury) — cada sistema del vehículo es un sub-modelo.
- **Bricks arch** (`3063b` = 40) y **bricks redondos** (`3941` = 27, `3062b` = 18) para pasos de rueda y carrocerías curvas.
- **Plate 1×1 con clip** (`6019` = 45) como elemento de detalle/décor (emblems, tornillos).
- **Paneles invertidos** (`3665`, `3665a`) repetidos = paneles laterales curvados.
- **Technic beam `28653`** aparece sólo en Model Team → chasis reforzado, único caso en este corpus no-Technic.

---

## Train (9 sets, 2592 piezas)

- **Sets en corpus:** 9
- **Piezas totales:** 2 592
- **Piezas/set media:** **288** (rango 0–681). 4558 Metroliner = 0 p (modelo no parseado, conserva sólo master steps).
- **Sub-builds/set media:** 11.4
- **Pasos/set media:** 24.2 (3 sets sin steps: 7730, 7834, 4536, 4546, 4549)
- **Piezas/paso mediana:** 6.2
- **Custom parts:** 8 (concentrados en 4558 Metroliner = 8 — tren futurista no-Technic custom).

**Top 15 piezas:**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `3023.dat` | **41** | plate 1×2 |
| 2 | `3023.DAT` | 33 | plate 1×2 (case variant) |
| 3 | `4166b.dat` | **32** | panel 1×6 — lateral de vagón |
| 4 | `3069B.DAT` | 28 | plate 1×2 |
| 5 | `4286.dat` | 26 | slope 33° 3×1 — techo inclinado |
| 6 | `3004.dat` | 22 | brick 1×2 |
| 7 | `3010.dat` | 22 | brick 1×1 |
| 8 | `2420.dat` | 18 | plate 2×2 |
| 9 | `2653.dat` | **18** | plate 1×4 with groove — base para vías |
| 10 | `3622.dat` | 16 | plate 3×3 |
| 11 | `3037.dat` | 16 | slope 45° 2×3 |
| 12 | `3230b.dat` | 16 | handle/plate train |
| 13 | `3229b.dat` | 16 | plate train 2×3 |
| 14 | `2867.dat` | **16** | train wheel tile (cubre-rueda) |
| 15 | `3069b.dat` | 15 | plate 1×2 |

**Bigramas canónicos:**
- `3069B → 3069B` = **22** (chasis de plate 1×2 repetido)
- `3023 → 3023` = 20
- `4166b → 4166b` = 16 (lateral de vagón en paneles 1×6 apilados)
- `4166b → 3230b` = 16 (lateral + manija)

**Piezas exclusivas Train (top-30 de ≥3 sets Train):**
- `2653.dat` (train track base plate) = 18 — aparece sólo en Train
- `2867.dat` (cubre-rueda) = 16 — sólo Train
- `4166b.dat` (1×6 panel) = 32 — concentradísimo

**Deltas dominantes — signature "chasis largo":**
- `dz=60` = **20** (1 stud profundidad)
- `dz=-100` = 19 (2 studs)
- `dz=-60` = 19 (1 stud)
- `dz=100` = 16
- `dz=-20` = 14
- `dx=-40` = 13

→ **Deltas principalmente en Z (profundidad), no en X** — los vagones se construyen a lo largo del eje Z. Esto es único: Town/Castle/Model Team usan X. La orientación "largo = Z" es convención Train.

**Ejemplo representativo:** **4565-1 Freight and Crane Railway** (681 p, 25 sub-builds, 132 steps, custom=0) — vagón de carga + grúa, máxima descomposición.

**Patrón:**
- **Panel 1×6** (`4166b`) como elemento lateral de vagón — pieza signature.
- **Train wheel tile** (`2867`) y **track base plate** (`2653`) — vocabulary único del tema.
- **Chasis largo construido sobre Z**, no X — el tren "mira" hacia Z+.
- **Slope 33° `4286` = 26** para techos inclinados de locomotoras.
- **Plates 1×2 repetidos** (`3069b` bigrama=22) — pattern de chasis en listones.

---

## Space (15 sets, 2088 piezas)

- **Sets en corpus:** 15 (segundo más numeroso tras Town)
- **Piezas totales:** 2 088
- **Piezas/set media:** **139** (rango 36–512). Mega Core Magnetizer (6989) = 512 p es el más grande.
- **Sub-builds/set media:** **12.6** — Space subdivide mucho, especialmente Mega sets: 6989 = **38 sub-builds**.
- **Pasos/set media:** **2.6** — la más baja del corpus. La mayoría de sets Space (10 de 15) tienen **0 steps** — sólo `6821 Shovel Buggy` y `6890 Cosmic Cruiser` tienen pasos.
- **Piezas/paso mediana:** **3.9** — pasos muy granulares cuando los hay.
- **Custom parts:** 1 (sólo 6989 Mega Core Magnetizer) — Space usa casi todo LEGO estándar.
- **Subparts embebidos:** 0.

**Top 15 piezas (por frecuencia total):**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `6141.dat` | **12** | plate 1×1 round — ojos de robot / luces |
| 2 | `3641.dat` | 8 | tyre |
| 3 | `4624.dat` | 8 | wheel 6×4 — rover |
| 4 | `2420.dat` | 8 | plate 2×2 |
| 5 | `4864a.dat` | 8 | panel 1×2×1 |
| 6 | `2401.dat` | 8 | brick 1×1 round — astronauta helmet |
| 7 | `2959c01.dat` | **7** | dish 4×4 inverted (radar) — sólo en 6989 |
| 8 | `2412a.dat` | 7 | technic plate 1×1 (rotor) |
| 9 | `4589.dat` | 6 | cone 1×1 — cohete pequeño |
| 10 | `3795.dat` | 6 | plate 2×6 |
| 11 | `3623.dat` | 6 | plate 1×3 |
| 12 | `4070.dat` | 6 | brick 1×1 con studs laterales |
| 13 | `2444.dat` | 6 | plate 2×2 con pin-hole |
| 14 | `2357.dat` | 6 | brick 2×2 |
| 15 | `3820.dat` | (aparece en 15/15 sets) | slope 45° 2×1 |

**Bigramas canónicos:**
- `4624 → 3641` = **8** (wheel + tyre = par de rueda montado)
- `3641 → 4624` = 7
- `6141 → 6141` = 7 (round plates apilados)

**Piezas exclusivas Space (en top-30 de ≥3 sets Space, sin aparecer en otros temas):**
- `3838.dat` (slope 33° 3×2 — wing) = 6 sets
- `4590.dat` (dish 2×2) = 5 sets
- `3069bp68.dat` (printed plate 1×2) = 3 sets
- `3960.dat` (dish 4×4 inverted — radar) aparece en Space (3 sets) y 1× Star Wars

**Deltas dominantes:**
- `dx=-60` = 23 (1 stud ancho)
- `dx=-100` = 23 (2 studs)
- `dx=60` = 19, `dx=100` = 5 (simétricos — modulación)
- `dy=-8` = 17 (1 plate de altura)
- `dz=240` = 6 (5 studs — módulos grandes apilados)

→ **Deltas mixtos X+Z** (no tan dominantes como Train), con mucha presencia de `-8` en Y → construcción **plana**, sets casi bidimensionales apoyados en placas.

**Ejemplo representativo:** **6989-1 Mega Core Magnetizer** (512 p, 38 sub-builds, 0 steps totales pero master=1, custom=1) — Mega set con 38 sub-builds, máxima descomposición de todos los Space.

**Patrón:**
- **Pocas o cero steps** en 13 de 15 sets — Space se entrega como **lista de sub-modelos sin instrucciones paso-a-paso detalladas** en OMR.
- **Round plates (`6141`)** como ojos / luces / cúpulas — vocabulary robótico/astronauta.
- **Wheel-Tyre bigrama (`4624`↔`3641`)** — róvers lunares.
- **Slope wings (`3838`)** exclusivas para Space — alerones de nave.
- **Dish radar (`3960`, `4590`)** exclusivas para Space — antenas parabólicas.

---

## Castle (9 sets, 1549 piezas)

- **Sets en corpus:** 9
- **Piezas totales:** 1 549
- **Piezas/set media:** **172** (rango 40–341). Siege Tower 6061 = 341 p es el más grande.
- **Sub-builds/set media:** 8.1
- **Pasos/set media:** **23.8**
- **Piezas/paso mediana:** **7.2**
- **Custom parts:** 5 (6059 Knight's Stronghold = 2, 6034 Black Monarch's Ghost = 2, 6061 Siege Tower = 1 — banderines, escudos impresos, ballestas).
- **Subparts embebidos:** 0.

**Top 15 piezas:**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `4-4cyli.dat` | **104** | cilindro (lanzas, pabellones) |
| 2 | `2417.dat` | **14** | plate 1×1 con 2 studs laterales — base de ballesta |
| 3 | `3623.dat` | 13 | plate 1×3 |
| 4 | `2339.dat` | **12** | brick 1×2 arch — arco de muralla |
| 5 | `3820.dat` | 10 | slope 45° 2×1 |
| 6 | `3022.dat` | 9 | plate 2×2 |
| 7 | `3665b.dat` | 9 | slope 45° 1×2 inverted — techo |
| 8 | `3004.dat` | 8 | brick 1×2 |
| 9 | `3062b.dat` | 8 | round brick 1×1 |
| 10 | `3700.dat` | 8 | technic brick 1×2 with hole |
| 11 | `3010.dat` | 8 | brick 1×1 |
| 12 | `3023.dat` | 7 | plate 1×2 |
| 13 | `3023b.dat` | 7 | plate 1×2 (case variant) |
| 14 | `3005.dat` | 6 | brick 1×1 |
| 15 | `4460a.dat` | 6 | slope 45° 2×2 |

**Bigramas canónicos:**
- `4-4cyli → 4-4cyli` = **103** (lanzas encadenadas, pabellones)
- `2417 → 2417` = 11 (ballesta/arquero base)
- `3623 → 3623` = 11 (muralla)
- `3062b → 3062b` = 7 (torre redonda)

**Piezas exclusivas Castle (en top-30 de ≥2 sets Castle, ausentes en otros temas):**
- `3626ap01.dat` = **6 sets** — plate decorada con cara/escudo, pieza más castle-distintiva del corpus
- `3847.dat` = 4 sets — slope 45° pequeño
- `4444.dat` = 4 sets — slope 45° 2×2
- `4489a.dat` = 4 sets — plate 1×1 con clip vertical (ballesta)
- `2345.dat` = 2 sets

→ Castle tiene **5 piezas signature** que sólo aparecen en este tema.

**Deltas dominantes — signature "muralla vertical":**
- `dx=60` = **15** (1 stud lateral)
- `dz=-100` = 14 (2 studs profundidad — grosor de muralla)
- `dy=-24` = 17 (1 brick de altura apilado) ← dominante
- `dy=-8` = 10–12 (1 plate de altura)
- `dz=-50, -180, -220` = 8 cada uno

→ **Deltas verticales en Y (`dy=-24`, `dy=-8`) MUY dominantes** = construcción de **torres/muros apilados brick a brick**.

**Ejemplo representativo:** **6061-1 Siege Tower** (341 p, 10 sub-builds, 36 steps, custom=1) — torre de asedio con ballesta, estandartes y muro.

**Patrón:**
- **Construcción vertical pura**: `dy=-24` es el delta más común del tema — apilado brick por brick.
- **Pieza signature `3626ap01`** (plate decorada con cara/escudo) en 6 de 9 sets Castle — único en el corpus.
- **Arco `2339`** para puertas de muralla (12 ocurrencias).
- **Plate con clip `4489a`** exclusivo de Castle = ballestas.
- **Cilindros primitivos** (4-4cyli=104) para **lanzas y pabellones** (no velas como en Pirates).
- **5 piezas signature únicas del tema** — Castle es el tema con vocabulario más distintivo.

---

## Star Wars (6 sets, 1120 piezas)

- **Sets en corpus:** 6 (todos 1999, los primeros LEGO SW)
- **Piezas totales:** 1 120
- **Piezas/set media:** **187** (rango 61–360). TIE Fighter & Y-wing (7150) = 360 p el mayor.
- **Sub-builds/set media:** 12.0
- **Pasos/set media:** **62.0** — la más alta del corpus, junto a Model Team.
- **Piezas/paso mediana:** **2.9** — la más granular del corpus. **Casi 1 pieza por step.**
- **Custom parts:** 1 (sólo 7121 Naboo Swamp) — y aún así los sets Star Wars tienen **la mayor variedad de piezas únicas** (300+ únicos por set).
- **Subparts embebidos:** 0.

**Top 15 piezas:**

| # | Pieza | Frec. | Notas |
|---|---|---|---|
| 1 | `756.dat` | **48** | baseplate 32×32 — explanada de hangar |
| 2 | `4286.dat` | **16** | slope 33° 3×1 — panel curvo de nave |
| 3 | `3794a.dat` | 12 | plate 1×2 con stud offset — detallado |
| 4 | `3020.dat` | 12 | plate 2×4 |
| 5 | `2654.dat` | **12** | plate 1×2 with grille — rejilla de nave |
| 6 | `3040b.dat` | 10 | slope 45° 2×1 |
| 7 | `6141.dat` | 10 | round plate 1×1 |
| 8 | `3660.dat` | 10 | slope 45° 2×2 inverted |
| 9 | `3004.dat` | 9 | brick 1×2 |
| 10 | `6019.dat` | 8 | plate 1×1 con clip |
| 11 | `2877.dat` | **8** | printed plate 1×6 — panel con patrón Star Wars |
| 12 | `3666.dat` | 8 | plate 1×6 |
| 13 | `3710.dat` | 8 | plate 1×4 |
| 14 | `3023.dat` | 8 | plate 1×2 |
| 15 | `3022.dat` | 8 | plate 2×2 |

**Bigramas canónicos:**
- `756 → 756` = **47** (baseplate 32×32 — los hangares Star Wars se construyen sobre baseplate repetido)
- `4286 → 4286` = 10
- `2654 → 2654` = 9 (paneles con rejilla)

**Piezas exclusivas Star Wars (en top-30 de ≥3 sets SW):**
- `2877.dat` = 4 sets — printed plate Star Wars
- `30364.dat` = 3 sets — technic slope
- `30365.dat` = 3 sets — technic slope
- `30374.dat` = 3 sets — technic slope

→ Star Wars usa las **tres pendientes Technic nuevas (30364/30365/30374)** sólo en este tema — son piezas diseñadas específicamente para las alas del X-wing y TIE Fighter.

**Deltas dominantes — signature "nave inclinada":**
- `dx=60` = **20** (1 stud)
- `dx=100` = 19 (2 studs)
- `dx=20` = 9 (½ stud — ajuste fino)
- `dy=-24` = 8 (vertical)
- `dx=-100` = 7

→ Combinación de deltas 60+100+20 — **construcción con slope panels en X, ajustados a ½-stud** (lo que indica el cuerpo facetado de las naves).

**Ejemplo representativo:** **7150-1 TIE Fighter & Y-wing** (360 p, 18 sub-builds, 110 steps, custom=0) — el más complejo Star Wars del corpus, ratio **3.27 p/step** = montaje muy granular.

**Patrón:**
- **Casi 1 pieza por step** (mediana 2.9 p/step) — la cadencia más fina del corpus. **Star Wars construye pieza por pieza**.
- **Baseplate 32×32** (`756`) repetido 48× — hangar/base.
- **Slope 33° 3×1** (`4286`) = 16 — los paneles curvos de nave (Y-wing, X-wing).
- **Rejillas impresas** (`2654`, `2877`) — vocabulary de nave industrial Star Wars.
- **3 technic slopes exclusivas** (`30364/30365/30374`) — diseñadas específicamente para X-wing y TIE Fighter.
- **Más variety de piezas únicas por set** (67.3 vs 49.8 Town) — sets más complejos, menos repetición.

---

## Tabla comparativa cross-theme

| Señal | Town | Pirates | Model Team | Train | Space | Castle | Star Wars |
|---|---|---|---|---|---|---|---|
| Tamaño medio (p/set) | 111 | 663 | 643 | 288 | 139 | 172 | 187 |
| Sub-builds/set | 4.6 | 11.4 | **23.8** | 11.4 | 12.6 | 8.1 | 12.0 |
| Pasos/set | 19.4 | 10.8 | 62.2 | 24.2 | **2.6** | 23.8 | 62.0 |
| Piezas/paso (med.) | 6.8 | 32.2* | 10.0 | 6.2 | 3.9 | 7.2 | **2.9** |
| Custom (total) | 12 | **23** | 14 | 8 | 1 | 5 | 1 |
| Subparts (total) | 0 | **26** | 6 | 0 | 0 | 0 | 0 |
| Pieza #1 (frec.) | `754` ×92 | `4-4cyli` ×1792 | `6019` ×45 | `3023` ×41 | `6141` ×12 | `4-4cyli` ×104 | `756` ×48 |
| Bigrama #1 | `754→754` 88 | `4-4cyli→4-4cyli` 1789 | `6019→6019` 29 | `3069B→3069B` 22 | `4624→3641` 8 | `4-4cyli→4-4cyli` 103 | `756→756` 47 |
| Delta #1 | `(0,0,0)` 26 | `(3.0,-0.1,-0.5)` 148 | `dx=180` 47 | `dz=60` 20 | `dx=-60/-100` 23 | `dy=-24` 17 | `dx=60` 20 |
| Eje dominante | X | micro-XYZ | X (largo) | **Z (largo)** | X (mixto) | **Y (vertical)** | X |
| Piezas únicas de tema | muchas | pocas (1-2) | pocas | 2-3 | 3 | **5** | 4 |

\*Pirates 32.2 está dominado por 6286 Schooner; sin él es ~7.8.

---

## Reglas (convenciones por theme)

1. **Town = modularidad horizontal.** Construye **muros y casas sobre baseplates** (`754` bigrama=88, `4862` baseplate 6×12, `3680c01`). Pieza signature: parabrisas y ventanas (`4084`, `4485`, `3823`, `2437`, `6157`). Deltas en múltiplos de 20 LDU (X+Z), `(0,0,0)` dominante → **apilado directo sin rotación**. Custom parts concentrados en playsets grandes (6541 Seaport, 6348 Surveillance).

2. **Pirates = velas y mástiles cilíndricos.** El tema está dominado por **el primitivo `4-4cyli`** (1.792 unidades, 1.789 encadenadas como bigrama) para mástiles y cañones, y por **`754` baseplate** (173 unidades, bigrama=165) como cubierta. Pieza única: **`2335p30` flag with pattern** (sólo 2 sets Pirates). Signature única: **deltas fraccionarios < 3 LDU** (rotación fina de velas). Custom+subparts = 23+26 — los más altos del corpus, todas en 6286 Schooner y 6279 Skull Island (velas modeladas como sub-parts).

3. **Model Team = vehículo detallado por módulos.** Subdivisión extrema (40 sub-builds en 5571 Giant Truck), piezas grandes de carrocería (`3063b` arch ×40, `3941` round ×27, `3665` inverted ×28), paneles de capó largos (`dx=180`, `220`, `260` dominantes — múltiplos de 4 studs). Pieza signature: **`6019` plate 1×1 con clip** (45 unidades, bigrama=29) para detalles. Único set del corpus que usa **`28653` technic beam** = chasis reforzado en un tema no-Technic.

4. **Train = chasis largo sobre eje Z.** Signature única: deltas principalmente en **Z** (`dz=60`, `-100`, `-60`, `100`, `-20`) no en X. Piezas exclusivas: **`2653` train track base plate** (18, sólo Train), **`2867` wheel cover tile** (16, sólo Train), **`4166b` panel 1×6** (32, lateral de vagón con bigrama=16). Pattern: `3069B→3069B` bigrama=22 = listones de chasis.

5. **Space = wheels + round plates + slopes de ala.** **Round plate `6141`** y **par wheel-tire `4624`↔`3641`** son vocabulary de rover/astronauta. Piezas únicas: **`3838` slope 33° 3×2** (6 sets, alas), **`4590` dish 2×2** (5 sets, radar), **`3069bp68` printed plate** (3 sets). **Casi nunca tiene steps** (10/15 sets con 0 steps; mediana 3.9 p/step cuando los hay) — Space se entrega como **sub-modelos sin instrucciones paso-a-paso** en OMR. Custom = 1 sólo.

6. **Castle = apilamiento vertical con vocabulario exclusivo.** **5 piezas únicas** del corpus (`3626ap01`, `3847`, `4444`, `4489a`, `2345`) — el tema con mayor identidad de catálogo. Delta dominante **`dy=-24`** (1 brick) — Castle es el único tema donde la vertical gana. `4-4cyli` (104) = lanzas y pabellones (no velas como Pirates). `2339` arch = puertas de muralla. `3626ap01` = plate decorada con cara/escudo en 6/9 sets.

7. **Star Wars = nave facetada pieza-por-pieza.** Cadencia más fina del corpus (**2.9 p/step**, casi 1 pieza por step), la mayor cantidad de pasos (62/set). Pieza signature: **`756` baseplate 32×32** (48, bigrama=47) para hangar. **3 technic slopes exclusivos** del tema (`30364`, `30365`, `30374`) diseñados para X-wing y TIE Fighter. **`4286` slope 33° 3×1** = 16 para paneles curvos de nave. **`2877` printed plate** = 8. **Deltas 60+100+20** = ½-stud fine-tuning del cuerpo de la nave.

---

## Observaciones transversales

- **El primitivo `4-4cyli` sólo domina en Pirates (1 792) y Castle (104)** — todos los demás temas construyen con bricks/plates estándar. La diferencia de escala (17×) refleja que Pirates tiene el **Skull's Eye Schooner**, el set más grande del corpus.
- **Los subparts embebidos son exclusivos de Pirates (26) y Model Team (6) + Fabuland (2)** — sólo estos 3 temas tienen piezas complejas renderizadas como sub-modelos LDraw.
- **Town (32 sets) representa el 32 % del corpus** pero sólo el 19 % de las piezas — Town hace **muchos sets pequeños**, no sets grandes.
- **Pirates y Model Team son gemelos en volumen (3 314 vs 3 215 p) pero opuestos en cadencia**: Pirates 32.2 p/step (chunky ship), Model Team 10.0 (sistémico).
- **Space y Star Wars son opuestos en cadencia pese a ser "sci-fi"**: Space 3.9 p/step con 0 steps en la mayoría, Star Wars 2.9 p/step con **62 pasos por set** (la mayor cadencia).
- **Train es el único tema con eje dominante Z** — todos los demás usan X. Esto se ve claramente en los deltas.
- **Castle es el único tema con delta Y dominante** — construcción vertical pura de murallas.
