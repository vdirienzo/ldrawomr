# LDraw — Guía Completa para diseñar piezas y modelos LEGO virtualmente

> Documento de referencia creado a partir de la documentación oficial de
> [LDraw.org](https://ldraw.org). Cubre el formato de archivo, las primitivas,
> la biblioteca de piezas, el nombrado, los headers, el coloreado, el culling,
> las MPD y los modelos. Pensado como base para crear y entender piezas y
> modelos LEGO virtuales con el formato LDraw.

---

## 1. ¿Qué es LDraw?

LDraw™ es un **estándar abierto** para programas CAD de LEGO creado por
James Jessiman en 1995. Permite:

- Documentar modelos LEGO físicos.
- Crear instrucciones de construcción tipo LEGO.
- Renderizar imágenes 3D foto-realistas.
- Hacer animaciones.

La biblioteca oficial actual contiene **17 116 formas/patrones únicos**.

- Web: <https://ldraw.org>
- Documentación: <https://www.ldraw.org/docs-main.html>
- Biblioteca/descargas: <https://library.ldraw.org>
- Wiki: <https://wiki.ldraw.org>
- Foros: <https://forums.ldraw.org>
- Mirror oficial en GitHub: <https://github.com/pybricks/ldraw>

---

## 2. Estructura de la biblioteca en disco

```
LDRAW/
├─ parts/             ← piezas terminadas (.dat)      ej: 3004.dat (Brick 1x2)
├─ parts/s/           ← subpartes                    ej: s\3004s01.dat
├─ p/                 ← primitivas baja resolución   ej: stud.dat, box5.dat
├─ p/48/              ← primitivas alta resolución   ej: 48\hires.dat
├─ models/            ← modelos del usuario (.ldr/.mpd)
└─ LDConfig.ldr       ← definición de colores
```

Reglas de nombres (oficial): **solo `a-z`, `0-9`, `_`, `-`; máx 25 caracteres;
sin distinción de mayúsculas** (pero todo en minúsculas por convención).

---

## 3. Sistema de coordenadas y unidad LDU

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

### Unidad LDraw (LDU)

| Pieza real             | Tamaño en LDU |
|------------------------|---------------|
| 1 ancho/prof. de brick | 20            |
| 1 altura de brick      | 24            |
| 1 altura de plate      | 8             |
| 1 diámetro de stud     | 12            |
| 1 altura de stud       | 4             |

Aproximación: 1 LDU ≈ 1/64 in ≈ 0.4 mm (usar solo para detalles pequeños).

### Origen y orientación por defecto de una pieza

- **Studs arriba** → `-Y`.
- **Tubos abajo** → `+Y`.
- Origen: **centro del grupo de studs superior** (la base de los studs en `y=0`).
- Para piezas con bisagras: origen en el punto de rotación.

---

## 4. Tipos de línea (line types)

Cada línea del archivo empieza con un entero que indica su tipo. Si el tipo es
inválido, la línea se ignora.

| Tipo | Significado                          |
|------|--------------------------------------|
| 0    | Comentario o comando META            |
| 1    | Referencia a sub-archivo (instancia) |
| 2    | Línea (edge)                         |
| 3    | Triángulo                            |
| 4    | Cuadrilátero (quad)                  |
| 5    | Línea opcional (conditional line)    |

Archivos basados en texto, **UTF-8 sin BOM**, líneas terminadas en `<CR><LF>`.
Un comando por línea, tokens separados por espacios/tabs.

### 4.1 Line Type 0 — Comentario / META

```
0 // esto es un comentario (preferido)
0 esto es un comentario (deprecado)
0 !<META_CMD> <args...>
```

Si la **primera línea** del archivo es `0 <texto>`, ese texto es el **título
del archivo** (descripción de la pieza).

Ejemplos de META oficiales: `!LDRAW_ORG`, `!LICENSE`, `!HELP`, `BFC`, `!CATEGORY`,
`!KEYWORDS`, `!HISTORY`, `!PREVIEW`, `!CMDLINE`, `STEP`, `WRITE`, `CLEAR`,
`PAUSE`, `SAVE`, `FILE` (MPD), `!DATA` (MPD), `!:` (MPD), `NOFILE` (MPD),
`!COLOUR`, `!TEXMAP START/END`, etc.

### 4.2 Line Type 1 — Sub-file reference (instancia de pieza)

```
1 <color> x y z  a b c  d e f  g h i  <archivo>
```

- `<color>` = nº de color.
- `x y z` = traslación (en LDU).
- `a b c / d e f / g h i` = matriz 3×3 de rotación/escalado (top-left de la
  matriz 4×4 homogénea). La transformación es:

```
u' = a*u + b*v + c*w + x
v' = d*u + e*v + f*w + y
w' = g*u + h*v + i*w + z
```

- `<archivo>` = ruta al sub-archivo (busca en `parts/`, `p/`, `parts/s/`,
  `models/`, ruta relativa o ruta completa).

**Ejemplo** (colocar un brick azul 1×2 en origen, sin rotar):

```
1 1 0 0 0  1 0 0  0 1 0  0 0 1  3004.dat
```

**No usar color 24** en una línea tipo 1 (resultado indefinido).

### 4.3 Line Type 2 — Línea

```
2 <color> x1 y1 z1  x2 y2 z2
```

- Solo color, dos extremos. Usada típicamente para **aristas (edges) con
  color 24**. No todos los renderers la muestran.

### 4.4 Line Type 3 — Triángulo

```
3 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3
```

- Triángulo relleno, 3 vértices en orden CW o CCW (ver BFC).

### 4.5 Line Type 4 — Quadrilátero

```
4 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3  x4 y4 z4
```

- 4 vértices coplanarios. Orden CW o CCW.
- **Prohibido**: vértices colineales, cóncavos, "bow-tie". Cada ángulo interior
  entre 0.025° y 179.9°.
- **Importante**: polígonos adyacentes deben **compartir vértices** para evitar
  el "dot creep" (huecos por truncado entero en el render).

### 4.6 Line Type 5 — Línea condicional (opcional)

```
5 <color> x1 y1 z1  x2 y2 z2  x3 y3 z3  x4 y4 z4
```

- `p1`, `p2` = extremos de la línea.
- `p3`, `p4` = puntos de control.
- La línea `p1-p2` **se dibuja solo si `p3` y `p4` están en el mismo lado** de
  la línea imaginaria `p1-p2` (proyectada en pantalla). Sirve para perfilar
  siluetas curvas (ej. bordes de cilindros).

---

## 5. Colores

### 5.1 Colores reservados

| Código | Significado                                                                       |
|--------|-----------------------------------------------------------------------------------|
| 16     | **Main color / current color**. Hereda el color de la línea tipo 1 que lo instanció. |
| 24     | **Edge / complement color**. Se sustituye por el color de borde definido en el LDConfig. |

**Recomendación**: en líneas tipo 1, usar el color real; en primitivas usar
siempre color 16 para que la pieza tome el color al instanciarla. Para aristas
usar 24.

### 5.2 Colores directos (Direct Colours)

Permiten un RGB literal:

```
1 0x2RRGGBB  x y z  a b c  d e f  g h i  archivo.dat
```

`0x2` + 6 dígitos hex en mayúsculas. Ej: `0x2008000` = verde oscuro
(R=0, G=128, B=0). **Desaconsejado en modelos** (usar `LDConfig.ldr`).

### 5.3 Definición de colores (!COLOUR)

Los colores se definen con la meta `!COLOUR` (en `LDConfig.ldr`):

```
0 !COLOUR Black CODE 0 VALUE #1B2A34 EDGE #808080
0 !COLOUR Red   CODE 4 VALUE #B40000 EDGE #333333
0 !COLOUR Trans_Red CODE 36 VALUE #C91A09 EDGE #660D05 ALPHA 128
```

Tags: `CODE`, `VALUE` (RGB hex con `#` o `0x`), `EDGE`, `ALPHA` (0–255;
128 = transparente estándar), `LUMINANCE`, y un acabado: `CHROME`,
`PEARLESCENT`, `RUBBER`, `MATTE_METALLIC`, `METAL`, `MATERIAL` (`GLITTER`,
`SPECKLE`, `FABRIC`).

Las definiciones de colores están en scope desde donde aparecen hasta el final
del archivo, y se transmiten a sub-archivos. `LDConfig.ldr` es global.

### 5.4 Colores más comunes (LDConfig.ldr)

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

(Ver lista completa en `LDConfig.ldr` actual: 200+ colores.)

---

## 6. Primitivas — la base para construir piezas

Las **primitivas** son componentes geométricos reusables de baja/media/alta
resolución guardados en `p/` (regular, 16 lados) y `p/48/` (alta, 48 lados).

Sirven para:

- Acelerar la autoría (reutilizar cilindro, stud, rect, etc.).
- Permitir **primitive substitution** en renderers (sustituir por versiones más
  detalladas).

### 6.1 Familia `box` — cuboides escalables

Convención: `boxF[-E][modificadores].dat`

- `box.dat` — cubo completo 2×2×2 LDU con caras y aristas.
- `box0.dat` — solo aristas (caja vacía).
- `box5.dat` — cubo **sin cara superior** (`-y`), origen en centro de la cara
  faltante, tamaño 2×1×2.
- `box4.dat` — sin caras superior ni inferior.
- `box4-1.dat`, `box4-2p.dat`, `box4-7a.dat`, etc. — variantes con menos
  aristas (para esquinas/empalmes).
- `box3-7a.dat` — sin 3 caras adyacentes (esquina interior).
- `box2-11.dat` — solo dos caras opuestas con su arista común.

### 6.2 Familia `rect` — rectángulos 2D en plano xz

- `rect.dat` — rectángulo 2×2 con 4 aristas.
- `rect3.dat` — sin arista `-z`.
- `rect2p.dat` — sin aristas `±x`.
- `rect2a.dat` — sin dos aristas adyacentes.
- `rect1.dat` — solo arista `+x`.

### 6.3 Familia `n-fcyli` — cilindros (¡clave!)

`n-fcyli.dat` = **fracción n/f** de un cilindro completo. Por defecto radio 1
LDU, alto 1 LDU, en plano xz. Convenciones:

- Centrado en el origen.
- Empieza en `+x,0` y avanza **CCW** visto desde arriba (`-y`).
- **No rotar fuera de 90°/180°** (errores de redondeo).

Familia 16-lados (regular): `1-16`, `1-8`, `3-16`, `1-4`, `5-16`, `3-8`,
`7-16`, `2-4`, `5-8`, `3-4`, `7-8`, `4-4`.

Familia 48-lados (hi-res, en `48/`):
`4-4cyli`, `4-4edge`, `4-4disc`, `4-4ringN`, `4-4ndis`, `1-4chrd`, etc.

**Escalado** (x = z = alto):

```
1 16 0 0 0  20 0 0  0 1 0  0 0 20  4-4edge.dat   ; aro radio 20
1 16 0 0 0   6 0 0  0 -4 0  0 0 6  4-4cyli.dat   ; cilindro radio 6, alto 4
```

### 6.4 Familia `disc` y `ring`

- `n-fdisc.dat` — sector circular relleno.
- `n-fedge.dat` — arco de círculo (solo aristas).
- `n-fchrd.dat` — segmento de disco entre arco y cuerda.
- `n-fcyli.dat` — manto cilíndrico.
- `n-fringN.dat` — anillo con radio interior N, exterior N+1.

### 6.5 Familia `stud`

- `stud.dat` — stud liso sin logo, 1×1, alto 4 LDU, centrado.
- `stud2.dat`, `stud3.dat`, `stud4.dat` — studs huecos de varias profundidades.
- `stud-logo.dat`, `stud-logo2.dat` — studs con logo LEGO.
- `stug<N>-<X>x<Z>.dat` — **grupo de studs** (matriz 2D) para colocar varios a
  la vez. `<N>` = tipo (regular, hueco…), `<X>` × `<Z>` = nº de studs.
  Combinaciones permitidas: `1xZ`, `Xx1`, `XxX` (cuadrados).
- `studa.dat` — stud accessory (alto 8).

### 6.6 Familia `tri3` — prismas triangulares rectángulos

- `tri3.dat` — prisma triangular 1×1×1, ortogonal en x y z, sin caras
  superior/inferior.
- `tri3-1.dat`, `tri3-3.dat`, `tri3a1.dat`, `tri3a4.dat`, `tri3u3.dat`,
  `tri4.dat` — variantes para empalmes y esquinas.

### 6.7 Cono, torus, cylinder/chrd especiales

- `n-fconN.dat` — secciones cónicas.
- Torus: `1-8torus.dat`, `4-4torus.dat`, `n-ftorus.dat`.
- Tubos Technic: `axlehol2.dat`, `axleho9.dat`, etc.
- Pin Technic: `technicpin.dat`, `technicpinhole.dat`.

### 6.8 Normas de escalado de primitivas

- Primitivas **regulares** (box, rect, cyli, disc): escalar **uniformemente en
  x y z** según tamaño. Para cilindros, mismo factor en x y z (radio), libre
  en y (altura).
- Primitivas con "no escalar" (studs, holes, clips, hinges): mantener escala
  1:1.
- 3 decimales bastan en piezas normales; 4 en primitivas hi-res.

---

## 7. BFC — Back Face Culling

Las piezas oficiales usan **back-face culling** (solo se dibujan las caras
frontales). Activado con:

```
0 BFC CERTIFY CCW
```

(antes del primer comando operativo).

Operadores:

- `0 BFC NOCERTIFY` — desactiva BFC para este archivo.
- `0 BFC CERTIFY [CW|CCW]` — declara archivo BFC-compliant (CCW por defecto).
- `0 BFC CW` / `0 BFC CCW` — cambia el winding del archivo en vivo.
- `0 BFC CLIP` / `0 BFC NOCLIP` — activa/desactiva el culling localmente.
- `0 BFC INVERTNEXT` — invierte la siguiente referencia sub-file (útil para
  caras interiores de cilindros). **Solo afecta a la línea siguiente inmediata**.

### Reglas de winding (CCW por defecto)

Sentido **counter-clockwise** visto desde el lado frontal. Si la matriz de
rotación de la línea tipo 1 tiene **determinante negativo** (refleja el
sub-archivo), el winding efectivo se invierte automáticamente.

```
            CW (visto de frente)
         1 ─────► 2
         ▲       │
         │       ▼
         4 ◄─────3
```

Las piezas se renderizan correctamente si todas las caras miran hacia afuera.

---

## 8. Headers oficiales (pequeño pero importante)

Una pieza oficial sigue este orden:

```
0 <Description>                ← ej: "Brick  1 x  2"
0 Name: <filename.dat>
0 Author: <RealName> [<username>]
0 !LDRAW_ORG Part UPDATE YYYY-RR
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt
0 !HELP texto opcional (max 50 chars/línea)
0 BFC CERTIFY CCW
0 !CATEGORY <category>
0 !KEYWORDS word1, word2, word3
0 !HISTORY YYYY-MM-DD [<user>] descripción
0 // comentarios libres
1 16 ... <pieza base>
```

Tipos `!LDRAW_ORG`:

- `Part`, `Subpart`, `Primitive`, `8_Primitive`, `48_Primitive`, `Shortcut`.
- Versión "Unofficial_*" para piezas en el Parts Tracker no oficiales.
- Cualificadores opcionales: `Alias`, `Flexible_Section` (Physical_Colour
  deprecado).

Prefijos en la descripción:

- `~` — subpartes, obsoletas, o partes de un ensamblaje.
- `=` — alias.
- `|` o `~|` — partes de terceros.

---

## 9. Numeración de piezas

| Patrón                      | Significado                                            |
|-----------------------------|--------------------------------------------------------|
| `NNN`, `NNNN`, `NNNNN`      | Design ID oficial de LEGO                              |
| `NNNa`, `NNNNa`             | Variante de molde (a, b, c…)                           |
| `uNNNN.dat`                 | Design ID desconocido (solicitar al admin)             |
| `tNNNN.dat`                 | Pieza de terceros (LEGO-compatible)                    |
| `s/NNNNsNN.dat`             | Subparte de `NNNN.dat`                                 |
| `NNNpCC(C).dat`             | Versión con patrón (printed)                           |
| `sNNNN.dat`                 | Sticker de hoja sin nº                                 |
| `NNNcNN.dat` o `-cXX`       | Shortcut (assembly) o variante flexible                |
| `NNNcNN-fN.dat`             | Variante posicional (flexible)                         |
| `NNNdNN.dat`                | Shortcut con sticker                                   |
| `NNNkNN.dat`                | Sub-componente flexible (mangueras, ejes)              |
| `stud...dat`                | Primitiva                                              |
| `stug*-X*x*Z*.dat`          | Grupo de studs                                         |
| `NNNNN[N]pCC(C).png`        | Imagen de textura (mismo nº base)                      |

Patrones de impresión: el primer dígito del código identifica el tema
(0=misc/Town, 3=Pirates, 4=Castle, 5-6=Space, 7-9=Modern Town, a=Adventurers,
b=Superheroes, cXY=Collectable Minifigures, etc.). Ver detalle en la
[Oficial Library Part Number Specification](https://www.ldraw.org/part-number-spec.html).

### Atajos (Shortcuts)

Cuando LEGO vende varias piezas pre-ensambladas, se crea un "shortcut" para
reutilizarlas como un único bloque en los modelos. Ej: `55969` (sensor de luz
NXT), `53787` (motor NXT completo).

### Piezas flexibles

Modeladas en su estado plano como archivo principal, y versiones curvadas
con sufijo `-f1`, `-f2`, etc.

---

## 10. Anatomía de una pieza — ejemplos reales

### 10.1 Brick 2×4 (`3001.dat`) — pieza canónica

```ldraw
0 Brick  2 x  4
0 Name: 3001.dat
0 Author: James Jessiman
0 !LDRAW_ORG Part UPDATE 2004-03
0 !LICENSE Licensed under CC BY 4.0 : see CAreadme.txt
0 BFC CERTIFY CCW
0 !HISTORY 2002-05-07 {unknown} BFC Certification
…
1 16 0 0 0 1 0 0 0 1 0 0 0 1 s\3001s01.dat    ; ← cuerpo del brick (subparte)
4 16 -40 0 -20 -40 24 -20 40 24 -20 40 0 -20   ; ← cara -z (inferior)
4 16  40 0  20  40 24 20 -40 24 20 -40 0 20    ; ← cara +z (superior)
```

### 10.2 Subparte `s\3001s01.dat` (cuerpo sin caras)

```ldraw
1 16 0 4 0 1 0 0 0 -5 0 0 0 1 stud3.dat        ; stud interior (centro)
0 BFC INVERTNEXT                                ; invierte el cilindro interior
1 16 0 24 0 16 0 0 0 -20 0 0 0 6 box5.dat      ; caja interna (sin tapa)
4 16 20 24 10 16 24 6 -16 24 6 -20 24 10       ; quads de la corona superior
…
1 16 0 24 0 20 0 0 0 -24 0 0 0 10 box4t.dat    ; caja con cara -y y -z fuera
1 16 30 0 -30 1 0 0 0 1 0 0 0 1 stud.dat        ; studs externos (8 en 2x4)
… (8 studs)
```

### 10.3 Stud (`stud.dat`) — primitiva esencial

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
1 16 0 0 0 6 0 0 0 -4 0 0 0 6 4-4cyli.dat  ; manto cilíndrico (alto 4)
1 16 0 -4 0 6 0 0 0 1 0 0 0 6 4-4disc.dat  ; tapa superior
```

### 10.4 Plate 2×2 (`3022.dat`) — usa `box5` y `INVERTNEXT`

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

**Patrón clave**: cada pieza es una **composición** de primitivas escaladas +
quads propios (rim superior) + studs. Los huecos entre studs usan
`0 BFC INVERTNEXT` para invertir la normal de la primitiva interior.

---

## 11. MPD — Multi-Part Documents

Un **.mpd** agrupa varios archivos LDraw en uno solo, separados por
`0 FILE <nombre>` o `0 !DATA <nombre>`:

```
0 FILE main.ldr
1 7 0 0 0 1 0 0 0 1 0 0 0 1 819.dat
1 4 80 -8 70 1 0 0 0 1 0 0 0 1 house.ldr     ; ← referencia a sub-modelo

0 FILE house.ldr                                ; ← inicio del sub-modelo
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
El primer bloque es el **modelo principal**; los demás solo se renderizan si
están referenciados.

Esto permite empaquetar un set LEGO completo (varios .ldr + piezas oficiales)
en **un único archivo** para distribuir.

---

## 12. Modelos — cómo se arman

Un modelo (`.ldr`) es una secuencia de líneas tipo 1 que **posicionan y
rotan piezas de la biblioteca**. Ejemplo (`car.ldr`):

```
0 Example Car for Demonstration of LDRAW Library
0 Name: car.ldr
0 Author: James Jessiman

1 0 0 0 -90  1 0 0  0 1 0  0 0 1  4315.dat      ; rueda negra, pos (0,0,-90)
1 7 0 0 -60  1 0 0  0 1 0  0 0 1  4600.dat      ; llanta gris, pos (0,0,-60)
1 0 0 0   0  1 0 0  0 1 0  0 0 1  3031.dat      ; brick 4x2 negro en origen
…

0 STEP                                          ; ← fin del paso 1
1 46 30 -8 -90  1 0 0  0 1 0  0 0 1  3024.dat   ; paso 2…
1 46 -30 -8 -90 1 0 0  0 1 0  0 0 1  3024.dat
…

0 STEP                                          ; ← fin del paso 2
1 4 0 -16 -30  1 0 0  0 1 0  0 0 1  3829c01.dat
```

**Comandos importantes en modelos**:

- `1 <color> x y z a b c d e f g h i <archivo>` — colocar una pieza.
- `0 STEP` — marca fin de paso de construcción.
- `0 FILE <name>` / `0 NOFILE` — delimitan sub-modelos dentro de MPD.
- `0 !COLOUR ...` — definir colores locales.
- `0 BFC ...` — activar culling.

**Cómo encajan las piezas**: por **estándar geométrico**:

- Studs (cilindros Ø12, alto 4) encajan en tubes (huecos cilíndricos Ø12,
  profundidad 4) en las caras opuestas.
- Studs encajan sobre studs si la pieza lo permite (rotación 0°).
- Tubes y studs están separados **20 LDU** en X/Z (centros de stud).
- Los ejes Technic (Ø5) encajan en cross-holes.

**Para colocar una pieza exactamente**:

1. Decide la posición del origen (centro de la base de studs).
2. Traslación: `x y z` en LDU (multiplica studs por 20, plates por 8).
3. Rotación: matriz identidad `1 0 0  0 1 0  0 0 1` por defecto. Para
   rotar 90° alrededor de Y: `0 0 -1  0 1 0  1 0 0`. Para voltear: determinante
   negativo (cuidado con la normal — BFC se ajusta solo).
4. Color: del 0–215+ según `LDConfig.ldr`.

### Ejemplo: muro 2×2 en azul

```
0 Name: muro.ldr

; Base de plates 2x2
1 1 0 0 0 1 0 0 0 1 0 0 0 1 3022.dat   ; plate 2x2 azul
1 1 0 -8 0 1 0 0 0 1 0 0 0 1 3022.dat  ; segunda plate 8 LDU arriba
1 1 0 -16 0 1 0 0 0 1 0 0 0 1 3022.dat ; tercera plate
0 STEP

; Brick 2x2 encima
1 1 0 -40 0 1 0 0 0 1 0 0 0 1 3003.dat ; brick 2x2 azul (alto 24)
0 STEP
```

### Reglas prácticas

- **Encaje vertical**: studs abajo (`-y`) ↔ tubes arriba. Sumar alturas en `y`.
- **Encaje lateral**: una pieza Technic con axle hole (Ø5) acepta un axle.
- **Encaje de clip**: estudiado en primitivas `clip*` y `clikits*`.
- **Rotación 90° vs 180°**: usar matrices con determinante ±1, evitar
  rotaciones extrañas (preferible `cyli/4` nativo o `cyli/16` a 22.5°).

---

## 13. Stickers (calcomanías)

- Geometría: caja fina de **0.25 LDU** de grosor, con `!TEXMAP START PLANAR`
  aplicando una imagen PNG encima.
- Cara superior a `y = -0.25`, paralela a X-Z.
- Color 16 (current color) en lados y cara inferior; el patrón en la cara
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
80 chars/línea, sin incluir el nombre de la pieza).

---

## 15. Cualificadores opcionales para piezas oficiales

- `Alias` — pieza visualmente idéntica a otra con distinto nº.
- `Flexible_Section` — sub-componente de pieza flexible.
- `Physical_Colour` (deprecado).

---

## 16. OMR — Official Model Repository

Modelos oficiales de sets LEGO documentados siguen el
[OMR Spec](https://www.ldraw.org/article/593.html):

- Nombre: `<SetNumber>[-<Qualifier>] - <SetName>[ - <SubModel>].mpd`
- Cabecera estándar con `!LDRAW_ORG Model` o `!LDRAW_ORG Unofficial_Model`.
- Cada sub-modelo en su propio `0 FILE` dentro del MPD.
- Prohibido espejado (rompe el logo y el BOM).
- Piezas no oficiales: incluir el `.dat` como sub-archivo renombrado dentro
  del MPD.

---

## 17. Plantilla mínima — cómo crear una pieza desde cero

Pasos (resumen):

1. **Decide origen y orientación**:
   - Studs arriba (`-y`).
   - Base de studs en `y=0`.
   - Centro del grupo de studs en X=0, Z=0.

2. **Elige primitivas**:
   - Cuerpo principal → `box5`/`box4-7a`/`boxjcyl4` escalados.
   - Hueco central para studs → `box5` invertido con `0 BFC INVERTNEXT`.
   - Studs externos → `1 16 x 0 z 1 0 0 0 1 0 0 0 1 stud.dat` (color 16).
   - Studs internos → `stud3.dat`, `stud4.dat`.

3. **Añade quads para el rim superior** (entre las dos filas de studs):
   - 4 quads `4 16 x1 y1 z1 x2 y2 z2 x3 y3 z3 x4 y4 z4`.
   - Orden CW o CCW desde arriba.

4. **Escribe el header** completo (ver §8).

5. **Verifica BFC** con una herramienta (LDView, BFC testing) — debe pasar
   `CERTIFY CCW`.

### Mini-ejemplo: brick 1×1 personalizado

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

; Tubo interior (anti-stud)
0 BFC INVERTNEXT
1 16 0 24 0 8 0 0 0 -20 0 0 0 4 box5.dat

; Caja exterior
1 16 0 24 0 10 0 0 0 -24 0 0 0 6 box5.dat

; Stud superior
1 16 0 0 0 1 0 0 0 1 0 0 0 1 stud.dat
```

Este brick 1×1 simple queda definido con solo **3 sub-archivos + 2 líneas de
meta**. Las primitivas escaladas generan toda la geometría; el stud queda en
el origen; el tubo interior invertido crea el hueco para encajar.

---

## 18. Mini-ejemplo: armar un modelo (`.ldr`)

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

Este modelo es apilable: cada pieza se coloca con su origen en el centro del
grupo de studs. Las plates están a `y=0`, `y=-8`, y el brick a `y=-8-24=-32`.

---

## 19. Recursos y referencias

| Recurso                                       | URL                                                  |
|-----------------------------------------------|------------------------------------------------------|
| Web oficial                                   | <https://ldraw.org>                                  |
| Documentación                                 | <https://www.ldraw.org/docs-main.html>               |
| Biblioteca online (búsqueda y descarga)       | <https://library.ldraw.org>                          |
| Wiki                                          | <https://wiki.ldraw.org>                             |
| Foros                                         | <https://forums.ldraw.org>                           |
| Mirror GitHub                                 | <https://github.com/pybricks/ldraw>                  |
| Tutoriales                                    | <http://wiki.ldraw.org/index.php?title=Category:Tutorials> |
| Parte authoring tutorial (Holly-Wood)         | <https://www.holly-wood.it/ldraw/authoring-en.html> |
| LDCad (editor recomendado)                    | <https://www.melvintec.com/ldcad>                    |
| LDView (visor)                                | <https://tcobbs.github.io/ldview/>                   |
| LeoCAD (otro editor)                          | <https://www.leocad.org>                             |
| MLCad (editor clásico, descontinuado)         | <https://mlcad.lm-software.com>                      |
| Spec completa formato de archivo              | <https://www.ldraw.org/article/218.html>             |
| Spec BFC                                      | <https://www.ldraw.org/article/415.html>             |
| Spec Colores                                  | <https://www.ldraw.org/article/299.html>             |
| Spec Header                                   | <https://www.ldraw.org/article/398.html>             |
| Spec Numeración                               | <https://www.ldraw.org/part-number-spec.html>        |
| Spec MPD                                      | <https://www.ldraw.org/article/47.html>              |
| Spec OMR                                      | <https://www.ldraw.org/article/593.html>             |
| Primitive Reference                           | <https://wiki.ldraw.org/wiki/Primitives_Reference>   |
| Colour chart                                  | <https://www.ldraw.org/article/547.html>             |

---

## 20. Resumen ejecutivo — recetas rápidas

| Necesito…                              | Solución                                                          |
|----------------------------------------|-------------------------------------------------------------------|
| Crear un nuevo brick                   | Componer con `box5` (exterior) + `box5` invertido (tubo) + N studs |
| Colocar un stud                        | `1 16 x 0 z 1 0 0 0 1 0 0 0 1 stud.dat`                           |
| Colocar un grupo de studs              | Usar `stug-2x2.dat`, `stug-3x1.dat`, etc.                         |
| Hacer un cilindro de radio N alto M    | `1 16 0 0 0 N 0 0 0 M 0 0 0 N 4-4cyli.dat`                       |
| Hacer un aro de radio R                | `1 16 0 0 0 R 0 0 0 1 0 0 0 R 4-4edge.dat`                        |
| Conectar una pieza encima (encaje)     | Sumar 24 (brick) u 8 (plate) al `y` de la siguiente pieza         |
| Conectar al lado (encaje stud ↔ stud)  | Sumar ±20 al `x` o `z` (centros de stud)                          |
| Encajar un axle Technic                | Usar pieza Technic con `axlehol2.dat` o cross-hole                |
| Definir un color local                 | `0 !COLOUR MiColor CODE 999 VALUE #FF0000 EDGE #800000`           |
| Marcar paso de construcción            | `0 STEP`                                                          |
| Encabezado pieza oficial               | Ver §8                                                            |
| Rotar pieza 90° alrededor de Y         | `1 c 0 0 z 0 0 1 0 1 0 -1 0 0` (CW) o `0 0 -1 0 1 0 1 0 0` (CCW)  |
| Empaquetar set completo                | MPD con un `0 FILE` por sub-modelo                                |
| Activar back face culling              | `0 BFC CERTIFY CCW` al inicio                                     |

---

## 21. Glosario

- **LDU** — LDraw Unit (0.4 mm).
- **Stud** — cilindro saliente (4 LDU alto, 12 LDU Ø).
- **Tube / Anti-stud** — cilindro hueco que aloja un stud.
- **Rim** — anillo elevado en la parte superior de bricks/plates (entre filas
  de studs).
- **Primitive** — pieza geométrica reusable de `p/` o `p/48/`.
- **Subpart** — pieza intermedia en `parts/s/`, referenciada por una o más
  partes.
- **Shortcut** — assembly pre-fabricado tratado como una sola pieza
  (`NNNcNN.dat`).
- **Patterned part** — pieza con impresión (`NNNpCC.dat`).
- **Sticker** — calcomanía aplicada a una pieza.
- **Flexible part** — pieza deformable (mangueras, telas).
- **STEP** — pausa/fin de paso en un modelo.
- **MPD** — Multi-Part Document, un archivo con varios sub-archivos.
- **BFC** — Back Face Culling, descartar caras traseras.
- **CCW/CW** — winding (counter-clockwise / clockwise) del polígono visto de
  frente.
- **INVERTNEXT** — invertir la normal de la siguiente referencia.
- **Primitive substitution** — sustitución automática de primitivas por
  versiones más detalladas en renderers.
- **Determinant** — `det(M)` de la matriz 3×3 de rotación. Si <0, refleja.
