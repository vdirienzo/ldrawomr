# LDraw — Análisis, documentación y generador

Proyecto para entender el formato LDraw (estándar abierto para LEGO CAD) y
aprender las convenciones de autoría analizando modelos oficiales del OMR
(Official Model Repository).

**Corpus**: **532 sets OMR** (108 760 piezas) en tres cohortes:
- 100 sets 80s/90s (no-Technic).
- 200 sets kids (small/affordable, post-1985).
- 232 sets classic (Plan C: distribución uniforme sobre 49 themes pre-2000).

---

## ⚡ RESUME FROM HERE (próxima sesión)

**Si querés continuar el corpus**, lee primero:
- **[NEXT_SESSION.md](./NEXT_SESSION.md)** — plan detallado de continuación.
- **[STATE.json](./STATE.json)** — estado persistente del proyecto (qué hay, qué falta).

**TL;DR**: Faltan **~938 sets OMR** por descargar (de 1 470 totales).
Pipeline de 1-2 horas: generar URLs → descargar → re-parsear → re-analizar →
sintetizar nuevo `LEARNED_CONVENTIONS_FINAL.md`.

**3 opciones para "lo que falta"**:
- (A) **Plan D completo**: terminar todo el OMR (~938 sets nuevos, 4 cohortes adicionales).
- (B) **Plan D enfocado**: solo themes subrepresentados en cohortes actuales.
- (C) **Plan D temático**: el usuario elige 3-5 themes específicos.

---

## Quick start

```bash
# 1. Generar modelos demo (3 estilos distintos)
cd generator/
python3 ldraw_gen.py
# Produce: demo_town.ldr, demo_kid.ldr, demo_classic.ldr

# 2. Re-analizar el corpus si se añaden más MPDs
cd analysis/
python3 deep_parse.py      # 2 sets (10252, 10218) — legacy
python3 batch_parse.py     # 100 sets (mpds/*.mpd) — legacy
python3 batch_parse2.py    # 300 sets (mpds/*.mpd + mpds_kids/*.mpd)
```

---

## Estructura del proyecto

