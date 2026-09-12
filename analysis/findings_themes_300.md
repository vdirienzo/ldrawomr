# Convenciones de construcción por THEME LEGO — corpus 300 sets

Análisis del corpus **OMR 1980–2019 no-Technic** (300 sets OMR: 100 sets 80s/90s + 200 sets kids, total **61 617 parts** — 18 670 80s/90s + 42 947 kids, **7 940 steps**, **2 374 sub-builds**, **597 custom parts** + 326 subparts embebidos). Datos extraídos de `cross_corpus2_stats.json` y `per_set_stats_300.json` y agregados por `meta.theme` (metodología idéntica a `cross_corpus_stats.json` previa, ahora con 200 sets kids adicionales). Las cifras se computan con `python -c` inline (sin scripts persistentes).

> **Metodología:** los top-pieces se obtienen sumando las frecuencias de las parts en `top_30_pieces` de cada set. Las **parts exclusivas** son las que aparecen en ≥3 sets del theme y en 0 otros themes (medida estricta). Los bigramas y deltas agregan el `top_30_bigrams` y `top_20_deltas` por set.

---

## Resumen 1-línea por theme

| Theme | Sets | parts | parts/set | Sub-builds/set | Pasos/set (med) | Custom (total / ratio) | parts-signatura |
|---|---|---|---|---|---|---|---|
| Town | 40 | 4 394 | 109.8 (med 81) | 4.62 (med 3) | 12 | 14 / 0.32 % | baseplate `754`, plate `3024`, round `6141` |
| Town > Classic Town | 36 | 5 848 | 162.4 (med 150) | 5.92 (med 5) | 17 | 23 / 0.39 % | plate `3024`, brick `3004`, slope `3820` |
| Fabuland | 23 | 896 | 39.0 (med 23) | 3.48 (med 2) | 3 | **83 / 9.26 %** | custom Fabuland `u9101`+`u9100` (cabeza+cuerpo) |
| Friends | 17 | 5 046 | **296.8** (med 202) | 11.24 (med 8) | 0 | **208 / 4.12 %** | round `6141` 223×, brick `3004` 218×, animal `4-4cyli` |
| Space | 15 | 2 088 | 139.2 (med 119) | **12.60** (med 11) | **0** | 1 / 0.05 % | slope wing `3838`, wheel `4624`+tyre `3641` |
| Creator > Creator 3-in-1 | 14 | 3 143 | 224.5 (med 72.5) | 4.43 (med 2.5) | 33 | 4 / 0.13 % | `54200` hinge 89×, plate `3023`, round `6141` |
| Western | 13 | 1 967 | 151.3 (med 70) | 9.08 (med 6) | 15 | 21 / 1.07 % | caballo `30136` 184× + `30137` 103×, saddle `30141` |
| Castle | 10 | 1 621 | 162.1 (med 130.5) | 8.00 (med 8) | 23.5 | 5 / 0.31 % | brick `3005`, slope `3820`, primitivo `4-4cyli` |
| Creator | 10 | 361 | 36.1 (med 36.5) | 2.20 (med 2) | 11.5 | 2 / 0.55 % | hinge `54200` 23×, round `6141` |
| Pirates | 5 | 3 314 | 662.8 (med 37) | 11.40 (med 4) | 0 | 23 / 0.69 % | primitivo `4-4cyli` 1 792×, baseplate `754` 173× |
| Train | 9 | 2 592 | 288.0 (med 362) | 11.44 (med 10) | 0 | 8 / 0.31 % | brick `3004` 105×, plate `3023`, arch `3063b` |
| Star Wars | 6 | 1 120 | 186.7 (med 153.5) | 12.00 (med 10.5) | **62** | 1 / 0.09 % | baseplate `756` 48×, slope `3820`, printed `2877` |
| Model Team | 5 | 3 215 | 643.0 (med 391) | **23.80** (med 28) | 37 | 14 / 0.44 % | plate `3023` 157×, round `6141` 136×, plate 1×4 `3710` |
| Creator > Designer Sets | 6 | 967 | 161.2 (med 44) | 8.50 (med 3.5) | 6 | 0 / 0 % | baseplate `754` 88×, plate `3023` |
| Promotional > Bricktober | 5 | 861 | 172.2 (med 175) | 2.00 | **45** | 0 / 0 % | plate `3024` 121×, brick `3005`, tile `3070b` |
| Harry Potter | 4 | 2 407 | 601.8 (med 721) | 14.25 (med 15.5) | **214.5** | 17 / 0.71 % | brick `3005` 127×, brick arch `60592`/`38320` 102× |
| Universal Building Set | 4 | 29 | 7.2 (med 8.5) | 1.50 | 0 | 0 / 0 % | brick `3004`, plate `3023`, printed `3003pe2` |
| **TOTAL corpus** | **300** | **61 617** | — | 2 374 totales | 7 940 totales | **597 / 0.97 %** | — |

> **Comparativa con corpus 100 sets (previo):** Town gana 8 sets más (40 vs 32), aparece Town > Classic Town (36 sets, ausente antes), Fabuland salta de 3 a **23 sets** (muchos kids sub-cohorte 1985-1989), Friends entra nuevo con **17 sets** todos kids, Creator 3-in-1 nuevo (14 sets), Castle familiar se reduce a 10 sets (antes 9 en sub-corpus 80s). Pirates se mantiene 5 sets pero con menor peso por parts promedio (mediana baja de 663 → 37 al añadir sets pequeños).

---

## Town (40 sets, 4 394 parts, 32 80s/90s + 8 kids)

- **Sets en corpus:** 40 (32 son 80s/90s = `meta.theme="Town"`, 8 son kids = theme_full con sub-temática "Town > Classic Town" pero meta.theme sigue siendo "Town"). Años: 1980-2005.
- **parts totales:** 4 394
- **parts/set media:** **109.8** (mediana 81, rango 0-550). Distribución sesgada a la derecha por 6541 Intercoastal Seaport (550 p), 6348 Surveillance Squad (332 p), 6473 Res-Q Cruiser (297 p), 6375 Trans Air Carrier (222 p), 10037 Breezeway Cafe (221 p).
- **Sub-builds/set media:** **4.62** (mediana 3). Town descompone moderadamente. El máximo: 6541 = 19 sub-builds.
- **Pasos/set mediana:** 12.0 (varios sets tienen 0 steps, sobre todo los 8 kids).
- **Custom parts:** 14 / **0.32 %** — concentrados en playsets grandes: 6541 = 5, 6348 = 5.

**Top 15 parts (frecuencia total):**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `6141.dat` | **142** | 21/40 | plate 1×1 round — ojos / tapones de rueda |
| 2 | `3024.dat` | 138 | 25/40 | plate 1×1 |
| 3 | `3023.dat` | 136 | 28/40 | plate 1×2 |
| 4 | `3820.dat` | 96 | 29/40 | slope 45° 2×1 |
| 5 | `754.dat` | **92** | 1/40 | baseplate 24×24 — pero 88 concentrados en un set (6541 Seaport) |
| 6 | `3710.dat` | 84 | 19/40 | plate 1×4 |
| 7 | `3004.dat` | 83 | 20/40 | brick 1×2 |
| 8 | `3069b.dat` | 72 | 23/40 | plate 1×2 (case variant) |
| 9 | `3010.dat` | 71 | 21/40 | brick 1×1 |
| 10 | `3020.dat` | 70 | 22/40 | plate 2×4 |
| 11 | `6014.dat` | 65 | 11/40 | wheel 5×4 |
| 12 | `6015.dat` | 64 | 12/40 | tyre 10×4 |
| 13 | `4862.dat` | 60 | 4/40 | baseplate 6×12 |
| 14 | `3001.dat` | 56 | 12/40 | brick 2×4 |
| 15 | `3022.dat` | 50 | 18/40 | plate 2×2 |

**Bigramas canónicos:**
- `754.dat → 754.dat` = **88** (repite baseplate 24×24 — patrón **6541 Seaport apilando módulos**).
- `6141.dat → 6141.dat` = 74 (en 16/40 sets — round plates apilados como pattern).
- `3024.dat → 3024.dat` = 57 (en 21/40 sets — plate 1×1 lineal).
- `6014.dat → 6015.dat` = **50** (wheel + tyre — par montado, en 10/40 sets).
- `6015.dat → 6014.dat` = 43 (tyre + wheel bidireccional, 11/40 sets).

**Deltas dominantes:**
- `(0, 0, 0)` = **195** (apilado directo, dominante)
- `(0, 0, -60)` = 107 (1 stud profundidad)
- `(-60, 0, 0)` = 74, `(0, 0, 60)` = 67, `(60, 0, 0)` = 60

