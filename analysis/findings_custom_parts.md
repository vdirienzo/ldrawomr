# Findings: cómo se autoran custom parts embebidas en MPDs OMR

Análisis basado en los MPDs oficiales OMR de **10252-1.mpd** (VW Beetle, 9004 líneas) y **10218-1.mpd** (Pet Shop, 2958 líneas), cruzados con `analysis/deep_stats.json` y `analysis/raw_stats.json`.

## Resumen numérico (verificado)

| Set       | custom parts (root `.dat`) | subparts `s\` | hi-res `48\` | decoraciones (`p`/sticker) | Total `.dat` |
|-----------|----------------------------|---------------|--------------|----------------------------|--------------|
| 10252     | 7                          | 2             | 1            | 10                         | **20**       |
| 10218     | 3                          | 0             | 0            | 0                          | **3**        |

`deep_stats.json` confirma: `embedded_custom_parts_count: 17 / subparts: 2 / hires: 1` para 10252; `3` para 10218 (nota: el parser agrupa las 10 decoraciones como "parts" raiz, de ahí 7+10=17).

---

## 1. Inventario de custom parts embebidas — 10252 (VW Beetle)

Raíz del MPD (7 partes principales):

| Línea  | Archivo                          | Líneas | Tipo1 | Tipo2 | Tipo3 | Tipo4 | Tipo5 |
|-------:|----------------------------------|-------:|------:|------:|------:|------:|------:|
|  5591  | `10252 - 24599.dat`              |     23 |     3 |     0 |     0 |     0 |    10 |
|  5618  | `10252 - 10252_towel.dat`        |     38 |    22 |     0 |     0 |     0 |     0 |
|  5660  | `10252 - 24246.dat`              |     12 |     2 |     0 |     0 |     1 |     0 |
|  5676  | `10252 - 23443.dat`              |    133 |    19 |    34 |    12 |    30 |    22 |
|  5813  | `10252 - 24607.dat`              |    150 |    40 |    31 |     8 |    37 |     0 |
|  7062  | `10252 - 98138p81.dat`           |     82 |     2 |     0 |    28 |    41 |     0 |
|  7147  | `10252 - 98138p82.dat`           |    239 |     4 |     0 |    32 |   194 |     0 |

Subpartes en `s\` (2):

| Línea  | Archivo                              | Líneas | Tipo1 | Tipo2 | Tipo3 | Tipo4 | Tipo5 |
|-------:|--------------------------------------|-------:|------:|------:|------:|------:|------:|
|  5967  | `s\10252 - 24599s01.dat`             |    791 |    29 |   286 |    66 |   205 |   163 |
|  6762  | `s\10252 - 24246s01.dat`             |     41 |    23 |     0 |     0 |     6 |     0 |

Hi-res en `48\` (1):

| Línea  | Archivo                              | Líneas | Tipo1 | Tipo2 | Tipo3 | Tipo4 | Tipo5 |
|-------:|--------------------------------------|-------:|------:|------:|------:|------:|------:|
|  6807  | `48\10252 - t08o2500.dat`            |    252 |     0 |     0 |     0 |    72 |   162 |

Decoraciones / stickers (`p` suffix o 8 dígitos, 10 archivos): `98138p81/p82` ya listadas; las demás (`6153754q/o/n/m/p/j/k/l/d/c`, líneas 7388-8929) son **overlays 2D** que aplican triángulos sobre partes oficiales (`box5-12.dat`, `3815bpXY.dat`, etc.) usando `0 BFC NOCLIP`:

| Línea  | Archivo                          | Líneas | Notas                                                |
|-------:|----------------------------------|-------:|------------------------------------------------------|
|  7388  | `10252 - 6153754q.dat`           |     14 | sticker 3.4×0.9 parabrisas trasero (`box5-12`)       |
|  7404  | `10252 - 6153754o.dat`           |    515 | sticker Al's BOARDS                                  |
|  7921  | `10252 - 6153754n.dat`           |    262 |                                                      |
|  8185  | `10252 - 6153754m.dat`           |     42 |                                                      |
|  8229  | `10252 - 6153754p.dat`           |    176 |                                                      |
|  8407  | `10252 - 6153754j.dat`           |    247 |                                                      |
|  8656  | `10252 - 6153754k.dat`           |    141 |                                                      |
|  8799  | `10252 - 6153754l.dat`           |    114 |                                                      |
|  8915  | `10252 - 6153754d.dat`           |     12 |                                                      |
|  8929  | `10252 - 6153754c.dat`           |     75 |                                                      |

---

## 2. Inventario de custom parts embebidas — 10218 (Pet Shop)

| Línea  | Archivo                                    | Líneas | Tipo1 | Tipo2 | Tipo3 | Tipo4 | Tipo5 |
|-------:|--------------------------------------------|-------:|------:|------:|------:|------:|------:|
|  2885  | `10218 - ldcRigid3mmHoseCap.dat`           |     25 |     5 |     0 |     0 |     0 |     0 |
|  2910  | `10218 - ldcRigid3mmHoseSeg.dat`           |     19 |     3 |     0 |     0 |     0 |     0 |
|  2929  | `10218 - ldcConRing-4-4.dat`               |     30 |     0 |     0 |     0 |     0 |    16 |

Sin subpartes `s\`, sin hi-res `48\`. Las 3 son donantes de **LDCad** para construir mangueras (path-deform). Solo líneas tipo 1 y 5.

---

## 3. Tres ejemplos concretos

### 3.1 Ejemplo SIMPLE — `10252 - 24246.dat` (12 líneas)

Tile 1×1 con borde redondeado. El más pequeño de las custom geométricas reales.

```
0 FILE 10252 - 24246.dat
0 Tile 1 x  1 with Rounded End
0 Name: 10252 - 24246.dat
0 Author: Owen Burgoyne [C3POwen]
0 !LDRAW_ORG Unofficial_Part
0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt

