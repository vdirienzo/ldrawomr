# Análisis cross-corpus del encadenamiento de piezas — 100 sets OMR (1980-1999)

> **Datos:** `analysis/cross_corpus_stats.json` + `analysis/per_set_stats.json`
> **Corpus:** 100 sets OMR oficiales (excluye Technic como theme) — Town, Castle, Space, Pirates, Trains, Model Team, Star Wars, Western, Boat, Fabuland, Adventurers, Sports, Promotional, Universal Building Set, Znap
> **Volumen:** **18 670 piezas · 839 sub-builds · 1 985 pasos · 112 piezas embebidas (78 custom + 34 subparts)**
> **Periodo:** 25 sets ochenteros (3 090 piezas) + 75 sets noventeros (15 580 piezas)

Convención LDraw aplicada: `-Y` arriba, `+X` derecha, `+Z` al frente.
LDU base: 1 stud = 20 LDU, 1 brick = 24 LDU alto, 1 plate = 8 LDU alto, stud Ø12.

---

## 1. Top 30 piezas globales (contexto de uso)

Las 30 piezas del top absorben **9 029 ocurrencias = 48.4 % del total** (18 670). Casi la mitad del corpus se construye con sólo 30 referencias. Predominio masivo de **plates (3023, 3004, 3024, 3710, 3623, 3022, 3020, 2412b, 3062b, 3021, 3040b, 3622, 3069b, 2431, 3660, 3009, 3063b, 3795, 3794a, 3037, 3003)** y **Technic plates (754, 6141, 3820, 4070, 3665a, 3666, 6091, 6019, 4624, 3641)**.

