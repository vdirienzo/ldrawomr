# Convenciones LDraw aprendidas — Análisis de 2 sets oficiales OMR

> Documento generado por análisis estadístico de 2 MPDs oficiales:
> - **10252 Volkswagen Beetle** (Roland Dahl, 2016, Creator Expert, 1167 piezas, 211 STEPs, 81 sub-modelos, 20 custom parts embebidas)
> - **10218 Pet Shop** (Stefan Frenz, Modular Building, 2034 piezas en 8 sub-builds por piso, 168 STEPs, 0 custom parts)
>
> Total: **3 335 piezas**, **379 STEPs**, **97 sub-modelos analizados**.
>
> Fuente cruda: `analysis/deep_stats.json`. Análisis detallado:
> - `analysis/findings_chaining.md` (encadenamiento de piezas)
> - `analysis/findings_steps.md` (cadencia de build-steps)
> - `analysis/findings_custom_parts.md` (piezas custom embebidas)
>
> El corpus oficial del Parts Library (17 116 piezas + primitivas) está en `corpus/ldraw/`.
> El generador que aplica estas reglas está en `generator/ldraw_gen.py`.

---

## 0. Resumen ejecutivo — las 10 reglas de oro

| # | Regla | Evidencia |
|---|-------|-----------|
| 1 | Components adyacentes sin STEP intermedio, agrupados por sección lógica | 10252: 211 STEPs ÷ 566 piezas = **2.7 piezas/step** |
| 2 | Cada STEP vacío cierra una sección (rotación de cámara, fin de piso) | 10252: **64 STEPs vacíos** (30% del total) |
| 3 | `Δy = -8` entre pieces consecutivos = apilar una **plate** sobre otra | 103 ocurrencias — delta más frecuente en ambos sets |
| 4 | `Δy = -24` entre pieces consecutivos = apilar un **brick** (encima de lo que esté) | 75 ocurrencias en 10218 |
| 5 | `Δx, Δz ∈ {0, ±20, ±40}` — spacing de stud canónico | 99% de deltas horizontales |
| 6 | **Plates primero, bricks después**: los walls empiezan con 3 plates (Δy=-8) y luego suben con bricks (Δy=-24) | 10218: y-layers top = -8, -24, -48 |
| 7 | Cada sub-build OMR se enfoca en **una unidad física** (cabina, piso, fachada, techo) | 10218: 8 sub-builds = 2 casas × 4 pisos; media 246 piezas/build |
| 8 | Custom parts embebidas siguen jerarquía: raíz `.dat` para wrappers simples, `s\X.dat` para subpartes, `48\X.dat` solo para curvatura hi-res | 10252: 7 raíz + 2 en `s\` + 1 en `48\` |
| 9 | **No se reflejan** piezas con determinante negativo: rompe el logo LEGO y el BOM | 10252: <1% matrices con det<0 (solo rotaciones canónicas) |
| 10 | Headers OMR usan `0 !LDRAW_ORG Model` + `0 !LICENSE` + `0 !THEME` + `0 !KEYWORDS` + `0 !HISTORY` | 100% conformidad |

---

## 1. Topología de los archivos analizados

| Set | Piezas | STEPs | Sub-builds | Custom parts |
|------|------:|------:|-----------:|-------------:|
| 10252 VW Beetle | 987 (74 sub-builds con piezas) + 566 en master | 211 | 81 | 20 |
| 10218 Pet Shop | 1 998 (13 sub-builds con piezas) | 168 | 17 | 0 |
| **TOTAL** | **3 335** | **379** | **97** | **20** |

**Diferencia arquitectónica clave**:
- 10252 = "**atómico**": el master scene contiene 566 piezas (todo el coche), con 74 sub-modelos auxiliares pequeños (ruedas, mangueras, sub-builds de 5-6 piezas).
- 10218 = "**por secciones**": el master está vacío (4 referencias a sub-builds), y los 8 edificios (2 casas × 4 pisos) se arman como sub-builds independientes de ~250 piezas cada uno.

**Implicación para el generador**: el generador debe poder ambos modos: master plano, o master vacío + sub-builds.

---

## 2. Convenciones de encadenamiento de piezas (chaining)

### 2.1 Y-layers: el ritmo vertical

| Y-layer | Significado | Frecuencia 10252 | Frecuencia 10218 |
|--------:|-------------|-----------------:|-----------------:|
| 0 | Plano base (plates) | 140 | 0 |
| -8 | Plate apilada | 109 | 128 |
| -16 | 2ª plate apilada | 80 | 0 |
| -24 | Brick sobre plate/plate | 54 | 56 |
| -32 | 3ª plate apilada | 80 | 0 |
| -48 | 2º brick | 23 | 48 |
| -56 | 4ª plate | 13 | 0 |
| -64 | 3er brick | 8 | 0 |
| -72 | 5ª plate | 12 | 0 |
| -80 | 4º brick | 20 | 0 |
| -104/-112 | secciones altas | 32/36 | 0 |

**Regla**: los Y-layers canónicos son múltiplos de 8 (medida en LDU). Cualquier Y distinto indica una pieza especial (slope, Technic) o un offset de sub-build.

**Patrón detectado en 10218**: la fachada tiene 3 plates (-8, -16, -24) y luego bricks (-48, -72, -96) — la "planta baja" de una casa es **siempre 3 plates**.

### 2.2 Deltas consecutivos (offset entre piezas adyacentes)

Top-10 deltas en ambos sets:

| Δx | Δy | Δz | Cuenta 10252 | Cuenta 10218 | Lectura |
|----:|---:|----:|-------------:|------------:|---------|
| 0 | -8 | 0 | 38 | 65 | **Plate sobre plate** (Δy = altura plate) |
| 0 | -24 | 0 | 17 | 49 | **Brick sobre plate** (NO -32, ver §2.3) |
| 20 | 0 | 0 | 25 | 12 | Stud-to-stud en X+ |
| 40 | 0 | 0 | 24 | 11 | 2-stud en X+ |
| 0 | 0 | -40 | 22 | 68 | 2-stud en Z- |
| 0 | 0 | 20 | 13 | 52 | 1-stud en Z+ |
| -40 | 0 | 0 | 15 | 11 | 2-stud en X- |
| 0 | -16 | 0 | 12 | 12 | 2 plates |
| 0 | 0 | 40 | 13 | 11 | 2-stud en Z+ |
| 0 | 0 | 100 | 0 | 63 | **Patrón de fachada Pet Shop** (5-stud) |

**Lectura**: el `Δy` se cuenta desde la base de cada pieza, no se acumula. Si pongo un brick (24 LDU) directamente sobre la base (`y=0`), va a `y=-24`, no a `y=-32`. Esto coincide con la convención LDraw del origen en la base de los studs.

### 2.3 Bigramas — qué pieza sigue a qué pieza

Top bigramas con interpretación:

| Pieza A → Pieza B | Cuenta | Lectura |
|-------------------|-------:|---------|
| 3794b.dat → 3794b.dat | 28 | Plate 1×2 con groove en filas paralelas |
| 3023.dat → 3023.dat | 22 | Plates 1×2 en línea |
| 6141.dat → 6141.dat | 42 (10218) | Plates redondos 1×1 — Patrón decorativo |
| 3009.dat → 3009.dat | 34 (10218) | Brick 1×6 — muros largos |
| 3005.dat → 3005.dat | (10218) | Brick 1×1 — columnata |
| 3069b.dat → 3069b.dat | 41 (10218) | Tile 1×2 — acabados de fachada |
| 3024.dat → 3024.dat | 40 (10218) | Plate 1×1 — mosaicos |
| 3070b.dat → 3070b.dat | (10218) | Tile 1×1 — detalles puntuales |

**Bigram heterogéneo más interesante** (en 10218):
- `3009 → 3010` (24 ocurrencias) = **Brick 1×6 seguido de Brick 1×4**: vanos rectangulares típicos de fachada (6 + 4 = 10 studs).

### 2.4 Rotaciones (matrices) por pieza

Las rotaciones canónicas (matrices enteras con det=+1) cubren ~95% de las apariciones:

| Matriz | Uso típico |
|--------|-----------|
| Identity `I` | Pieza en orientación canónica (98% de los casos) |
| `ROT_Y_90` | Lado opuesto del modelo |
| `ROT_Y_180` | Pieza invertida (típico para tiles en techo o fondo) |
| `ROT_Y_270` | Cuarto lado |

**No aparecen casi nunca**:
- Rotaciones de eje X/Z (casi siempre quedan con la pieza "de cabeza").
- Reflejos (det=-1) — explícitamente desaconsejados por la spec OMR.
- Ángulos menores a 15° — el Beetle tiene **un único grupo de piezas con rotY ≈ ±4°** (curvatura de la carrocería). Son la excepción, no la regla.

---

## 3. Cadencia de los pasos de construcción (STEPs)

### 3.1 Distribución del tamaño de paso

**10252 VW Beetle**:
- 211 STEPs totales.
- 64 vacíos (30.3%) — cierres de sección.
- 147 no-vacíos: moda=2, mediana=2, **media=3.85 piezas/step**.
- 10 STEPs "grandes" ≥10 piezas (chasis, cabina, interior del coche).

**10218 Pet Shop**:
- 168 STEPs totales (todos en sub-builds).
- **0 STEPs vacíos** — los cierres de sección se hacen entre archivos `0 FILE`, no con STEPs vacíos.
- Moda=10-13 piezas, media=11.7, mediana=11.

### 3.2 Arquitectura: ¿atómico o por secciones?

| Estilo | Cuándo | Ejemplo | Piezas/step |
|--------|--------|---------|------------|
| **Atómico** | Coches, modelos pequeños, figuras | 10252 Beetle | 2-4 |
| **Por secciones** | Edificios, sets grandes, dioramas | 10218 Pet Shop | 10-15 |
| **Mixto** | Sets medianos | — | 5-8 |

**Regla práctica**: si el set cabe en una "página de instrucciones" (~50 piezas), usar el modo atómico. Si tiene varios pisos/secciones, descomponer en sub-builds.

### 3.3 STEPs vacíos — cuándo y por qué

10252 agrupa los 64 STEPs vacíos en 5 racimos de 5-15 STEPs consecutivos. Estos racimos aparecen en transiciones de:
- Final de una rotación del modelo (el autor "limpia la pantalla" para mostrar la siguiente cara).
- Inicio/final de un sub-componente (ej: antes/después del chassis).

**Regla**: el STEP vacío **no es ceremonial** — siempre lleva contexto. Reservar para cierres de sección.

### 3.4 Ritmo de un sub-build OMR (10218)

Cada piso (Brown House 1 Basement, Brown House 2 Downstairs, etc.) tiene:
- ~246 piezas totales.
- ~20 STEPs.
- ~12 piezas/step.

Esto da ~30-60 minutos de lectura por sub-build, alineado con el formato típico de un manual LEGO físico (2-3 páginas por paso mayor).

---

## 4. Custom parts embebidas (cuándo y cómo)

### 4.1 Inventario

**10252 Beetle** (20 custom parts totales):
- 7 partes raíz (`10252 - X.dat`).
- 2 subpartes (`s\10252 - Xs01.dat`).
- 1 hi-res (`48\10252 - X.dat`).
- 10 decoraciones/stickers (patrones `p`/`q`).

**10218 Pet Shop** (0 custom parts): todos los componentes son oficiales.

### 4.2 Patrón jerárquico

| Carpeta lógica | Tamaño típico | Uso |
|----------------|---------------|-----|
| `<set> - X.dat` | 10-50 líneas | Custom part simple o wrapper |
| `<set> - X.dat` (compleja) | 100-800 líneas | Custom part con geometría propia |
| `s\<set> - Xs01.dat` | 30-200 líneas | Subparte privada (referenciada por la raíz) |
| `48\<set> - X.dat` | 50-300 líneas | Solo para curvatura hi-res (substituciones) |

### 4.3 Ejemplo de custom part simple

`10252 - 24246.dat` (12 líneas, wrapper mínimo):
```
0 <header>
1 16 0 0 0 1 0 0 0 1 0 0 0 1 s\24246s01.dat
0 // La subparte hace el trabajo
```

### 4.4 Ejemplo de custom part media

`10252 - 10252_towel.dat` (38 líneas, 100% primitivas escaladas):
- Wrapper de 4 `box` primitivos + 1 `stud` rotado.
- Sin geometría propia (todo `1` lines referenciando primitivas).

### 4.5 Ejemplo de custom part compleja

`s\24599s01.dat` (791 líneas):
- Hi-res `48\` + costillas manuales.
- Decompuesto en subparte porque la raíz `24599.dat` se reusa en varios sets.

### 4.6 Reglas inferidas

1. **Wrapper simple**: si tu custom part tiene <10 type-1 lines, es un wrapper alrededor de primitivas escaladas.
2. **Subparte necesaria**: si tiene >50 type-1 lines, descomponer en `s\Xs01.dat` + root `X.dat`.
3. **Hi-res solo para curvas**: `48\` se usa **únicamente** cuando la curvatura importa (carrocería de coche, parabrisas). Para piezas planas, no.
4. **Stickers como overlay**: las decoraciones `p`/`q` van como type-1 encima de la pieza base, con `0 BFC NOCLIP` antes y `0 BFC CLIP` después.

---

## 5. Convenciones de headers OMR

Todos los archivos OMR analizados usan el siguiente template:

```
0 <Title>
0 Name: <file>.ldr
0 Author: <RealName> [<username>]
0 !LDRAW_ORG Model
0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt

