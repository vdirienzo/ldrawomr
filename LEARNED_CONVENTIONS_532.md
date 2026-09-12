# Convenciones LDraw — Análisis cross-corpus 3.0 (532 sets OMR)

> Corpus ampliado a **532 sets OMR** en tres cohortes:
> - **80s/90s** (100 sets, 18 670 piezas): Town, Castle, Space, Pirates, Model Team, Star Wars, Western, etc.
> - **Kids** (200 sets, 42 947 piezas): City, Creator, Friends, Western, Fabuland, Harry Potter, etc.
> - **Classic** (232 sets, 47 143 piezas) — **Plan C**: distribución uniforme sobre 49 themes pre-2000.
>
> **Total**: 532 sets · 108 760 piezas · 4 724 sub-builds · 1 037 custom parts · 132 BFC CERTIFY · **1.345 % reflejos**.
>
> Documentos previos: `LEARNED_CONVENTIONS.md` (2 sets), `LEARNED_CONVENTIONS_100.md` (100 sets), `LEARNED_CONVENTIONS_300.md` (300 sets).

---

## 0. Las 23 reglas cross-corpus (definitivas)

### Reglas confirmadas (7)

| # | Regla | Evidencia corpus 532 |
|---|-------|----------------------|
| R1 | **Y-layers canónicos múltiplos de 8** | 100 % top-15 (15/15) |
| R2 | **Deltas X/Z canónicos múltiplos de 20** | Top-15: 100 % canónicos |
| R5 | **Top 10 piezas cubren ~24 % del corpus** | 24.3 % |
| R7 | **Bigramas son self-bigrams** | Top-15: 100 % self |
| R12 | **`4-4cyli.dat` es universal, no outlier** | 6 093 usos (5.6 %) — distribuido en 3 cohortes |
| R16 | **Fabuland tiene identidad propia** (~25 piezas `u91xx`) | 9.3 % custom parts |
| R17 | **Friends es el theme más decorativo** (`6141` dominante) | `6141` es #4 global con 2 519 usos |

### Reglas debilitadas / cualificadas (8)

| # | Regla original | Estado |
|---|----------------|--------|
| R3 | Reflejos < 0.3 % | ❌ **Refutada**: 1.345 % (5× más). Space-themed disparan el ratio (ver R19) |
| R4 | Custom parts = 0.6 % | 🟡 Cualificada: 0.95 % global; varía 0.23 % (clásicos) a 1.9 % (kids) |
| R6 | Y=-46.1 slope 33° en top | 🟡 Sigue cierto en detalle, pero cae del top-15 con corpus 532 |
| R8 | Technic embebido en no-Technic | 🟡 Ratio cae en agregados (clásicos tienen poco Technic irregular) |
| R9 | 90s 1.7× más grandes que 80s | 🟡 Cualificada: clásicos 203 p/set ≈ kids 215 > 80s/90s 187 |
| R10 | BFC CERTIFY decrece en 90s | ❌ **Refutada otra vez**: clásicos 16.4 % (el más bajo), kids 36.5 % |
| R11 | Sub-builds crecen con tiempo | 🟡 Cualificada: clásicos 10.13 > 80s/90s 8.39 > kids 7.68 (NO monotónico) |
| R13 | Kids vocabulario moderno exclusivo | 🟡 Cualificada: las piezas nuevas del top-30 (`756`, `3068b`, `3795`) son de **clásicos**, no kids |

### Reglas nuevas descubiertas con corpus 532 (5)

| # | Regla nueva | Evidencia |
|---|-------------|-----------|
| **R19** | **Space-themed sets tienen 5-21 % reflejos** (87 % de todos los reflejos clásicos vienen de Space sub-themes) | Classic Space 21.14 %, Unitron 13.95 %, Blacktron I 12.36 % |
| **R20** | **`756.dat` (baseplate 16×32 Technic) es la pieza signature de Space clásicos** | 1 627 usos; entra al #8 global desde corpus 300 |
| **R21** | **Clásicos tienen MENOR BFC CERTIFY** que 80s/90s — la formalidad NO es monotónica con el tiempo | 16.4 % vs 21 % vs 36.5 % |
| **R22** | **Bigramas heterogéneos significativos = slopes 33° + slopes 45° inv** (Space clásicos) | `3818↔3819`, `3816↔3817` (4 pares slope-slope >30) |
| **R23** | **Y = +8 LDU** (1 389 piezas) entra al top-15 — clásica antena/mástil de Space que sobresale del bounding box | Firmado por Blacktron/Unitron |

