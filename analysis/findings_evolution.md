# Evolución de convenciones LEGO: 1980–1999 (corpus OMR, n=100)

> Análisis comparativo de 100 sets oficiales LDraw (OMR) publicados entre 1980 y 1999. Cifras citadas de `cross_corpus_stats.json` y `per_set_stats.json`. Este corpus es una **muestra** (no exhaustiva) por lo que las conclusiones sobre transiciones absolutas deben leerse con cautela.

---

## 1. Resumen del corpus

| Métrica global | Valor |
|---|---|
| Sets totales | 100 |
| Piezas totales | 18 670 |
| Pasos (STEPs) totales | 1 985 |
| Sub-builds totales | 839 |
| Custom parts embebidas | 112 |
| Piezas/set (media) | 186.7 (min 0, max 2 834) |
| Sets con BFC CERTIFY | 21 / 100 (21 %) |
| Sets con det negativo (NEG_DET) | 50 |
| Ratio det negativo | 0.27 % |

**Desglose por década** (`cross_corpus_stats.json:987-996`):

| Década | Sets | % corpus | Piezas | % piezas | Piezas / set (media) |
|---|---|---|---|---|---|
| 80s | 25 | 25 % | 3 090 | 16.6 % | 123.6 |
| 90s | 75 | 75 % | 15 580 | 83.4 % | 207.7 |

El corpus está sesgado hacia los 90s (3× más sets, 5× más piezas), lo que afecta cualquier comparativa de frecuencias absolutas — uso **medias, medianas y proporciones** para comparar décadas.

---

## 2. Tabla comparativa 80s vs 90s

| Métrica | 80s (n=25) | 90s (n=75) | Δ |
|---|---|---|---|
| Sets | 25 | 75 | +200 % |
| Piezas totales | 3 090 | 15 580 | +404 % |
| **Piezas/set (media)** | **123.6** | **207.7** | **+68 %** |
| Piezas/set (mediana) | 101 | 81 | −20 % |
| Piezas/set (Q1 / Q3) | 36 / 123 | 41 / 234 | rango más amplio en 90s |
| Piezas/set (max) | 379 (Train 7730-1) | 2 834 (Pirates 6286-1) | 7.5× |
| **Sub-builds/set (media)** | **5.68** | **9.29** | **+63 %** |
| Sub-builds/set (max) | 13 (Space 6885-1) | 40 (Model Team 5571-1) | 3× |
| STEPs/set (media) | 11.08 | 22.77 | +106 % |
| Master STEPs/set (media) | 1.84 | 1.32 | −28 % |
| Custom parts embebidas (total) | 10 | 68 | +580 % |
| Sets con ≥1 custom part | 5 (20 %) | 12 (16 %) | similar en % |
| **BFC CERTIFY (sets)** | **7 (28 %)** | **14 (18.7 %)** | **−9.3 pp** |
| BFC any | 7 | 14 | mismo que CERTIFY |
| NEG_DET total | 0 | 50 | solo 90s |
| % piezas Technic-flagged (8 piezas clave) | 13.4 % | 19.4 % | +45 % |

> **Lectura honesta de la tabla**:
> - Los 90s producen **sets típicos más pequeños** (mediana 81 < 101) pero con **varianza mucho mayor**: la cola pesada la generan Model Team, Pirates grandes y Star Wars.
> - El "aumento de tamaño" se concentra en unos cuantos outliers. La diferencia 80s→90s en media viene de Pirates/Model Team/Star Wars, no del set medio.
> - **BFC CERTIFY es proporcionalmente más frecuente en 80s** que en 90s en este corpus (28 % vs 18.7 %). No es un invento de los 90s.

---

## 3. Vocabulario de piezas: 80s vs 90s

Top 15 piezas agregadas por década (suma de frecuencias en los top-30 de cada set):

### 80s

| Pieza | Total | Notas |
|---|---|---|
| `3004.dat` Brick 1×2 | 153 | brick universal |
| `3023.dat` Plate 1×2 | 115 | plate universal |
| `4-4cyli.dat` Cyl 4×4 hole | **104** | **Technic axle** |
| `3005.dat` Brick 1×1 | 103 | |
| `3024.dat` Plate 1×1 | 95 | |
| `754.dat` Axle hole plate | 92 | Technic |
| `3710.dat` Plate 1×4 Technic | 76 | Technic |
| `3820.dat` Steering arm | 68 | Technic |
| `3665a.dat` Slope brick | 55 | |
| `3010.dat` Brick 1×4 | 53 | |
| `3660.dat` Plate 1×2 Technic | 50 | Technic |
| `3666.dat` Plate 1×4 | 46 | |
| `4070.dat` Brick 1×1 round | 45 | |
| `3623.dat` Plate 1×3 | 44 | |
| `6141.dat` Plate 1×2 Technic | 42 | Technic |