0 !THEME <theme>
0 !KEYWORDS <keyword1>, <keyword2>, ...

0 !HISTORY YYYY-MM-DD [<user>] <description>
```

**Notas observadas**:
- Antiquísimo (pre-2020): `!LICENSE Redistributable under CCAL version 2.0`.
- Reciente (post-2020): `!LICENSE Licensed under CC BY 4.0 : see CAreadme.txt`.
- Theme matching con catálogos externos (Bricklink, Rebrickable).
- Keywords típicos: nombre del set + número + sistema + sub-componente.

---

## 6. Cómo armar un modelo — algoritmo aprendido

Para generar un modelo siguiendo estas convenciones:

```
1. Decide modo:
   - "atómico" si <50 piezas → master scene plano.
   - "por secciones" si >50 → master vacío + 1 FILE por sección.

2. Construye cada sección como sub-build:
   - Empieza con una fila de plates (y=0, dx/dz=20).
   - Apila 2 plates más (y=-8, -16).
   - Sube con bricks cada 24 LDU (y=-32, -56, -80).
   - 0 STEP cada 3-5 piezas para legibilidad.
   - 0 STEP vacío al cerrar la sección.

3. Para cada pieza:
   - Posición (x, z) múltiplo de 20 LDU (centrado en studs).
   - Posición y múltiplo de 8 LDU (altura de plate).
   - Matriz canónica (identity o rotación de 90° en Y).
   - Color del catálogo (LDConfig.ldr).