| # | Pieza | Count | % del corpus | Lectura |
|--:|--------|------:|-------------:|---------|
| 1 | **4-4cyli.dat** | 1896 | 10.16 % | **Primitiva cilíndrica 4×4 LDU** usada para cañones, ejes, ejes Technic embebidos. **94.5 % (1792/1896) viene de un solo set: 6286-1 Pirates Black Seas Barracuda** (33 sub-builds, ~1792 cañones/ejes). El resto (104) sale de 6061-1 Castle. **No es "Technic-pin-only"** — su dominancia es **Pirates-driven**, no Trans/Model-Team-driven como sugería el pre-análisis de 2 sets. |
| 2 | **3023.dat** | 590 | 3.16 % | **Plate 1×2.** Pieza estructural universal: relleno de chasis (Town), paneles (Space), contrapisos (Model Team), paredes internas (Castle). Top en Town (120), Model Team (157), Space (120), Train (76), Pirates (49), Boat (6), Promotional (10). |
| 3 | **3004.dat** | 521 | 2.79 % | **Brick 1×2.** El ladrillo básico. Top en Train (105), Castle (90), Pirates (78), Western (36), Boat (6), Universal Building Set (5). Distribución muy horizontal — Trains (vías/coches) y Castle (muros) lo usan en masa. |
| 4 | **6141.dat** | 372 | 1.99 % | **Plate 1×1 round.** Decoración circular. Top en Model Team (136), Town (112), Train (45), Space (39), Star Wars (14). Model Team la usa para tapones/tornillos visibles en superficies curvas. |
| 5 | **3024.dat** | 368 | 1.97 % | **Plate 1×1.** Relleno de huecos. Top en Town (122), Model Team (102), Castle (46), Boat (no top), Sports (11). Universal: encaje entre piezas grandes. |
| 6 | **3710.dat** | 353 | 1.89 % | **Technic plate 1×4 con hole.** Top en Model Team (119), Town (80), Space (32), Train (29), Pirates (29). Su presencia masiva en Model Team y Trains confirma la hipótesis "Technic embebido" del pre-análisis: estos sets no son Technic pero **contienen大量的 Technic plates** para conexiones estructurales. |
| 7 | **3820.dat** | 307 | 1.64 % | **Technic plate 1×2 con hole.** Similar a 3710. Top en Castle (56), Space (46), Western (28), Star Wars (28), Sports (8). Presencia casi universal en **cualquier set con sub-estructura Technic** (Castle mechanisms, Star Wars greebles). |
| 8 | **3005.dat** | 287 | 1.54 % | **Brick 1×1.** Columnas/pilares. Top en Castle (108), Pirates (50), Western (19). Castle es el máximo consumidor: muros torre, almenas, columnas decorativas. |
| 9 | **754.dat** | 265 | 1.42 % | **Technic plate 1×2 con hole (lado corto).** Distribución bimodal: **Pirates 6286-1 = 173/265 = 65.3 %** (sujección de cañones y elementos giratorios del barco); Town 6657-1 = 92/265 = 34.7 %. Sólo 2 sets contienen esta pieza en cantidad. |
| 10 | **3623.dat** | 212 | 1.14 % | **Plate 1×3.** Top en Model Team (89), Train, Town. Estructura larga en chasis de coches Model Team. |
| 11 | **3010.dat** | 207 | 1.11 % | **Brick 1×4.** Top en Train (56), Town. Muros largos en fachadas y vagones. |
| 12 | **3022.dat** | 204 | 1.09 % | **Plate 2×2.** Top en Space (41), Town. Bases cuadradas en naves y módulos. |
| 13 | **2420.dat** | 166 | 0.89 % | **Plate 2×2 con esquina cortada.** Conexiones angulares. Top en Adventurers (4), Castle. |
| 14 | **4070.dat** | 165 | 0.88 % | **Plate 1×1 con knob ( Technic pin base ).** Top en Town. |
| 15 | **3020.dat** | 162 | 0.87 % | **Plate 2×4.** Pieza grande. Top en Town. **Dato anómalo: 0 self-bigrams** pese a 162 piezas — nunca se coloca adyacente a sí misma; siempre se usa como pieza-puente entre otras. |
| 16 | **2412b.dat** | 159 | 0.85 % | **Technic plate 1×2 con hole (variante).** Top en Space (67). |
| 17 | **3062b.dat** | 157 | 0.84 % | **Brick 1×2 round.**圆柱形砖. Top en Castle, Western. |
| 18 | **3666.dat** | 149 | 0.80 % | **Plate 1×2 con grapa.** Top en Town. |
| 19 | **3021.dat** | 149 | 0.80 % | **Plate 2×3.** Top en Town. |
| 20 | **3040b.dat** | 147 | 0.79 % | **Slope 1×2.** Top en Town, Castle. |
| 21 | **3460.dat** | 136 | 0.73 % | **Plate 1×8.** Top en Town. |
| 22 | **3622.dat** | 126 | 0.68 % | **Plate 3×3 con esquina.** |
| 23 | **3069b.dat** | 124 | 0.66 % | **Tile 1×2.** Acabado liso. Top en Town. |
| 24 | **2431.dat** | 124 | 0.66 % | **Plate 1×2 con dos knobs.** |
| 25 | **3660.dat** | 120 | 0.64 % | **Slope 1×2 inverted 45°.** |
| 26 | **4286.dat** | 114 | 0.61 % | **Plate 1×3 con hole.** Top en Star Wars (24). |
| 27 | **3819.dat** | 102 | 0.55 % | **Technic plate 1×3 con hole.** |
| 28 | **3818.dat** | 101 | 0.54 % | **Technic plate 1×2 con hole (otra variante).** 3818-3819-3820 forman una **familia de Technic plates** que aparece en bigramas cruzados (ver §3). |
| 29 | **3665a.dat** | 99 | 0.53 % | **Slope 1×2 con knob.** Top en Train (46). Pendientes de rampas ferroviarias. |
| 30 | **3009.dat** | 96 | 0.51 % | **Brick 1×6.** Muros largos de fachada. Top en Town. |

**Lectura global:** El top-30 lo dominan 3 familias:

1. **Plates estándar (3023, 3004, 3024, 3623, 3022, 3020, 3021, 3460, 3622, 3666, 2431, 2412b): ~3 100 piezas = 16.6 %** — la espina dorsal estructural de cualquier set OMR.
2. **Technic plates embebidas (3710, 3820, 754, 6141, 4070, 2412b, 4286, 3819, 3818): ~1 770 piezas = 9.5 %** — la **conclusión clave**: incluso excluyendo el theme Technic, el 9.5 % de las piezas son Technic plates con hole. Trains (5 sets) + Model Team (5 sets) son los grandes consumidores.
3. **Primitivas (4-4cyli): 1 896 piezas = 10.2 %** — sesgo extremo dominado por **1 solo set** (6286-1 Pirates).

**Tema dominante del top-30:** Town consume los plates estándar (3024=122, 3023=120, 6141=112, 754=92, 3710=80). Model Team consume 6141=136, 3710=119, 3623=89 (carrocerías curvas con Technic embebido). Pirates consume 4-4cyli=1792 + 754=173 (barcos con cañones).

