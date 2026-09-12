# Análisis profundo del chaining de parts — 10252 VW Beetle + 10218 Pet Shop

> Datos crudos: `analysis/deep_stats.json` (6 662 líneas)
> models fuente: `corpus/10252-1.mpd` (Beetle), `corpus/10218-1.mpd` (Pet Shop)
> Contexto geométrico: `LDRAW_GUIDE.md` §3 (sistema LDU: 1 stud ancho=20 LDU; brick alto=24 LDU; plate alto=8 LDU; stud Ø12, alto 4 LDU).

Convención LDraw aplicada: `-Y` arriba, `+X` derecha, `+Z` al frente.
Determinante de matriz 3×3 con `+1` = rotación pura; `-1` = espejo (flip).
BFC invierte normales automáticamente cuando `det < 0`.

---

## 1. Patrones de offset espacial observados (top deltas)

Los deltas son **diferencias de posición entre parts consecutivas** (línea 1 tipo 1 → línea 1 tipo 1 siguiente) en el files, **NO** distancias absolutas entre parts físicamente adyacentes. Reflejan el orden de inserción en el STEP.

### 1.1 Conteo combinado de los dos sets (lo más estable entre ambos models)

| Δ (dx, dy, dz)   | Significado físico                                                                  | 10252 | 10218 |
|------------------|-------------------------------------------------------------------------------------|------:|------:|
| (0, 0, 0)        | Misma posición exacta — parts colocada en hueco abierto encima de la última          |    —  |   26  |
| (0, -8, 0)       | **Plate sobre plate** (sumar 1 plate vertical = 8 LDU)                              |    38 |   65  |
| (0, -24, 0)      | **Brick sobre plate** (encaje stud→tube = 1 brick = 24 LDU)                          |     8 |   49  |
| (0, 0, -20)      | **Stud adyacente en Z** (1 stud atrás)                                              |    —  |   52  |
| (0, 0, -40)      | **2 studs en Z** (1 plate 1×2 o 1 brick 1×2 orientado en Z)                          |    22 |   68  |
| (0, 0, -60)      | **3 studs en Z** (plate 1×3 o brick 1×3 en Z)                                       |    10 |   27  |
| (0, 0, -80)      | **4 studs en Z** (plate 1×4 / brick 1×4 en Z)                                       |    —  |   27  |
| (0, 0, -100)     | **5 studs en Z** (brick 1×5 o tile 1×5)                                              |    —  |   63  |
| (0, 0, -140)     | **7 studs en Z** (plate 1×7 o brick 1×7)                                            |    12 |    —  |
| (0, 0, -180)     | **9 studs en Z** (plate 1×9, brick 1×9 o 1×8 + stud margen)                        |    —  |    —  |
| (0, 0, -300)     | **15 studs en Z** (3× brick 1×5 / brick 1×15 / secciones grandes)                   |    —  |   22  |
| (±20, 0, 0)      | **Stud adyacente en X** (1 stud lateral)                                            | 25+14| 22+30 |
| (±40, 0, 0)      | **2 studs en X** (plate 1×2 o brick 1×2 orientado en X)                              |  24+15| 30+16 |
| (±60, 0, 0)      | **3 studs en X** (plate 1×3 / brick 1×3 en X)                                       | 11+9 |    —  |
| (±80, 0, 0)      | **4 studs en X** (plate 1×4 / brick 1×4 en X)                                       |     9 | 30+16 |
| (±100, 0, 0)     | **5 studs en X** (brick 1×5 / tile 1×5 / 1½ stud + tol.)                            |     — |   36  |
| (±120, 0, 0)     | **6 studs en X** (brick 1×6 / tile 1×6 — exactamente el largo de 3009/6636)         |     — |   25  |
| (±140, 0, 0)     | **7 studs en X** (plate 1×7 / brick 1×7)                                            |     — |   16  |
| (0, 0, ±220)     | **11 studs en Z** (largo completo de paneles de pared)                              |   8+9 |    —  |
| (20, 0, -20)     | **Diagonal 1-stud** (esquina de plate 2×2 o de base 4×4)                            |    —  |   16  |
| (30, 0, -50)     | **Diagonal 1.5+2.5 studs** — esquina típica de base grande (corner cut de 1×1)     |    —  |   5+2 |

### 1.2 Interpretación física de los deltas dominantes