```
.
├── README.md                       ← este archivo
├── NEXT_SESSION.md                 ← plan de continuación para próxima sesión
├── STATE.json                      ← estado persistente del proyecto
├── LDRAW_GUIDE.md                  ← especificación del formato LDraw
│                                     (formato de archivo, primitivas,
│                                     BFC, colores, headers, MPD, OMR)
│
├── LEARNED_CONVENTIONS.md          ← LEGACY: análisis de 2 sets
│                                     (10252 Beetle + 10218 Pet Shop).
│                                     Conservado por trazabilidad.
├── LEARNED_CONVENTIONS_100.md      ← análisis de 100 sets 80s/90s.
├── LEARNED_CONVENTIONS_300.md      ← análisis de 300 sets (80s/90s + kids).
├── LEARNED_CONVENTIONS_532.md      ← CANÓNICO: 23 reglas (18 + 5 nuevas)
│                                     aprendidas de 532 sets OMR.
│
├── corpus/
│   ├── ldraw/                      ← Parts Library oficial completa
│   │                                 (mirror de pybricks/ldraw, ~28k archivos)
│   ├── 10252-1.mpd                 ← 2 sets analizados inicialmente
│   ├── 10218-1.mpd                   (Volkswagen Beetle + Pet Shop)
│   ├── mpds/                       ← 100 MPDs 80s/90s (6.7 MB)
│   ├── mpds_kids/                  ← 200 MPDs kids (25 MB)
│   ├── mpds_classic/                ← 232 MPDs Plan C classic (8.5 MB)
│   ├── setlist_80s90s.{txt,json}   ← lista 100 sets 80s/90s
│   ├── setlist_kids.{txt,json}      ← lista 200 sets kids
│   ├── setlist_classic.{txt,json}   ← lista 232 sets classic Plan C
│   ├── plan_c_distribution.json     ← plan Plan C + shortfalls
│   └── all_omr_themes.json          ← catálogo completo de themes OMR
│
├── analysis/
│   ├── parse_omr.py                ← parser OMR nivel-1 (stats básicas)
│   ├── deep_parse.py               ← parser nivel-2 (2 sets, bigramas,
│   │                                 matrices, deltas, Y-layers)
│   ├── batch_parse.py              ← parser batch (100 sets)
│   ├── batch_parse2.py             ← parser batch 2.0 (300 sets,
│   │                                 cross-cohorte)
│   ├── batch_parse3.py             ← parser batch 3.0 (532 sets,
│   │                                 3 cohortes, per_set_stats_532)
│   ├── raw_stats.json              ← stats nivel-1 (2 sets)
│   ├── deep_stats.json             ← stats nivel-2 (2 sets)
│   ├── cross_corpus_stats.json     ← stats globales (100 sets) [legacy]
│   ├── per_set_stats.json          ← stats por set (100 sets) [legacy]
│   ├── cross_corpus2_stats.json    ← stats globales (532 sets) — 4 cohortes
│   ├── per_set_stats_300.json      ← stats por set (532 sets)
│   │
│   ├── findings_chaining.md        ← chaining 2 sets [legacy]
│   ├── findings_steps.md           ← cadencia de STEPs (2 sets)
│   ├── findings_custom_parts.md    ← custom parts embebidas (2 sets)
│   ├── findings_chaining_100.md    ← cross-corpus chaining (100 sets)
│   ├── findings_themes.md          ← convenciones por theme (100 sets)
│   ├── findings_evolution.md       ← 80s vs 90s (100 sets)
│   ├── findings_chaining_300.md    ← cross-corpus chaining (300 sets)
│   ├── findings_cohorts.md         ← 80s/90s vs kids (300 sets)
│   ├── findings_themes_300.md      ← convenciones por theme (300 sets)
│   ├── findings_chaining_300.md    ← chaining cross-corpus (532 sets)
│   ├── findings_cohorts_3.md       ← 3 cohortes 80s/90s vs kids vs classic
│   └── findings_themes_532.md      ← convenciones por theme (532 sets)
│
└── generator/
    ├── ldrw_gen.py                ← generador Python de modelos
    │                                 (clase LdrBuilder, validaciones,
    │                                  templates por theme, demo)
    ├── demo_town.ldr               ← demo estilo Town 80s (29 piezas)
    ├── demo_kid.ldr                ← demo estilo kids 2010s (18 piezas)
    ├── demo_classic.ldr            ← sanity check brick 2x4 (1 pieza)
    ├── demo_castle_lion_knights.ldr ← demo Castle con espejos (28 piezas)
    ├── demo_space_classic.ldr      ← demo Space Classic (18 piezas)
    └── demo_model.ldr              ← demo principal (legacy, 52 piezas)
```

---

## Documentos principales

| Documento | Para qué |
|-----------|----------|
| **[LDRAW_GUIDE.md](./LDRAW_GUIDE.md)** | Spec completa del formato LDraw. Lo que necesitas para **escribir o leer** archivos .dat/.ldr/.mpd. |
| **[LEARNED_CONVENTIONS_532.md](./LEARNED_CONVENTIONS_532.md)** | Convenciones aprendidas de **532 sets** (108 760 piezas). Lo que necesitas para **armar modelos al estilo OMR**. |
| **[LEARNED_CONVENTIONS_300.md](./LEARNED_CONVENTIONS_300.md)** | Análisis previo (300 sets). Conservado por trazabilidad. |
| **[LEARNED_CONVENTIONS_100.md](./LEARNED_CONVENTIONS_100.md)** | Análisis previo (100 sets). Conservado por trazabilidad. |
| **[LEARNED_CONVENTIONS.md](./LEARNED_CONVENTIONS.md)** | (Legacy) Análisis de 2 sets. Conservado por trazabilidad. |
| **[analysis/findings_cohorts_3.md](./analysis/findings_cohorts_3.md)** | 3 cohortes — diferencias estructurales. |
| **[analysis/findings_themes_532.md](./analysis/findings_themes_532.md)** | Convenciones específicas por theme LEGO. |
| **[analysis/findings_chaining_300.md](./analysis/findings_chaining_300.md)** | Detalle cuantitativo de encadenamiento. |
| **[generator/ldraw_gen.py](./generator/ldraw_gen.py)** | Generador Python que aplica las reglas aprendidas. |

---

## Las 23 reglas canónicas (corpus 532 sets)