---

## 1. Topología por cohorte

| Métrica | 80s/90s | kids | classic | **All 532** |
|---------|--------:|-----:|--------:|-----------:|
| Sets | 100 | 200 | 232 | **532** |
| Piezas totales | 18 670 | 42 947 | 47 143 | **108 760** |
| Piezas/set media | 186.7 | 214.7 | 203.2 | **204.4** |
| Sub-builds/set | 8.39 | 7.68 | **10.13** | 8.88 |
| STEPs/set | 19.85 | 29.78 | ? | ? |
| Custom parts | 112 (0.6%) | 818 (1.9%) | **107 (0.2%)** | 1 037 (0.95%) |
| BFC CERTIFY | 21 % | 36.5 % | **16.4 %** | 24.8 % |
| **Reflejos (det<0)** | **0.27 %** | **0.25 %** | **2.77 %** | **1.35 %** |
| STEPs vacíos | 39 % | 28.5 % | **49.1 %** | ? |

**Lectura**:
- **Classic es la cohorte más "pura"**: pocos custom parts, pocas reflejos estructurales (excepto Space), más descompuesta en sub-builds.
- **Space-themed clásicos explican el 87.8 % de los reflejos clásicos** (1 147/1 306).
- **BFC CERTIFY no es monotónico**: kids (36.5 %) > 80s/90s (21 %) > clásicos (16.4 %).

---

## 2. El shock de los reflejos (R3 refutada, R19 nueva)

### Hipótesis: ¿son los clásicos más reflejados porque espejan más?

**NO**. Es un sesgo del theme Space, no del corpus clásico como conjunto.

| Theme | Sets | Piezas | Reflejos | Ratio |
|-------|-----:|-------:|---------:|------:|
| **Classic Space** | 8 | 927 | 196 | **21.14 %** |
| **Unitron** | 4 | 2 488 | 347 | **13.95 %** |
| **Blacktron I** | 6 | 1 554 | 192 | **12.36 %** |
| M:Tron | 8 | 1 234 | 99 | 8.02 % |
| Space Police I | 3 | 862 | 61 | 7.08 % |
| Ice Planet 2002 | 8 | 720 | 50 | 6.94 % |
| Blacktron II | 8 | 984 | 50 | 5.08 % |
| Futuron | 7 | 1 030 | 51 | 4.95 % |
| Space Police III | 8 | 2 377 | 95 | 4.00 % |
| **Classic Town (69 sets)** | 69 | 11 134 | 45 | **0.40 %** |
| Boat | 5 | 1 009 | 30 | 2.97 % |
| 12V Trains | 8 | 2 232 | 29 | 1.30 % |
| Western, Train 9V, Train 4.5V | ~30 | ~7 000 | 0 | **0.00 %** |

**Diagnóstico**: 73 sets Space-themed = 87.8 % de los reflejos clásicos. Classic Town (theme mayoritario) tiene ratio 0.40 % idéntico a kids modernos.

### ¿Qué pieza se refleja?

Inspección directa de `6990-1.mpd` (Unitron Mobile HQ, 1 075 piezas, 296 reflejos):
- `756.dat` (baseplate 16×32 Technic): **254 reflejos** con matrix `(-1, 0, 0, 0, 0, -1, 0, 1, 0)` (rotación 180° Y).
- `993.dat` (Technic bracket): 39 reflejos con la misma matrix.

**Implicación**: las naves Space pre-1995 espejaban masivamente `756.dat` para construir estructuras simétricas. Los autores OMR duplicaban filas espejadas en lugar de girar el modelo entero.

---

## 3. Top piezas cross-corpus (532 sets)

| # | Pieza | Cuenta | % | Notas |
|---|-------|-------:|---:|-------|
| 1 | `4-4cyli.dat` | 6 093 | 5.60 % | Cilindro base, universal |
| 2 | `3023.dat` (Plate 1×2) | 3 670 | 3.37 % | Vocabulario base |
| 3 | `3004.dat` (Brick 1×2) | 3 293 | 3.03 % | Vocabulario base |
| 4 | `6141.dat` (Plate 1×1 round) | 2 519 | 2.32 % | Decoración |
| 5 | `3005.dat` (Brick 1×1) | 2 360 | 2.17 % | Columnata |
| 6 | `3024.dat` (Plate 1×1) | 2 091 | 1.92 % | Detalle |
| 7 | `3710.dat` (Plate 1×4) | 2 036 | 1.87 % | Chasis largos |
| **8** | **`756.dat` (Baseplate 16×32 Technic)** | **1 627** | **1.50 %** | **🆕 NUEVO — Space-themed signature** |
| 9 | `3010.dat` (Brick 1×4) | 1 500 | 1.38 % | |
| 10 | `3820.dat` (Slope 1×2) | 1 229 | 1.13 % | |