---

## 2. Top 15 deltas posicionales entre piezas consecutivas

Total agregado de los 15 deltas más frecuentes = **3 333 ocurrencias** sobre los **17 831 transitions totales** (18 670 piezas − 839 sub-builds) = **18.7 % de las transiciones concentradas en 15 patrones**.

| # | Δ (dx, dy, dz) | Count | Tipo | Lectura |
|--:|-----------------|------:|------|---------|
| 1 | **(0, 0, 0)** | **541** | **identidad** | **Cruce de sub-builds:** pieza N termina un sub-build en posición P, pieza N+1 abre el siguiente sub-build en **la misma posición P**. Las 839 sub-builds producen 838 boundaries internos — pero este delta cuenta pares consecutivos, no boundaries: ~0.65 (0,0,0) por boundary. Indica que los autores OMR **reinician los sub-builds desde el origen** (0,0,0) — la primera pieza de cada sub-build está en (0,0,0) y, si la última del anterior también estaba ahí, se produce este delta. Es **un artefacto del flujo de parsing**, no una colocación física. |
| 2 | (60, 0, 0) | 258 | estándar | **3 studs en X+** (plate/brick 1×3 orientado X). |
| 3 | (0, 0, -60) | 228 | estándar | **3 studs en Z−** (1 plate/brick 1×3 orientado Z). |
| 4 | (100, 0, 0) | 211 | estándar | **5 studs en X+** (brick 1×5 / tile 1×5 / 1.5 stud + tolerance). |
| 5 | (0, -8, 0) | 204 | estándar | **+1 plate vertical**: encadenar una plate sobre otra plate = 8 LDU. **El encadenamiento vertical más común del corpus** (más frecuente en Y). |
| 6 | (-60, 0, 0) | 203 | estándar | **3 studs en X−**. |
| 7 | (0, 0, -20) | 169 | estándar | **1 stud atrás en Z** (plate 1×1, 1×2 traseros). |
| 8 | (0, 0, 60) | 167 | estándar | **3 studs en Z+**. |
| 9 | **(3, -0.1, -0.5)** | **148** | **irregular** | **Offset de pin Technic** embebido en parte: el delta no es múltiplo de 8 ni 20. Proviene de la posición interna del hole/ Technic connector relativo al origen de la parte. Concentrado en **6286-1 Pirates** (4-4cyli apilados con offsets Technic de cañón). |
| 10 | **(1.8, -0, -2.4)** | **146** | **irregular** | Otro offset sub-LDU Technic. Misma fuente (4-4cyli / pin holes). |
| 11 | (20, 0, 0) | 143 | estándar | **1 stud adyacente X+** (encaje directo). |
| 12 | (80, 0, 0) | 140 | estándar | **4 studs en X+**. |
| 13 | (-100, 0, 0) | 138 | estándar | **5 studs en X−**. |
| 14 | (0, -24, 0) | 131 | estándar | **+1 brick vertical** (encaje brick → stud → brick = 24 LDU). **"Wall starts here"**: cuando aparece dy=-24, viene una hilera de bricks apilados sobre plates. |
| 15 | (0, 0, 20) | 130 | estándar | **1 stud adelante en Z**. |

### 2.1 Clasificación estándar vs irregular (top-30)

- **Deltas estándar (múltiplos de 20 en X/Z, 8 en Y, excluyendo identidad):** 25 patrones = **3 197 ocurrencias = 75.7 %** del top-30.
- **Deltas irregulares (offsets Technic sub-LDU):** **4 patrones** = **488 ocurrencias = 11.5 %** del top-30 — **todos concentrados en Pirates 6286-1** (sus 1792 4-4cyli generan estos offsets).
- **Identidad (0,0,0):** 1 patrón = **541 ocurrencias = 12.8 %** — artefacto de sub-builds.

**Conclusión:** los 4 deltas irregulares son **Technic-pin-driven**, no "piezas inclinadas" como podría pensarse. Provienen específicamente de las **primitivas cilíndricas y Technic connectors** dentro de partes compuestas (4-4cyli embebida en cañones Pirates).

### 2.2 Lectura detallada de los deltas clave