Las 12 reglas del corpus 100 se reevaluaron con 532 sets (3 cohortes). Resumen:

- **7 reglas confirmadas** (R1, R2, R5, R7, R12, R16, R17).
- **8 reglas debilitadas o cualificadas** (R3, R4, R6, R8, R9, R10, R11, R13).
- **2 reglas refutadas** (R3 — los Space-themed disparan reflejos, R10 — BFC NO es monotónico).
- **5 reglas nuevas** (R19–R23) — centradas en Space clásicos.

Las **3 reglas más importantes** que cambian con el corpus 532:

| # | Regla canónica | Evidencia corpus 532 |
|---|----------------|----------------------|
| R1 | Y-layers múltiplos de 8 | ✅ 100 % top-15 canónicos |
| R2 | Deltas X/Z múltiplos de 20 | ✅ 100 % top-15 canónicos |
| R3 | Reflejos < 0.3 % | ❌ 1.345 % en corpus 532 — **Space-themed disparan el ratio a 5-21 %** |
| **R19** 🆕 | Space-themed tienen 5-21 % reflejos | Classic Space 21.14 %, Unitron 13.95 % |
| **R20** 🆕 | `756.dat` (baseplate 16×32 Technic) es signature Space | 1 627 usos, entra #8 global |
| **R23** 🆕 | Y = +8 LDU = antenas/mástiles | 1 389 piezas (firmado por Space-themed) |

Ver **[LEARNED_CONVENTIONS_532.md §0](./LEARNED_CONVENTIONS_532.md)** para el detalle de las 23 reglas.

---

## Generador

`generator/ldraw_gen.py` expone la clase `LdrBuilder` con:

**Métodos principales**:
- `place(file, color, x, y, z, matrix=None)` — colocar una pieza.
- `place_offset(file, color, dx, dy, dz)` — delta relativo a la última pieza.
- `place_with_rotation(file, color, x, y, z, axis, angle)` — rotación canónica.
- `step()` — inserta `0 STEP`.
- `close_section(comment)` — STEP vacío + comentario.
- `validate()` — verifica Y múltiplos de 8, X/Z múltiplos de 20, det=±1.

**Atajos**:
- `plate_2x2(x, y, z, color)`
- `brick_2x2(x, y, z, color)`
- `stud_at(x, z, color)`
- `build_wall(width, height, color, brick)`
- `build_floor(width, depth, color)`
- `build_stud_grid(rows, cols, color, plate_height)`

**Templates por theme**:
- `build_town()` — Town house (1980s style).
- `build_castle()` — Castle tower.
- `build_castle_lion_knights()` — Castle Lion Knights con estandartes espejados.
- `build_castle_black_falcons()` — Castle Black Falcons (paleta negra).
- `build_space()` — Space base.
- `build_space_base(theme='classic' | 'blacktron' | 'm_tron')` — Space por sub-theme.
- `build_pirates()` — Pirate ship base.
- `build_kid_set(theme, base_size)` — set kids post-2010 con roof slopes y chimenea.

**Reflejos**:
- `place_mirrored(file, color, x, y, z, axis='x')` — aplica matriz de reflexión canónica.
- `LdrBuilder(allow_mirrors=True)` — flag para permitir reflejos (sin warning en `validate()`).

**Constantes**: 22 colores, 9 matrices canónicas + 3 matrices de reflexión, 21 piezas (incluyendo `SLOPE_45_2X1 = "756.dat"` 🆕), medidas.

### 5 Demos distintos

```bash
cd generator/
python3 ldraw_gen.py
```

Genera **5 archivos** con estilos distintos:

| Demo | Tema | Piezas | STEPs | Files | Reflejos | Validación |
|------|------|-------:|------:|------:|---------:|------------|
| `demo_town.ldr` | Town 80s | 29 | 12 | 9 | 0 | 0e/0w |
| `demo_kid.ldr` | City Modern 2010s | 18 | 7 | 6 | 0 | 0e/0w |
| `demo_classic.ldr` | Sanity check brick 2×4 | 1 | 1 | 1 | 0 | 0e/0w |
| `demo_castle_lion_knights.ldr` | Castle con espejos | 28 | 9 | 7 | 4 | 0e/0w |
| `demo_space_classic.ldr` | Space Classic | 18 | 8 | 6 | 0 | 0e/0w |