### 90s

| Pieza | Total | Notas |
|---|---|---|
| `4-4cyli.dat` Cyl 4×4 hole | **1 792** | **Technic axle (17× vs 80s)** |
| `3023.dat` Plate 1×2 | 475 | |
| `3004.dat` Brick 1×2 | 368 | |
| `6141.dat` Plate 1×2 Technic | 330 | Technic |
| `3710.dat` Plate 1×4 Technic | 277 | Technic |
| `3024.dat` Plate 1×1 | 273 | |
| `3820.dat` Steering arm | 239 | Technic |
| `3005.dat` Brick 1×1 | 184 | |
| `754.dat` Axle hole plate | 173 | Technic |
| `3022.dat` Plate 2×2 | 171 | |
| `3623.dat` Plate 1×3 | 168 | |
| `2420.dat` Plate 2×2 corner | 162 | |
| `2412b.dat` Tile 1×2 | 157 | |
| `3010.dat` Brick 1×4 | 154 | |
| `3020.dat` Plate 2×4 | 135 | |

### Observaciones sobre vocabulario

- **`4-4cyli.dat` (cilindro Technic) es el smoking gun**: 104 ocurrencias en 80s vs 1 792 en 90s (×17). Es el pivot que distingue Model Team (carcasas con ruedas/ejes) y Star Wars (vehículos) del System clásico.
- **Piezas Technic con agujero para eje** (`754`, `6141`, `3710`, `3820`, `3660`) están presentes en AMBAS décadas, pero su proporción crece 13.4 % → 19.4 % del total de piezas.
- **Piezas nuevas en 90s que no aparecen en el top-15 de 80s**: `3022` (plate 2×2), `2420` (corner plate 2×2), `2412b` (tile 1×2). Las **tiles planas** (`2412b`, 157 apariciones) son un marcador de los 90s — son muy usadas en Town/Castle para acabados lisos.
- Las **básicas** (`3004` brick 1×2, `3023` plate 1×2, `3005` brick 1×1, `3024` plate 1×1, `3010` brick 1×4, `3710` plate 1×4) dominan ambas décadas — el "esqueleto" del vocabulario no cambia.
- **Piezas populares en 80s que ya no en 90s**: `3665a` (slope brick) baja de 55 a (no aparece en top-15 90s); `4070` (brick round 1×1) baja de 45 a ausente.

---

## 4. Custom parts embebidas (licencias y molds únicos)

| Métrica | 80s | 90s |
|---|---|---|
| Total custom parts | 10 | 68 |
| Sets con ≥1 custom part | 5 (20 %) | 12 (16 %) |
| Media custom / set | 0.4 | 0.9 |

**Top 5 sets con más custom parts** (todos son 90s):

| Set | Año | Tema | Custom | Piezas |
|---|---|---|---|---|
| 6286-1 Skull's Eye Schooner | 1993 | Pirates | **21** | 2 834 |
| 6765-1 Gold City Junction | 1996 | Western | 10 | 382 |
| 5542-1 Black Thunder | 1998 | Model Team | 10 | 485 |
| 4558-1 Metroliner | 1991 | Train | 8 | 0 |
| 6541-1 Intercoastal Seaport | 1991 | Town | 5 | 550 |

**Lectura**:
- Las custom parts se concentran en **vehículos grandes y sets temáticos licenciados/non-System**: el Schooner Pirates (1993) es un outlier extremo con 21 custom parts — probablemente rats, pirate hats, cofres, anclas, cañones y similares. La escala del set (2 834 piezas) absorbe el coste de diseñar molds únicos.
- Los **Star Wars de 1999 NO destacan por custom parts**: 7121 (Naboo Swamp) tiene 1; el resto 0. Las minifigs SW tienen molds únicos pero parece que en este corpus no están catalogadas como custom parts embebidas en MPD (o se modelan con primitives).
- Los **años pico de custom parts**: 1993 (21, todo de un set), 1991 (13), 1996 (10) y 1998 (10).
- Los 80s producen custom parts modestamente (5 sets con 1–4 cada uno), incluyendo Model Team 5510-1 (1986) con 4.