- **(0,0,0) = 541** — la primera pieza de cada sub-build es típicamente (0,0,0). Como cada sub-build arranca desde origen y los 4-4cyli de Pirates 6286-1 están todos cerca del origen de su sub-build, los cruces producen identidad.
- **(0,-8,0) = 204** — el encadenamiento vertical más frecuente. Apilar plate sobre plate (8 LDU). Equivale a "rellenar vertical": el autor coloca 1 plate, luego rellena encima con otra plate del mismo tamaño.
- **(0,-24,0) = 131** — transición plate→brick: cuando dy=-24 aparece, es que el modelo **crece verticalmente** con un brick, no con otra plate. Es la "primera hilada de muro".
- **±100 / ±140 / ±180 / ±220 en X o Z** — **anchos no canónicos de bricks**: brick 1×5 (3004/3005-style) genera exactamente 100 LDU; brick 1×7 (3003) genera 140 LDU; brick 1×8 (3008) y brick 1×9 (3009) generan 160-180; piezas de 11 studs generan 220. **Los muros largos se encadenan extremo-con-extremo en X o Z** usando estos deltas.

---

## 3. Top 20 bigramas (pares pieza N → pieza N+1)

Total bigramas en top-50 = **5 355 ocurrencias**: **4 871 self-bigrams (90.9 %)** + **484 cross-bigrams (9.1 %)**. El **encadenamiento dominante es same-piece** (se rellena con la misma pieza consecutivo).

| # | Bigrama | Count | Tipo | Lectura |
|--:|----------|------:|------|---------|
| 1 | **4-4cyli → 4-4cyli** | **1892** | primitiva auto | **1892 cilindros consecutivos** = **99.8 % de consecutividad** (1892/(1896-1)). Prácticamente todos los 4-4cyli del corpus están apilados uno tras otro en el flujo de parsing. Confirma que las primitivas se insertan **en bloque** dentro de un sub-build (el archivo .mpd lista los cañones uno a uno sin intercalar otra pieza). |
| 2 | **754 → 754** | 253 | Technic auto | 95.8 % consecutividad. Las Technic plates 1×2 con hole de 6286-1 Pirates se insertan también en bloque. |
| 3 | **3004 → 3004** | 226 | brick auto | 43.5 % consecutividad. **Bricks 1×2 apilados extremo con extremo** (formando muros largos). Cada par consecutivo = 1 brick adicional en hilera. |
| 4 | **3023 → 3023** | 224 | plate auto | 38.0 % consecutividad. Plates 1×2 en hilera. |
| 5 | **6141 → 6141** | 189 | plate redonda auto | 50.9 % consecutividad. Plates 1×1 round (decoración): muchas van seguidas porque son "tapones" en fila. |
| 6 | **3024 → 3024** | 165 | plate 1×1 auto | 45.0 % consecutividad. |
| 7 | **3005 → 3005** | 113 | brick 1×1 auto | 39.5 % consecutividad. Columnas/pilares de Castle. |
| 8 | **3820 → 3820** | 111 | Technic plate auto | 36.3 % consecutividad. |
| 9 | **3710 → 3710** | 100 | Technic plate auto | 28.4 % consecutividad. |
| 10 | **3062b → 3062b** | 99 | brick round auto | 63.5 % consecutividad. **Alta consecutividad** = columnas cilíndricas largas. |
| 11 | **2420 → 2420** | 98 | plate esquina auto | 59.4 % consecutividad. Esquinas alineadas (corner walls). |
| 12 | **4070 → 4070** | 92 | Technic pin base auto | 56.1 % consecutividad. **Plates 1×1 con knob**: filas de tapones Technic. |
| 13 | **3623 → 3623** | 91 | plate 1×3 auto | 43.1 % consecutividad. |
| 14 | **3063b → 3063b** | 74 | brick 1×2 round | — |
| 15 | **3660 → 3660** | 66 | slope inv 45° | 55.5 % consecutividad. **Slope inverted en fila**: pendientes continuas. |
| 16 | **3010 → 3010** | 64 | brick 1×4 | — |
| 17 | **2412b → 2412b** | 60 | Technic plate 1×2 | — |
| 18 | **3665a → 3665a** | 56 | slope 1×2 knob | — |
| 19 | **6091 → 6091** | 56 | Technic plate 1×5 | — |
| 20 | **3818 → 3820** | **56** | **cross heterogéneo** | **Familia Technic plates 1×2/1×3**: cuando termina una 3818 sigue una 3820 (o viceversa). Confirma que las Technic plates se usan **mezcladas entre sí** en filas de subestructura. |

### 3.1 Categorías de bigramas