0 BFC CERTIFY CCW

1 16 0 0 0 1 0 0 0 1 0 0 0 1 s\10252 - 24246s01.dat
4 16 -9 0 9 -9 0 0 9 0 0 9 0 9
1 16 0 0 0 9 0 0 0 1 0 0 0 -9 2-4disc.dat
```

- **Primitivas usadas:** `s\10252 - 24246s01.dat` (subparte con la geometría), `2-4disc.dat` (disco radio 9, alto -9 para la cara inferior), 1 quad tipo 4.
- **Geometría propia:** un único quad tipo 4 cierra la cara superior cuadrada.
- **Líneas tipo 1:** 2 (1 referencia a la subparte, 1 disco). **Líneas tipo 4:** 1.
- **Headers:** 5 meta-líneas (`FILE`, título corto, `Name:`, `Author:`, `!LDRAW_ORG Unofficial_Part`) + 1 `!LICENSE` + 1 `BFC CERTIFY CCW`.
- **Patrón:** "wrapper minimalista" — la parte compleja vive en `s\24246s01.dat` (41 líneas, 23 tipo 1) y el archivo raíz solo la referencia + 1 quad de tapa + 1 disco inferior.

### 3.2 Ejemplo MEDIO — `10252 - 10252_towel.dat` (38 líneas)

Toalla enrollada del VW Beetle, hecha con cilindros escalados.

```
0 FILE 10252 - 10252_towel.dat
0 10252 Volkswagen Beetle Towel 6x14
0 Name: 10252 - 10252_towel.dat
0 Author: Roland Dahl

0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt

1 14 0 0 -52.6 14 0 0 0 0 14 0 -7.4 0 4-4cyli.dat
1 15 0 0 -44   14 0 0 0 0 14 0 -8.6 0 4-4cyli.dat
... (16 cilindros más en colores 14/15 alternados)
1 14 0 0 60    14 0 0 0 0 14 0 -7.4 0 4-4cyli.dat

1 14 0 0 -60 -1 0 0 0 0 1 0 1 0 4-4rin13.dat
1 14 0 0 -60 -1 0 0 0 0 1 0 1 0 4-4rin12.dat
1 14 0 0  60 1 0 0 0 0 1 0 -1 0 4-4rin13.dat
1 14 0 0  60 1 0 0 0 0 1 0 -1 0 4-4rin12.dat