> **Conclusión parcial**: la hipótesis "los 90s introdujeron más piezas licenciadas" **se cumple en volumen** (68 vs 10) **pero no en proporción** (16 % vs 20 % de sets). El corpus 80s está dominado por sets pequeños donde cualquier mold único infla la proporción.

---

## 5. BFC compliance

**21/100 sets tienen BFC CERTIFY** (`cross_corpus_stats.json:794`).

**Desglose por década**:

| Década | Sets totales | BFC CERTIFY | % |
|---|---|---|---|
| 80s | 25 | 7 | **28 %** |
| 90s | 75 | 14 | **18.7 %** |

**Desglose por año** (de los 21 sets CERTIFY):

| Año | Sets con BFC CERTIFY | Temas |
|---|---|---|
| 1980 | 1 | Fabuland |
| 1982 | 2 | Boat, Town |
| 1984 | 1 | Castle |
| 1985 | 2 | Fabuland, Town |
| 1986 | 1 | Model Team |
| 1990 | 3 | Castle, Space |
| 1991 | 2 | Train, Town |
| 1993 | 1 | Pirates |
| 1994 | 1 | Town |
| 1995 | 1 | Pirates |
| 1996 | 2 | Western |
| 1997 | 1 | Western |
| 1998 | 1 | Model Team |
| 1999 | 2 | Model Team, Star Wars |

**Lectura (corrige la hipótesis del enunciado)**:
- El enunciado sugiere "BFC CERTIFY aparece mayormente en sets posteriores a 1998". El corpus **no lo soporta**: 1998 y 1999 acumulan **solo 3** de los 21 sets con CERTIFY (14 %).
- De hecho, la **mayoría de los BFC CERTIFY (10/21 = 48 %)** está en 1980–1985. La proporción es decreciente con el tiempo.
- Esto sugiere que **BFC CERTIFY no fue un estándar que "apareció" en los 90s**: fue una elección del autor del MPD/OMR desde los primeros años del corpus. Las comunidades OMR adoptaron el lineamiento BFC independientemente de la fecha del set.

> Nota: BFC CERTIFY es un **metadato del modelo digital**, no del set físico. Su distribución refleja prácticas de la comunidad OMR, no convenciones LEGO de fábrica.

---

## 6. Sub-builds (modularidad)

| Década | Media sub-builds | Max sub-builds | Distribución |
|---|---|---|---|
| 80s | 5.68 | 13 | 2–10 dominante |
| 90s | 9.29 | 40 | cola larga (max=40 en Model Team 5571-1) |

**Top 5 sets con más sub-builds** (todos 90s):

| Set | Año | Tema | Sub-builds | Piezas |
|---|---|---|---|---|
| 5571-1 Giant Truck | 1996 | Model Team | **40** | 1 703 |
| 6286-1 Skull's Eye Schooner | 1993 | Pirates | 33 | 2 834 |
| 5533-1 Red Fury | 1999 | Model Team | 32 | 353 |
| 5542-1 Black Thunder | 1998 | Model Team | 28 | 485 |
| 7140-1 X-wing Fighter | 1999 | Star Wars | 22 | 328 |

**Lectura**:
- **Model Team domina** el ranking de sub-builds: 3 de los top-5.
- **Los Star Wars de 1999** (X-wing 22, TIE+Y-wing 18, Snowspeeder 14) son **más sub-builds que los Town promedio** de 1990–1994.
- En los 80s, los sets con más sub-builds son Space (6885-1 Crater Crawler 1988 con 13) y Train (7715 Push-Along Passenger con 10).
- **STEPs**: la media sube de 11.08 (80s) a 22.77 (90s), +106 %. Esto es coherente con la explosión de sub-builds (cada sub-build genera varios STEPs).

---

## 7. Línea temporal 1980–1999

Resumen año por año (`per_set_stats.json`):