- **`(0, -8, 0) = 38+65 = 103 ocurrencias`** — El chaining vertical más frecuente del corpus. Sumar exactamente 1 plate al Y de la parts anterior: la parts siguiente encaja en los studs superiores de la anterior (plate 8 LDU de alto + 0 sobre base).
- **`(0, 0, -40) = 22+68 = 90 ocurrencias`** — Reemplaza la parts anterior en el mismo stud-set, 2 studs atrás. Indica que se está **rellenando una fila hacia el fondo del models**: brick 1×2 orientado en Z, o tile 1×2 en Z, o dos plates 1×2 seguidos en fila Z.
- **`(0, 0, -100) = 63 ocurrencias (sólo Pet Shop)**` — Distancia exacta de 5 studs en Z: coincide con la dimensión de un **brick 1×5 (3004 variante) o tile 1×5**. Aparece casi exclusivamente en Pet Shop porque el models de 3 plantas tiene paredes largas en Z.
- **`(0, -24, 0) = 8+49 = 57 ocurrencias`** — Saltar 1 brick verticalmente = coloca un brick (3004) directamente sobre la última plate. Es la **transición "wall starts here"**: cuando aparece un `dy=-24`, lo que viene es una hilera de bricks encajados en los studs superiores de la última hilada de plates.
- **`(100, 0, 0) = 36 ocurrencias (sólo Pet Shop)**` — Distancia **no múltiplo de 20**: no es encaje de studs. Corresponde a posiciones donde se coloca una parts cuyo origen **NO** está en el centro de stud, sino descentrado (p.ej. puertas, ventanas, parts Technic). Indica elementos de ancho 5 studs con tolerance (±10 LDU).

### 1.3 Deltas del mismo tipo (same-piece deltas)

Para entender cómo se **encadenan parts idénticas** entre sí:

- **`30244.dat` (plate 1×2 con 1×1 cutout)** se repite con `(±40, 0, 0) = 4+4 = 8`: es una parts que se usa para ir rellenando una hilera de **2 studs por parts** consecutivamente (Brick Beetle tiene filas de plates con ventanas de 1×1).
- **`3009.dat` (brick 1×6) en Pet Shop** se encadena a sí mismo con **`(120, 0, 0) = 11 ocurrencias`**: exactamente 6 studs en X (120 = 20×6), o sea, se están **apilando bricks 1×6 extremo con extremo** para formar muros largos.
- **`3024.dat` (plate 1×1)** en Pet Shop con **`(0, -8, 0) = 6` y `(0, 0, -40) = 7`**: la plate 1×1 se usa tanto para **apilar vertical** como para **saltar 2 studs en Z** (se usa como tapado de stud suelto entre parts más grandes).
- **`3023.dat` (plate 1×2)** en ambos sets: `(0, 0, -40) = 3+5` (en Z) y `(0, 0, 40)=1` (otra orientación): se encadena en la **dirección larga de la parts**.
- **`4216.dat` (Technic liftarm 1×7)** en Pet Shop con **`(0, -24, 0) = 25 ocurrencias`**: 1 liftarm sobre otro liftarm = 24 LDU. **El liftarm se apila a sí mismo** como si fuera un brick, ignorando los holes Technic.
- **`60481.dat` (slope brick 1×3 invertido)** con **`(0, -8, -20) = 7` y `(0, 8, -20) = 5`**: se encadena con **1 plate vertical de diferencia y 1 stud en Z**. Esto es la pendiente tejado: el slope se apoya en el stud siguiente pero la pendiente lo hace bajar 8 LDU.
- **`3005.dat` (brick 1×1)** en Pet Shop `(0, -24, 0) = 7`: brick 1×1 sobre brick 1×1 — **apilado vertical puro** de 24 LDU (sin plate intermedia), lo que forma columnas/pilares.

---

## 2. Bigramas más frecuentes (interpretados)

Bigrama = parts N → parts N+1 en el orden del files.

### 2.1 10252 VW Beetle (top 15)

| #  | Bigrama                      | count | Lectura                                                                                                  |
|----|------------------------------|------:|----------------------------------------------------------------------------------------------------------|
|  1 | 3794b → 3794b                |    28 | **Filas paralelas de plates 1×2 con groove** (carrocería del coche, costados)                              |
|  2 | 3023 → 3023                  |    22 | **Filas paralelas de plates 1×2** (estructura interna del chasis, sin groove)                             |
|  3 | 3069b → 3069b                |    18 | **Filas de tiles 1×2** (acabado liso exterior del coche)                                                |
|  4 | 3623 → 3623                  |    16 | **Filas de plates 1×3** (estructura larga del chasis)                                                    |
|  5 | 3024 → 3024                  |    16 | **Plates 1×1 en hilera** (relleno de huecos, ventanas)                                                    |
|  6 | 6141 → 6141                  |    15 | **Plates redondos 1×1** (decoración: faros, tapones, tornillos visibles)                                |
|  7 | 30244 → 30244                |    15 | **Plates 1×2 con cutout** (rejillas, huecos de ventilación del motor)                                    |
|  8 | 85984 → 85984                |    14 | **Roof tiles 2×1 con knob** (techo curvo del Beetle, lomos)                                              |
|  9 | 2780 → 2780                  |    10 | **Technic pins 1×1** (conectores Technic del chasis interior)                                            |
| 10 | 87087 → 87087                |    10 | **Technic axle pin** (engranajes/ejes del coche)                                                          |
| 11 | 11215 → 11215                |     9 | **Plates 4×4 con esquina cortada** (panel del suelo del coche)                                          |
| 12 | 3004 → 3004                  |     9 | **Bricks 1×2 en hilera** (estructura vertical de la cabina)                                              |
| 13 | 3622 → 3622                  |     9 | **Plates 3×3 con esquina** (panel del suelo del coche)                                                   |
| 14 | 93606 → 93606                |     9 | **Slope curved** (parabrisas, ventanillas curvas)                                                         |
| 15 | 92280 → 92280                |     8 | **Slope 1×2 inverted** (parte baja de la carrocería)                                                     |