0 Innen
1 14 0 0 -60 12 0 0 0 0 12 0 60 0 4-4cyli.dat
0 Mitte
1 14 0 0  0 12 0 0 0 0 12 0 60 0 4-4cyli.dat
```

- **Primitivas usadas:** `4-4cyli.dat` (cilindro 4-4 cono, 22 veces), `4-4rin13.dat` y `4-4rin12.dat` (anillos, 2+2).
- **Geometría propia:** cero tipo 2/3/4 — **toda la forma es primitivas escaladas** (cilindros 14×14×variable en X, anillos para los bordes laterales).
- **Líneas tipo 1:** 22 cilindros + 2 cilindros "Innen/Mitte" + 4 anillos = 22 + 4 = 22 reales (los Innen/Mitte también son tipo 1, total 22 según el parser).
- **Headers:** mínimos — sin `!LDRAW_ORG`, sin `BFC` (no necesita BFC porque no usa CSG).
- **Patrón:** "solo primitivas con overrides de color" — 16 cilindros paralelos de colores 14/15 alternados para simular el patrón a rayas de la toalla, más 2 cilindros interiores (Innen/Mitte) que conectan los extremos.

### 3.3 Ejemplo COMPLEJO — `s\10252 - 24599s01.dat` (791 líneas)

Subparte del Brick 5×5 Corner Round. La pieza embebida más grande del MPD.

```
0 FILE s\10252 - 24599s01.dat
0 ~Brick 5 x  5 Corner Round - Half
0 Name: s\10252 - 24599s01.dat
0 Author: Magnus Forsberg [MagFors]
0 !LDRAW_ORG Unofficial_Subpart
0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt

0 BFC CERTIFY CCW

1 16 0 20 0 80 0 0 0 -80 0 0 0 80 48\10252 - t08o2500.dat   ← toro hi-res
1 16 0  0 0 20 0 0 0 1 0 0 0 20 48\1-8ring3.dat                ← anillo 1/8 hi-res
1 16 0  0 0 60 0 0 0 1 0 0 0 60 48\1-8edge.dat                ← edge hi-res
0 BFC INVERTNEXT
1 16 0  0 0 60 0 0 0 20 0 0 0 60 48\1-8cyli.dat                ← cilindro hi-res (invertido)
1 16 80 20 0 20 0 0 0 0 -20 0 1 0 48\1-4edge.dat
1 16 80 20 0 20 0 0 0 0 -20 0 1 0 48\1-4chrd.dat
0 // inside
2 24 64 24 4 96 24 4
... (286 líneas 2/24 con las costillas curvas del interior)
4 16 94.478 13.877 4 96 20 4 76 4 4 83.654 5.218 4
... (205 quads tipo 4)
5 24 76.162 20 58.441 74.954 13.877 57.515 81.82 13.877 47.239 66.806 13.877 66.806
... (163 conditional lines)
```

- **Primitivas usadas:** **6 primitivas hi-res `48\`** (`t08o2500.dat`, `1-8ring3.dat`, `1-8edge.dat`, `1-8cyli.dat`, `1-4edge.dat`, `1-4chrd.dat`) — la pieza entera es hi-res para conseguir curvatura suave.
- **Geometría propia:** 286 tipo 2 + 205 tipo 4 + 163 tipo 5 = **654 líneas de geometría construida a mano** que trazan las "costillas" curvas del interior del ladrillo en esquina.
- **Líneas tipo 1:** 29 referencias a primitivas; **tipo 2:** 286; **tipo 3:** 66; **tipo 4:** 205; **tipo 5:** 163.
- **Headers:** 7 meta-líneas (`FILE`, título, `Name:`, `Author:`, `!LDRAW_ORG Unofficial_Subpart`, `!LICENSE`) + `BFC CERTIFY CCW`. La tilde `~` en el título indica subparte en LDraw.
- **Patrón:** "subparte curva = hi-res + costillas densas" — la curvatura exterior se obtiene con primitivas de 48 subdivisiones; el interior se construye con líneas tipo 2 trazadas a mano siguiendo la curva.

### Bonus — patrón de `10252 - 24599.dat` (parte principal, 23 líneas)

```
0 FILE 10252 - 24599.dat
0 Brick 5 x  5 Corner Round
0 Name: 10252 - 24599.dat
0 Author: Magnus Forsberg [MagFors]
0 !LDRAW_ORG Unofficial_Part
0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt
0 BFC CERTIFY CCW
1 16 0 0 0 1 0 0 0 1 0 0 0 -1 s\10252 - 24599s01.dat   ← refleja la subparte
1 16 0 0 0 0 0 1 0 1 0 -1 0 0 s\10252 - 24599s01.dat    ← la rota 90°
1 16 60 20 -60 0 0 1 0 -1 0 -1 0 0 stud4a.dat            ← stud antideslizante en una esquina
5 24 42.426 24 -42.426 42.426 20 -42.426 47.604 24 -36.528 36.528 24 -47.604
... (10 conditional lines que cierran las costuras entre las dos mitades)
```

- **Patrón:** "composición por simetría" — solo 3 tipo 1 (la subparte reflejada, la subparte rotada, un stud) más 10 tipo 5 para que BFC considere el conjunto CCW. Toda la geometría vive en la subparte.

---

## 4. Patrones observados en la autoría de custom parts

### 4.1 Reuso de primitivas existentes

**Casi universal.** Las custom parts casi nunca inventan geometría nueva:

- `10252_towel.dat`: 100% cilindros `4-4cyli` + anillos `4-4rin12/13`. Cero líneas propias.
- `10252 - 24246.dat`: subparte (que a su vez reusa primitivas) + 1 disco `2-4disc` + 1 quad.
- `s\10252 - 24599s01.dat`: solo 6 primitivas hi-res + líneas propias para curvatura.
- `10218 - ldcRigid3mmHoseCap/Seg.dat`: 100% `4-4cyli` + `4-4edge` + `4-4ring1`.
- `10218 - ldcConRing-4-4.dat`: solo 16 `5 24` (conditional lines) — es una primitiva LDCad que solo dibuja el "anillo condicional" entre segmentos de manguera.

Los nombres primitivos oficiales (`stud4a`, `stug3-1x4`, `box3u2p`, `1-4cylo`, `4-4ndis`, `2-4disc`, `4-4ring2`, `1-8cyli`, `t08o2500`, etc.) muestran **reuso masivo del catálogo LDraw oficial**.

### 4.2 Complejidad del header

| Elemento              | Frecuencia                                              |
|-----------------------|---------------------------------------------------------|
| `0 FILE`              | 100%                                                    |
| `0 Name:`             | 100%                                                    |
| `0 Author:`           | 100%                                                    |
| `0 !LDRAW_ORG`        | 95% — `Unofficial_Part`, `Unofficial_Subpart`, `UNOFFICIAL PART`, `UNOFFICIAL PRIMITIVE` (Pet Shop usa el formato antiguo) |
| `0 !LICENSE`          | 100% — siempre `CCAL version 2.0 : see CAreadme.txt`    |
| `0 BFC CERTIFY CCW`   | 100% cuando hay CSG; ausente en partes solo-primitivas (ej. towel) |
| `0 !HELP`             | ocasional (ej. 23443.dat incluye ejemplo de uso)        |
| `0 !KEYWORDS`         | decoraciones (98138p81: "Volkswagen, Set 10252, Beetle") |
| `0 !CATEGORY`         | solo en las donantes LDCad del Pet Shop                 |
| Comentarios `0 //`    | comunes en LDCad (explican generación path-deform)      |
| Comentarios `0 // 0`  | casi universal en 10252 — separadores semánticos de sección |