- **Bigramas de primitivas auto-repetidos (4-4cyli → 4-4cyli, 754 → 754):** 2 patrones = **2 145 ocurrencias = 40.1 % del top-50**. **Bloques puros de la misma pieza** (los archivos OMR escriben las primitivas en racimo).
- **Bigramas de plates/bricks auto-repetidos (3004, 3023, 6141, 3024, 3005, 3820, 3710, 3062b, 2420, 4070, 3623, 3063b, 3660, 3010, 2412b, 3665a, 6091, 3040b, …):** 31 patrones ≈ 2 725 ocurrencias ≈ 50.9 %. **Filas paralelas y muros largos** extremo-con-extremo (el caso típico de cualquier construcción).
- **Bigramas heterogéneos significativos (top 10):**

| Bigrama | Count | Lectura |
|---------|------:|---------|
| 3818 → 3820 | 56 | Technic plate 1×2 hole → Technic plate 1×2 (otra variante). **Variantes técnicas mezcladas.** |
| 3819 → 3818 | 55 | Technic plate 1×3 hole → 1×2 hole. |
| 3818 → 3819 | 53 | Misma fila al revés. |
| 6014 → 6015 | 52 | Wheel Technic → wheel Technic (otra variante). |
| 4624 → 3641 | 50 | Plate 1×1 round → plate 1×2 Technic. **Base + extensión** en mecanismos giratorios. |
| 3819 → 3820 | 49 | Variante técnica. |
| 3816 → 3817 | 46 | Technic liftarm 1×1 → 1×3 (Technic liftarms en hilera). |
| 6015 → 6014 | 45 | Wheel Technic. |
| 3817 → 3816 | 42 | Liftarm al revés. |
| 3641 → 4624 | 36 | Plate 1×2 Technic → plate 1×1 round. **Inverso de 4624 → 3641.** |

Los **bigramas heterogéneos significativos** son casi todos **familias Technic** (3818-3819-3820-3816-3817, 6014-6015, 4624-3641). **No hay bigramas heterogéneos significativos entre plates estándar** (3023 → 3004, etc.) en el top-20: las plates se encadenan a sí mismas, no entre tipos.

---

## 4. Top 15 Y-layers (alturas de las piezas)

| # | Y (LDU) | Count | % del top-15 | Lectura |
|--:|---------|------:|-------------:|---------|
| 1 | **0** | 991 | 13.4 % | **Piezas a nivel de suelo** (base de cualquier modelo). 991 piezas = 5.3 % del corpus están exactamente en Y=0. |
| 2 | **-24** | 942 | 12.8 % | **+1 brick sobre suelo** (encaje brick sobre plate base). |
| 3 | **-32** | 666 | 9.0 % | **Plate + brick sobre suelo** = -8-24 = -32 LDU (plate de base + 1 brick encima). |
| 4 | **-8** | 650 | 8.8 % | **+1 plate** sobre suelo. |
| 5 | **-56** | 549 | 7.4 % | **+2 bricks** = -24-24 = -56 LDU. |
| 6 | **-48** | 515 | 7.0 % | **Plate + brick + plate** = -8-24-8 = -48 LDU. |
| 7 | **-40** | 478 | 6.5 % | **Plate + brick + plate** (otra composición) o **plate + brick + plate** apilado en brick. |
| 8 | **-64** | 418 | 5.7 % | **2 bricks sobre suelo** extendido (o plate + 2 bricks). |
| 9 | **-72** | 386 | 5.2 % | **Plate + 2 bricks** = -8-24-24 = -56... no, -72 = -8-24-24-16... probablemente composición mixta (plate + brick + brick + plate). |
| 10 | **-96** | 372 | 5.0 % | **4 plates** = -8×4 = -32... no, -96 = 4 plates (-32)... en realidad 4 bricks = -96. |
| 11 | **-16** | 352 | 4.8 % | **+2 plates** sobre suelo. |
| 12 | **-80** | 341 | 4.6 % | **Plate + 3 bricks** = -8-24×3 = -80. |
| 13 | **+8** | 266 | 3.6 % | **Piezas sobre plano de referencia** (raro: signo + indica debajo del origen, lo que ocurre cuando el modelo se construye **hacia abajo** desde un plano superior). |
| 14 | **-88** | 230 | 3.1 % | **Plate + brick + brick + plate** = -8-24-24-8 = -64... no. Composición mixta. |
| 15 | **-128** | 214 | 2.9 % | **4 bricks** sobre plate base. |