→ Construcción **modular de pared**: deltas múltiplos de 20 LDU (1 stud) en X/Z, `(0,0,0)` dominante → apilado brick sobre brick sin rotación.

**parts exclusivas:** **0** (Town no tiene parts únicas — comparte vocabulario con Town > Classic Town, Castle, Model Team, etc.).

**examples representativo:** **6541-1 Intercoastal Seaport** (550 p, 19 sub-builds, 76 steps, 5 custom parts) — el mayor set Town del corpus, wall + crane + boat + truck construidos como sub-models sobre 88 unidades de `754` baseplate.

**Patrón narrativo:**
Town construye **muros y vehículos modulares sobre baseplates 24×24** (`754`), usando plates 1×1 (`3024`), 1×2 (`3023`), 1×4 (`3710`) y slopes 45° 2×1 (`3820`) para fachadas y capós. La parts signature del theme "adulto" 80s/90s es el **par wheel/tyre `6014↔6015`** (50+43 bigramas = par montado de vehículo). Los 8 sets kids del theme son todos Classic Town recoloreados con vocabulary idéntico — Town **no innova en parts**, sólo varía la combinación de plates estándar.

---

## Town > Classic Town (36 sets, 5 848 parts, todos kids)

- **Sets en corpus:** 36 (todos clasificados "kids" en OMR — 15 publicados en los 80s + 21 en los 90s; es el bloque "Town" de la era System reform como Classic Town).
- **parts totales:** 5 848 (más parts que Town a pesar de tener menos sets — los sets kids son más grandes).
- **parts/set media:** **162.4** (mediana 150, rango 0-636). Distribución bimodal: sets medianos (100-200 p) y playsets grandes (300-636 p).
- **Sub-builds/set media:** **5.92** (mediana 5) — más descomposición que Town 80s.
- **Pasos/set mediana:** 17.0.
- **Custom parts:** 23 / **0.39 %**.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3024.dat` | **210** | 24/36 | plate 1×1 |
| 2 | `3023.dat` | 205 | 25/36 | plate 1×2 |
| 3 | `3004.dat` | 160 | 19/36 | brick 1×2 |
| 4 | `6141.dat` | 153 | 24/36 | round plate 1×1 |
| 5 | `3710.dat` | 132 | 22/36 | plate 1×4 |
| 6 | `3069b.dat` | 113 | 20/36 | plate 1×2 (case variant) |
| 7 | `3010.dat` | 106 | 19/36 | brick 1×1 |
| 8 | `3005.dat` | 100 | 18/36 | brick 1×1 |
| 9 | `3020.dat` | 96 | 19/36 | plate 2×4 |
| 10 | `3022.dat` | 94 | 19/36 | plate 2×2 |
| 11 | `3032.dat` | 73 | 12/36 | plate 2×3 |
| 12 | `3623.dat` | 72 | 14/36 | plate 1×3 |
| 13 | `3001.dat` | 64 | 14/36 | brick 2×4 |
| 14 | `3009.dat` | 61 | 16/36 | brick 1×6 |
| 15 | `3062b.dat` | 56 | 14/36 | round brick 1×1 |

**Bigramas canónicos:**
- `3024.dat → 3024.dat` = **96** (en 20/36 sets — plate 1×1 lineal, **doble de frecuente que Town 80s**).
- `6141.dat → 6141.dat` = 72 (en 17/36 sets).
- `3004.dat → 3004.dat` = 59 (en 11/36 sets — pared de brick 1×2).
- `3023.dat → 3023.dat` = 58 (en 20/36 sets — plate 1×2 plano).
- `6014.dat → 6015.dat` = 49 (en 9/36 sets — wheel/tyre).

**Deltas dominantes:**
- `(0, 0, 0)` = **308** (apilado, dominante absoluto).
- `(0, 0, -60)` = 130, `(-60, 0, 0)` = 124, `(60, 0, 0)` = 123, `(0, 0, 60)` = 108 — todos simétricos en X y Z, nada de deltas fraccionarios.

**parts exclusivas:** 2 (`3738.dat` en 3/36 sets = 7 unidades; `973P0A.DAT` en 3/36 sets = 3 unidades — **débil identidad exclusiva**, igual que Town).

**examples representativo:** **6368-1 Jet Airliner** (147 p, 5 sub-builds, 14 steps, custom=0) — vehículo aéreo, decomposition mínima.

**Patrón narrativo:**
Classic Town construye **plataformas planas 2D con plates 1×1 (`3024`) y 1×2 (`3023`) repetidos en bigramas largos** — es el theme donde el **plate 1×1 domina con 210 unidades** (el doble de Town 80s). Los muros usan `3004` (brick 1×2) bigrama=59. La descomposición es baja (5.92 sub-builds/set) porque cada set es típicamente **un vehículo o edificio monolítico**. A diferencia de Town 80s, **no usa baseplate 24×24** como signature — los playsets grandes se renderizan como geometría libre sin ancla de suelo.

---

## Fabuland (23 sets, 896 parts, 3 80s/90s + 20 kids)

- **Sets en corpus:** 23 (3 80s/90s: 3602/3784/3795; 20 kids: 3624-3798, todos 1985-1989). Es el theme con **mayor crecimiento entre corpus 100 y 300** (3 → 23 sets).
- **parts totales:** 896 — el corpus Fabuland es **diminuto**: mediana 23 p/set.
- **parts/set media:** **39.0** (mediana 23, rango 10-151).
- **Sub-builds/set media:** **3.48** (mediana 2 — la más baja de los themes grandes).
- **Pasos/set mediana:** 3.0 (sólo 3 sets tienen steps > 0).
- **Custom parts:** **83 / 9.26 %** — el **ratio más alto del corpus entero**, 7× sobre Town.
- **Subparts embebidos:** **49** (segundo más alto, sólo detrás de Friends).

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `u9101.dat` | **78** | **23/23** | cabeza Figura Fabuland (parts custom — 100 % de los sets) |
| 2 | `u9100.dat` | **78** | **23/23** | cuerpo Figura Fabuland (100 % de los sets) |
| 3 | `3004.dat` | 64 | 9/23 | brick 1×2 estándar |
| 4 | `u9103.dat` | **39** | **23/23** | cabeza animal Fabuland (perro/gato) — 100 % de los sets |
| 5 | `3003.dat` | 39 | 5/23 | brick 2×2 |
| 6 | `u9102.dat` | 15 | 12/23 | variante cabeza Fabuland |
| 7 | `6264.dat` | 16 | 9/23 | plate 1×2 rounded |
| 8 | `4727.dat` | 13 | 6/23 | plate 1×2 modified — pedestal |
| 9 | `4222a.dat` | 12 | 9/23 | plate 1×3 rounded |
| 10 | `3890c04.dat` | 11 | 4/23 | minifig accessory (printed) |
| 11 | `2145.dat` | 10 | 3/23 | slope 45° 1×2 |
| 12 | `2040.dat` | 13 | 3/23 | tile 1×2 |
| 13 | `3023.dat` | 9 | 6/23 | plate 1×2 |
| 14 | `3010.dat` | 9 | 6/23 | brick 1×1 |
| 15 | `3794a.dat` | 8 | 4/23 | plate 1×2 con stud offset |

**Bigramas canónicos:**
- `3004.dat → 3004.dat` = **33** (en 8/23 sets — pared de brick 1×2).
- `u9101.dat → u9101.dat` = 24 (en 22/23 sets — heads Fabuland en filas).
- `u9100.dat → u9100.dat` = 24 (en 22/23 sets — bodies en filas).
- `3003.dat → 3003.dat` = 19 (en 5/23 sets — brick 2×2 para base de edificios).
- `u9101.dat → u9100.dat` = 18 (en 14/23 sets — **head-body bigrama, anatomy canónica del Figura Fabuland**).

**Deltas dominantes:**
- `(0, -24, 0)` = **50** (1 brick de altura — apilado vertical puro).
- `(20, 0, 0)` = 26 (½ stud offset — **signature Fabuland: paredes con studs en offset**).
- `(-46, 0, 0)` = 25 (offset raro — paredes Fabuland son más estrechas que 1 stud).
- `(-10, 0, 0)` = 25.
- `(0, 30, 0)` = 18.

→ Fabuland tiene **deltas NO múltiplos de 20 LDU** (`-46`, `-10`, `30`) — la firma del theme es **parts con studs en offset ½-stud** (patas de animal, cuellos de Figura).

**parts exclusivas:** **23 parts únicas** (la mayor cantidad del corpus entero):
- `u9101.dat` (cabeza Figura, 23/23 sets = 100 %)
- `u9100.dat` (cuerpo Figura, 23/23 sets = 100 %)
- `u9103.dat` (cabeza animal, 23/23 sets = 100 %)
- `u9102.dat` (cabeza variante, 12/23 sets)
- `6264.dat`, `4222a.dat`, `3890c04.dat`, `4727.dat`, `2145.dat`, `2040.dat` (todas en 3+ sets Fabuland, 0 otros themes)

**examples representativo:** **3641-1 Car & Camper** (23 p, 4 sub-builds, 4 steps, **6 custom parts**) — el set Fabuland típico: 2 figuras + 1 animal + 1 vehículo, todo construido sobre las 6 parts custom exclusivas del theme.

**Patrón narrativo:**
Fabuland es un theme **encapsulado en su propio catálogo de parts custom** (`u91xx` serie). Cada set es esencialmente **2 figuras Fabuland (cabeza `u9101` + cuerpo `u9100`) + 1 animal (`u9103`) + 1 mini-escenario** construido con **brick 1×2 (`3004`)**. Las parts estándar LEGO se usan en **volumen mínimo** (mediana 23 p/set). La construcción se caracteriza por **deltas sub-stud (`-46`, `-10`, `30` LDU)** — los animales Fabuland tienen patas/cuellos a ½-stud que ningún otro theme usa. Es el theme con **mayor identidad exclusiva** del corpus: 23 parts no aparecen en ningún otro theme.

---

## Friends (17 sets, 5 046 parts, todos kids)

- **Sets en corpus:** 17 (todos kids, años 2012-2018). **Friends no tiene representación 80s/90s** — el theme fue lanzado en 2012.
- **parts totales:** 5 046 (3.er theme más grande del corpus).
- **parts/set media:** **296.8** (mediana 202, rango 34-1137).
- **Sub-builds/set media:** **11.24** (mediana 8) — **segunda descomposición más alta** (sólo detrás de Model Team).
- **Pasos/set mediana:** 0.0 — **la mayoría de sets Friends no tienen steps** (12/17 con 0).
- **Custom parts:** **208 / 4.12 %** — segundo ratio más alto del corpus (sólo detrás de Fabuland).
- **Subparts embebidos:** **136** — el más alto del corpus.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `6141.dat` | **223** | **16/17** | plate 1×1 round — signature Friends, 4.4 % del theme |
| 2 | `3004.dat` | 218 | 12/17 | brick 1×2 — pared estándar |
| 3 | `3023.dat` | 172 | 13/17 | plate 1×2 |
| 4 | `3010.dat` | 123 | 11/17 | brick 1×1 |
| 5 | `3062b.dat` | 119 | 10/17 | round brick 1×1 — cabeza animal/figura |
| 6 | `3069b.dat` | 108 | 12/17 | plate 1×2 (variant) |
| 7 | `3710.dat` | 107 | 11/17 | plate 1×4 |
| 8 | `3020.dat` | 100 | 13/17 | plate 2×4 |
| 9 | `3005.dat` | 92 | 9/17 | brick 1×1 |
| 10 | `2431.dat` | 91 | 8/17 | plate 2×2 with side studs — anclaje de cabello |
| 11 | `4-4cyli.dat` | **88** | 2/17 | cilindro primitivo — concentración en 2 playsets (animales grandes,树木) |
| 12 | `2412b.dat` | 68 | 8/17 | slope 45° 1×1 con stud |
| 13 | `3009.dat` | 65 | 7/17 | brick 1×6 |
| 14 | `3666.dat` | 64 | 7/17 | plate 1×6 |
| 15 | `3068b.dat` | 61 | 6/17 | tile 2×2 |

**Bigramas canónicos:**
- `3004.dat → 3004.dat` = **113** (en 12/17 sets — pared de brick 1×2 dominante).
- `6141.dat → 6141.dat` = 103 (en 11/17 sets — round plates apilados para ojos/pastel).
- `4-4cyli.dat → 4-4cyli.dat` = **82** (en 2/17 sets — concentración: 3934 Heartlake Stable + 41314 Stephanie's Beach House).
- `3062b.dat → 3062b.dat` = 77 (en 8/17 sets — redondos apilados).
- `3023.dat → 3023.dat` = 68 (en 7/17 sets — plate 1×2 plano).

**Deltas dominantes:**
- `(20, 0, 0)` = **109** (½ stud offset — **signature Friends: paredes con offset**).
- `(0, -8, 0)` = 96 (1 plate de altura — apilado fino).
- `(80, 0, 0)` = 91 (4 studs — módulos largos).
- `(300, 0, 0)` = **91** (15 studs — módulos extra-largos, único del theme).
- `(0, -24, 0)` = 83 (1 brick — pared estándar).
- `(140, 0, 0)` = 68 (7 studs).

→ Friends usa **deltas de 20 y 80 LDU** (½-stud y 4-stud) **más que cualquier otro theme** — los muebles Friends tienen geometría con **offset de ½-stud para detalles decorativos**.

**parts exclusivas:** 3 (`59349.dat` en 3/17 = 10 unidades; `92244.dat` en 5/17 = 6; `92245.dat` en 5/17 = 6 — parts decorativas pastel específicas).

**examples representativo:** **3186-1 Emma's Horse Trailer** (202 p, 9 sub-builds, **0 steps**, **24 custom parts**) — vehículo + caballo, máxima custom-parts density.

**Patrón narrativo:**
Friends es el theme **post-2010 más decorativo**: usa **`6141` plate 1×1 round** (223 unidades = 4.4 % del theme) **y `3062b` brick 1×1 round** (119 = 2.4 %) como **signature para ojos/pastel de animales y figuras humanas**. Las paredes se construyen con **`3004` brick 1×2 en bigrama 113** (el más alto del corpus entero para `3004→3004`). Los sets usan **deltas de 20 y 80 LDU** (½-stud y 4-stud) — geometry con offset decorativo. **Custom parts = 208 (4.12 %)** — todo el cabello, accesorios y decoración son subparts. Friends **no comparte parts con Fabuland** (vocabularios opuestos: Fabuland es custom `u91xx`, Friends es standard + custom pastel).

---

## Space (15 sets, 2 088 parts, todos 80s/90s)

- **Sets en corpus:** 15 (todos 80s/90s, 1979-1995; **Space no tiene sets kids** en este corpus).
- **parts totales:** 2 088
- **parts/set media:** **139.2** (mediana 119, rango 36-512).
- **Sub-builds/set media:** **12.60** (mediana 11) — Space subdivide mucho (especialmente el Mega set 6989 = 38 sub-builds).
- **Pasos/set mediana:** **0.0** — la mayoría de sets (10/15) tienen **0 steps**.
- **Custom parts:** 1 / 0.05 % (sólo 6989 Mega Core Magnetizer).
- **Subparts embebidos:** 0.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3023.dat` | **120** | 12/15 | plate 1×2 |
| 2 | `2412b.dat` | 67 | 9/15 | slope 45° 1×1 con stud — micro-ramp |
| 3 | `3820.dat` | 46 | **15/15** | slope 45° 2×1 — **100 % de los sets** |
| 4 | `3022.dat` | 41 | 11/15 | plate 2×2 |
| 5 | `4589.dat` | 40 | 10/15 | cone 1×1 — nozzles/cohete pequeño |
| 6 | `3069b.dat` | 33 | 9/15 | plate 1×2 (variant) |
| 7 | `3641.dat` | 31 | 9/15 | tyre |
| 8 | `4624.dat` | 31 | 8/15 | wheel 6×4 — rover |
| 9 | `6141.dat` | 39 | 8/15 | plate 1×1 round |
| 10 | `3004.dat` | 30 | 8/15 | brick 1×2 |
| 11 | `2420.dat` | 29 | 8/15 | plate 2×2 |
| 12 | `3024.dat` | 29 | 8/15 | plate 1×1 |
| 13 | `3020.dat` | 28 | 8/15 | plate 2×4 |
| 14 | `3062b.dat` | 25 | 8/15 | round brick 1×1 |
| 15 | `3001.dat` | 23 | 7/15 | brick 2×4 |