**Lectura global del Beetle:** Predominio absoluto de plates (3023, 3024, 3794b, 3623) y tiles (3069b, 3070b, 85984) — models **plano y liso** con muchas superficies. Los bigramas misma-parts = **se están construyendo hileras largas** (chasis, suelo, techo curvo).

### 2.2 10218 Pet Shop (top 15)

| #  | Bigrama                      | count | Lectura                                                                                                  |
|----|------------------------------|------:|----------------------------------------------------------------------------------------------------------|
|  1 | 6141 → 6141                  |    42 | **Plates redondos 1×1** (decoración fachada: buhardillas, círculos ornamentales)                         |
|  2 | 3069b → 3069b                |    41 | **Tiles 1×2** (acabado liso de paredes del edificio)                                                     |
|  3 | 3024 → 3024                  |    40 | **Plates 1×1** (relleno entre bricks grandes)                                                            |
|  4 | 3009 → 3009                  |    34 | **Bricks 1×6** (muro largo de fachada — pared exterior)                                                  |
|  5 | 3794a → 3794a                |    34 | **Plates 1×2 sin groove** (estructura, contrapiso)                                                        |
|  6 | 3005 → 3005                  |    33 | **Bricks 1×1** (columnas, esquinas, decoración)                                                          |
|  7 | 3068b → 3068b                |    32 | **Tiles 2×2** (acabado liso de tejado, grandes paños)                                                    |
|  8 | 3070b → 3070b                |    32 | **Tiles 1×1** (detalles fachada, gárgolas, ventanas individuales)                                         |
|  9 | 3023 → 3023                  |    32 | **Plates 1×2** (estructura piso, contrapisos)                                                             |
| 10 | 4216 → 4216                  |    31 | **Technic liftarm 1×7** (estructura interna, vigas del ático)                                            |
| 11 | 3010 → 3010                  |    29 | **Bricks 1×4** (muros intermedios)                                                                       |
| 12 | **3009 → 3010**              |  **24**| **TRANSICION brick 1×6 → brick 1×4** (fin de muro largo, inicio de esquina)                            |
| 13 | 6636 → 6636                  |    23 | **Tiles 1×6** (acabado liso de techo corrido)                                                            |
| 14 | **3010 → 3009**              |  **22**| **TRANSICION inversa brick 1×4 → brick 1×6** (cierre simétrico de muro)                                |
| 15 | 60481 → 60481                |    21 | **Slope brick inverted** (cornisa, remate de fachada)                                                     |

**Lectura global del Pet Shop:** Equilibrio bricks/plates/tiles. Los bigramas **3009↔3010** son únicos del Pet Shop: muestra el **patrón de fachada rectangular** — alternar ladrillo 6 con ladrillo 4 (probablemente la fachada tiene ventanas o paños alternados de 6 studs y 4 studs).

### 2.3 Bigramas heterogéneos notables

En Pet Shop hay además:

- **3009 → 3005 (count=19)** — Cada **brick 1×6 del muro va seguido de un brick 1×1**: típico cuando el muro termina en una columna/esquina, y el brick 1×1 cierra el hueco final de 1 stud.
- **3009 → 3010 → 3010 (count=14, trigrama)** — Muro: brick 1×6 → 2 bricks 1×4 consecutivos. Reemplaza 1 brick 1×6 + parte de un 1×4.

---

## 3. Trigramas destacados (sólo ensambles reconocibles)

La mayoría de los trigramas son runs de la misma parts (Brick 1×1 tres veces = columna). Los **verdaderamente informativos** son los **heterogéneos**:

### 3.1 10252 Beetle