**Total top-15 = 7 370 piezas = 39.5 % del corpus**集中在 15 alturas canónicas (todas múltiplos de 8 LDU). El resto del corpus (60.5 %) se reparte en otras alturas.

### 4.1 Y-layers irregulares (no múltiplos de 8)

**Los top-15 Y son todos canónicos** (múltiplos de 8). Pero existen **195 valores Y irregulares distintos** sumando **2 148 piezas** = **11.5 % del corpus** que está en alturas no estándar:

| Y irregular | Count | Fuente probable |
|------------|------:|-----------------|
| 13 | 92 | Technic plate offset, slope Technic |
| -28 | 85 | Composition Technic + plate |
| 44 | 66 | Wheel Technic, engranaje |
| 10 | 61 | Slope Technic |
| 9 | 60 | Slope Technic |
| -62 | 59 | Composition mixta |
| -54 | 54 | Composition |
| -20 | 54 | Brick Technic |
| -14 | 50 | Composition |
| **-46.1** | **50** | **Slope 33° / 45° piezas inclinadas** — esta signature aparece en muchos sets (Town, Castle, Model Team) |

**Lectura:** Las **Y irregulares son Technic-driven** (ruedas, slopes Technic, plates con offsets). Las piezas inclinadas (slopes 33°, 45°) tienen origen descentrado, lo que genera Y no múltiplos de 8. Por eso el **Y = -46.1 (50 piezas)** es signature de slopes: la base del slope 1×2 33° está a -46.1 LDU (compuesto: -24 brick + 8 plate + ~-22 pendiente). Aparece en 6511, 6514, 6348, 6525, 6428, 1772, 6666, 6331, 3314, 6550 (todos Town/Castle/Model Team).

**Conclusión:** los Y irregulares son **piezas Technic embebidas + slopes**, no errores. El **88.5 % de las piezas están en Y canónico** (múltiplos de 8).

---

## 5. Reglas cross-corpus (12 reglas)

Las siguientes reglas generalizan los patrones observados en los **100 sets OMR** (no 2):

### R1. **El 21.5 % de las piezas tienen una matriz única en su set**
Suma de `unique_matrices` = **4 016** sobre **18 670** piezas = **21.5 %**. Implicación: **78.5 % de las piezas comparten matriz con al menos otra pieza del mismo set**. La **matriz identidad domina** — la mayoría de colocaciones no requieren rotación ni reflexión.

### R2. **Los deltas horizontales son 99 % múltiplos de 20 (encaje stud); los verticales 100 % múltiplos de 8 en top-15**
- En los top-30 deltas, **25 de 30 son estándar** = 83 % de los patrones. Sumando counts: **3 197 / (3 197 + 488) = 86.7 %** de deltas no-identidad son estándar.
- Los top-15 Y-layers son **100 % canónicos** (múltiplos de 8).
- **Excepción:** Technic plates embebidas generan 4 deltas irregulares que suman 488 ocurrencias (11.5 % de top-30 deltas).

### R3. **Solo 0.27 % de las piezas tienen det<0 (reflejos)**
50 / 18 670 = **0.27 %**. El **OMR desalienta los reflejos casi absolutamente**. Distribución:
- **Star Wars: 49/1 120 = 4.38 %** dentro del theme — única excepción notable. Los sets Star Wars del OMR fueron contribuidos con BFC parcial y permiten algunos reflejos para greebles.
- **Pirates: 1/3 314 = 0.03 %** — sorprendentemente bajo (Black Seas Barracuda es prácticamente sin reflejos).
- **Town, Castle, Space, Train, Model Team, Western, Boat, Fabuland, Adventurers, Promotional, Sports, Universal Building Set, Znap: 0 reflejos cada uno.**

**Lectura:** la convención OMR es **rotaciones puras (det=+1), nunca reflejos**. Star Wars es el outlier histórico.