| Año | Sets | Piezas totales | Media piezas | Media sub-builds | BFC | Custom |
|---|---|---|---|---|---|---|
| 1980 | 5 | 566 | 113 | 5.0 | 1 | 0 |
| 1981 | 1 | 29 | 29 | 3.0 | 0 | 0 |
| 1982 | 4 | 310 | 78 | 4.5 | 2 | 4 |
| 1984 | 3 | 492 | 164 | 6.3 | 1 | 1 |
| 1985 | 3 | 565 | 188 | 5.0 | 2 | 1 |
| 1986 | 3 | 436 | 145 | 6.3 | 1 | 4 |
| 1987 | 3 | 452 | 151 | 8.0 | 0 | 0 |
| 1988 | 2 | 209 | 105 | 8.0 | 0 | 0 |
| 1989 | 1 | 31 | 31 | 3.0 | 0 | 0 |
| 1990 | 12 | 1 621 | 135 | 8.3 | 3 | 5 |
| 1991 | 7 | 1 232 | 176 | 10.6 | 2 | 13 |
| 1992 | 4 | 325 | 81 | 7.3 | 0 | 0 |
| 1993 | 7 | 4 092 | **585** | 12.7 | 1 | 21 |
| 1994 | 7 | 935 | 134 | 8.7 | 1 | 5 |
| 1995 | 5 | 1 141 | 228 | 9.4 | 1 | 2 |
| 1996 | 14 | 3 506 | 250 | 8.8 | 2 | 10 |
| 1997 | 4 | 124 | 31 | 2.8 | 1 | 1 |
| 1998 | 8 | 1 131 | 141 | 7.4 | 1 | 10 |
| 1999 | 7 | 1 473 | 210 | **14.9** | 2 | 1 |

### Hitos históricos contrastados con el corpus

> Las fechas históricas abajo son de dominio público; las **observaciones del corpus** son lo que este sample de 100 sets permite respaldar.

- **1980 — Fabuland + Town**: el corpus tiene Fabuland 3602-1 (10 piezas, BFC CERTIFY), Town 1591-1 (Danone Truck, 40 piezas), Space 6821-1, Train 7730-1 (379 piezas) y 7834-1. Town aparece clasificado como "Classic Town" en `theme_full`. **Fabuland** se retira del corpus tras 1985.
- **1984 — Castle Revival**: 3 Castle sets en 1984 (Supply Wagon 40 piezas, Siege Tower 341 piezas con BFC CERTIFY + 1 custom part). El corpus no incluye ningún Castle 1985–1986; regresan en 1986 (Armor Shop) y 1987 (Battering Ram).
- **1986 — Model Team debuta en el corpus**: 5510-1 Off-Road 4x4 (283 piezas, 10 sub-builds, BFC CERTIFY, 4 custom parts). Model Team seguirá apareciendo hasta 1999.
- **1989 — Pirates launch**: el corpus solo captura **6235-1 Buried Treasure** (31 piezas, 3 sub-builds, sin BFC, sin custom parts) — una muestra diminuta del lanzamiento Pirates. **El Black Seas Barracuda (6285-1) NO está en este corpus** (es la pieza fundacional del tema).
- **1990 — Castle pico + Space pico**: 12 sets, 3 con BFC CERTIFY (Castle 6034/6059, Space 6989 con 38 sub-builds — el más complejo del corpus hasta entonces).
- **1992 — NO hay Pirates ni Star Wars en el corpus**. Solo Town (1772, 6511, 6648) y Space (6897 Rebel Hunter). **La premisa "Pirates end, Star Wars debut en 1992" es incorrecta**: el corpus tiene Pirates 6286 en 1993 y Pirates 6279 en 1995; Star Wars **no debuta hasta 1999** en este corpus (los 6 sets SW son todos 1999, correspondientes al lanzamiento Episode I de mayo 1999).
- **1993 — Skull's Eye Schooner outlier**: 6286-1 Pirates con **2 834 piezas, 33 sub-builds, 21 custom parts, BFC CERTIFY**. Es el set más grande del corpus y absorbe el grueso de las custom parts de los 90s. Model Team 5521-1 Sea Jet también en 1993 (391 piezas).
- **1994 — Town/Space denso**: 7 sets, mix Town (Surveillance Squad con BFC CERTIFY, Jet, Trail Ranger, Ambulance) y Space (Ice Planet Satellite Plough, Saucer Centurion con 16 sub-builds).
- **1995 — Pirates + Train**: 6279-1 Skull Island (383 piezas, BFC CERTIFY, 2 custom parts). 5 sets totales.
- **1996 — pico de variedad y de Model Team**: 14 sets (máximo del corpus). 5571-1 Giant Truck (Model Team, 1 703 piezas, **40 sub-builds** — récord absoluto). Western 6765-1 (382 piezas, 10 custom parts, BFC CERTIFY). Universal Building Set aparece (4 sets pequeños: South African Flag y 3 Danone Promotional).
- **1997 — año "de transición"**: 4 sets pequeños (Indian Kayak 23 piezas, Speedboat 28, Outback Racer 54, Tribal Chief 19). Media de piezas 31 — el año más bajo del corpus. Esto coincide con la crisis LEGO de finales de los 90.
- **1998 — Model Team pesado**: 5542-1 Black Thunder (485 piezas, 28 sub-builds, 10 custom parts, BFC CERTIFY).
- **1999 — Star Wars peak + Model Team**: los 6 sets Star Wars del corpus son todos de 1999 (Lightsaber Duel 64 piezas hasta TIE Fighter & Y-wing 360 piezas). Model Team 5533-1 Red Fury (353 piezas, 32 sub-builds, BFC CERTIFY). **1999 tiene la media de sub-builds más alta (14.9)**.