**Bigramas canónicos:**
- `3023.dat → 3023.dat` = **47** (en 8/15 sets — plate 1×2 lineal).
- `2412b.dat → 2412b.dat` = 31 (en 5/15 sets — micro-slopes apilados).
- `4624.dat → 3641.dat` = **23** (en 4/15 sets — par wheel-tire rover).
- `3641.dat → 4624.dat` = 17 (bidireccional, 4/15 sets).
- `6141.dat → 6141.dat` = 15 (en 6/15 sets — round plates apilados).

**Deltas dominantes:**
- `(0, 0, 0)` = 97 (apilado).
- `(60, 0, 0)` = 57, `(-60, 0, 0)` = 53, `(-100, 0, 0)` = 37 — deltas en X módulos grandes (rovers).
- `(0, -8, 0)` = 42 (1 plate — construcción **plana**).

**parts exclusivas:** 2:
- `3069bp68.dat` (printed plate 1×2 con patrón Space, 3/15 sets = 8 unidades).
- `3838.dat` (slope 33° 3×2 — ala de nave, 6/15 sets = 6 unidades).

**examples representativo:** **6884-1 Aero Module** (119 p, 11 sub-builds, 0 steps, custom=0) — mediana exacta del theme.

**Patrón narrativo:**
Space se construye en **plataformas planas con wheel-tire pairs** (`4624↔3641` bigrama=23+17) para róvers lunares y usa **`4589` cone 1×1** (40 unidades) como nozzles de cohete. La slope 45° 2×1 `3820` aparece en **15/15 sets** (100 % — universal). Space **no tiene steps** en la mayoría de sets (10/15 = 0) — los Mega sets (6989 con 38 sub-builds, 6952 Solar Power Carrier) se entregan como **listas de sub-models sin instrucciones paso-a-paso**. Las únicas parts exclusivas son el **`3838` slope 33° 3×2** (ala de nave, 6/15 sets) y la **`3069bp68` printed plate** con decoración Space.