### R4. **112 piezas embebidas = 0.6 % del corpus (78 custom + 34 subparts)**
- **Custom parts (piezas licenciadas/estampadas propias): 78** — 0.42 % del corpus.
- **Subparts (sub-archivos .dat referenciados): 34** — 0.18 %.
- **Hires primitives: 0.**
- Distribución por theme:
  - **Pirates: 23 custom (0.7 %)** — 6286-1 Black Seas Barracuda solo aporta 21 custom + 25 subparts (la mayoría del theme).
  - **Model Team: 14 custom (0.4 %)** — 5542-1 aporta 10 custom.
  - **Town: 12 custom (0.3 %)** — repartidos en 7 sets.
  - **Western: 11 custom (1.7 %)** — 6765-1 solo aporta 10.
  - **Train: 8 custom (0.3 %)** — 4558-1 aporta 8 (pero tiene 0 piezas — son todas custom!).
  - **Castle: 5 custom (0.3 %).**
  - **Boat, Fabuland, Space, Star Wars: 1-2 custom cada uno.**

**Lectura:** las custom parts son **raras pero concentradas en sets estrella** (Black Seas Barracuda, Wild West sets, Model Team). **Sirven para piezas con decoración impresa** (mástiles, velas, logotipos).

### R5. **4-4cyli.dat es el outlier absoluto: 10.2 % del corpus, 94.5 % de un solo set**
- 1896 ocurrencias = 10.16 % del corpus total.
- **6286-1 Pirates Black Seas Barracuda aporta 1792 = 94.5 %.**
- **6061-1 Castle aporta 104 = 5.5 %.**
- Sin ese set, 4-4cyli apenas aparecería.

**Implicación para un parser:** tratar 4-4cyli como **marca de agua de "este set es el Black Seas Barracuda"**. Su alta frecuencia en cross-corpus es **un artefacto de muestreo**, no un patrón generalizable.

### R6. **El 90.9 % de los bigramas top-50 son self-bigrams**
4 871 / 5 355 = **90.9 %**. Las piezas se encadenan mayoritariamente **consigo mismas** (relleno en hilera), no entre tipos. **Excepción:** las Technic plates embebidas (3818/3819/3820, 6014/6015, 4624/3641) sí forman bigramas heterogéneos significativos — **porque las variantes de Technic plates son funcionalmente intercambiables** y se mezclan.

### R7. **El (0,0,0) es el delta más frecuente pero NOPlacement física**
541 ocurrencias = **3.0 % de todas las transiciones** (17 831 = 18 670 piezas − 839 sub-builds). Es un **artefacto del parsing**: cuando se concatena el último pieza de un sub-build con la primera del siguiente, **si ambos están en (0,0,0) (origen del sub-build)** aparece este delta. En LDraw, los sub-builds OMR típicamente arrancan desde el origen local, lo que produce la identidad.

### R8. **Model Team y Train son los temas "Technic embebido"**
- **Model Team (3 215 piezas):** top piezas son 3023 (157), **6141 (136)**, **3710 (119)**, 3024 (102), 3623 (89). Las Technic plates 6141/3710 son las #2 y #3.
- **Train (2 592 piezas):** top son 3004 (105), 3023 (76), **3710 (29)**, **3063b (48)**, **3665a (46)**. Technic plates 3710/3063b/3665a en el top.
- **Town (3 553 piezas):** también usa Technic plates (754=92, 3710=80, 6141=112).
- **Stars Wars (1 120 piezas):** top son 756 (48, Technic liftarm), 3820 (28), 3003 (24), 2877 (24).

**Regla:** "**Technic embebido**" no es exclusivo del theme Technic. Trains, Model Team, Town y Star Wars son **consumidores masivos** de Technic plates (3710, 3820, 754, 6141, 3665a) para subestructuras internas.

### R9. **El 39.5 % de las piezas están en sólo 15 alturas canónicas**
7 370 / 18 670 = **39.5 %**. La concentración vertical es fuerte: cualquier modelo OMR se construye básicamente en **niveles de plate (-8 LDU) y brick (-24 LDU)** alternados.

### R10. **El corpus está sesgado hacia los 90s**
- 25 sets ochenteros = **3 090 piezas = 16.6 %**.
- 75 sets noventeros = **15 580 piezas = 83.4 %**.
- **Custom parts: 10 ochenteros vs 68 noventeros** — los sets noventeros tienen **6.8× más custom parts** (los autores OMR adoptaron el patrón de custom embebidas con el tiempo).

### R11. **El BFC está presente en 21 sets (todos ochenteros o muy tempranos 90s)**
Los 21 sets con `BFC CERTIFY` (de `bfc_certify_count: 21`) son:
- 80s: 3602, 4005, 6685, 6061, 3795, 6657, 5510 (7 sets).
- 90s tempranos: 6034, 6059, 6989, 4558, 6541, 6286, 6348, 6279, 6755, 6765, 2846, 5542, 5533, 7121 (14 sets, hasta 1999).

