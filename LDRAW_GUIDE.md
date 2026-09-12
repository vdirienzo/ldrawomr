# LDraw — Complete Guide to Designing LEGO Parts and Models Virtually

> Reference document created from the official documentation at
> [LDraw.org](https://ldraw.org). Covers the file format, primitives, the
> parts library, naming, headers, coloring, culling, MPDs and models.
> Designed as a foundation for creating and understanding LEGO parts and
> virtual models in the LDraw format.

---

## 1. What is LDraw?

LDraw™ is an **open standard** for LEGO CAD programs created by
James Jessiman in 1995. It enables:

- Documentar models LEGO físicos.
- Crear instructions de construcción type LEGO.
- render imágenes 3D foto-realistas.
- Hacer animaciones.

The current official library contains **17,116 unique shapes/patterns**.

- Web: <https://ldraw.org>
- Documentación: <https://www.ldraw.org/docs-main.html>
- library/descargas: <https://library.ldraw.org>
- Wiki: <https://wiki.ldraw.org>
- Foros: <https://forums.ldraw.org>
- Mirror oficial en GitHub: <https://github.com/pybricks/ldraw>

---

## 2. Library directory structure

```
LDRAW/
├─ parts/             ← parts terminadas (.dat)      ej: 3004.dat (Brick 1x2)
├─ parts/s/           ← subparts                    ej: s\3004s01.dat
├─ p/                 ← primitives baja resolución   ej: stud.dat, box5.dat
├─ p/48/              ← primitives alta resolución   ej: 48\hires.dat
├─ models/            ← models del usuario (.ldr/.mpd)
└─ LDConfig.ldr       ← definition de colors
```

Reglas de nombres (oficial): **solo `a-z`, `0-9`, `_`, `-`; máx 25 caracteres;
sin distinción de mayúsculas** (pero todo en minúsculas por convención).

---

## 3. Coordinate system and LDU unit

```
        -Y (arriba)
         │
         │
         └────► +X
        ╱
       ╱
      +Z
```

- Sistema **dextrógiro**, con `-Y` hacia arriba.
- `+X` a la derecha, `+Z` hacia el frente, `-Y` arriba.

### LDraw Unit (LDU)

| Pieza real             | Tamaño en LDU |
|------------------------|---------------|
| 1 brick width/depth | 20            |
| 1 altura de brick      | 24            |
| 1 altura de plate      | 8             |
| 1 diámetro de stud     | 12            |
| 1 altura de stud       | 4             |

Aproximación: 1 LDU ≈ 1/64 in ≈ 0.4 mm (usar solo para detalles pequeños).

### Default origin and orientation of a part

- **Studs arriba** → `-Y`.
- **tubes abajo** → `+Y`.
- origin: **centro del grupo de studs superior** (la base de los studs en `y=0`).
- For hinge parts: origin at the rotation point.

---

## 4. Line types

Each line of the file starts with an integer indicating its type. Si el type es
inválido, la line se ignora.

| type | Significado                          |
|------|--------------------------------------|
| 0    | Comentario o comando META            |
| 1    | reference a sub-file (instancia) |
| 2    | line (edge)                         |
| 3    | triangle                            |
| 4    | quadrilateral (quad)                  |
| 5    | line optional (conditional line)    |

files basados en texto, **UTF-8 sin BOM**, lines terminadas en `<CR><LF>`.
Un comando por line, tokens separados por espacios/tabs.

### 4.1 Line Type 0 — Comment / META

```
0 // this is a comment (preferred)
0 this is a comment (deprecated)
0 !<META_CMD> <args...>
```

If the **first line** of the file is `0 <text>`, that text is the **file
title** (description of the part).

examples de META oficiales: `!LDRAW_ORG`, `!LICENSE`, `!HELP`, `BFC`, `!CATEGORY`,
`!KEYWORDS`, `!HISTORY`, `!PREVIEW`, `!CMDLINE`, `STEP`, `WRITE`, `CLEAR`,
`PAUSE`, `SAVE`, `FILE` (MPD), `!DATA` (MPD), `!:` (MPD), `NOFILE` (MPD),
`!COLOUR`, `!TEXMAP START/END`, etc.

### 4.2 Line Type 1 — Sub-file reference (piece instance)

```
1 <color> x y z  a b c  d e f  g h i  <file>
```

- <color> = color code.
- `x y z` = translation (in LDU).
- `a b c / d e f / g h i` = matrix 3×3 de rotation/scaled (top-left de la
  matrix 4×4 homogénea). La transformación es:

```
u' = a*u + b*v + c*w + x
v' = d*u + e*v + f*w + y
w' = g*u + h*v + i*w + z
```

- `<file>` = ruta al sub-file (busca en `parts/`, `p/`, `parts/s/`,
  `models/`, ruta relativa o ruta completa).

**example** (colocar un brick azul 1×2 en origin, sin rotate):

```
1 1 0 0 0  1 0 0  0 1 0  0 0 1  3004.dat
```

**No usar color 24** en una line type 1 (resultado indefinido).

### 4.3 Line Type 2 — Line

```
2 <color> x1 y1 z1  x2 y2 z2
```

- color only, two endpoints. Usada típicamente para **edges (edges) con
  color 24**. No todos los renderers la muestran.

### 4.4 Line Type 3 — Triangle

```
3 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3
```

- Filled triangle, 3 vertices in CW or CCW order (see BFC).

### 4.5 Line Type 4 — Quadrilátero

```
4 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3  x4 y4 z4
```

- 4 coplanar vertices. CW or CCW order.
- **prohibited**: vertices colineales, cóncavos, "bow-tie". Cada ángulo interior
  entre 0.025° y 179.9°.
- **important**: polygons adyacentes deben **compartir vertices** para evitar
  el "dot creep" (huecos por truncado entero en el render).

### 4.6 Line Type 5 — Conditional Line (optional)

```
5 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3  x4 y4 z4
```

- `p1`, `p2` = endpoints de la line.
- `p3`, `p4` = points de control.
- La line `p1-p2` **se dibuja solo si `p3` y `p4` están en el mismo lado** de
  la line imaginaria `p1-p2` (proyectada en display). Sirve para perfilar
  siluetas curvas (ej. bordes de cylinders).

---

## 5. Colors

### 5.1 Reserved colors

| code | Significado                                                                       |
|--------|-----------------------------------------------------------------------------------|
| 16     | **Main color / current color**. Hereda el color de la line type 1 que lo instanció. |
| 24     | **Edge / complement color**. Se sustituye por el color de borde definido en el LDConfig. |

**Recommendation**: for type-1 lines, use the actual color; for primitives
always use color 16 so the part takes the color when instantiated. For edges,
use 24.

### 5.2 Direct colors

Allow a literal RGB:

```
1 0x2RRGGBB  x y z  a b c  d e f  g h i  file.dat
```

`0x2` + 6 uppercase hex digits. E.g. `0x2008000` = dark green
(R=0, G=128, B=0). **Discouraged in models** (use `LDConfig.ldr`).

### 5.3 color Definition (!COLOUR)

Colors are defined with the `!COLOUR` meta (in `LDConfig.ldr`):

```
0 !COLOUR Black CODE 0 VALUE #1B2A34 EDGE #808080
0 !COLOUR Red   CODE 4 VALUE #B40000 EDGE #333333
0 !COLOUR Trans_Red CODE 36 VALUE #C91A09 EDGE #660D05 ALPHA 128
```

Tags: `CODE`, `VALUE` (RGB hex with `#` or `0x`), `EDGE`, `ALPHA` (0–255;
128 = standard transparency), `LUMINANCE`, and a finish: `CHROME`,
`PEARLESCENT`, `RUBBER`, `MATTE_METALLIC`, `METAL`, `MATERIAL` (`GLITTER`,
`SPECKLE`, `FABRIC`).

Las definiciones de colors están en scope desde donde aparecen hasta el final
del file, y se transmiten a sub-files. `LDConfig.ldr` es global.

### 5.4 colors más comunes (LDConfig.ldr)

| Code | Nombre              | Code | Nombre              |
|------|---------------------|------|---------------------|
| 0    | Black               | 14   | Yellow              |
| 1    | Blue                | 15   | White               |
| 2    | Green               | 19   | Tan                 |
| 3    | Dark_Turquoise      | 25   | Orange              |
| 4    | Red                 | 27   | Lime                |
| 5    | Dark_Pink           | 28   | Dark_Tan            |
| 6    | Brown               | 70   | Reddish_Brown       |
| 7    | Light_Grey          | 71   | Light_Bluish_Grey   |
| 8    | Dark_Grey           | 72   | Dark_Bluish_Grey    |
| 9    | Light_Blue          | 326  | Yellowish_Green     |
| 10   | Bright_Green        | 36   | Trans_Red           |
| 11   | Light_Turquoise     | 47   | Trans_Clear         |
| 12   | Salmon              | 383  | Chrome              |
| 13   | Pink                | 462  | Medium_Orange       |

(Ver lista completa en `LDConfig.ldr` actual: 200+ colors.)

---

## 6. Primitives — the base for building parts

**Primitives** are reusable low/medium/high-resolution geometric
components stored in `p/` (regular, 16-sided) and `p/48/` (high, 48-sided).

They serve to:

- Speed up authoring (reuse cylinder, stud, rect, etc.).
- allow **primitive substitution** en renderers (sustituir por versiones más
  detalladas).

### 6.1 `box` family — scalable cuboids

Convention: `boxF[-E][modifiers].dat`

- `box.dat` — complete 2×2×2 LDU cube with faces and edges.
- `box0.dat` — edges only (empty box).
- `box5.dat` — cube **sin face superior** (`-y`), origin en centro de la face
  faltante, tamaño 2×1×2.
- `box4.dat` — sin faces superior ni inferior.
- `box4-1.dat`, `box4-2p.dat`, `box4-7a.dat`, etc. — variantes con menos
  edges (para esquinas/empalmes).
- `box3-7a.dat` — sin 3 faces adyacentes (esquina interior).
- `box2-11.dat` — solo dos faces opuestas con su edge common.

### 6.2 `rect` family — 2D rectangles in xz plane

- `rect.dat` — rectangle 2×2 con 4 edges.
- `rect3.dat` — sin edge `-z`.
- `rect2p.dat` — sin edges `±x`.
- `rect2a.dat` — sin dos edges adyacentes.
- `rect1.dat` — solo edge `+x`.

### 6.3 `n-fcyli` family — cylinders (key!)

`n-fcyli.dat` = **fraction n/f** of a complete cylinder. Por defecto radio 1
LDU, tall 1 LDU, en plano xz. Convenciones:

- Centrado en el origin.
- Starts at `+x,0` and progresses **CCW** as seen from above (`-y`).
- **Do not rotate outside 90°/180°** (rounding errors).

Familia 16-lados (regular): `1-16`, `1-8`, `3-16`, `1-4`, `5-16`, `3-8`,
`7-16`, `2-4`, `5-8`, `3-4`, `7-8`, `4-4`.

Familia 48-lados (hi-res, en `48/`):
`4-4cyli`, `4-4edge`, `4-4disc`, `4-4ringN`, `4-4ndis`, `1-4chrd`, etc.

**scaled** (x = z = tall):

```
1 16 0 0 0  20 0 0  0 1 0  0 0 20  4-4edge.dat   ; aro radio 20
1 16 0 0 0   6 0 0  0 -4 0  0 0 6  4-4cyli.dat   ; cylinder radio 6, tall 4
```

### 6.4 `disc` and `ring` family

- `n-fdisc.dat` — sector circular relleno.
- `n-fedge.dat` — arco de círculo (solo edges).
- `n-fchrd.dat` — segmento de disc entre arco y cuerda.
- `n-fcyli.dat` — manto cilíndrico.
- `n-fringN.dat` — anillo con radio interior N, exterior N+1.

### 6.5 `stud` family

- `stud.dat` — plain stud without logo, 1×1, 4 LDU tall, centered.
- `stud2.dat`, `stud3.dat`, `stud4.dat` — hollow studs of various depths.
- `stud-logo.dat`, `stud-logo2.dat` — studs con logo LEGO.
- `stug<N>-<X>x<Z>.dat` — **grupo de studs** (matrix 2D) para colocar varios a
  la vez. `<N>` = type (regular, hueco…), `<X>` × `<Z>` = nº de studs.
  Combinaciones permitidas: `1xZ`, `Xx1`, `XxX` (squares).
- `studa.dat` — stud accessory (tall 8).

### 6.6 `tri3` family — rectangular triangular prisms

- `tri3.dat` — prism triangular 1×1×1, ortogonal en x y z, sin faces
  superior/inferior.
- `tri3-1.dat`, `tri3-3.dat`, `tri3a1.dat`, `tri3a4.dat`, `tri3u3.dat`,
  `tri4.dat` — variantes para empalmes y esquinas.

### 6.7 Cone, torus, special cylinder/chrd

- `n-fconN.dat` — sections cónicas.
- Torus: `1-8torus.dat`, `4-4torus.dat`, `n-ftorus.dat`.
- tubes Technic: `axlehol2.dat`, `axleho9.dat`, etc.
- Pin Technic: `technicpin.dat`, `technicpinhole.dat`.

### 6.8 Primitive scaling rules

- primitives **regulares** (box, rect, cyli, disc): scale **uniformemente en
  x y z** según tamaño. Para cylinders, mismo factor en x y z (radio), libre
  en y (altura).
- primitives con "no scale" (studs, holes, clips, hinges): mantener scale
  1:1.
- 3 decimales bastan en parts normals; 4 en primitives hi-res.

---

## 7. BFC — Back Face Culling

Official parts use **back-face culling** (only front faces are drawn).
Enabled with:

```
0 BFC CERTIFY CCW
```

(antes del primer comando operativo).

Operadores:

- `0 BFC NOCERTIFY` — desactiva BFC para este file.
- `0 BFC CERTIFY [CW|CCW]` — declara file BFC-compliant (CCW por defecto).
- `0 BFC CW` / `0 BFC CCW` — cambia el winding del file en vivo.
- `0 BFC CLIP` / `0 BFC NOCLIP` — activa/desactiva el culling localmente.
- `0 BFC INVERTNEXT` — invierte la siguiente reference sub-file (useful para
  faces interiores de cylinders). **Solo afecta a la line siguiente inmediata**.

### Reglas de winding (CCW por defecto)

Sentido **counter-clockwise** visto desde el lado frontal. Si la matrix de
rotation de la line type 1 tiene **determinante negativo** (refleja el
sub-file), el winding efectivo se invierte automáticamente.

```
            CW (visto de frente)
         1 ─────► 2
         ▲       │
         │       ▼
         4 ◄─────3
```

Las parts se renderizan correctamente si todas las faces miran hacia afuera.

---

## 8. Official Headers (small but important)

An official part follows this order:

```
0 <Description>                ← e.g. "Brick  1 x  2"
0 Name: <filename.dat>
0 Author: <RealName> [<username>]
0 !LDRAW_ORG Part UPDATE YYYY-RR
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt
0 !HELP texto optional (max 50 chars/line)
0 BFC CERTIFY CCW
0 !CATEGORY <category>
0 !KEYWORDS word1, word2, word3
0 !HISTORY YYYY-MM-DD [<user>] descripción
0 // comentarios libres
1 16 ... <pieza base>
```

`!LDRAW_ORG` types:

- `Part`, `Subpart`, `Primitive`, `8_Primitive`, `48_Primitive`, `Shortcut`.
- Versión "Unofficial_*" para parts en el Parts Tracker no oficiales.
- Cualificadores opcionales: `Alias`, `Flexible_Section` (Physical_Colour
  deprecado).

Prefijos en la descripción:

- `~` — subparts, obsoletas, o partes de un ensamblaje.
- `=` — alias.
- `|` o `~|` — partes de terceros.

---

## 9. Part numbering

| Pattern                      | Meaning                                            |
|-----------------------------|--------------------------------------------------------|
| `NNN`, `NNNN`, `NNNNN`      | Official LEGO Design ID                              |
| `NNNa`, `NNNNa`             | Mold variant (a, b, c…)                           |
| `uNNNN.dat`                 | Unknown Design ID (request from admin)             |
| `tNNNN.dat`                 | Third-party part (LEGO-compatible)                    |
| `s/NNNNsNN.dat`             | Subpart of `NNNN.dat`                                 |
| `NNNpCC(C).dat`             | Patterned version (printed)                           |
| `sNNNN.dat`                 | Sticker of unknown sheet                              |
| `NNNcNN.dat` or `-cXX`       | Shortcut (assembly) or flexible variant                |
| `NNNcNN-fN.dat`             | Positional variant (flexible)                         |
| `NNNdNN.dat`                | Shortcut with sticker                                   |
| `NNNkNN.dat`                | Flexible sub-component (hoses, axles)              |
| `stud...dat`                | Primitive                                              |
| `stug*-X*x*Z*.dat`          | Stud group                                         |
| `NNNNN[N]pCC(C).png`        | Texture image (same base number)                      |

Patrones de impresión: el primer dígito del code identifica el tema
(0=misc/Town, 3=Pirates, 4=Castle, 5-6=Space, 7-9=Modern Town, a=Adventurers,
b=Superheroes, cXY=Collectable Minifigures, etc.). Ver detalle en la
[Oficial Library Part Number Specification](https://www.ldraw.org/part-number-spec.html).

### Atajos (Shortcuts)

Cuando LEGO vende varias parts pre-ensambladas, se crea un "shortcut" para
reutilizarlas como un único bloque en los models. Ej: `55969` (sensor de luz
NXT), `53787` (motor NXT completo).

### parts flexibles

Modeladas en su estado plano como file principal, y versiones curvadas
con sufijo `-f1`, `-f2`, etc.

---

## 10. Anatomy of a part — real examples

### 10.1 Brick 2×4 (`3001.dat`) — canonical part

```ldraw
0 Brick  2 x  4
0 Name: 3001.dat
0 Author: James Jessiman
0 !LDRAW_ORG Part UPDATE 2004-03
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt
0 BFC CERTIFY CCW
0 !HISTORY 2002-05-07 {unknown} BFC Certification
…
1 16 0 0 0 1 0 0 0 1 0 0 0 1 s\3001s01.dat    ; ← body del brick (subpart)
4 16 -40 0 -20 -40 24 -20 40 24 -20 40 0 -20   ; ← face -z (inferior)
4 16  40 0  20  40 24 20 -40 24 20 -40 0 20    ; ← face +z (superior)
```

### 10.2 subpart `s\3001s01.dat` (body sin faces)

```ldraw
1 16 0 4 0 1 0 0 0 -5 0 0 0 1 stud3.dat        ; stud interior (centro)
0 BFC INVERTNEXT                                ; invierte el cylinder interior
1 16 0 24 0 16 0 0 0 -20 0 0 0 6 box5.dat      ; caja interna (sin tapa)
4 16 20 24 10 16 24 6 -16 24 6 -20 24 10       ; quads de la corona superior
…
1 16 0 24 0 20 0 0 0 -24 0 0 0 10 box4t.dat    ; caja con face -y y -z fuera
1 16 30 0 -30 1 0 0 0 1 0 0 0 1 stud.dat        ; studs externos (8 en 2x4)
… (8 studs)
```

### 10.3 Stud (`stud.dat`) — essential primitive

```ldraw
0 Stud
0 Name: stud.dat
0 Author: James Jessiman
0 !LDRAW_ORG Primitive UPDATE 2012-01
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt
0 BFC CERTIFY CCW
0 !HISTORY …
1 16 0 0 0 6 0 0 0 1 0 0 0 6 4-4edge.dat    ; aro inferior (y=0, radio 6)
1 16 0 -4 0 6 0 0 0 1 0 0 0 6 4-4edge.dat  ; aro superior (y=-4)
1 16 0 0 0 6 0 0 0 -4 0 0 0 6 4-4cyli.dat  ; manto cilíndrico (tall 4)
1 16 0 -4 0 6 0 0 0 1 0 0 0 6 4-4disc.dat  ; tapa superior
```

### 10.4 Plate 2×2 (`3022.dat`) — uses `box5` and `INVERTNEXT`

```ldraw
0 Plate  2 x  2
0 Name: 3022.dat
…
0 BFC CERTIFY CCW
1 16 0 4 0 1 0 0 0 -1 0 0 0 1 stud4.dat       ; hueco interior de studs
0 BFC INVERTNEXT                                ; invierte para mirar hacia adentro
1 16 0 8 0 16 0 0 0 -4 0 0 0 16 box5.dat      ; caja interna invertida
4 16 20 8 20 16 8 16 -16 8 16 -20 8 20         ; quads del rim
…
1 16 0 8 0 20 0 0 0 -8 0 0 0 20 box5.dat       ; caja exterior
1 16 10 0 10 1 0 0 0 1 0 0 0 1 stud.dat        ; studs externos (4)
…
```

**Key pattern**: each part is a **composition** of scaled primitives +
own quads (top rim) + studs. Los huecos entre studs usan
`0 BFC INVERTNEXT` para invertir la normal de la primitive interior.

---

## 11. MPD — Multi-Part Documents

Un **.mpd** agrupa varios files LDraw en uno solo, separados por
`0 FILE <nombre>` o `0 !DATA <nombre>`:

```
0 FILE main.ldr
1 7 0 0 0 1 0 0 0 1 0 0 0 1 819.dat
1 4 80 -8 70 1 0 0 0 1 0 0 0 1 house.ldr     ; ← reference a sub-model

0 FILE house.ldr                                ; ← inicio del sub-model
1 16 0 0 0 1 0 0 0 1 0 0 0 1 3023.dat
…

0 FILE sticker.ldr
…

0 !DATA sticker.png
0 !: iVBORw0KGgoAAAA...                          ; PNG en base64
0 !: jwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQ...
…
```

Meta MPD: `0 FILE`, `0 !DATA`, `0 !: <base64>`, `0 NOFILE`.
El primer bloque es el **model principal**; los demás solo se renderizan si
están referenciados.

Esto permite empaquetar un set LEGO completo (varios .ldr + parts oficiales)
en **un único file** para distribuir.

---

## 12. models — cómo se arman

Un model (`.ldr`) es una secuencia de lines type 1 que **posicionan y
rotan parts de la library**. example (`car.ldr`):

```
0 Example Car for Demonstration of LDRAW Library
0 Name: car.ldr
0 Author: James Jessiman

1 0 0 0 -90  1 0 0  0 1 0  0 0 1  4315.dat      ; wheel negra, pos (0,0,-90)
1 7 0 0 -60  1 0 0  0 1 0  0 0 1  4600.dat      ; llanta gris, pos (0,0,-60)
1 0 0 0   0  1 0 0  0 1 0  0 0 1  3031.dat      ; brick 4x2 negro en origin
…

0 STEP                                          ; ← fin del paso 1
1 46 30 -8 -90  1 0 0  0 1 0  0 0 1  3024.dat   ; paso 2…
1 46 -30 -8 -90 1 0 0  0 1 0  0 0 1  3024.dat
…

0 STEP                                          ; ← fin del paso 2
1 4 0 -16 -30  1 0 0  0 1 0  0 0 1  3829c01.dat
```

**Comandos importantes en models**:

- `1 <color> x y z a b c d e f g h i <file>` — colocar una pieza.
- `0 STEP` — marca fin de paso de construcción.
- `0 FILE <name>` / `0 NOFILE` — delimitan sub-models dentro de MPD.
- `0 !COLOUR ...` — definir colors locales.
- `0 BFC ...` — activar culling.

**Cómo encajan las parts**: por **estándar geométrico**:

- Studs (cylinders Ø12, tall 4) encajan en tubes (huecos cilíndricos Ø12,
  profundidad 4) en las faces opuestas.
- Studs encajan sobre studs si la pieza lo permite (rotation 0°).
- Tubes y studs están separados **20 LDU** en X/Z (centros de stud).
- Los axes Technic (Ø5) encajan en cross-holes.

**Para colocar una pieza exactamente**:

1. Decide la position del origin (centro de la base de studs).
2. translation: `x y z` en LDU (multiplica studs por 20, plates por 8).
3. rotation: matrix identidad `1 0 0  0 1 0  0 0 1` por defecto. Para
   rotate 90° alrededor de Y: `0 0 -1  0 1 0  1 0 0`. Para voltear: determinante
   negativo (cuidado con la normal — BFC se ajusta solo).
4. color: del 0–215+ según `LDConfig.ldr`.

### example: muro 2×2 en azul

```
0 Name: muro.ldr

; Base de plates 2x2
1 1 0 0 0 1 0 0 0 1 0 0 0 1 3022.dat   ; plate 2x2 azul
1 1 0 -8 0 1 0 0 0 1 0 0 0 1 3022.dat  ; segunda plate 8 LDU arriba
1 1 0 -16 0 1 0 0 0 1 0 0 0 1 3022.dat ; tercera plate
0 STEP

; Brick 2x2 encima
1 1 0 -40 0 1 0 0 0 1 0 0 0 1 3003.dat ; brick 2x2 azul (tall 24)
0 STEP
```

### Reglas prácticas

- **Vertical fit**: studs down (`-y`) ↔ tubes up. Sum heights in `y`.
- **Side fit**: a Technic part with axle hole (Ø5) accepts an axle.
- **Clip fit**: studied in `clip*` and `clikits*` primitives.
- **rotation 90° vs 180°**: usar matrices con determinante ±1, evitar
  rotations extrañas (preferable `cyli/4` nativo o `cyli/16` a 22.5°).

---

## 13. Stickers (calcomanías)

- Geometría: caja fina de **0.25 LDU** de grosor, con `!TEXMAP START PLANAR`
  aplicando una imagen PNG encima.
- face superior a `y = -0.25`, paralela a X-Z.
- color 16 (current color) en lados y face inferior; el patrón en la face
  superior.
- Orientación: el "arriba" del gráfico alineado con `+Z`.
- Backing box (lateral/inferior) según [Sticker Box Standard](https://www.ldraw.org/docs-main/ldraw-org-official-library-standards/sticker-box-standard.html).
- `0 BFC NOCLIP` antes del patrón, `0 BFC CLIP` después (si hay geometría
  no-patrón después).

---

## 14. Categorías y palabras clave

`!CATEGORY` define la categoría principal (Brick, Plate, Slope, Tile,
Technic, Minifig, Wheel, Hinge, Animal, Sticker, …). Lista completa en
la [especificación](https://www.ldraw.org/article/340.html).

`!KEYWORDS` son términos libres para búsqueda (separados por comas, máx
80 chars/line, sin incluir el nombre de la pieza).

---

## 15. Cualificadores opcionales para parts oficiales

- `Alias` — pieza visualmente idéntica a otra con distinto nº.
- `Flexible_Section` — sub-componente de pieza flexible.
- `Physical_Colour` (deprecado).

---

## 16. OMR — Official Model Repository

models oficiales de sets LEGO documentados siguen el
[OMR Spec](https://www.ldraw.org/article/593.html):

- Nombre: `<SetNumber>[-<Qualifier>] - <SetName>[ - <SubModel>].mpd`
- Cabecera estándar con `!LDRAW_ORG Model` o `!LDRAW_ORG Unofficial_Model`.
- Cada sub-model en su propio `0 FILE` dentro del MPD.
- prohibited espejado (rompe el logo y el BOM).
- parts no oficiales: incluir el `.dat` como sub-file renombrado dentro
  del MPD.

---

## 17. Plantilla mínima — cómo crear una pieza desde cero

Pasos (resumen):

1. **Decide origin y orientación**:
   - Studs up (`-y`).
   - Base de studs en `y=0`.
   - Centro del grupo de studs en X=0, Z=0.

2. **Elige primitives**:
   - body principal → `box5`/`box4-7a`/`boxjcyl4` escalados.
   - Hueco central para studs → `box5` invertido con `0 BFC INVERTNEXT`.
   - Studs externos → `1 16 x 0 z 1 0 0 0 1 0 0 0 1 stud.dat` (color 16).
   - Studs internos → `stud3.dat`, `stud4.dat`.

3. **Añade quads para el rim superior** (entre las dos filas de studs):
   - 4 quads `4 16 x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4`.
   - Orden CW o CCW desde arriba.

4. **Escribe el header** completo (ver §8).

5. **Verifica BFC** con una herramienta (LDView, BFC testing) — debe pasar
   `CERTIFY CCW`.

### Mini-example: brick 1×1 personalizado

```ldraw
0 Brick  1 x  1 Custom
0 Name: u9001.dat
0 Author: Mi Nombre [miuser]
0 !LDRAW_ORG Part UPDATE 2026-01
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt

0 BFC CERTIFY CCW

0 !CATEGORY Brick
0 !KEYWORDS custom, test

0 !HISTORY 2026-09-11 [miuser] Initial creation

; tube interior (anti-stud)
0 BFC INVERTNEXT
1 16 0 24 0 8 0 0 0 -20 0 0 0 4 box5.dat

; Caja exterior
1 16 0 24 0 10 0 0 0 -24 0 0 0 6 box5.dat

; Stud superior
1 16 0 0 0 1 0 0 0 1 0 0 0 1 stud.dat
```

Este brick 1×1 simple queda definido con solo **3 sub-files + 2 lines de
meta**. Las primitives escaladas generan toda la geometría; el stud queda en
el origin; el tube interior invertido crea el hueco para encajar.

---

## 18. Mini-example: armar un model (`.ldr`)

```ldraw
0 My First Build
0 Name: build.ldr
0 Author: Mi Nombre [miuser]
0 !LDRAW_ORG Model

; Fila base: dos plates 2x4
1 4 -20 0 0 1 0 0 0 1 0 0 0 1 3022.dat    ; plate 2x2 roja a la izquierda
1 4  20 0 0 1 0 0 0 1 0 0 0 1 3022.dat    ; plate 2x2 roja a la derecha
0 STEP

; Fila media: dos bricks 2x2
1 1 -20 -8 0 1 0 0 0 1 0 0 0 1 3003.dat    ; brick 2x2 azul
1 1  20 -8 0 1 0 0 0 1 0 0 0 1 3003.dat
0 STEP

; Tope: un brick 2x4
1 14 0 -32 0 1 0 0 0 1 0 0 0 1 3001.dat    ; brick 2x4 amarillo
0 STEP

0 NOFILE
```

Este model es apilable: cada pieza se coloca con su origin en el centro del
grupo de studs. Las plates están a `y=0`, `y=-8`, y el brick a `y=-8-24=-32`.

---

## 19. Recursos y referencias

| Resource                                       | URL                                                  |
|-----------------------------------------------|------------------------------------------------------|
| Official website                              | <https://ldraw.org>                                  |
| Documentation                                 | <https://www.ldraw.org/docs-main.html>               |
| Online library (search and download)       | <https://library.ldraw.org>                          |
| Wiki                                          | <https://wiki.ldraw.org>                             |
| Forums                                         | <https://forums.ldraw.org>                           |
| GitHub mirror                                 | <https://github.com/pybricks/ldraw>                  |
| Tutorials                                    | <http://wiki.ldraw.org/index.php?title=Category:Tutorials> |
| Part authoring tutorial (Holly-Wood)         | <https://www.holly-wood.it/ldraw/authoring-en.html> |
| LDCad (recommended editor)                    | <https://www.melvintec.com/ldcad>                    |
| LDView (viewer)                                | <https://tcobbs.github.io/ldview/>                   |
| LeoCAD (another editor)                          | <https://www.leocad.org>                             |
| MLCad (classic editor, discontinued)         | <https://mlcad.lm-software.com>                      |
| Complete file format spec              | <https://www.ldraw.org/article/218.html>             |
| BFC spec                                      | <https://www.ldraw.org/article/415.html>             |
| Colors spec                                  | <https://www.ldraw.org/article/299.html>             |
| Header spec                                   | <https://www.ldraw.org/article/398.html>             |
| Numbering spec                               | <https://www.ldraw.org/part-number-spec.html>        |
| MPD spec                                      | <https://www.ldraw.org/article/47.html>              |
| OMR spec                                      | <https://www.ldraw.org/article/593.html>             |
| Primitive Reference                           | <https://wiki.ldraw.org/wiki/Primitives_Reference>   |
| Colour chart                                  | <https://www.ldraw.org/article/547.html>             |

---

## 20. Resumen ejecutivo — recetas rápidas

| I need to…                              | Solution                                                          |
|----------------------------------------|-------------------------------------------------------------------|
| Create a new brick                   | Compose with `box5` (outer) + inverted `box5` (tube) + N studs |
| Place a stud                        | `1 16 x 0 z 1 0 0 0 1 0 0 0 1 stud.dat`                           |
| Place a group of studs              | Use `stug-2x2.dat`, `stug-3x1.dat`, etc.                         |
| Make a cylinder of radius N height M    | `1 16 0 0 0 N 0 0 0 M 0 0 0 N 4-4cyli.dat`                       |
| Make a ring of radius R                | `1 16 0 0 0 R 0 0 0 1 0 0 0 R 4-4edge.dat`                        |
| Connect a piece on top (fit)     | Sum 24 (brick) or 8 (plate) to `y` of next piece         |
| Connect to the side (stud ↔ stud fit)  | Sum ±20 to `x` or `z` (stud centers)                          |
| Fit a Technic axle                | Use Technic part with `axlehol2.dat` or cross-hole                |
| Define a local color                 | `0 !COLOUR MiColor CODE 999 VALUE #FF0000 EDGE #800000`           |
| Mark build step            | `0 STEP`                                                          |
| Official part header               | See §8                                                            |
| rotate pieza 90° alrededor de Y         | `1 c 0 0 z 0 0 1 0 1 0 -1 0 0` (CW) o `0 0 -1 0 1 0 1 0 0` (CCW)  |
| Package complete set                | MPD with one `0 FILE` per sub-model                                |
| Activate back face culling              | `0 BFC CERTIFY CCW` at the beginning                                     |

---

## 21. Glosario

- **LDU** — LDraw Unit (0.4 mm).
- **Stud** — protruding cylinder (4 LDU high, 12 LDU Ø).
- **Tube / Anti-stud** — hollow cylinder that fits a stud.
- **Rim** — anillo elevado en la parte superior de bricks/plates (entre filas
  de studs).
- **Primitive** — reusable geometric part from `p/` or `p/48/`.
- **Subpart** — pieza intermedia en `parts/s/`, referenciada por una o más
  partes.
- **Shortcut** — assembly pre-fabricado tratado como una sola pieza
  (`NNNcNN.dat`).
- **Patterned part** — piece with printing (`NNNpCC.dat`).
- **Sticker** — decal applied to a piece.
- **Flexible part** — deformable piece (hoses, fabrics).
- **STEP** — pause/end of step in a model.
- **MPD** — Multi-Part Document, a file with multiple sub-files.
- **BFC** — Back Face Culling, discard back faces.
- **CCW/CW** — winding (counter-clockwise / clockwise) del polygon visto de
  frente.
- **INVERTNEXT** — invert the normal of the next reference.
- **Primitive substitution** — sustitución automática de primitives por
  versiones más detalladas en renderers.
- **Determinant** — `det(M)` of the 3×3 rotation matrix. If <0, reflects.