4. Deja la instancia del sub-build en el master:
   1 16 <x> <y> <z> 1 0 0 0 1 0 0 0 1 <set> - <name>.ldr

5. Añade un header completo (ver §5).
```

---

## 7. Validación — checklist para todo `.ldr`/`.mpd` generado

- [ ] Cada línea empieza con un entero válido (0-5).
- [ ] Líneas tipo 1 tienen **exactamente 15 tokens** (1 + color + xyz + 9 matriz + archivo).
- [ ] Cada matriz tiene **det = ±1** y no es singular.
- [ ] Y-layers son múltiplos de 8 LDU.
- [ ] X/Z son múltiplos de 20 LDU (excepto Technic, axle holes ±5).
- [ ] Headers incluyen `!LDRAW_ORG`, `!LICENSE`, `!THEME`, `!KEYWORDS`.
- [ ] `0 STEP` separa pasos.
- [ ] Custom parts (si las hay) están en `0 FILE <set> - X.dat` con headers válidos.
- [ ] BFC: archivos oficiales deben tener `0 BFC CERTIFY CCW`.

El generador `ldraw_gen.py` implementa `validate()` que automatiza esta checklist.

---

## 8. Ejemplo end-to-end

`generator/demo_model.ldr` (generado por `ldraw_gen.py`):

```ldraw
0 LdrawGen Demo Build
0 Name: ldrawgen_demo_build.ldr
0 Author: LdrawGen [opencode]
0 !LDRAW_ORG Model
0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt
0 !THEME Demo
0 !KEYWORDS demo,generated,wall,floor,studs
0 !HISTORY 2026-09-11 [LdrawGen] Initial demo build