**Patrón de header oficial vs custom:**
- Oficial: `0 Name: 24599.dat` — sólo nombre
- Custom: `0 FILE 10252 - 24599.dat` ← declarado con el prefijo del set para evitar colisiones
         `0 Name: 10252 - 24599.dat` ← el name real LDraw-compatible también lleva el prefijo

### 4.3 Ubicación de almacenamiento

| Carpeta                | Cuándo se usa                                                                 | Casos en 10252            |
|------------------------|-------------------------------------------------------------------------------|---------------------------|
| Raíz (sin prefijo)     | Partes que se referencian directamente desde los `.ldr` con `1 16 ... 10252 - X.dat` | 24599, 10252_towel, 24246, 23443, 24607, 98138p81/p82, 6153754* |
| `s\`                   | Subpartes que solo se referencian desde otra custom part (nunca desde .ldr)   | s\24599s01.dat, s\24246s01.dat |
| `48\`                  | Primitivas hi-res usadas por subpartes curvas                                 | 48\t08o2500.dat (torus)   |

**Nunca** se ve una subparte `s\` referenciada directamente desde un `.ldr` de paso. Las `48\` tampoco — son alcance exclusivo de las subpartes.

### 4.4 Descomposición en subpartes

Observado en 10252:

| Parte principal | Subparte(s) | Justificación |
|-----------------|-------------|---------------|
| 24599.dat (23 líneas) | s\24599s01.dat (791) | brick 5×5 corner es simétrico → una "mitad" rotada + reflejada forma la pieza completa |
| 24246.dat (12 líneas) | s\24246s01.dat (41)  | la cara superior redondeada se construye una vez y se referencia |

**No se observa** descomposición en 3+ subpartes. Las piezas verdaderamente grandes (>500 líneas) son single-file (ej. `s\24599s01.dat` mismo, o `48\t08o2500.dat` con 252 líneas). La división se hace **solo cuando hay simetría clara** que el autor quiere explotar.

### 4.5 Patrones de nomenclatura

Verificados en todos los `.dat` embebidos:

| Forma                       | Significado                                                | Ejemplos                              |
|-----------------------------|------------------------------------------------------------|---------------------------------------|
| `NNNNN.dat`                 | Parte principal                                            | `24599.dat`, `24246.dat`, `23443.dat`, `24607.dat` |
| `NNNNNsNN.dat` (en `s\`)    | Subparte N de la parte NNNNN                               | `s\24599s01.dat`, `s\24246s01.dat`    |
| `NNNNNpNN.dat`              | Variante de decoración/printed de la parte NNNNN           | `98138p81.dat`, `98138p82.dat`        |
| `8digits[a-z].dat`          | Variantes sticker (mismo prefijo, sufijo letra)            | `6153754q.dat`, `6153754o.dat`, …     |
| `description.dat`           | Naming "descriptivo" usado por LDCad                       | `ldcRigid3mmHoseCap.dat`              |
| `t08o2500.dat` (en `48\`)   | Primitiva hi-res catálogo LDraw oficial, reusada          | `48\t08o2500.dat` (torus hi-res)      |

**Convención de nombre en el FILE/Name:** siempre `"{set_number} - {original_name}"` (ej. `10252 - 24599.dat`). Esto evita colisiones con la biblioteca oficial.

---

## 5. Reglas inferidas

1. **Custom parts simples (<40 líneas)** suelen ser **composiciones de primitivas escaladas con override de color** (ver `10252_towel.dat`: 38 líneas, 0 geometría propia, 22 cilindros). El header puede incluso omitir `BFC` y `!LDRAW_ORG` cuando no hay CSG.

2. **Custom parts medias (40-150 líneas)** mezclan 1-3 primitivas, un subconjunto de tipo 2/3/4 y un `BFC CERTIFY CCW`. Ejemplo: `23443.dat` (133 líneas, 19 tipo 1 + 34 tipo 2 + 30 tipo 4 + 22 tipo 5).

3. **Custom parts complejas (>150 líneas)** o se mantienen single-file (`48\t08o2500.dat`, 252 líneas) o se **dividen en UNA subparte `s\X - Xs01.dat`** que concentra la geometría curva. La parte principal pasa a ser un wrapper de 10-25 líneas que refleja/rota la subparte (caso `24599.dat` ↔ `s\24599s01.dat`).

4. **Curvatura suave = primitivas hi-res `48\`**. La única `48\` observada (`t08o2500.dat`) es un toro hi-res usado para construir la curvatura del ladrillo en esquina. La regla: si la pieza tiene una superficie curva de radio pequeño, se carga desde `48\`; si es eje-recta o polígono plano, basta con primitivas estándar.

5. **Los nombres siguen un patrón fijo**: `FILE/Name: "{set} - {ldraw_name}.dat"`. La parte `ldraw_name` puede ser (a) el ID oficial (`24599.dat`), (b) un nombre descriptivo del autor (`10252_towel.dat`, `ldcRigid3mmHoseCap.dat`), (c) el ID + sufijo de decoración `pNN`/`q`/`o`…, o (d) el nombre hi-res estándar reusado (`t08o2500.dat`). **Nunca** se duplica el `FILE` con sólo el nombre oficial — siempre se antepone el set.

6. **Subpartes en `s\` son alcance privado**: solo las referencia otra custom part embebida, nunca un `.ldr` del set. Equivalen a funciones helper del archivo.

7. **Las "decoraciones" (`p`/`q`/stickers, 10 archivos en 10252) son overlays 2D**, no geometría real: 0 tipo 1 (excepto una referencia al sustrato tipo `box5-12.dat`), docenas de triángulos tipo 3 y quads tipo 4, todo bajo `0 BFC NOCLIP`. Sirven para estarcir el patrón (logo VW, parabrisas, texto "Al's BOARDS") sobre una parte base ya existente.

---

## Anexo: comparativa 10218 vs 10252

10218 (Pet Shop) sólo embebe **3 archivos**, todos del autor `LDCad` y usados como **donantes para path-deform** (generador procedural de mangueras dentro del editor LDCad):

| Archivo                     | Rol                                         |
|-----------------------------|---------------------------------------------|
| `ldcRigid3mmHoseSeg.dat`    | Segmento recto de manguera rígida           |
| `ldcRigid3mmHoseCap.dat`    | Tapa del extremo                            |
| `ldcConRing-4-4.dat`        | Anillo de conditional lines entre segmentos |

Confirma la regla 6: son private donors para generar la manguera neumática del set, y `ldcConRing-4-4.dat` es prácticamente una primitiva (16 `5 24`).