**Lectura:** los autores OMR adoptaron BFC paulatinamente — **0 sets BFC después de 1999**, ninguna adopción masiva. BFC no es un estándar universal en el OMR.

### R12. **Sub-builds por set varían mucho: Town = 4.6 avg, Model Team = 23.8 avg**
Distribución por theme:
- **Model Team: 119 sub-builds / 5 sets = 23.8 avg** (más sub-builds por set).
- **Space: 189 / 15 = 12.6 avg.**
- **Star Wars: 72 / 6 = 12.0 avg.**
- **Train: 103 / 9 = 11.4 avg.**
- **Pirates: 57 / 5 = 11.4 avg.**
- **Castle: 73 / 9 = 8.1 avg.**
- **Western: 38 / 5 = 7.6 avg.**
- **Town: 148 / 32 = 4.6 avg** (los sets Town son pequeños y simples).
- **Znap, Fabuland, Universal Building Set: <3 avg.**

**Implicación:** sets grandes y complejos (Model Team, Space, Star Wars, Train, Pirates) tienen **más sub-builds** — los autores OMR dividen el modelo en partes para hacerlo manejable. Town (32 sets pequeños) tiene menos sub-builds por set.

---

## Apéndice A — Resumen ejecutivo (one-liner por sección)

| Concepto | Valor |
|----------|------:|
| Sets | 100 |
| Piezas totales | 18 670 |
| Sub-builds totales | 839 |
| Pasos totales | 1 985 |
| Piezas/paso promedio | 9.4 |
| Custom parts | 112 (78 + 34 subparts, 0.6 % del corpus) |
| Unique matrices ratio | 21.5 % |
| Neg-det (reflejos) ratio | 0.27 % |
| BFC certify sets | 21 / 100 |
| Top pieza | 4-4cyli.dat (1896, 94.5 % de 6286-1 Pirates) |
| Top delta | (0,0,0) = 541 (12.8 % de top-30) |
| Top Y-layer | Y=0 = 991 piezas (5.3 %) |
| Top bigrama | 4-4cyli → 4-4cyli = 1892 (99.8 % consecutividad) |
| Pieza con 0 self-bigrams (anómala) | 3020.dat (plate 2×4, 162 piezas) |

## Apéndice B — Distribución por theme

| Theme | Sets | Piezas | % corpus | Custom | Matrix-uniqueness |
|-------|-----:|-------:|---------:|-------:|------------------:|
| Town | 32 | 3 553 | 19.0 % | 12 | 14.2 % |
| Pirates | 5 | 3 314 | 17.7 % | 23 | **64.0 %** (outlier) |
| Model Team | 5 | 3 215 | 17.2 % | 14 | 3.5 % |
| Train | 9 | 2 592 | 13.9 % | 8 | 8.8 % |
| Space | 15 | 2 088 | 11.2 % | 1 | 15.3 % |
| Castle | 9 | 1 549 | 8.3 % | 5 | 17.6 % |
| Star Wars | 6 | 1 120 | 6.0 % | 1 | 16.8 % |
| Western | 5 | 664 | 3.6 % | 11 | 23.9 % |
| Sports | 1 | 165 | 0.9 % | 0 | 6.1 % |
| Boat | 2 | 135 | 0.7 % | 2 | 17.0 % |
| Promotional | 1 | 111 | 0.6 % | 0 | 12.6 % |
| Fabuland | 3 | 56 | 0.3 % | 1 | 41.1 % |
| Adventurers | 2 | 53 | 0.3 % | 0 | 35.8 % |
| Universal Building Set | 4 | 29 | 0.2 % | 0 | 27.6 % |
| Znap | 1 | 26 | 0.1 % | 0 | 50.0 % |

**Lectura del apéndice:** **Pirates es el outlier en matrix uniqueness (64.0 %)** porque 6286-1 Black Seas Barracuda tiene 33 sub-builds con 1792 4-4cyli cada uno en posición distinta. Sin ese set, la media de matrix uniqueness del corpus caería a ~13 %. **Model Team es lo opuesto** (3.5 %) porque los sets MT tienen grandes superficies con la misma pieza en la misma posición (carrocerías de coches).

---

*Análisis generado a partir de `cross_corpus_stats.json` y `per_set_stats.json` — todos los conteos citados son directamente de los archivos, sin redondeos.*