---

## Creator > Creator 3-in-1 (14 sets, 3 143 parts, todos kids)

- **Sets en corpus:** 14 (todos kids, 2006-2019; precursor moderno 4896 Roaring Roadsters 2006).
- **parts totales:** 3 143
- **parts/set media:** **224.5** (mediana 72.5, rango 0-924) — **distribución bimodal extrema**: 7 sets pequeños (≤100 p) y 5 playsets grandes (≥250 p).
- **Sub-builds/set media:** **4.43** (mediana 2.5).
- **Pasos/set mediana:** 33.0 — **alto para ser kids** (sólo detrás de Star Wars, Harry Potter y Model Team).
- **Custom parts:** 4 / 0.13 %.
- **Subparts embebidos:** 3.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3023.dat` | **194** | 13/14 | plate 1×2 — base de Creator 3-in-1 |
| 2 | `6141.dat` | 185 | 11/14 | plate 1×1 round — segundo más alto del corpus para esta parts |
| 3 | `3004.dat` | 120 | 8/14 | brick 1×2 |
| 4 | `54200.dat` | **89** | 10/14 | **hinge plate 1×2 with pin** — la parts signature de Creator |
| 5 | `3623.dat` | 84 | 9/14 | plate 1×3 |
| 6 | `3005.dat` | 76 | 10/14 | brick 1×1 |
| 7 | `3069b.dat` | 75 | 11/14 | plate 1×2 (variant) |
| 8 | `3024.dat` | 68 | 11/14 | plate 1×1 |
| 9 | `3022.dat` | 67 | 9/14 | plate 2×2 |
| 10 | `3020.dat` | 58 | 9/14 | plate 2×4 |
| 11 | `3001.dat` | 56 | 10/14 | brick 2×4 |
| 12 | `2780.dat` | **49** | 6/14 | **technic pin with friction** — característico del mecanismo 3-en-1 |
| 13 | `3660.dat` | 49 | 7/14 | slope 45° 2×2 inverted |
| 14 | `2420.dat` | 43 | 9/14 | plate 2×2 |
| 15 | `4070.dat` | 42 | 7/14 | brick 1×1 con studs laterales |

**Bigramas canónicos:**
- `6141.dat → 6141.dat` = **94** (en 9/14 sets — round plates para ruedas/details).
- `3023.dat → 3023.dat` = 67 (en 4/14 sets).
- `3004.dat → 3004.dat` = 56 (en 6/14 sets — pared).
- `54200.dat → 54200.dat` = **33** (en 8/14 sets — **hinges en pares** = módulos articulados).
- `3623.dat → 3623.dat` = 23 (en 4/14 sets).

**Deltas dominantes:**
- `(20, 0, 0)` = 80 (½ stud offset — **firma Creator: detalle modular con offset**).
- `(60, 0, 0)` = 77, `(-20, 0, 0)` = 54.
- `(0, -8, 0)` = 66 (1 plate).
- `(0, 0, -20)` = 48 (½ stud en Z).

**parts exclusivas:** 0. Creator 3-in-1 usa **vocabulario 100 % estándar** — la firma está en el **`54200` hinge** (89 unidades, 10/14 sets) y **`2780` technic pin** (49 unidades, 6/14 sets) que permiten la conversión 3-en-1.

**examples representativo:** **4917-1 Mini Robots** (77 p, 2 sub-builds, 8 steps, custom=0) — set pequeño representativo del patrón modular.

**Patrón narrativo:**
Creator 3-in-1 es el theme **post-2010 más ingenieril** del corpus. Su parts signature es **`54200` hinge plate 1×2 con pin** (89 unidades, en 10/14 sets = 71 %) que aparece en **bigrama `54200→54200` = 33** (8/14 sets) — patrón "módulos articulados en pares". El segundo elemento signature es **`2780` technic pin con fricción** (49 unidades, 6/14 sets) — el theme usa elementos Technic en un contexto System para permitir la conversión 3-en-1. La construcción usa **deltas de 20 LDU (½-stud) muy frecuentes** — `(20,0,0) = 80` y `(0,0,-20) = 48` son signatures únicos. **No usa baseplate** (0 ocurrencias de `754`/`756`) — los models son geometría libre auto-soportada por la modularidad de las hinges.

---

## Western (13 sets, 1 967 parts, 5 80s/90s + 8 kids)

- **Sets en corpus:** 13 (5 80s/90s: 6765/6766/6716/6761/6762; 8 kids: 2010-2024 minifig-figuuritas). Western **creció dramáticamente** entre corpus (5 → 13) por la línea BrickHeadz/Promos.
- **parts totales:** 1 967
- **parts/set media:** **151.3** (mediana 70, rango 19-707) — **bimodal**: 8 sets pequeños (mediana ~70) y 2 playsets grandes (6769 Fort Legoredo = 707 p + 6765 Gold City Junction = 382 p).
- **Sub-builds/set media:** **9.08** (mediana 6).
- **Pasos/set mediana:** 15.0.
- **Custom parts:** 21 / 1.07 %.
- **Subparts embebidos:** 0.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `30136.dat` | **184** | 5/13 | **cabeza de caballo con cuello movable** — 9.4 % del theme |
| 2 | `30137.dat` | 103 | 3/13 | **cuerpo de caballo** — 5.2 % del theme |
| 3 | `3004.dat` | 83 | 7/13 | brick 1×2 — pared de saloon |
| 4 | `3820.dat` | 76 | **12/13** | slope 45° 2×1 — techo de saloon / capa |
| 5 | `3005.dat` | 48 | 4/13 | brick 1×1 |
| 6 | `3818.dat` | 38 | 7/13 | slope 45° 1×3 — techo inclinado |
| 7 | `3819.dat` | 38 | 7/13 | slope 45° 1×3 (variant) |
| 8 | `3062b.dat` | 38 | 6/13 | round brick 1×1 — cabeza de figura |
| 9 | `30141.dat` | **37** | 9/13 | **saddle** — parts signature Western |
| 10 | `3815.dat` | 34 | 5/13 | slope 45° 1×1 — chimenea |
| 11 | `4865a.dat` | 34 | 7/13 | panel 1×2×1 |
| 12 | `3816.dat` | 33 | 5/13 | slope 45° 1×1 (variant) |
| 13 | `3817.dat` | 33 | 5/13 | slope 45° 1×2 inverted |
| 14 | `3023.dat` | 30 | 7/13 | plate 1×2 |
| 15 | `30140.dat` | 23 | 3/13 | **horse saddle completo** |

**Bigramas canónicos:**
- `30136.dat → 30136.dat` = **137** (en 4/13 sets — **caballos apilados: signature Western**).
- `30137.dat → 30137.dat` = 82 (en 3/13 sets — **cuerpos de caballo apilados**).
- `3004.dat → 3004.dat` = 37 (en 4/13 sets — pared de saloon).
- `3820.dat → 3820.dat` = 34 (en 12/13 sets — slopes apilados para techo/capa).
- `3818.dat → 3819.dat` = 21 (en 6/13 sets — pendiente con transición).
- `209.dat` (printed brick) bigrama = 18 — pared decorada de saloon.

**Deltas dominantes:**
- `(0, 0, 0)` = 85 (apilado).
- `(0, -24, 0)` = 52 (1 brick vertical — pared).
- `(80, 0, 0)` = 38, `(-80, 0, 0)` = 28 (4 studs — pared larga).
- `(31, 0, 0)` = **24** (offset 31 LDU — **signature Western: caballo con cuello en offset no-1-stud**).

**parts exclusivas:** 7:
- `30141.dat` (saddle, 9/13 sets = 37 unidades).
- `3629.dat` (printed plate 1×3 con letra, 5/13 sets = 8).
- `30133.dat` (printed horse accessory, 4/13 sets = 8).
- `6064.dat` (printed accessory, 3/13 sets = 7).
- `3069bpw2.dat` (printed plate "WANTED", 3/13 sets = 7).
- `30127p01.dat` (printed brick, 3/13 sets = 4).
- `4491b.dat` (printed piece, 3/13 sets = 3).

**examples representativo:** **6716-1 Covered Wagon** (70 p, 6 sub-builds, 23 steps, custom=0) — carro cubierto, el set Western canónico con caballo.

**Patrón narrativo:**
Western es un theme con **dos módulos**: (a) **caballo** (`30136` cabeza + `30137` cuerpo + `30141` saddle) — la signature, con bigramas `30136→30136=137` y `30137→30137=82` que dominan el corpus entero; (b) **saloon / carro cubierto** — pared de `3004` brick 1×2 (bigrama=37) + slopes 45° `3820` apiladas para techo (bigrama=34). El delta signature es **`(31, 0, 0)`** (24 ocurrencias) — offset no-1-stud usado para los cuellos movibles del caballo. **parts impresas**: 7 parts únicas del theme (`30141` saddle, `3629` printed plate, `30133` printed horse, `3069bpw2` "WANTED" plate, etc.) — Western usa decoraciones impresas **más que cualquier otro theme no-Castle**.

---

## Castle (10 sets, 1 621 parts, 9 80s/90s + 1 kids)

- **Sets en corpus:** 10 (9 80s/90s: 6010-6043; 1 kids: 6102 Castle Mini Figures 1985). Castle **casi no tiene representación kids** en este corpus (la mayoría están en sub-themes Castle > Lion Knights, Black Falcons, etc.).
- **parts totales:** 1 621
- **parts/set media:** **162.1** (mediana 130.5, rango 40-341).
- **Sub-builds/set media:** **8.00** (mediana 8).
- **Pasos/set mediana:** 23.5.
- **Custom parts:** 5 / 0.31 %.
- **Subparts embebidos:** 0.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3005.dat` | **108** | 7/10 | brick 1×1 — torre/muro |
| 2 | `4-4cyli.dat` | **104** | 1/10 | cilindro primitivo — bandera/lanza (1 set: 6061 Siege Tower) |
| 3 | `3004.dat` | 90 | 8/10 | brick 1×2 |
| 4 | `3820.dat` | 68 | 9/10 | slope 45° 2×1 — techo torre |
| 5 | `3024.dat` | 46 | 6/10 | plate 1×1 |
| 6 | `3023.dat` | 44 | 7/10 | plate 1×2 |
| 7 | `3062b.dat` | 39 | 7/10 | round brick 1×1 — torre redonda |
| 8 | `3710.dat` | 37 | 7/10 | plate 1×4 |
| 9 | `3022.dat` | 36 | 6/10 | plate 2×2 |
| 10 | `3020.dat` | 30 | 6/10 | plate 2×4 |
| 11 | `4444.dat` | 28 | 5/10 | slope 45° 2×2 — techo |
| 12 | `3010.dat` | 27 | 6/10 | brick 1×1 |
| 13 | `3069b.dat` | 27 | 6/10 | plate 1×2 (variant) |
| 14 | `6091.dat` | 25 | 5/10 | slope 45° 1×1 inverted |
| 15 | `3847.dat` | 23 | 5/10 | slope 45° 1×2 small — **única parts exclusiva Castle** |