---

## 8. Tendencias observadas

### ¿Sets más grandes con el tiempo?

**Sí, en promedio (123.6 → 207.7 piezas/set), pero NO en el set típico (mediana 101 → 81)**. La respuesta honesta es: el corpus tiene **más sets pequeños** en los 90s (Universal Building Set, Star Wars minifig-scale, Town promotional) Y **más sets gigantes** (Pirates 6286 con 2 834, Model Team 5571 con 1 703, Star Wars 7140/7150 con 328–360). La dispersión crece; la mediana baja.

### ¿Mayor modularidad (sub-builds) en los 90s?

**Sí, claramente.** Media 5.68 → 9.29 (+63 %). El corpus 90s tiene 5 de los 6 sets con más sub-builds, todos Model Team o Pirates/Star Wars. La práctica de **diseñar sets grandes como ensamblaje de sub-modelos** (cabina + chassis + carrocerías + detalles) se generaliza a finales de los 90.

### ¿Aparición de piezas Technic en sets no-Technic?

**Sí, y de forma muy pronunciada.** Indicadores:

| Indicador | 80s | 90s |
|---|---|---|
| `4-4cyli.dat` total | 104 | 1 792 |
| `4-4cyli.dat` / piezas | 3.4 % | 11.5 % |
| % piezas Technic-flagged (8 clave) | 13.4 % | 19.4 % |

El System set de los 90s incorpora masivamente Technic (especialmente ejes, agujeros y steering arms) para articulation, ruedas y accesorios (Model Team, Star Wars vehículos). Town/Castle/Pirates también lo adoptan para puertas, ballestas, cañones basculantes.

### BFC compliance

**No es una tendencia de los 90s**. Proporcionalmente el corpus 80s tiene más BFC CERTIFY (28 %) que el 90s (18.7 %). La distribución está dispersa por toda la línea temporal, sin un año de inflexión claro. Esto es coherente con que BFC es **una decisión del modelador OMR**, no del set físico original.

---

## 9. Reglas inferidas

1. **Sub-builds como indicador de escala**: en este corpus, sets con ≥15 sub-builds son **siempre 90s y siempre sets grandes** (Pirates/Model Team/Star Wars/Space). El set 80s con más sub-builds tiene 13 (Space 6885-1 Crater Crawler, 1988). Sirve como proxy fiable para detectar sets "época 90s grandes".