| Trigrama                                | count | Lectura                                                                                |
|-----------------------------------------|------:|----------------------------------------------------------------------------------------|
| 44728 → 2420 → 3005                     |     4 | **Base slope → slope 45° → brick 1×1** (rampa del morro/del maletero: el slope 2420 "sube" y el brick 1×1 lo corona) |
| 3623 → 3623 → 3023                      |     3 | **Plate 1×3 → plate 1×3 → plate 1×2** (transición de hilera 3 studs a hilera 2 studs: la pared se estrecha) |

### 3.2 10218 Pet Shop (heterogéneos útiles)

| Trigrama                                | count | Lectura                                                                                |
|-----------------------------------------|------:|----------------------------------------------------------------------------------------|
| 3009 → 3010 → 3010                      |    14 | **Brick 1×6 → brick 1×4 → brick 1×4** (muro largo continúa con 2 unidades de 4 studs)  |
| 3009 → 3009 → 3010                      |     - | No presente en top-15 pero inferible: dos bricks 1×6 consecutivos seguidos de 1×4       |

### 3.3 Trigramas de stacking vertical (todos los models)

Casi todos los trigramas AAA con `count >= 6` son **stacking vertical de plates** (`plate → plate → plate` con Δy=-8) o **stacking de la misma parts con Δy=-24** (brick sobre brick).

examples Beetle: `3794b → 3794b → 3794b (count=20)` → "tres plates con groove consecutivas", generalmente apiladas en Y.

examples Pet Shop: `4216 → 4216 → 4216 (count=28)` → **28 trigramas de 3 liftarms apilados verticalmente** — la estructura interna del ático del Pet Shop es básicamente **un muro de Technic liftarms apilados**.

### 3.4 Trigramas notables por patrón constructivo

| Tipo de ensamble             | Trigrama representativo                  | Interpretación                                          |
|------------------------------|------------------------------------------|---------------------------------------------------------|
| **Base → pared → techo**     | 3022 → 3004 → 6091 (inferido del top-15) | Plate 2×2 (base) → brick 1×2 (pared) → slope (tejado)   |
| **Muro largo → fin de muro** | 3009 → 3010 → 3005 (Pet Shop)            | Brick 1×6 (sigue muro) → brick 1×4 (esquina) → brick 1×1 (cierre) |
| **Pilar de bricks**          | 3004 → 3004 → 3004 (count=4 Beetle)      | **Pilar vertical** de 3 bricks (72 LDU alto)             |

---

## 4. Rotaciones (matrices) por parts

La matriz por defecto es `1 0 0 0 1 0 0 0 1` (identidad, sin rotación). Rotaciones en Y de 90° son:

- `0 0 1 0 1 0 -1 0 0` (90° CW alrededor de Y, det=+1)
- `0 0 -1 0 1 0 1 0 0` (90° CCW alrededor de Y, det=+1)
- `-1 0 0 0 1 0 0 0 -1` (180° alrededor de Y, det=+1)

Rotaciones con det=-1 son **espejos** (raros; OMR los prohíbe en logos pero aparecen en detalles curvos).

### 4.1 Top-10 parts del Beetle con su rotación dominante