Cada demo tiene `!THEME` y `!KEYWORDS` distintos para identificar la
cohorte. Las métricas se comparan contra la media del corpus 532
(204 piezas/set, reflejos ratio 1.34 %).

---

## Pipeline de adquisición

```bash
# 1. Descargar corpus (Parts Library oficial)
git clone --depth 1 https://github.com/pybricks/ldraw.git corpus/ldraw

# 2. Descargar 300 MPDs OMR (100 80s/90s + 200 kids)
mkdir -p corpus/mpds corpus/mpds_kids
curl -sL "https://library.ldraw.org/library/omr/1591-1.mpd" -o corpus/mpds/1591-1.mpd
# ... (ver corpus/setlist_80s90s.txt y corpus/setlist_kids.txt para los 300 URLs)

# 3. Parsear todo (300 sets, cross-cohorte)
python3 analysis/batch_parse2.py
```

---

## Estadísticas del corpus (532 sets)

| Métrica | 80s/90s | Kids | Classic | **All 532** |
|---------|--------:|-----:|--------:|-----------:|
| Sets | 100 | 200 | 232 | **532** |
| Piezas totales | 18 670 | 42 947 | 47 143 | **108 760** |
| Piezas/set media | 186.7 | 214.7 | 203.2 | **204.4** |
| Sub-builds/set | 8.39 | 7.68 | **10.13** | 8.88 |
| Custom parts | 112 | 818 | 107 | **1 037** |
| Custom ratio | 0.6 % | 1.9 % | **0.2 %** | 0.95 % |
| BFC CERTIFY | 21 % | 36.5 % | **16.4 %** | 24.8 % |
| Reflejos (det<0) | 0.27 % | 0.25 % | **2.77 %** | **1.35 %** |

**Themes** (top-10 en 532): Town > Classic Town (109 sets combinados) · Train > 9V (14) · Castle Lion Knights (10) · Space Classic Space (8) · Train 12V (8) · M:Tron (8) · Friends (17) · Pirates (7) · Model Team (5).

**Décadas** (532 sets): 1980s (140) · 1990s (165) · 2000s (140) · 2010s (80) · 2020s (7).

---

## Limitaciones

1. **532 sets**, no los 1 470 del OMR — muestra diverseada pero no exhaustiva
   (36.2 % del OMR).
2. **OMR incompleto**: faltan muchos sets (Ninjago, Star Wars post-2010 en su
   mayoría); esto sesga los themes analizados.
3. **Plan C shortfall**: Pirates I (0/8), Castle Forestmen/Black Knights/Dragon
   Knights (todos shortfall), Sports Soccer (0/3) — sets ya estaban en cohortes previos.
4. **Pirates outlier**: 6286 Skull's Eye Schooner (2 834 piezas) + 6285 Black
   Seas Barracuda (2 975 piezas) = 91.9 % del theme Pirates.
5. **BFC CERTIFY** todavía bajo (24.8 %) — sesgo editorial del OMR.
6. **Sin análisis de TEXMAP/texturas** — muchos sets modernos usan texturas PNG.
7. **Sin análisis de sub-modelos anidados** (jerarquía dentro del MPD).
8. **Sin comparación con MOCs** (la comunidad no-OMR puede tener otras
   convenciones).

---

## Próximos pasos sugeridos

- Incluir sets Technic de los 80s/90s para cuantificar la influencia Technic
  (sería una 4ª cohorte).
- Comparar OMR con MOCs para validar universalidad.
- Analizar texturas (TEXMAP) en sets modernos.
- Clustering estructural para detectar sub-ensamblajes recurrentes.
- Entrenar modelo de lenguaje sobre las 108 760 instancias.
- Comparar OMR con MOCs para medir universalidad de las convenciones.

---

## Licencia y atribución

- **LDraw.org** — formato y bibliotecas bajo CC BY 4.0.
- **LEGO®** — marca registrada de The LEGO Group, no patrocinada.
- **pybricks/ldraw** (mirror GitHub) — distribución oficial de las bibliotecas.
- **OMR (Official Model Repository)** — modelos contribuidos por la comunidad.