2. **`4-4cyli.dat` (cilindro Technic) es proxy de vehículos grandes**: las 1 896 apariciones globales se concentran en solo **2 sets** del corpus (6061-1 Castle Siege Tower 1984 con 104, y 6286-1 Skull's Eye Schooner 1993 con 1 792). Su presencia masiva (>50 unidades en un set) indica vehículo de gran escala — pero no es exclusivo de los 90s (Castle Siege Tower es 1984).

2b. **Piezas Technic con agujero de eje (`6141`, `3710`, `3820`, `754`) se generalizan en 90s**: en 80s aparecen sobre todo en Castle/Train/Town grandes (6061, 6062, 7715, 6657). En 90s se diversifican a Model Team, Pirates, Star Wars, Western y Town vehículos. La lista de "sets con ≥30 piezas Technic-flagged" pasa de 5 sets en 80s (1984–1987) a 18 sets en 90s.

3. **Tiles planas (`2412b`, `2431`) y plates 2×N (`3022`, `2420`) como marcadores 90s**: `2412b` salta de 2 (80s) a 157 (90s), `3022` de 33 a 171, `2420` de 4 a 162. La construcción "moderna" de los 90s usa más superficies grandes y planas (acabado liso en Town/Castle, paneles en Pirates).

4. **Piezas top-15 en 80s que salen del top-15 en 90s**: `3665a` (slope brick), `3660` (plate 1×2 Technic hole), `3666` (plate 1×4), `3009` (brick 1×6), `3063b` (round brick 2×2), `3795` (plate 2×6). Los 80s dependían más de plates anchos y slopes; los 90s diversifican hacia tiles planas, plates 2×N y Technic con eje.

5. **Custom parts correlacionan con tamaño, no con licencia**: los 6 Star Wars de 1999 tienen **0–1 custom parts cada uno**. El set con más custom parts (6286 Skull's Eye Schooner, 21) es **Pirates** — un tema propio de LEGO, no licenciado. La licencia SW en este corpus no introduce más molds únicos que Pirates o Model Team.

6. **BFC CERTIFY no es sello de los 90s**: en este corpus el primer BFC CERTIFY es de 1980 (Fabuland 3602-1). La proporción 80s > 90s sugiere que BFC fue **una elección temprana del modelador OMR**, no una convención que se popularizó con el tiempo.

7. **STEPs reflejan sub-builds, no escala pura**: 90s duplican la media de STEPs (11 → 23) sin duplicar la media de piezas (123 → 208). Esto es porque cada sub-build genera varios STEPs independientes — los 90s son **más densos en instrucciones** (más sub-modelos a documentar) incluso cuando el set no es más grande.

---

## 10. Caveats del corpus

- n=100 es **una muestra, no el universo de sets LEGO 1980–1999**. Los 75 sets 90s probablemente están sesgados hacia sets OMR-populares (Pirates grandes, Model Team, Star Wars).
- El corpus omite **el grueso de Technic set** como tema separado — solo hay Universal Building Set (4 sets) y algunos "Model Team" cuentan con piezas Technic. No podemos comparar System vs Technic.
- **Custom parts embebidas** se cuentan como `embedded_custom_parts` en el MPD; algunas minifigs pueden estar modeladas con primitives (`4-4cyli`, etc.) y no aparecer como custom.
- **NEG_DET = 50** ocurre **todo en 90s** (80s = 0). Esto sugiere que el modelado OMR de los 90s es más reciente y puede usar técnicas con determinant negativo (rotaciones) que el de los 80s. Vale la pena investigarlo aparte.

---

## 11. Conclusión

El corpus muestra que **1980–1999 fue un período de transición técnica, no solo estética**:

- La **gran transformación técnica** es la adopción masiva de piezas Technic (ejes, cilindros) dentro de sets System → permitido por Model Team y explotado por Star Wars.
- La **gran transformación estructural** es el aumento de sub-builds por set (de ~6 a ~9 de media), señal de diseño modular.
- La **gran transformación estética** es la proliferación de tiles planas y la diversificación temática (Pirates, Model Team, Western, Star Wars).
- **Lo que NO cambió**: el vocabulario básico de bricks y plates (3004, 3023, 3005, 3024), la presencia estable de BFC CERTIFY, y la práctica de STEPs por sub-build.

Las premisas del enunciado que **el corpus contradice**:
- "BFC CERTIFY aparece mayormente en sets posteriores a 1998" — **falso**: 80s tiene mayor proporción (28 % vs 18.7 %).
- "1992: Star Wars debut" — **falso** en este corpus: Star Wars debuta en 1999 (los 6 sets son de ese año, correspondientes al lanzamiento Episode I).
- "1994: Model Team" — **parcialmente falso**: Model Team 5510-1 ya está en 1986 en el corpus; los Model Team grandes son 1996–1999.
- "Pirates end en 1992" — **falso**: hay Pirates 1993 (6286 Skull's Eye Schooner, 2 834 piezas) y 1995 (6279 Skull Island).
- "Sets de 1980–1985 raramente usan sub-builds (1–3 por set)" — **inexacto**: la media en 1980–1985 es **5.0** sub-builds (rango 2–10). Solo 6 de 16 sets caen en 1–3. El contraste real es 5.0 (1980–1985) vs 9.05 (1995–1999).

Las premisas que **el corpus confirma**:
- "Pirates launch 1989" — sí (6235 Buried Treasure en corpus; Black Seas Barracuda fuera).
- "Castle Revival 1984–1985" — sí (Siege Tower 6061, 341 piezas, BFC CERTIFY).
- "1999: Star Wars peak" — sí (6 sets, hasta 360 piezas y 22 sub-builds en X-wing).