**Bigramas canónicos:**
- `4-4cyli.dat → 4-4cyli.dat` = **103** (1 set — 6061 Siege Tower).
- `3005.dat → 3005.dat` = **51** (en 7/10 sets — torre de brick 1×1).
- `3004.dat → 3004.dat` = 39 (en 5/10 sets — muro de brick 1×2).
- `3820.dat → 3820.dat` = 29 (en 7/10 sets — pendiente).
- `3819.dat → 3818.dat` = **25** (en 6/10 sets — **transición de slopes** = techo en esquina).

**Deltas dominantes:**
- `(0, 0, 0)` = 68 (apilado).
- `(0, -8, 0)` = 46 (1 plate vertical — apilado brick).
- `(0, -24, 0)` = **38** (1 brick vertical — **delta signature Castle: torres apiladas**).
- `(0, 0, 100)` = 26 (2 studs profundidad).
- `(16, 9, 0)` = **25** (offset X-Y combinado — **signature Castle: esquinas y remates**).

**parts exclusivas:** 1 (`3847.dat` en 5/10 sets = 23 unidades — slope 45° 1×2 small). **Castle pierde exclusividad al fragmentarse**: las parts que eran signature Castle (3626ap01, 4489a, 2345) están ahora en **Castle > Lion Knights / Forestmen / Black Falcons** que cuentan como sub-themes separados en la metodología.

**Comparación 80s/90s vs kids (en este corpus):** los slopes del corpus Castle (10 sets) tienen 56 unidades de `3820` en 80s/90s vs 12 en 1 set kids — **insuficiente muestra kids para comparar slopes**. En la familia Castle entera (21 sets, 5 141 parts): 80s/90s (9 sets) usa `3820`=56, `4444`=14, `2436a`=9; kids (12 sets) usa `3820`=92, `3665a`=48, `3665b`=32, `4444`=26 → **los sets kids (post-2010) tienen más diversidad de slopes** (`3665a/b`, `3039`, etc.) que los 80s donde `3820`+`4444` dominaban.

**examples representativo:** **6041-1 Armor Shop** (123 p, 6 sub-builds, 17 steps, custom=0) — tienda medieval + herrero, el set Castle "mediano" típico.

**Patrón narrativo:**
Castle construye **torres y murallas con `3005` brick 1×1 en bigrama 51** y `3004` brick 1×2 en bigrama 39 — los muros son literalmente torres de brick vertical. El **delta signature es `(0, -24, 0) = 38`** (1 brick en Y) y `(0, -8, 0) = 46` (1 plate en Y) — **Castle es el único theme donde la vertical domina**. El `4-4cyli` (104 unidades) viene **todo de un solo set (6061 Siege Tower)** con banderines. Las pendientes usan `3820` 45° 2×1 en bigrama 29 y la transición `3819→3818` (=25) — patrón de techo en esquina. Custom parts = 5 (muro decorado, ballesta impresa).

---

## Creator (10 sets, 361 parts, todos kids)

- **Sets en corpus:** 10 (todos kids, 2006-2019). Creator es la **serie promocional/económica** de Creator — sets pequeños (mediana 36 p) sin playsets.
- **parts totales:** 361 — el corpus Creator es **el más pequeño de los themes grandes** (junto con Universal Building Set).
- **parts/set media:** **36.1** (mediana 36.5, rango 0-74).
- **Sub-builds/set media:** **2.20** (mediana 2) — la **menor descomposición** de los themes grandes.
- **Pasos/set mediana:** 11.5.
- **Custom parts:** 2 / 0.55 %.
- **Subparts embebidos:** 3.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `54200.dat` | **23** | 4/10 | hinge plate 1×2 — **compartido con Creator 3-in-1 pero usado en miniatura** |
| 2 | `6141.dat` | 17 | 6/10 | round plate 1×1 |
| 3 | `3023.dat` | 16 | 5/10 | plate 1×2 |
| 4 | `3022.dat` | 11 | 5/10 | plate 2×2 |
| 5 | `3021.dat` | 11 | 3/10 | plate 2×3 |
| 6 | `3005.dat` | 10 | 4/10 | brick 1×1 |
| 7 | `2420.dat` | 9 | 4/10 | plate 2×2 |
| 8 | `3004.dat` | 9 | 4/10 | brick 1×2 |
| 9 | `3660.dat` | 9 | 4/10 | slope 45° 2×2 inverted |
| 10 | `2780.dat` | 8 | 3/10 | technic pin — mecanismo mini |
| 11 | `3623.dat` | 8 | 4/10 | plate 1×3 |
| 12 | `2877.dat` | 7 | 1/10 | printed plate 1×6 |
| 13 | `85080.dat` | 7 | 1/10 | technic brick específico |
| 14 | `3010.dat` | 6 | 3/10 | brick 1×1 |
| 15 | `3070b.dat` | 6 | 4/10 | tile 1×1 round |