| parts    | count | Rotación dominante (matriz)                              | count | Por qué                                                                                   |
|----------|------:|----------------------------------------------------------|------:|-------------------------------------------------------------------------------------------|
| **3023** (plate 1×2) | 69 | `1 0 0 0 1 0 0 0 1` (identidad)                          |    21 | Orientation default es la **natural**; el brick 1×2 tiene lado "largo" en X, "corto" en Z.  |
|          |      | `0 0 1 0 1 0 -1 0 0` (90° Y CW)                          |    17 | Plate girada 90°: ahora el lado largo va en Z.                                            |
|          |      | `-1 0 0 0 1 0 0 0 -1` (180° Y)                           |    14 | Plate invertida (extremo a extremo).                                                      |
|          |      | `0 0 -1 0 1 0 1 0 0` (90° Y CCW)                         |     7 | Equivalente visual a la primera 90° (lado largo en Z, otro sentido).                      |
| **3024** (plate 1×1) | 47 | Identidad                                                |    22 | Cuadrada — visualmente indistinguible en X/Z. La identidad es la **opción por defecto**. |
|          |      | 90° Y (cualquier sentido)                                |   6+3 | Mismo motivo — 1×1 = 360°/4 simetrías rotacionales.                                       |
| **3794b** (plate 1×2 con groove) | 41 | `0 0 1 0 1 0 -1 0 0` (90° Y CW) | **26** | **La groove (ranura) debe alinearse con el flujo del coche**: corre en una dirección específica (Z), por eso 26 vs 5 del otro sentido. |
|          |      | 180° Y                                                   |     6 | Plate invertida extremo a extremo.                                                        |
|          |      | 90° Y CCW                                                |     5 | Ranura en el otro sentido (5× menos común).                                              |
| **3623** (plate 1×3) | 40 | Identidad                                                |    17 | Orientación natural: 3 studs en X.                                                        |
|          |      | 180° Y                                                   |    10 | Plate invertida.                                                                          |
| **3069b** (tile 1×2) | 39 | `0 0 1 0 1 0 -1 0 0` y `1 0 0 0 1 0 0 0 1` (empate)     | 10+10 | **Empate entre identidad y 90° Y**: las dos orientaciones se usan ~igualmente (mitad paredes longitudinales, mitad paredes transversales). |
|          |      | 90° Y CCW                                                |     5 | Otro sentido.                                                                             |
|          |      | Inclinada `0 -0.819 -0.574 0 0.574 -0.819 1 0 0 0`      |     4 | **Tile inclinada ~35°** (curvatura del coche).                                            |
| **6141** (plate round 1×1) | 37 | `0 0 -1 0 1 0 1 0 0` (90° Y CCW) |    12 | **Plato circular: 4 simetrías rotacionales**; las 4 orientaciones Y deberían estar igualadas (12+11+4+2=29 ≈ 25% cada una). Real: ligera asimetría por dirección del "frente" del coche. |
|          |      | Identidad                                                |    11 | Default.                                                                                  |
|          |      | `-1 0 0 0 0 1 0 1 0` (espejo, det=-1)                    |     2 | **Raro**: aparece el flip solo en parts donde se quiere romper simetría.                  |
| **3070b** (tile 1×1) | 30 | Identidad / 90° Y                                        | 6+6 | Cuadrada; 4 simetrías.                                                                    |
| **85984** (slope tile 2×1) | 25 | `0 0 1 0 1 0 -1 0 0` (90° Y)        |     4 | **La dirección del slope es importante**: 4 en un sentido. Empate con rotación en X (4). |
|          |      | `1 0 0 0 0 -1 0 1 0` (rotación en X 90°)                 |     4 | Slope girado para que la pendiente mire al lado opuesto.                                 |
|          |      | Rotaciones ~4° (`0.998 0 0.07 0 1 0 -0.07 0 0.998`)       |   3+3 | **Slope ligeramente inclinado** — el techo del Beetle NO es plano, tiene curvatura.        |
| **30244** (plate 1×2 con cutout) | 21 | Identidad                                                |    13 | **Default dominante** (60%): el cutout tiene una dirección preferida.                     |
|          |      | 90° Y CW                                                 |     5 | Cutout en el otro sentido.                                                                |
| **3622** (plate 3×3 con esquina) | 19 | Identidad                                                |     7 | Esquina en su posición natural.                                                           |
|          |      | `(-0.998 0 -0.07 ...) ... (0.07)`                         |   5+5 | **Rotación de ~4°** (de nuevo, curvatura del Beetle).                                     |
| **3004** (brick 1×2) | 18 | Identidad                                                |     9 | Default.                                                                                  |
|          |      | 180° Y                                                   |     5 | Brick invertido.                                                                          |

### 4.2 Top-10 parts del Pet Shop con su rotación dominante