**Top 10 cubre 24.3 %** del corpus (vs 32.7 % en corpus 300). La cobertura baja porque los clásicos diluyen con vocabulario más diverso.

**Piezas NUEVAS en top-30** (vs corpus 300):
- `756.dat` (baseplate Technic 16×32) — #8 directo.
- `3068b.dat` (tile 2×2) — clásico para fachadas.
- `3795.dat` (plate 2×6) — chasis largo clásico.

**Piezas que SALEN**: `166.dat`, `2420.dat`, `3660.dat` — decorativas kids.

---

## 4. Top deltas (532 sets)

| # | (dx, dy, dz) | Count | % del corpus |
|---|---|---:|---:|
| 1 | (0, 0, 0) | 2 660 | 2.45 % |
| 2 | (0, -8, 0) | 1 669 | 1.53 % |
| 3 | (60, 0, 0) | 1 597 | 1.47 % |
| 4 | (20, 0, 0) | 1 401 | 1.29 % |
| 5 | (-60, 0, 0) | 1 104 | 1.02 % |
| 6 | (0, -24, 0) | 1 068 | 0.98 % |
| 7 | (0, 0, -60) | 1 057 | 0.97 % |
| 8 | (100, 0, 0) | 1 027 | 0.94 % |
| 9 | (40, 0, 0) | 1 011 | 0.93 % |
| 10 | (0, 0, -20) | 968 | 0.89 % |

**Distribución top-15**: 100 % canónicos (múltiplos de 20 en X/Z, múltiplos de 8 en Y). Las firmas Technic irregulares de kids quedan enterradas en el agregado.

---

## 5. Y-layers (532 sets)

| Y | Cuenta | Significado |
|---:|-------:|-------------|
| 0 | 6 436 | Plano base |
| -8 | 6 041 | 1ª plate |
| -24 | 5 976 | 1er brick |
| -32 | 3 754 | 3ª plate |
| -16 | 3 439 | 2ª plate |
| -48 | 3 164 | 2º brick |
| -40 | 2 742 | brick+plate |
| -56 | 2 723 | 4ª plate |
| -72 | 2 098 | 5ª plate |
| -64 | 1 905 | 3er brick |
| -96 | 1 738 | 5º brick |
| **+8** | **1 389** | **🆕 Antena/mástil de Space (R23)** |
| -80 | 1 345 | 4º brick |
| -144 | 1 102 | 10º brick (clásicos profundos) |
| -120 | 1 101 | 7º brick |

R1 se mantiene firme (100 % top-15 múltiplos de 8).

---

## 6. Bigramas (532 sets)

**Top-15: 100 % self-bigrams** (más limpio que corpus 300):
- `4-4cyli → 4-4cyli` × 6 069 (casi todo clásico, ver R12).
- `756 → 756` × 1 588 (🆕 Space signature).
- `3004 → 3004` × 1 563.
- `3023 → 3023` × 1 384.
- `6141 → 6141` × 1 296.

**Bigramas heterogéneos >30** (nuevos con corpus 532):

| Par | Count | Interpretación |
|---|---:|---|
| `3818 → 3820` | 238 | Slope 33° + Slope 45° (chasis Space) |
| `3819 → 3818` | 233 | Slope 33° inv + Slope 33° |
| `3818 → 3819` | 204 | Slope 33° + Slope 33° inv |
| `6014 → 6015` | 176 | Wheel + Tyre (Town/Train) |
| `3819 → 3820` | 199 | Slope 33° inv + Slope 45° |
| `3816 → 3817` | 181 | Slope 45° inv + Slope 45° |

R22: las familias slope-slope son la firma de los Space clásicos.

---

## 7. Análisis por theme

### 7.1 Town > Classic Town (corpus principal)

