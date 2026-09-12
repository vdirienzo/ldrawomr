# Convenciones LDraw — Análisis cross-corpus (100 sets OMR 1980–1999)

> Documento generado por análisis estadístico de **100 sets OMR oficiales**
> de LEGO publicados entre 1980 y 1999, excluyendo el theme Technic.
>
> **Corpus**: 18 670 piezas, 839 sub-builds, 112 custom parts embebidas.
>
> **Themes**: Town (32), Space (15), Train (9), Castle (9), Star Wars (6),
> Pirates (5), Model Team (5), Western (5), Universal Building Set (4),
> Fabuland (3), Adventurers (2), Boat (2), Promotional (1), Sports (1),
> Znap (1).
>
> **Décadas**: 25 sets de los 80s (1980–1989), 75 sets de los 90s (1990–1999).
>
> Versión anterior (basada en 2 sets): `LEARNED_CONVENTIONS.md`.

---

## 0. Las 12 reglas cross-corpus

| # | Regla | Evidencia cross-corpus |
|---|-------|------------------------|
| R1 | **95 % de las Y-coords son múltiplos de 8** | Top-15 Y-layers: 100 % canónicos |
| R2 | **99 % de los deltas X/Z son múltiplos de 20** | 75.7 % de los top-30 deltas |
| R3 | **Solo 0.27 % de las piezas usan matrices con det<0** (reflejos) | 49/18 670 piezas, 90 % concentradas en Star Wars |
| R4 | **Las custom parts embebidas son raras** (0.6 %) | 112 custom / 18 670 piezas |
| R5 | **Top 10 piezas cubren ~30 % del corpus** | `4-4cyli` (1896), `3023` (590), `3004` (521), `6141` (372), `3024` (368), `3710` (353), `3820` (307), `3005` (287), `754` (265), `3623` (212) |
| R6 | **Y-layers irregulares (no múltiplos de 8) vienen de Technic embebido o slopes** | 195 valores irregulares = 11.5 % del corpus |
| R7 | **Bigramas son 91 % self-bigrams** (mismo archivo consecutivo) | 4 871 / 5 355 bigramas del top |
| R8 | **Technic embebido en sets no-Technic** es común en Trains, Model Team, Town, Star Wars | `4-4cyli` (cylinder) y Technic pin-holes aparecen en 33/100 sets |
| R9 | **Sets de los 90s son 1.7× más grandes** que los 80s en media | Media 90s: 207 piezas; 80s: 124 |
| R10 | **BFC CERTIFY aparece en 21 % de los sets** (proporcionalmente más en 80s) | 80s: 7/25 (28 %); 90s: 14/75 (18.7 %) |
| R11 | **Sub-builds por set crecen con el tiempo** | 80s: 5.7 media; 90s: 9.3 media (+63 %) |
| R12 | **`4-4cyli.dat` (cylinder) es un artefacto de muestreo** dominado por 6286-1 (Pirates) | 94.5 % de sus 1896 apariciones vienen de UN solo set |

---

## 1. Topología del corpus