| parts    | count | Rotación dominante                                       | count | Por qué                                                                                  |
|----------|------:|----------------------------------------------------------|------:|------------------------------------------------------------------------------------------|
| **3009** (brick 1×6) | 113 | Identidad                                              |    60 | **53%** — la fachada es muy estable en la orientación por defecto (largo en X).          |
|          |      | 180° Y                                                   |    33 | Brick invertido: usado para paños que van al lado opuesto.                              |
|          |      | 90° Y                                                    | 12+8 | Menos común: solo cuando el muro cambia de orientación.                                 |
| **3005** (brick 1×1) | 113 | Identidad                                              |    46 | Cuadrado, default dominante.                                                              |
|          |      | 90° Y CW / CCW                                           | 29+26 | Casi igual a identidad (sumando 75 de 113 = 66% identidad, 34% rotaciones de 90°).    |
| **6141** (plate round 1×1) | 88 | Identidad                                            |    27 | Default.                                                                                  |
|          |      | 90° Y CCW                                                |    23 | Platos circulares: 4 simetrías. Algo más identidad (27/88 = 31%) porque la fachada "delantera" usa una orientación canónica. |
|          |      | 45° (`-0.707 0 -0.707 ...`)                              |     8 | **Platos a 45°**: decoración diagonal en fachada.                                        |
| **3010** (brick 1×4) | 86 | Identidad                                              |    44 | Muro en X, default.                                                                       |
|          |      | 180° Y                                                   |    24 | Paños invertidos.                                                                         |
| **3069b** (tile 1×2) | 84 | 90° Y CCW                                                |    20 | Tile con lado largo en Z (rotada de default).                                            |
|          |      | 90° Y CW                                                 |    18 | Otro sentido.                                                                            |
|          |      | 90° en X (rotación de pared)                              |    13 | **Tile girada para quedar vertical en lugar de horizontal** (cornisa).                    |
|          |      | Identidad                                                |    11 | Por defecto.                                                                              |
| **3023** (plate 1×2) | 80 | 90° Y CCW                                                |    31 | **38% en una sola rotación**: indica uso mayoritario con el lado largo en Z.             |
|          |      | Identidad                                                |    21 | Paños con lado largo en X.                                                               |
| **3024** (plate 1×1) | 69 | Identidad                                              |    30 | Default.                                                                                  |
|          |      | 90° Y CCW                                                |    21 | Cuadrada, indistinguible.                                                                 |
| **3004** (brick 1×2) | 67 | 90° Y CCW                                                |    30 | **45%** en una sola rotación: paredes con el lado largo en Z.                            |
|          |      | Identidad                                                |    17 | Lado largo en X.                                                                         |
|          |      | 180° Y                                                   |    11 | Invertido.                                                                                |
| **3070b** (tile 1×1) | 54 | Identidad                                              |    20 | Default.                                                                                  |
|          |      | 90° Y CW                                                 |    12 | Cuadrada.                                                                                 |
| **3794a** (plate 1×2 sin groove) | 53 | 180° Y |    18 | **Default NO domina aquí** (sólo 12 de 53 = 23%). La plate 1×2 sin groove se usa MAYORMENTE invertida (rotada 180°), lo cual es interesante — sugiere que en Pet Shop las plates 1×2 sin groove se colocan "con el lado A hacia atrás" en muchos casos. |
|          |      | Identidad / 90° Y CW                                     | 12+12 | Empate.                                                                                   |

### 4.3 Observaciones generales sobre rotaciones

1. **La matriz identidad siempre está en el top-3**, pero no siempre es la #1. En parts **cuadradas o con simetría rotacional** (3024, 3005, 3070b, 6141) las 4 rotaciones cardinales se reparten el uso.
2. **Las rotaciones a 90° en Y** son las más comunes (siempre det=+1). Las rotaciones a 90° en X o Z aparecen sólo en tiles inclinadas, slopes y bricks Technic.
3. **Los flips (det=-1) son raros**: ~2-5% del total. Aparecen cuando:
   - se quiere romper una simetría visual (detalles del Beetle)
   - se monta una parts Technic en orientación invertida
   - hay una parts con un detalle que sólo tiene sentido en una dirección (logos, pegatinas)
4. **Rotaciones a 4° o ángulo raro** (`±0.07`, `±0.574`, `±0.819` ≈ `cos(55°)`, `sin(35°)`) son **casi exclusivas del Beetle** (3024, 3022, 3622, 85984) — confirman que **el cuerpo del coche tiene curvatura**. En Pet Shop estas rotaciones aparecen sólo en la cúpula del ático (60593c01, 60478, 3820).
5. **Las rotaciones a 22.5° / 45°** (`±0.707`, `0.707 0 0.707`) están ligadas a slopes diagonales o paneles de buhardilla.

---

## 5. Reglas inferidas de chaining

Cada regla incluye: observación numérica + interpretación física + examples concreto del JSON.

### Regla 1 — Plate sobre plate usa exactamente Δy = -8 LDU

- **Observación:** El delta `(0, -8, 0)` aparece **38 veces en Beetle + 65 en Pet Shop = 103 ocurrencias** — el delta vertical más frecuente del corpus.
- **Interpretación:** Cada vez que la siguiente parts es otra plate (8 LDU de alto) y debe encajar en los studs superiores de la anterior, se resta exactamente 8 al Y. El origen de la parts plate es su **base de studs** (no la cara superior), así que colocar una plate encima de otra plate requiere Y → Y - 8.
- **examples:** Trigrama `3023 → 3023 → 3023 (count=5 en Beetle)` con Δy=-8 cada vez → **una columna de 3 plates = 24 LDU vertical** (equivalente en altura a un brick, pero dividido en 3 capas).

### Regla 2 — Brick sobre plate acumula Δy = -24 (no -8)