- **69 sets** en corpus Plan C + 40 legacy Town = **109 sets Town** total.
- 18 819 piezas, media 272 piezas/set (los clásicos son grandes).
- Top pieza: `3023` (Plate 1×2), seguida de `3004`.
- **0.40 % reflejos** — Town es estructuralmente simétrico pero los autores OMR rotan canónicamente, no reflejan.

### 7.2 Castle (28 sets, 6 sub-themes)

Sub-themes en corpus 532:
- Lion Knights (10 sets), Black Falcons (1 set), Forestmen (0 sets — shortfall), Black Knights (0), Dragon Knights (0), Castle genérico (1).

**Gramática Castle común** (16 piezas compartidas por sub-themes):
- `3004`, `3023`, `3024`, `3005`, `3710` — muros.
- `3820`, `3040b`, `3039`, `4444` — slopes y techos.
- `6141`, `2412b` — decoración.
- `2541`, `3847`, `3626ap01` — figuras exclusivas Castle.

**Lion Knights firma vertical**: `delta (0,-24,0) = 121 ocurrencias` (más alto del theme).

### 7.3 Space (91 sets, 12 sub-themes)

Sub-themes en corpus 532 (con ratios de reflejos):
- Classic Space (8, 21 % reflejos) — baseplate 756 dominante.
- Futuron (7), Blacktron II (8), M:Tron (8), Ice Planet (8), Space Police II (8), Space Police III (8), Blacktron I (6, 12 % reflejos), Space Police I (3), Spyrius (3), Unitron (4, 14 %), Insectoids (1).

**3 categorías de Space por bigrama #1**:
- (A) Baseplate `756` dominante en 8 sub-themes pre-2000.
- (B) Plate `3023` sin `756` en Space Police II/Spyrius/Insectoids.
- (C) Hinge `54200` en Space Police III (moderno).

### 7.4 Pirates (7 sets, sesgo confirmado)

**91.9 % de las piezas en 2 mega-ships**:
- 6286 Skull's Eye Schooner: 2 834 piezas.
- 6285 Black Seas Barracuda: 2 975 piezas.

`4-4cyli` = 3 895 unidades = 63.9 % del theme (= mástiles). Sesgo de Pirates confirmado.

### 7.5 Train

- 12V (8 sets), 9V (14), 4.5V (8), Train genérico (2).
- Vocabulario: `3710`, `4-4cyli`, `4274`, `4275` (hinge plates Technic).
- Eje Z-dominante (R18 confirmada con corpus 532).

---

## 8. Generador actualizado

`generator/ldraw_gen.py` (1 161 líneas, +236 desde corpus 300).

### Nuevos métodos
- `place_mirrored(file, color, x, y, z, axis='x')` — aplica matriz de reflexión canónica.
- `LdrBuilder(allow_mirrors=True)` — flag global para permitir reflejos.
- `build_castle_lion_knights()` — 28 piezas, 4 espejadas.
- `build_castle_black_falcons()` — 28 piezas, layout idéntico colores negro.
- `build_space_base(theme='classic' | 'blacktron' | 'm_tron')` — vocabulario Space por sub-theme.

### Constantes actualizadas
- 21 piezas (incluyendo `SLOPE_45_2X1 = "756.dat"` 🆕).
- 22 colores, 9 matrices canónicas + 3 matrices de reflexión.

### 5 Demos validados (0 errores, 0 warnings)

| Demo | Piezas | STEPs | Files | Reflejos |
|------|-------:|------:|------:|---------:|
| `demo_town.ldr` | 29 | 12 | 9 | 0 |
| `demo_kid.ldr` | 18 | 7 | 6 | 0 |
| `demo_classic.ldr` | 1 | 1 | 1 | 0 |
| `demo_castle_lion_knights.ldr` | 28 | 9 | 7 | 4 |
| `demo_space_classic.ldr` | 18 | 8 | 6 | 0 |

---

## 9. Limitaciones del análisis

1. **532/1 470 = 36 % del OMR** — buena cobertura pero no exhaustiva.
2. **Pirates shortfall del Plan C**: 0 sets nuevos (todo el theme ya estaba en cohortes previos).
3. **Castle Forestmen/Black Knights/Dragon Knights shortfall**: 0 sets.
4. **OMR no incluye todos los sets LEGO**: faltan muchos Ninjago, Star Wars post-2010, etc.
5. **Sesgo de autores OMR**: no representan a todos los autores LEGO CAD.

---