**Bigramas canónicos:**
- `54200.dat → 54200.dat` = **11** (en 4/10 sets — hinges en pares, mismo patrón que Creator 3-in-1).
- `6141.dat → 6141.dat` = 7 (en 3/10 sets).
- `2877.dat → 2877.dat` = 6 (en 1 set).
- `85080.dat → 85080.dat` = 6.
- `15573.dat → 15573.dat` = 6.

**Deltas dominantes:**
- `(60, 0, 0)` = 11 (1 stud lateral).
- `(0, 0, -20)` = 11, `(0, 0, 20)` = 10 (½ stud Z — **offset, mismo que Creator 3-in-1**).
- `(-20, 0, 0)` = 10, `(-60, 0, 0)` = 8.

**parts exclusivas:** 0. Creator usa **exactamente el mismo vocabulario que Creator 3-in-1** (`54200`, `2780`, `6141`, `3023`) — la diferencia es **el tamaño**: Creator son miniatura (mediana 36 p), Creator 3-in-1 son playsets (mediana 72-924 p).

**examples representativo:** **7601-1 LEGO Go-Kart Set** (41 p, 2 sub-builds, 24 steps, custom=0) — miniatura promocional.

**Patrón narrativo:**
Creator es la **réplica miniaturizada de Creator 3-in-1**: misma parts signature **`54200` hinge** (bigrama 11 en 4/10 sets), mismo **`2780` technic pin**, misma **`6141` round**. La diferencia es volumétrica: Creator = 36 p mediana, Creator 3-in-1 = 72.5 p mediana. **Mismo vocabulario, misma firma modular con offset ½-stud (`(0,0,-20)=11`, `(0,0,20)=10`)** — Creator es "Creator 3-in-1 en escala 1:2". **Subparts embebidos = 3** (pequeñas parts pre-ensambladas para figuras y detalles).

---

## Pirates (5 sets, 3 314 parts, todos 80s/90s)