- **Observación:** El delta `(0, -24, 0)` aparece **8 veces en Beetle + 49 en Pet Shop = 57 ocurrencias**.
- **Interpretación:** Cuando la parts anterior es una plate (8 LDU) y la siguiente es un brick (24 LDU), la diferencia de altura es **24** (alto del brick), NO la suma 8+24=32. Esto es porque el origen del brick es **su base**, igual que la plate: el brick se coloca de modo que su base apoye en los studs superiores de la plate → Y = Y_plate - 24.
- **examples:** En Pet Shop, trigrama `3005 → 3005 → 3005 (count=12)` con Δy=-24 cada vez → **3 bricks 1×1 apilados = 72 LDU de columna vertical**.

### Regla 3 — Las parts Technic liftarm (4216) se apilan verticalmente como si fueran bricks

- **Observación:** Para `4216.dat` (Technic liftarm 1×7), `same_piece_deltas` muestra `(0, -24, 0) = 25 ocurrencias` en Pet Shop.
- **Interpretación:** Aunque el liftarm Technic tiene holes para pins, los autores lo apilan verticalmente a intervalos de **24 LDU (1 brick)**, no de 20 LDU (1 stud). Es decir, se monta en encaje de studs como un brick, no en encaje Technic.
- **examples:** Trigrama `4216 → 4216 → 4216 (count=28)` → **el ático del Pet Shop es literalmente un muro de 28 liftarms apilados verticalmente**.

### Regla 4 — Encadenar la misma parts en X sin solape requiere Δx = 20 × ancho

- **Observación:**
  - `3009.dat` (brick 1×6, ancho 6 studs = 120 LDU) tiene `same_piece_delta (120, 0, 0) = 11 ocurrencias` en Pet Shop.
  - `3010.dat` (brick 1×4, ancho 4 studs = 80 LDU) tiene `same_piece_delta (80, 0, 0) = 12 ocurrencias` en Pet Shop.
  - `6636.dat` (tile 1×6) tiene `same_piece_delta (120, 0, 0) = 6 ocurrencias`.
  - `30244.dat` (plate 1×2 con cutout) tiene `same_piece_delta (±40, 0, 0) = 4+4 ocurrencias` en Beetle.
- **Interpretación:** Para encadenar N parts idénticas extremo con extremo en X sin solape, Δx = 20 × studs_de_la_pieza. El origen de la parts está en el centro del stud-set, por eso 6 studs = 120 LDU entre centros.
- **examples:** Construcción de muro de 8 studs en Pet Shop = `3009 (1×6) + 3010 (1×4) extremo con extremo` — exactamente los bigramas heterogéneos `3009→3010 (count=24)` y `3010→3009 (count=22)`.

### Regla 5 — Las diagonales se construyen con deltas asimétricos

- **Observación:** Delta `(20, 0, -20)` aparece **16 veces en Pet Shop** (NO en Beetle). Delta `(30, 0, -50)` aparece 5+2 veces (sólo Pet Shop).
- **Interpretación:** En esquinas, las parts no se centran en stud — se desplazan al corner. (20, 0, -20) = diagonal 1-stud (esquina de plate 2×2 o de 1×1 individual). (30, 0, -50) = esquina con offset raro: 30 LDU = 1.5 studs, 50 LDU = 2.5 studs — corresponde a colocar una parts descentrada sobre la esquina de una base 4×4 con un 1×1 cortado en la esquina.
- **examples:** `3010.dat same_piece_delta (30, 0, -50) = 5 ocurrencias` → un brick 1×4 colocado en una esquina de base con desplazamiento de 1.5+2.5 studs (típico cuando el muro arranca en un corner cut).

### Regla 6 — Las parts Technic pin (2780, 87087) se colocan cada 40-60 LDU (no 20)

- **Observación:**
  - `2780.dat` same-piece deltas: `(0, 0, -40) = 4 ocurrencias` (Beetle).
  - `87087.dat` same-piece deltas: `(20, 0, ±1.4) = 4+4 ocurrencias` en Beetle — ¡**valores no enteros**!
- **Interpretación:** Los Technic pins no encajan en studs, sino en Technic holes separados **40 LDU (2 studs)**. La tolerancia de ±1.4 LDU en 87087 es el ajuste típico para encajes Technic con clip: el pin se asienta en el hole con un pequeño margen.
- **examples:** Cuatro pins Technic 87087 colocados en fila a `(20, 0, ±1.4)` forman una **hilera Technic** con 1 stud de pitch (20 LDU) — esto es propio de engranajes/ejes del Beetle.

### Regla 7 — El techo curvo del Beetle usa rotaciones a ~4° (no 0° ni 22.5°)