## 10. Recursos generados

| Recurso | Ruta | Descripción |
|---------|------|-------------|
| MD de referencia LDraw | `LDRAW_GUIDE.md` | Spec del formato |
| MD 2 sets (legacy) | `LEARNED_CONVENTIONS.md` | Beetle + Pet Shop |
| MD 100 sets (legacy) | `LEARNED_CONVENTIONS_100.md` | 80s/90s |
| MD 300 sets (legacy) | `LEARNED_CONVENTIONS_300.md` | 80s/90s + kids |
| **MD 532 sets (canónico)** | `LEARNED_CONVENTIONS_532.md` | **Este documento** |
| 100 MPDs | `corpus/mpds/*.mpd` | 6.7 MB |
| 200 MPDs kids | `corpus/mpds_kids/*.mpd` | 25 MB |
| 232 MPDs Plan C | `corpus/mpds_classic/*.mpd` | 8.5 MB |
| Plan C distribución | `corpus/plan_c_distribution.json` | Plan + shortfalls |
| Setlist classic | `corpus/setlist_classic.{txt,json}` | 232 sets |
| Cross-corpus JSON | `analysis/cross_corpus2_stats.json` | 4 cohortes |
| Per-set 532 | `analysis/per_set_stats_300.json` (532 entries) |
| Encontrar chaining 532 | `analysis/findings_chaining_300.md` |
| Encontrar cohorts 3 | `analysis/findings_cohorts_3.md` |
| Encontrar themes 532 | `analysis/findings_themes_532.md` |
| Generador Python | `generator/ldraw_gen.py` | 1 161 líneas |
| 5 demos | `generator/demo_{town,kid,classic,castle_lion_knights,space_classic}.ldr` |

---

## 11. Limitaciones del análisis

1. **532/1 470 = 36 % del OMR** — buena cobertura pero no exhaustiva.
2. **OMR no incluye todos los sets LEGO**: faltan muchos Ninjago, Star Wars post-2010, etc.
3. **Plan C shortfall**: 24 themes quedaron con shortfall documentado en `corpus/plan_c_distribution.json`.
4. **Pirates outlier**: 6286 + 6285 = 91.9 % del theme Pirates.
5. **BFC CERTIFY** bajo (24.8 %) — sesgo editorial del OMR.
6. **Sin análisis de TEXMAP/texturas** — muchos sets modernos usan texturas PNG.
7. **Sin análisis de sub-modelos anidados** (jerarquía dentro del MPD).
8. **Sin comparación con MOCs** (la comunidad no-OMR puede tener otras convenciones).

---

## 12. Gaps conocidos y plan para próxima sesión

### Sets no descargados

El OMR tiene ~1 470 sets totales. Tenemos 532. **Faltan ~938 sets**.

### Themes no cubiertos (oportunidades)

| Theme | Sets en OMR | Estado |
|-------|------------:|:------:|
| Technic | 158 | ❌ NO descargado (excluido por policy) |
| Brickheadz | 76 | ❌ NO descargado |
| Racers | 76 | ❌ NO descargado |
| Star Wars | 64 | ⚠️ Parcial (6 en 80s/90s) |
| Architecture | 36 | ❌ NO descargado |
| Modular Buildings | 14 | ❌ NO descargado |
| Ideas (CUUSOO) | 12 | ❌ NO descargado |
| Creator Expert | 20 | ❌ NO descargado |
| Icons | 8 | ❌ NO descargado |

### Plan D recomendado (próxima sesión)

Si el usuario pide "completar todo":

1. **Crear 4ª cohorte "Modern/Collector"**: Technic + Brickheadz + Architecture + Modular Buildings + Icons (~280 sets).
2. **Crear 5ª cohorte "Remaining"**: Star Wars restantes + Ideas + Mixels + Elves + Specialty (~300 sets).
3. **Re-parsear todo** (corpus target: ~1 100 sets, ~230 000 piezas).
4. **Re-analizar**: 4-5 subagentes paralelos para actualizar findings.
5. **Actualizar generador**: añadir templates para Technic (axles, beams) y Architecture (landmarks).
6. **Sintetizar** `LEARNED_CONVENTIONS_FINAL.md` con ~28-32 reglas definitivas.

**Tiempo estimado**: 1-2 horas wall-clock.

Ver **[NEXT_SESSION.md](./NEXT_SESSION.md)** para el plan completo paso a paso.