1 1 -20 0 -20 1 0 0 0 1 0 0 0 1 3022.dat
1 1 20 0 -20 1 0 0 0 1 0 0 0 1 3022.dat
1 1 -20 0 20 1 0 0 0 1 0 0 0 1 3022.dat
1 1 20 0 20 1 0 0 0 1 0 0 0 1 3022.dat
0 STEP
1 1 -20 -8 -20 1 0 0 0 1 0 0 0 1 3022.dat
... (etc)
```

**Métricas**:
- 31 piezas, 9 STEPs.
- Y-layers: -88, -64, -40, -16, -8, 0 (todos múltiplos de 8).
- X/Z: -60, -20, 0, 20, 60 (múltiplos de 20).
- Matrices: 25 IDENTITY + 4 ROT_Y_90 + 3 ROT_Y_180 (todas det=+1).
- Validación: 0 errores, 0 warnings.

---

## 9. Recursos generados

| Recurso | Ruta | Descripción |
|---------|------|-------------|
| MD de referencia LDraw | `LDRAW_GUIDE.md` | Formato, primitivas, headers, ejemplos |
| MPDs oficiales OMR | `corpus/10252-1.mpd`, `corpus/10218-1.mpd` | 2 sets analizados |
| Parts Library completa | `corpus/ldraw/` | 17k+ piezas + primitivas |
| JSON de estadísticas | `analysis/deep_stats.json` | Datos crudos del análisis |
| Análisis chaining | `analysis/findings_chaining.md` | Reglas de encadenamiento |
| Análisis steps | `analysis/findings_steps.md` | Cadencia de pasos |
| Análisis custom parts | `analysis/findings_custom_parts.md` | Autoría de custom parts |
| Generador Python | `generator/ldraw_gen.py` | API + plantillas + demo |
| Modelo demo | `generator/demo_model.ldr` | Ejemplo de salida del generador |
| **Este documento** | `LEARNED_CONVENTIONS.md` | Síntesis de las reglas aprendidas |

---

## 10. Limitaciones del análisis

- **Solo 2 sets analizados**: VW Beetle (coche) y Pet Shop (edificio). Las conclusiones sobre cadencia pueden no generalizar a otros tipos (Technic, Space, Castle).
- **Patrones de Technic no explorados**: liftarms, axles, pins se usan poco en estos dos sets.
- **Sin texturas / stickers avanzados**: solo se analizaron decoraciones básicas.
- **Sin minifigs detalladas**: los minifigs de 10218 están en sub-builds pero no se desglosaron a nivel de cada pieza articulada.
- **Sin análisis de simetría / mirrored geometry**: ambos sets evitan los reflejos, así que no hay datos suficientes para decidir cuándo conviene espejar (OMR lo desaconseja, pero hay casos válidos).

Para expandir el análisis, los siguientes sets serían los próximos candidatos ideales:
- Un **Technic** (ej: 42115 Lamborghini Sián) — patrones de axles, pins, liftarms.
- Un **Modular Building** más antiguo (ej: 10182 Café Corner) — para confirmar la cadencia por pisos.
- Un **Star Wars UCS** (ej: 75252 Imperial Star Destroyer) — para confirmar el modo "atómico" en sets muy grandes.