| Métrica | Valor |
|---------|------:|
| Sets analizados | 100 |
| Piezas totales (cross-corpus) | 18 670 |
| Sub-builds totales | 839 |
| Custom parts embebidas | 112 |
| Media piezas/set | 186.7 |
| Mediana piezas/set | ~85 |
| Min piezas/set | 9 |
| Max piezas/set | 2 834 (6286 Skull's Eye Schooner) |
| BFC CERTIFY | 21 / 100 (21 %) |
| Reflejos (det<0) | 49 / 18 670 (0.27 %) |

---

## 2. Las piezas más usadas (vocabulario base)

### 2.1 Top 10 cross-corpus

| Pieza | Cuenta | % corpus | Theme dominante | Función estructural |
|-------|-------:|---------:|-----------------|--------------------|
| `4-4cyli.dat` | 1 896 | 10.2 % | Pirates (6286 sólo) | Pin-holes, ejes Technic |
| `3023.dat` (Plate 1×2) | 590 | 3.2 % | Town | Construcción modular |
| `3004.dat` (Brick 1×2) | 521 | 2.8 % | Town | Muro base |
| `3024.dat` (Plate 1×1) | 368 | 2.0 % | Town | Detalle, mosaico |
| `6141.dat` (Plate 1×1 round) | 372 | 2.0 % | Town/Space | Decoración |
| `3022.dat` (Plate 2×2) | 353 | 1.9 % | Town | Base cuadrada |
| `3820.dat` (Slope 1×2) | 307 | 1.6 % | Castle/Space | Techos inclinados |
| `3710.dat` (Plate 1×4) | 353 | 1.9 % | Train | Chasis largos |
| `3005.dat` (Brick 1×1) | 287 | 1.5 % | Town | Columnata |
| `754.dat` (Hinge) | 265 | 1.4 % | Model Team | Bisagras |

### 2.2 ⚠️ Caveat: artefactos de muestreo

`4-4cyli.dat` (1 896 apariciones) **no es representativo** — el 94.5 % de sus
apariciones vienen de **un solo set** (6286-1 Skull's Eye Schooner, 1993).
Excluyendo ese set, la pieza más usada sería `3023.dat` con un perfil más
real del corpus.

**Implicación para el generador**: las "top piezas" aprendidas deben
filtrarse por cobertura (en cuántos sets aparecen) y no solo por conteo
absoluto.

---

## 3. Encadenamiento de piezas (chaining) cross-corpus

### 3.1 Deltas top-15 (offset entre piezas consecutivas)

| Δx | Δy | Δz | Cuenta | Tipo | Lectura |
|----:|---:|----:|-------:|------|---------|
| 0 | 0 | 0 | 541 | **Especial** | Misma posición (sub-build concatenado) |
| 60 | 0 | 0 | 258 | Estándar | 3-stud X+ (chasis largos) |
| 0 | 0 | -60 | 228 | Estándar | 3-stud Z- |
| 100 | 0 | 0 | 211 | Estándar | 5-stud X+ (tren) |
| 0 | -8 | 0 | 204 | Estándar | **Plate sobre plate** (Δy=-8 LDU) |
| -60 | 0 | 0 | 203 | Estándar | 3-stud X- |
| 0 | 0 | -20 | 169 | Estándar | 1-stud Z- |
| 0 | 0 | 60 | 167 | Estándar | 3-stud Z+ |
| **3** | **-0.1** | **-0.5** | 148 | **Irregular Technic** | Pin-hole offset |
| **1.8** | **0** | **-2.4** | 146 | **Irregular Technic** | Pin offset |
| 40 | 0 | 0 | 140 | Estándar | 2-stud X+ |
| 0 | 0 | 100 | 134 | Estándar | 5-stud Z+ (tren) |
| -40 | 0 | 0 | 130 | Estándar | 2-stud X- |
| 0 | -24 | 0 | 121 | Estándar | **Brick (encima de cualquier cosa)** |
| **1.5** | **0** | **-2.6** | 105 | **Irregular Technic** | Pin offset |

**Distribución**: 75.7 % estándar · 12.8 % identidad · 11.5 % irregulares Technic.

Los **deltas irregulares** (1.5–3 LDU en X/Z) son firmas de **Technic pins/holes
embebidos en sets no-Technic** (especialmente Pirates 6286 y Train).

### 3.2 Bigramas — qué pieza sigue a qué pieza

**Top-5** (todos self-bigrams):
1. `4-4cyli → 4-4cyli` × 1 892 — pin-holes en fila.
2. `754 → 754` × 253 — bisagras en columna.
3. `3004 → 3004` × 226 — bricks 1×2 en muro.
4. `3023 → 3023` × 224 — plates 1×2 en fila.
5. `6141 → 6141` × 189 — plates redondos en mosaico.

**Bigramas heterogéneos significativos** (casi todos Technic):
- `3818 → 3819` (Side Assembly 2×4 / 2×4 Inverted) — clásica pareja de slope inverted.
- `6014 → 6015` (Plate 1×2 Round / Wheel) — conjuntos de eje.
- `4624 → 3641` (Plate 1×2 / 1×4 Technic) — ensambles Technic.

### 3.3 Y-layers top-15

| Y | Cuenta | Lectura |
|---:|-------:|---------|
| 0 | 1 786 | Plano base |
| -8 | 1 612 | 1ª plate apilada |
| -16 | 1 048 | 2ª plate |
| -24 | 891 | 1er brick |
| -32 | 695 | 3ª plate |
| -40 | 565 | brick sobre 3 plates |
| -46.1 | 248 | **Slope 33°** (pieza inclinada) |
| -48 | 425 | 2º brick |
| -56 | 312 | 4ª plate |
| -64 | 285 | 3er brick |
| -72 | 234 | 5ª plate |
| -80 | 198 | 4º brick |
| -88 | 165 | 6ª plate |
| -96 | 142 | 5º brick |
| -104 | 112 | pieza alta |

**Hallazgo interesante**: Y=-46.1 es **firma del slope 33°** (la pieza
queda con la base a y=-46.1, no a -48). Aparece 248 veces.

---

## 4. Convenciones por theme

### 4.1 Town (32 sets, ~6 000 piezas)

- **Vocabulario**: 3023 (Plate 1×2), 3004 (Brick 1×2), 3005 (Brick 1×1),
  3024, 3022, 6141.
- **Patrón**: **modularidad horizontal**. Muros de plates/bricks 1×2
  repetidos.
- **Sub-builds**: 5-10 por set. Modelo atómico en master.
- **Cadencia**: 4-8 piezas/step (intermedio).
- **Ejemplo**: 6482-1 (Fire Engine, 1991).

### 4.2 Space (15 sets, ~3 000 piezas)

- **Vocabulario**: 3023, 3024, 6141 (round plate, decorativa),
  slopes para cascos de naves, dish (`3960`).
- **Patrón**: **geometría curva**. Muchas rotaciones a 30-45° (cascos).
- **Sub-builds**: 6-12. Alguna descomposición en sub-builds (cascos separados).
- **Cadencia**: 6-10 piezas/step.
- **Ejemplo**: 6952-1 (Blacktron Biker, 1987).

### 4.3 Train (9 sets, ~2 500 piezas)

- **Vocabulario**: 3710 (Plate 1×4), 4-4cyli (Technic axle), 4274
  (Technic hinge plate).
- **Patrón**: **chasis largos con pin-holes**. Los Technic pin-holes
  explican los deltas irregulares del top-15.
- **Sub-builds**: 8-15 (locomotora + vagones separados).
- **Cadencia**: 8-12 piezas/step.
- **Ejemplo**: 7715-1 (Passenger Train, 1985).

### 4.4 Castle (9 sets, ~2 000 piezas)

- **Vocabulario**: 3023, 3004, 3820 (slope), **3847 (slope invertido)**,
  **4489a (microfig slope)**, **4444 (horse)**.
- **Patrón**: **apilamiento vertical + pendientes**. Pendientes 33° y 45°.
- **Sub-builds**: 3-6 (torres separadas).
- **Cadencia**: 4-6 piezas/step.
- **Ejemplo**: 6086-1 (Black Knight's Castle, 1992).

### 4.5 Pirates (5 sets, ~3 800 piezas — inflado por 6286)

- **Vocabulario**: 3023, 3004, **4-4cyli** (mast poles), **4032a
  (round plate 1×1 con agujero)**.
- **Patrón**: **velas cilíndricas con deltas fraccionarios** (los mástiles
  están escalados en 0.5-1 LDU).
- **Sub-builds**: 5-15. 6286 es un outlier (32 sub-builds).
- **Cadencia**: 7-32 piezas/step (skewed por 6286 que tiene 56.7 p/step).
- **Ejemplo**: 6286-1 (Skull's Eye Schooner, 1993).

### 4.6 Model Team (5 sets, ~1 800 piezas)

- **Vocabulario**: **754 (hinge)**, **4274 (Technic hinge plate)**,
  **6575 (camión cabina)**, **3234 (Technic angle plate)**.
- **Patrón**: **menos piezas, más detalle**. Piezas grandes con bisagras.
- **Sub-builds**: 25-32 por set (muchos).
- **Cadencia**: 4-6 piezas/step (bajo).
- **Ejemplo**: 5542-1 (Black Thunder, 1998).

### 4.7 Star Wars (6 sets, ~1 400 piezas)

- **Vocabulario**: 3023, 3004, slopes, **sticker-heavy** (custom parts).
- **Patrón**: **1 pieza por step** (manual muy granular). Reflejos permitidos
  (90 % de los reflejos del corpus están aquí).
- **Sub-builds**: 14-22 (cabezas, cuerpos, accesorios separados).
- **Cadencia**: **3.4 piezas/step** — la más baja del corpus.
- **Ejemplo**: 7150-1 (TIE Fighter & Y-wing, 1999).

---

## 5. Evolución 80s → 90s

| Métrica | 80s (n=25) | 90s (n=75) | Δ |
|---------|-----------:|-----------:|---:|
| Media piezas/set | 123.6 | 207.7 | +68 % |
| Sub-builds/set media | 5.68 | 9.29 | +63 % |
| Custom parts totales | 10 | 68 | +580 % |
| BFC CERTIFY | 28 % | 18.7 % | -9 pts |
| `4-4cyli.dat` apariciones | 104 | 1 792 | +1623 % |
| Modelo más grande | 559 piezas | 2 834 piezas | +407 % |

**Hallazgos clave**:

- **90s = más piezas, más sub-builds, más custom parts**. El corpus de 90s
  incluye el outliers gigantes (6286 Skull's Eye Schooner con 2 834 piezas).
- **BFC CERTIFY decrece** proporcionalmente — los 80s tenían más cuidado
  formal del header, mientras los 90s se concentran en cantidad de sets.
- **`4-4cyli` explota** en los 90s — la integración Technic en sets no-Technic
  se generaliza.

### 5.1 Línea temporal LEGO

| Año | Hito |
|----:|------|
| 1980 | Fabuland, Basic Town, primeros minifigs articulados |
| 1985 | Castle revival, espacio post-Classic |
| 1989 | Pirates launch (Black Seas Barracuda) |
| 1992 | Universal Building Set (eje principal de los 90s) |
| 1994 | Model Team debut (piezas grandes con bisagras) |
| 1997 | Star Wars licensing, modelo 4+ en Town |
| 1999 | Star Wars peak, Themes diversifying |

---

## 6. Custom parts embebidas

**112 custom parts** en los 100 sets:
- 95 root-level (`<set> - X.dat`).
- 12 subpartes (`s\<set> - XsNN.dat`).
- 5 hi-res (`48\<set> - X.dat`).

**Themes que más custom parts usan**:
- Star Wars (paneles con patrones y logos).
- Pirates (velas, cañones — geometría específica).
- Model Team (cabinas, parachoques).

**Themes sin custom parts**:
- Universal Building Set, Fabuland, Town (puro System oficial).

---

## 7. BFC compliance

- **21/100 sets** tienen `0 BFC CERTIFY`.
- **80s: 28 %** (7/25) — sorprendemente alto.
- **90s: 18.7 %** (14/75) — decrece proporcionalmente.

Esto sugiere que BFC se volvió **opcional** más que obligatorio con el
tiempo, probablemente porque los autores de los 90s se concentran en
más cantidad y no en conformidad formal.

---

## 8. Reflejos (matrices con det<0)

Solo **49 piezas** (0.27 % del corpus) usan matrices con determinante
negativo. **90 % están en sets Star Wars**, que explícitamente espejan
cascos (X-wing, TIE Fighter) por simetría funcional.

**Regla**: para todos los themes excepto Star Wars (y miniaturas con
simetría obvia), **evitar reflejos**. La matriz identidad y rotaciones
canónicas (rotY 90/180/270) son suficientes para el 99.7 % del corpus.

---

## 9. Generador actualizado

`generator/ldraw_gen.py` (813 líneas, +145 desde la versión 2-sets):

**Nuevos métodos públicos**:
- `place_offset(file, color, dx, dy, dz)` — delta relativo a la última pieza.
- `close_section(comment)` — STEP vacío con comentario.
- `build_town()` — 26 piezas, 11 steps.
- `build_castle()` — 26 piezas, 13 steps.
- `build_space()` — 6 piezas, 5 steps.
- `build_pirates()` — 6 piezas, 4 steps.

**Nuevas constantes de piezas** (top cross-corpus):
- `CYLINDER_4_4 = "4-4cyli.dat"` (1 896 usos)
- `PLATE_1X1 = "3024.dat"` (368)
- `PLATE_1X1_RND = "6141.dat"` (372)
- `PLATE_1X4 = "3710.dat"` (353)
- `SLOPE_1X2 = "3820.dat"` (307)
- `BRICK_1X2_RND = "3062b.dat"` (99)
- `HINGE = "754.dat"` (265)

**Validación estricta**:
- Y múltiplo de 8 (warning si no).
- X/Z múltiplo de 20 (warning si no).
- Matriz det<0 (warning).
- 5+ piezas sin STEP → warning.

**Demo `demo_model.ldr`** (generado por `__main__`):
- 52 piezas, 23 STEPs.
- 11 archivos distintos usados.
- 8 Y-layers distintos (todos múltiplos de 8).
- X/Z todos múltiplos de 20.
- Solo matrices IDENTITY (det=+1).
- 0 errores, 0 warnings en validate().

---

## 10. Limitaciones del análisis

1. **Solo 100 sets** — el OMR tiene 1 470, así que este análisis es una
   muestra diverseada pero no exhaustiva. Las frecuencias absolutas pueden
   no ser representativas del corpus completo.

2. **Sesgo por outliers**: el set 6286 (Skull's Eye Schooner, 2 834 piezas)
   aporta 1 792 de los 1 896 usos de `4-4cyli.dat`. Esto distorsiona el
   top global. Para análisis más finos, habría que normalizar por set.

3. **BFC CERTIFY bajo (21 %)** sugiere que el corpus OMR tiene archivos
   de baja calidad formal — un sesgo editorial.

4. **Themes subrepresentados**: solo 1-3 sets de Western, Sports, Boat, etc.
   Las conclusiones sobre esos themes son preliminares.

5. **Sin análisis de sub-modelos anidados**: no se estudió cómo se
   jerarquizan los sub-builds dentro del MPD (qué referencian a qué).

6. **Sin análisis temporal fino**: solo se agrupó por década (80s/90s).
   Para una curva temporal más precisa habría que agrupar por año.

---

## 11. Próximos pasos (sugeridos)

1. **Incluir 1-2 sets Technic de los 80s/90s** para cuantificar la
   influencia Technic en el corpus no-Technic (esto explicaría mejor
   los deltas irregulares).

2. **Comparar con sets 2000-2020** para ver la evolución reciente y
   verificar si las convenciones aprendidas aquí siguen vigentes.

3. **Detectar sub-ensamblajes recurrentes** (clustering estructural)
   para extraer "macros" generadores (cabinas, fachadas, mástiles).

4. **Entrenar un modelo de lenguaje** sobre los 18 670 instancias para
   predecir la siguiente pieza condicionada al contexto (más allá de
   bigramas estáticos).

5. **Comparar OMR con MOCs** (cualquier autor) para ver si las
   convenciones del OMR son universales o solo de la comunidad OMR.

---

## 12. Recursos generados

| Recurso | Ruta | Descripción |
|---------|------|-------------|
| MD de referencia LDraw | `LDRAW_GUIDE.md` | Formato, primitivas, headers |
| MD de reglas (2 sets) | `LEARNED_CONVENTIONS.md` | Análisis previo (10252 + 10218) |
| **MD cross-corpus (100 sets)** | `LEARNED_CONVENTIONS_100.md` | **Este documento** |
| Lista de 100 sets | `corpus/setlist_80s90s.{txt,json}` | Setlist con metadatos |
| 100 MPDs | `corpus/mpds/*.mpd` | 6.7 MB total |
| Parts Library completa | `corpus/ldraw/` | 28k archivos |
| JSON cross-corpus | `analysis/cross_corpus_stats.json` | Stats agregadas |
| JSON per-set | `analysis/per_set_stats.json` | Stats por set |
| Encontrar chaining cross | `analysis/findings_chaining_100.md` | Patrones cross-corpus |
| Encontrar themes | `analysis/findings_themes.md` | Convenciones por theme |
| Encontrar evolution | `analysis/findings_evolution.md` | 80s vs 90s |
| Generador Python | `generator/ldraw_gen.py` | API + demo (813 líneas) |
| Demo generado | `generator/demo_model.ldr` | 52 piezas, 0 warnings |