- **Sets en corpus:** 5 (todos 80s/90s, 1989-1996). Pirates **no creció** entre corpus (5 → 5).
- **parts totales:** 3 314 — el **segundo corpus más grande por theme**, sólo detrás de Pirates > Pirates I.
- **parts/set media:** **662.8** (mediana 37, rango 29-2 834) — **distribución extrema**: 4 sets pequeños (mediana 37) y **un gigante** (6286 Skull's Eye Schooner = 2 834 p = 86 % del theme).
- **Sub-builds/set media:** **11.40** (mediana 4).
- **Pasos/set mediana:** 0.0 (sólo 2/5 sets con steps).
- **Custom parts:** 23 / 0.69 % (concentrados en 6286).
- **Subparts embebidos:** **26** — los más altos del corpus (junto con Fabuland y Friends).

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `4-4cyli.dat` | **1 792** | 1/5 | **cilindro primitivo — 86 % del theme, todo de 6286 Schooner** |
| 2 | `754.dat` | **173** | 1/5 | baseplate 24×24 — cubierta del barco |
| 3 | `3004.dat` | 78 | 3/5 | brick 1×2 — casco |
| 4 | `3005.dat` | 50 | 2/5 | brick 1×1 |
| 5 | `3023.dat` | 49 | 4/5 | plate 1×2 |
| 6 | `3062b.dat` | 47 | 4/5 | round brick 1×1 — cañones |
| 7 | `3820.dat` | 33 | 4/5 | slope 45° 2×1 |
| 8 | `3069b.dat` | 32 | 4/5 | plate 1×2 (variant) |
| 9 | `3010.dat` | 30 | 3/5 | brick 1×1 |
| 10 | `3710.dat` | 28 | 3/5 | plate 1×4 |
| 11 | `3020.dat` | 26 | 4/5 | plate 2×4 |
| 12 | `3022.dat` | 25 | 4/5 | plate 2×2 |
| 13 | `2431.dat` | 24 | 3/5 | plate 2×2 con side studs — anclaje vela |
| 14 | `3024.dat` | 24 | 3/5 | plate 1×1 |
| 15 | `3623.dat` | 22 | 3/5 | plate 1×3 |

**Bigramas canónicos:**
- `4-4cyli.dat → 4-4cyli.dat` = **1 789** (1 set — **mástil multi-segmento del Schooner**, el bigrama más alto del corpus entero).
- `754.dat → 754.dat` = **165** (1 set — cubierta del Schooner con baseplates apilados).
- `3062b.dat → 3062b.dat` = 29 (en 3/5 sets — cañones redondos).
- `3004.dat → 3004.dat` = 22 (en 3/5 sets — casco).
- `3820.dat → 3820.dat` = 16 (en 4/5 sets — pendiente).

**Deltas dominantes:**
- `(3, -0.1, -0.5)` = **148** — micro-rotación de vela/bandera (signature Pirates).
- `(1.8, 0, -2.4)` = 146.
- `(1.5, 0, -2.6)` = 101.
- `(2.2, 0.1, 2.0)` = 93.
- `(-2, 0, -2)` = 50.

→ **Deltas fraccionarios < 3 LDU** — los barcos Pirates tienen **velas con orientaciones sub-stud** que ningún otro theme usa.

**parts exclusivas:** 8 (`70501a/b/c/d.dat` flag variants en 2/5 sets, `2335p30.dat` flag con calavera, `3626bp35.dat` printed plate Pirates, `2543.dat` plate 6×6 round, `2562.dat` — todas en 2 sets). Pirates **comparte `2543` con Pirates > Pirates I** y otras con Castle (4-4cyli, 3820).

**examples representativo:** **6232-1 Skeleton Crew** (37 p, 4 sub-builds, 0 steps, custom=0) — el set Pirates "mediano" sin contar el Schooner.

**Patrón narrativo:**
Pirates está **dominado por un solo set (6286 Skull's Eye Schooner = 2 834 p = 86 % del theme)** — sin él, los 4 sets restantes promedian **120 p/set**. El theme se caracteriza por: **mastil cilíndrico multi-segmento** (`4-4cyli` bigrama 1789 = 1 set), **baseplate de barco apilado** (`754` bigrama 165 = 1 set), **cañones con `3062b` round brick** (bigrama 29), y **velas con deltas fraccionarios < 3 LDU** — orientation sub-stud única del theme. **Custom+subparts = 23+26** — los más altos del corpus (junto con Fabuland).

---

## Train (9 sets, 2 592 parts, todos 80s/90s)

- **Sets en corpus:** 9 (todos 80s/90s, 1980-1996). Train **no creció** entre corpus (9 → 9). Las variantes modernas (Train > 9V 6 sets, Trains 12V 1 set) están en sub-themes separados.
- **parts totales:** 2 592
- **parts/set media:** **288.0** (mediana 362, rango 0-681) — sets grandes uniformes (el más pequeño excluyendo 4558 Metroliner=0 p = 82 p).
- **Sub-builds/set media:** **11.44** (mediana 10).
- **Pasos/set mediana:** 0.0 (3 sets con 0 steps; 4565 = 132 steps).
- **Custom parts:** 8 / 0.31 % (concentrados en 4558 Metroliner).
- **Subparts embebidos:** 0.

**Top 15 parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3004.dat` | **105** | 6/9 | brick 1×2 — chasis principal |
| 2 | `3023.dat` | 76 | 5/9 | plate 1×2 |
| 3 | `3010.dat` | 56 | 5/9 | brick 1×1 |
| 4 | `3063b.dat` | **48** | 2/9 | brick arch 1×2 — pasos de rueda |
| 5 | `3665a.dat` | **46** | 3/9 | slope 45° 1×2 inverted — capó/lateral |
| 6 | `3062b.dat` | 38 | 4/9 | round brick 1×1 — faros |
| 7 | `2420.dat` | 38 | 5/9 | plate 2×2 |
| 8 | `3009.dat` | 36 | 5/9 | brick 1×6 — vagón largo |
| 9 | `3069b.dat` | 35 | 5/9 | plate 1×2 (variant) |
| 10 | `3024.dat` | 33 | 4/9 | plate 1×1 |
| 11 | `6141.dat` | 32 | 5/9 | round plate 1×1 |
| 12 | `3020.dat` | 31 | 5/9 | plate 2×4 |
| 13 | `3069B.DAT` | 31 | 4/9 | plate 1×2 (case variant) |
| 14 | `3622.dat` | 28 | 4/9 | plate 3×3 |
| 15 | `3022.dat` | 26 | 5/9 | plate 2×2 |

**Bigramas canónicos:**
- `3004.dat → 3004.dat` = **66** (en 5/9 sets — pared de vagón).
- `3063b.dat → 3063b.dat` = **45** (en 2/9 sets — paso de rueda modelado).
- `3665a.dat → 3665a.dat` = **38** (en 3/9 sets — pendiente invertida para capó).
- `3023.dat → 3023.dat` = 35 (en 4/9 sets).
- `3062b.dat → 3062b.dat` = 29 (en 2/9 sets).
- `3069B.DAT → 3069B.DAT` = **22** (en 4/9 sets — **chasis de plate 1×2 repetido = listones del tren**).

**Deltas dominantes:**
- `(0, 0, -60)` = **68** (1 stud profundidad Z).
- `(0, 0, 60)` = 65 (1 stud Z reverso).
- `(0, 0, -100)` = 52 (2 studs Z).
- `(0, 0, 0)` = 51.
- `(100, 0, 0)` = 46.

→ **Train es el único theme donde los deltas dominan en Z**, no en X — los vagones se construyen **a lo largo del eje Z** (el tren "mira" hacia Z+).

**parts exclusivas:** 0 en este corpus de meta.theme="Train" — `2653` (track base), `2867` (wheel tile), `4166b` (1×6 panel) están en Train > 9V (sub-theme separado). El `3069B.DAT` (case variant de plate 1×2) bigrama 22 es signature Train.

**examples representativo:** **7715-1 Push-Along Passenger Steam Train** (362 p, 10 sub-builds, 26 steps, custom=0) — locomotora + 2 vagones.

**Patrón narrativo:**
Train construye **chasis largos sobre el eje Z** con `3004` brick 1×2 (bigrama 66) y `3069B.DAT` plate 1×2 case-variant (bigrama 22) como **listones**. Los pasos de rueda se modelan con `3063b` brick arch 1×2 (bigrama 45, 2/9 sets) y los capós con `3665a` slope 45° inverted (bigrama 38, 3/9 sets). **Deltas dominantes en Z (`dz=-60`, `dz=60`, `dz=-100`)** — único theme donde la profundidad Z gana sobre el ancho X. Custom parts = 8 concentrados en **4558 Metroliner** (tren futurista no-Technic custom). Subparts = 0 (no hay parts complejas embebidas en Train 80s).

---

## Universal Building Set (4 sets, 29 parts, todos 80s/90s)

- **Sets en corpus:** 4 (todos 80s/90s, 1985-1996). Es el **corpus más pequeño de los themes reportados** — sólo 29 parts en total.
- **parts totales:** 29
- **parts/set media:** **7.2** (mediana 8.5, rango 0-12). **Sets promocionalmente diminutos**.
- **Sub-builds/set media:** **1.50** (mediana 2).
- **Pasos/set mediana:** 0.0 (todos los sets tienen 0 steps).
- **Custom parts:** 0.
- **Subparts embebidos:** 0.

**Top parts:**

| # | parts | Frec. | En sets | Notas |
|---|---|---|---|---|
| 1 | `3004.dat` | 5 | 2/4 | brick 1×2 |
| 2 | `3023.dat` | 4 | 2/4 | plate 1×2 |
| 3 | `3020.dat` | 3 | 2/4 | plate 2×4 |
| 4 | `3003pe2.dat` | **3** | 3/4 | **brick 2×2 printed con logo LEGO** — parts signature Universal |
| 5 | `3003.dat` | 3 | 2/4 | brick 2×2 |

**Bigramas canónicos:**
- `3004.dat → 3004.dat` = 2 (en 2/4 sets).
- `3023.dat → 3023.dat` = 2 (en 1/4 sets).

**Deltas dominantes:**
- `(0, -8, 0)` = 2, `(0, 24, -10)` = 2 — deltas menores, sets planos.

**parts exclusivas:** 1 (`3003pe2.dat` printed brick 2×2 con logo LEGO, 3/4 sets = 3 unidades).

**examples representativo:** **2130-1 Danone Promotional Set: Duck** (7 p, 2 sub-builds, 0 steps, custom=0) — promotional diminuto.

**Patrón narrativo:**
Universal Building Set es un theme **promocional efímero**: 4 sets de ≤12 parts, todos entregados sin instrucciones paso-a-paso (0 steps) y construidos con **sólo 13 parts únicas** en todo el corpus. La única signature es la **`3003pe2` brick 2×2 printed con logo LEGO** (3/4 sets = 3 unidades). Las construcciones son esencialmente **mini-arquitecturas planas** sin descomposición significativa (mediana 2 sub-builds/set).

---

## Tabla comparativa cross-theme (300 sets)

| Señal | Town | Classic Town | Fabuland | Friends | Space | Creator 3-in-1 | Western | Castle | Creator | Pirates | Train | Star Wars | Model Team | HP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Sets** | 40 | 36 | 23 | 17 | 15 | 14 | 13 | 10 | 10 | 5 | 9 | 6 | 5 | 4 |
| **parts** | 4 394 | 5 848 | 896 | 5 046 | 2 088 | 3 143 | 1 967 | 1 621 | 361 | 3 314 | 2 592 | 1 120 | 3 215 | 2 407 |
| **P/set media** | 110 | 162 | 39 | **297** | 139 | 225 | 151 | 162 | 36 | 663 | 288 | 187 | 643 | 602 |
| **P/set mediana** | 81 | 150 | 23 | 202 | 119 | 73 | 70 | 131 | 37 | 37 | 362 | 154 | 391 | 721 |
| **Sub-b/set** | 4.6 | 5.9 | 3.5 | 11.2 | **12.6** | 4.4 | 9.1 | 8.0 | 2.2 | 11.4 | 11.4 | 12.0 | **23.8** | 14.3 |
| **Pasos/set (med)** | 12 | 17 | 3 | 0 | **0** | 33 | 15 | 24 | 12 | 0 | 0 | **62** | 37 | **215** |
| **Custom (total)** | 14 | 23 | **83** | **208** | 1 | 4 | 21 | 5 | 2 | 23 | 8 | 1 | 14 | 17 |
| **Custom ratio** | 0.32 % | 0.39 % | **9.26 %** | **4.12 %** | 0.05 % | 0.13 % | 1.07 % | 0.31 % | 0.55 % | 0.69 % | 0.31 % | 0.09 % | 0.44 % | 0.71 % |
| **Subparts (total)** | 0 | 0 | 49 | **136** | 0 | 3 | 0 | 0 | 3 | 26 | 0 | 0 | 6 | 0 |
| **Vocabulario (parts únicas top-30)** | **357** | 308 | 160 | 208 | 190 | 163 | 157 | 121 | 103 | 89 | 165 | 107 | 90 | 75 |
| **parts #1 (frec.)** | `6141` 142 | `3024` 210 | `u9101` 78 | `6141` 223 | `3023` 120 | `3023` 194 | `30136` 184 | `3005` 108 | `54200` 23 | `4-4cyli` 1792 | `3004` 105 | `756` 48 | `3023` 157 | `3005` 127 |
| **Bigrama #1** | `754→754` 88 | `3024→3024` 96 | `3004→3004` 33 | `3004→3004` 113 | `3023→3023` 47 | `6141→6141` 94 | `30136→30136` 137 | `4-4cyli→...` 103 | `54200→54200` 11 | `4-4cyli→...` 1789 | `3004→3004` 66 | `756→756` 47 | `3023→3023` 79 | `60592→38320` 51 |
| **Delta #1** | `(0,0,0)` 195 | `(0,0,0)` 308 | `(0,-24,0)` 50 | `(20,0,0)` 109 | `(0,0,0)` 97 | `(20,0,0)` 80 | `(0,0,0)` 85 | `(0,0,0)` 68 | `(60,0,0)` 11 | `(3,-0.1,-0.5)` 148 | `(0,0,-60)` 68 | `(60,0,0)` 50 | `(180,0,0)` 89 | `(0,0,0)` 85 |
| **Eje dominante** | X+Z (mixto) | X+Z (mixto) | Y (vertical) | X+Z (½-stud) | X | X (½-stud) | Y (vertical) | **Y (vertical)** | X | **XYZ frac.** | **Z (depth)** | X | **X (large)** | Y (vertical) |
| **parts exclusivas** | 0 | 2 | **23** | 3 | 2 | 0 | 7 | 1 | 0 | 8 | 0 | 2 | 0 | 3 |

---

## Reglas (convenciones por theme en el corpus 300)

1. **Town/City es el theme con mayor vocabulario (357 parts únicas en top-30) y mayor volumen de corpus (76 sets = 25 % de los 300).** Las dos mitades — Town 80s (40 sets) y Town > Classic Town kids (36 sets) — comparten **el mismo vocabulario de plates (`3024`, `3023`) y slopes (`3820`)**, pero Town > Classic Town usa **doble de plate 1×1** (210 vs 138) y **más bigramas de pared `3004→3004`** (59 vs 22), reflejando una evolución hacia **plataformas planas detalladas**.

2. **Fabuland es el theme con vocabulario más exclusivo (23 parts únicas del corpus, todas serie `u91xx`)**, ratio de custom parts más alto (**9.26 %**) y patrones de deltas sub-stud (`-46`, `-10`, `30` LDU) que ningún otro theme usa. Cada set Fabuland es esencialmente **2 figuras custom (cabeza `u9101` + cuerpo `u9100`) + 1 animal (`u9103`) + mini-escenario de `3004` brick 1×2** (mediana 23 p/set).

3. **Friends es el theme post-2010 más decorativo**, con `6141` plate 1×1 round como signature (223 unidades, **16/17 sets = 94 %**) y `3062b` round brick 1×1 (119 unidades). Su **bigrama dominante es `3004→3004 = 113`** (el más alto del corpus para `3004→3004`), formando paredes de brick 1×2. parts custom pastel: **208 (4.12 %)** y 136 subparts embebidos. Friends usa **deltas `dx=20` (½-stud) y `dx=80` (4-stud) más que cualquier otro theme** — geometría con offset decorativo.

4. **Pirates es el theme más "monoset"**: **6286 Skull's Eye Schooner = 2 834 parts = 86 % del theme**. Su bigrama `4-4cyli→4-4cyli = 1 789` es el más alto del corpus entero (mástil multi-segmento del Schooner). Pirates es el **único theme con deltas fraccionarios < 3 LDU** (`(3, -0.1, -0.5) = 148` micro-rotación de vela) — todos los demás themes usan múltiplos de 20 LDU.

5. **Train es el único theme con eje dominante Z** (no X): los deltas top son `(0, 0, -60) = 68`, `(0, 0, 60) = 65`, `(0, 0, -100) = 52`. Los vagones se construyen **a lo largo del eje Z** (el tren "mira" hacia Z+). parts signature: **`3069B.DAT` plate 1×2 case-variant** bigrama 22 (4/9 sets) — listones del chasis. No hay parts exclusivas en este corpus (las parts Train únicas están en Train > 9V sub-theme).

6. **Castle es el único theme con delta Y dominante en su corpus principal** — `(0, -24, 0) = 38` y `(0, -8, 0) = 46` son los deltas más altos. Castle **construye vertical**: `3005` brick 1×1 (108 unidades, 7/10 sets) + `3004` brick 1×2 (90 unidades) en bigramas (`3005→3005 = 51`, `3004→3004 = 39`) apilados como torres. Las pendientes usan **`3820` 45° 2×1** (68 unidades, 9/10 sets) y la transición `3819→3818` (=25) signature de techo en esquina. **Pero Castle pierde identidad exclusiva al fragmentarse** — las parts signature (`3626ap01`, `4489a`, `2345`) están en sub-themes separados (`Castle > Lion Knights`, `Forestmen`, `Black Falcons`) que cuentan aparte.

7. **Creator 3-in-1 tiene la parts signature `54200` hinge plate 1×2 con pin** (89 unidades, **10/14 sets = 71 %**) que aparece en bigrama `54200→54200 = 33` (8/14 sets) — patrón "módulos articulados en pares". Combinado con **`2780` technic pin con fricción** (49 unidades, 6/14 sets), el theme usa elementos Technic en contexto System para permitir la conversión 3-en-1. **Mismo vocabulario que Creator simple** (que es su versión miniaturizada con mediana 36 p).

8. **Western es un theme bimodal signature-caballo**: `30136` cabeza de caballo (184 unidades, 5/13 sets) + `30137` cuerpo (103) + `30141` saddle (37) dominan los bigramas (`30136→30136 = 137`, `30137→30137 = 82`). Para los saloon/carros usa `3004` brick 1×2 (bigrama 37) + `3820` slope 45° 2×1 (bigrama 34). **Delta signature `(31, 0, 0) = 24`** — offset no-1-stud para cuellos movibles del caballo. **7 parts impresas exclusivas** (`3629`, `3069bpw2` WANTED plate, `30133`, `30141`, etc.) — Western es el segundo theme con más decoración impresa (después de Castle con banderines).

9. **Space es el theme con menos instrucciones paso-a-paso** (mediana 0 pasos, 10/15 sets con 0 steps). Construye **plataformas planas con wheel-tire pairs** (`4624↔3641` bigrama 23+17) para róvers lunares y usa **`4589` cone 1×1** (40 unidades) como nozzles. **`3820` slope 45° 2×1 aparece en 15/15 sets (100 %)** — la pendiente universal. parts exclusiva más distintiva: **`3838` slope 33° 3×2** (ala de nave, 6/15 sets).

10. **Harry Potter (4 sets) tiene la mayor cadencia de pasos** (mediana 215 pasos/set, máximo 216 en 75953 Whomping Willow). Su parts signature es **`3005` brick 1×1** (127 unidades, 4/4 sets = 100 %) con bigrama `3005→3005 = 44` (4/4 sets = 100 %). Construye **muros de Hogwarts con bricks 1×1 apilados** y bigramas exclusivos `60592→38320 = 51` y `38320→60592 = 42` (2/4 sets = 50 %) — bricks arch que forman la arquitectura gótica. **Custom ratio 0.71 %** (concentrado en Hogwarts Whomping Willow).

---

## Observaciones transversales

- **Town + Town > Classic Town = 76 sets (25 % del corpus) y 10 242 parts (16 %)** — domina por volumen pero **sólo 0.32-0.39 % de custom parts**. Town **no innova en vocabulario**, sólo recombina plates estándar.
- **Fabuland (23 sets) y Friends (17 sets) son gemelos en custom density**: Fabuland 9.26 %, Friends 4.12 %. Pero Fabuland es 100 % serie custom `u91xx` mientras Friends es 100 % standard + decoración pastel — **dos estrategias opuestas para personajes**.
- **Creator + Creator 3-in-1 = 24 sets, 3 504 parts** — el theme **post-2010 más ingenieril** del corpus con `54200` hinge + `2780` technic pin como signature única. **Custom ratio = 0.13-0.55 %** (mínimo) — Creator es **cero custom, máxima modularidad estándar**.
- **Pirates y Model Team son los dos únicos themes donde un set individual pesa más del 50 % del theme**: 6286 Schooner = 86 % de Pirates (2 834/3 314 p), 5571 Giant Truck = 53 % de Model Team (1 703/3 215 p). El resto son sets pequeños.
- **Los deltas de Construcción son la firma más distintiva**:
  - **Town/Classic Town/Space/Creator 3-in-1/Star Wars/Creator**: X-dominantes.
  - **Train**: **Z-dominante** (eje de profundidad).
  - **Castle/Western/Harry Potter**: **Y-dominante** (vertical).
  - **Fabuland**: deltas sub-stud únicos (`-46`, `-10`, `30`).
  - **Pirates**: **deltas fraccionarios** (`3`, `-0.1`, `-0.5`).
- **Custom parts ratio ordena los themes así**: Fabuland (9.26 %) >> Friends (4.12 %) > Pirate/Castle (0.7 %) > resto (<0.5 %). **Los themes con mini-figuras antropomórficas requieren custom; los de vehículos/muros no**.
- **Subparts embebidos están concentrados en 4 themes**: Friends (136), Fabuland (49), Pirates (26), Model Team (6). **Town/Train/Space/Castle/Star Wars = 0 subparts** — sus parts complejas se modelan con primitives estándar (`4-4cyli`, slopes).
- **El corpus 300 confirma el corpus 100** en los themes clásicos (Pirates, Model Team, Train, Space, Castle, Star Wars) — las métricas son consistentes. La **gran adición** son los themes kids (Town > Classic Town, Friends, Creator, Creator 3-in-1, Western kids, Harry Potter) que **duplican el vocabulario sin innovar**: Town > Classic Town = Town 80s con plates más frecuentes; Creator = Creator 3-in-1 miniaturizado.
- **Universal Building Set es un outlier absoluto**: 4 sets, 29 parts, 13 parts únicas en todo el corpus. Es el único theme sin identidad constructiva — **promocionales efímeros**.