- **Observación:** Las matrices `(-0.998 0 0.07 0 1 0 -0.07 0 -0.998)` (= `cos(-4°) -sin(-4°); sin(-4°) cos(-4°)`) aparecen 2 veces en `3024`, 2 veces en `3004`, 2 veces en `3622`, 1 vez en `3666`. Todas en Beetle.
- **Interpretación:** `cos(4°) ≈ 0.998`, `sin(4°) ≈ 0.07`. El Beetle tiene una **curvatura continua del techo** lograda con rotaciones pequeñas acumuladas: cada panel del techo se gira 4° respecto al anterior. Sumando 5 paneles a 4° cada uno = 20° de curvatura total.
- **examples:** Secuencia de tiles del techo en Beetle: cada tile está girada 4° respecto a la anterior, creando la **silueta curvada del VW Beetle original**.

### Regla 8 — El ático del Pet Shop usa rotaciones a 45° (no 0°)

- **Observación:** `6141.dat` (platos redondos) tiene `-0.707 0 -0.707 0 1 0 0.707 0 -0.707` (= matriz de rotación en X 45°) con **count=8** en Pet Shop.
- **Interpretación:** Los platos redondos de la fachada se ponen a 45° respecto a X. Esto los convierte en **rombos visuales** (4 platos redondos en cuadro forman un patrón de buhardilla).
- **examples:** Buhardillas del ático del Pet Shop: 4 platos redondos 6141 orientados a 45° forman el detalle de las **ventanas circulares de las buhardillas**.

### Regla 9 — Los deltas no múltiplos de 20 identifican parts con tolerancia o descentradas

- **Observación:** Deltas "raros" del corpus:
  - `(20, 0, ±1.4)` — pins Technic con tolerancia.
  - `(30, 0, -50)` — esquina de base con corner cut.
  - `(11.5, 16.4, 0)` en `3069b.dat` — slope colocado en ángulo sobre superficie irregular.
  - `(40.1, -57.3, 50)` en `99206.dat` — parts con posición off-center.
  - `(-0.819 -0.574 0 ...)` en `3024.dat` y `2420.dat` — rotaciones a 35° (slopes).
- **Interpretación:** Cualquier delta en X o Z que **no sea múltiplo de 20 LDU** indica una parts cuyo origen NO está en el centro del stud-set, o una parts colocada con ajuste fino (Technic, slope, ventana, sticker).
- **examples:** `99206.dat same_piece_delta (-40.1, -57.3, 50)` indica que esta parts (probablemente una **window frame**) se descentra 0.05 LDU en X, 0.65 en Y, 0.50 en Z — valores típicos de **window pieces** que se montan sobre studs pero tienen tolerance.

### Regla 10 — Las transiciones de parts entre filas en X+Z suelen ir a Δx y Δz **simétricos** o **inversos**

- **Observación:**
  - En Beetle: `3009` → `3010` (count=24, transición 6-stud → 4-stud); `3010` → `3009` (count=22, transición inversa). Total = 46 transiciones simétricas.
  - En Pet Shop bigramas: `3009 → 3005 (count=19)`: brick 1×6 → brick 1×1 (muro termina en esquina con cierre).
- **Interpretación:** En muros rectangulares, el patrón es **parts larga + parts corta + parts 1×1** para cerrar la esquina. La simetría `3009↔3010` indica **muros de fachada rectangular con ventana central** (brick 1×6 a ambos lados de la ventana, brick 1×4 entre la ventana y la esquina).
- **examples:** Trigrama `3009 → 3010 → 3010 (count=14)` describe exactamente el patrón "**muro 1×6 + dos muros 1×4 consecutivos**" — un paño de 14 studs de fachada que es 6+4+4.

---

## Notas finales sobre calidad de los datos

- **10252 Beetle** tiene **211 STEPs** (alta resolución temporal: cada paso tiene de media 2.7 parts). Esto hace que los bigramas reflejen **orden de construcción**, no necesariamente adyacencia física. Los delta-deltas consecutivos sí son buenas señales de adyacencia.
- **10218 Pet Shop** tiene **sólo 1 STEP en el models maestro** (`step_count: 1, master_piece_count: 0`) — el main.ldr sólo referencia 17 sub-models. La construcción está detallada **dentro de cada sub-models**, donde sí hay muchos STEPs. Los bigramas del corpus Pet Shop que mostramos vienen de los sub-models (`total_pieces_in_subbuilds: 1998`).
- **Beetle = 150 parts únicas + 81 sub-models** → es un models "complejo con muchas parts especiales reutilizadas".
- **Pet Shop = 206 parts únicas + 17 sub-models** → más "building system" clásico, menos sub-ensambles.

El contraste entre ambos corpus confirma que los patrones de chaining son **genéricos del sistema LEGO** (studs cada 20 LDU, plates de 8 LDU, bricks de 24 LDU) y **no específicos de un set**. Las diferencias (4° de rotación, paneles de 4 studs vs 6 studs) reflejan la **forma del models final**, no la gramática de chaining.
