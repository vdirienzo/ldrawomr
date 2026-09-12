# Hallazgos: Diferencias estructurales entre cohortes 80s/90s y kids

Análisis basado en `cross_corpus2_stats.json` y `per_set_stats_300.json` (300 sets OMR, 61 617 parts totales).

---

## 1. Tamaño y cadencia

| Métrica                                | 80s/90s              | kids                  | Δ (kids − 80s/90s)   |
|----------------------------------------|----------------------|------------------------|----------------------|
| Sets                                   | 100                  | 200                    | +100 (+100%)         |
| parts totales                         | 18 670               | 42 947                 | +24 277 (+130%)      |
| **parts/set media**                   | 186.70               | 214.74                 | **+28.0** (+15%)     |
| **parts/set mediana**                 | 82.5 (avg de 82, 83) | 87.5 (avg de 87, 88)   | **+5.0** (+6%)       |
| **Sub-builds/set media**               | 8.39                 | 7.675                  | **−0.71** (−8.5%)    |
| **Sub-builds/set mediana**             | 5.5 (avg de 5, 6)    | 5 (avg de 5, 5)        | **−0.5**             |
| **STEPs/set media**                    | 19.85                | 29.775                 | **+9.93** (+50%)     |
| **STEPs/set mediana**                  | 7 (avg de 5, 9)      | 10.5 (avg de 7, 14)    | **+3.5** (+50%)      |
| **parts/STEP media**                  | 9.41                 | 7.21                   | **−2.20** (−23%)     |

**Lectura**: kids tiene sets ligeramente más grandes (15% más parts en media), pero sobre todo **el doble de granularidad constructiva** (más STEPs/set, menos parts/step). Es un salto cualitativo, no solo de tamaño.

---

## 2. Vocabulario diferencial

### Top 10 parts exclusivas de **80s/90s** (en top-50 80s/90s, **no en top-30 kids**)

| # | parts                | Count | Categoría funcional                                  |
|---|----------------------|-------|------------------------------------------------------|
| 1 | `754.dat`            | 265   | Roof tile / slope classic                           |
| 2 | `2420.dat`           | 166   | Plate 2×2 corner (angular classic)                  |
| 3 | `3460.dat`           | 136   | Plate 1×8 (larga)                                   |
| 4 | `3660.dat`           | 120   | Slope / arco 2×1 45°                                |
| 5 | `4286.dat`           | 114   | Slope brick 33° 1×2                                 |
| 6 | `3819.dat`           | 102   | Baseplate 32×32 (base grande clásica)               |
| 7 | `3818.dat`           | 101   | Baseplate grande clásica                            |
| 8 | `3665a.dat`          | 99    | Slope brick 1×2 45° (Technic-friendly)              |
| 9 | `3700.dat`           | 95    | **Technic brick 1×2 con hole** (Technic embebido)   |
| 10 | `4085c.dat`          | 93    | Plate 1×1 con clip (Technic interface)              |

Más allá del top-10, también exclusivos: `3063b.dat` (brick 1×2 con hole), `4624.dat` (plate hinge), `6091.dat`, `6019.dat` (clip vertical), `4589.dat` (cono 1×1), `3039.dat` (slope 2×2), `6014.dat`/`6015.dat` (wheels antiguos), `3641.dat` (steering wheel), `3023.DAT` (case-variant legacy).

**Patrón 80s/90s**: dominio de **plates y bricks básicos**, slopes clásicos, **Technic embebido** (3700, 4085c, 3063b, 4624, 6091), y **baseplates grandes** (3818, 3819).

### Top 10 parts exclusivas de **kids** (en top-50 kids, **no en top-30 80s/90s**)

| # | parts                | Count | Categoría funcional                                  |
|---|----------------------|-------|------------------------------------------------------|
| 1 | `166.dat`            | 426   | Antenna / detail piece                              |
| 2 | `3070b.dat`          | 409   | **Tile 1×1 with groove** (moderna)                   |
| 3 | `54200.dat`          | 318   | **Slope 1×1×45° invertido** (moderna)                |
| 4 | `3003.dat`           | 265   | Brick 2×2 (más frecuente en kids)                   |
| 5 | `2357.dat`           | 222   | Brick 2×2 corner (más frecuente en kids)            |
| 6 | `3068b.dat`          | 228   | **Tile 2×2** (moderna)                              |
| 7 | `30136.dat`          | 205   | Cookie / life preserver (decorativa moderna)        |
| 8 | `2780.dat`           | 236   | Handle / Technic pin-with-friction                  |
| 9 | `4865a.dat`          | 175   | Panel 1×2×1 (carcasa moderna)                       |
| 10 | `98283.dat`          | 172   | **Tile 1×2 round** (moderna)                        |

Más allá: `2454.dat`, `6636.dat`, `3001.dat`, `15573.dat`, `98138.dat`, `4162.dat`, `30137.dat` (todas modernas, decoración/curvas/printed).

**Patrón kids**: predominio de **tiles con groove** (3070b, 3068b, 98283), **slopes 1×1** (54200), **paneles curvos** (4865a), y **parts decorativas** (30136 cookie, 166 antenna, 2454, 6636).

### parts compartidas (intersección del top-30)

**22 parts compartidas** (73% del top-30 80s/90s; 80% del top-30 kids):

```
4-4cyli.dat, 3023.dat, 3004.dat, 6141.dat, 3024.dat, 3710.dat, 3820.dat,
3005.dat, 3623.dat, 3010.dat, 3022.dat, 4070.dat, 3020.dat, 2412b.dat,
3062b.dat, 3666.dat, 3021.dat, 3040b.dat, 3622.dat, 3069b.dat, 2431.dat, 3009.dat
```

Estas 22 parts suman **7 217 occurrences** en 80s/90s (38.7% del total) y **13 793** en kids (32.1%). El **core de bricks/plates básicos** es estable; la **diferencia está en la larga cola** (tiles modernas, Technic embebido, decorativos).

---

## 3. Patrones de deltas

Analizando los **deltas con componentes no enteros** (rotaciones Technic irregulares como 1.5, 2.8, −0.2, etc.):

**80s/90s** (4 entradas en top-30 con deltas no enteros):
- `(3.0, −0.1, −0.5)` → 148 (Technic pin 3L offset)
- `(1.8, 0.0, −2.4)` → 146
- `(1.5, 0.0, −2.6)` → 101
- `(2.2, 0.1, 2.0)` → 93

**Total: 488 occurrences / 18 670 parts = 2.61%**

**kids** (4 entradas en top-30 con deltas no enteros):
- `(2.8, −0.6, 0.8)` → 229
- `(−0.2, 0.3, −2.0)` → 175
- `(−2.1, 0.0, 2.1)` → 134
- `(1.9, 0.5, 0.2)` → 104

**Total: 642 occurrences / 42 947 parts = 1.50%**

**Resultado contrario al esperado**: 80s/90s tiene **ratio más alto** (1.74×) de deltas Technic irregulares. Kids compensó con más Technic embebido en count absoluto (642 vs 488) pero su cohorte es 2.3× más grande.

**Implicación**: el Technic embebido en System es proporcionalmente **más frecuente en los 80s/90s**; en kids el System es más "limpio" en offsets, con Technic relegado a sub-builds dedicados.

---

## 4. Cadencia constructiva

| Métrica                                     | 80s/90s      | kids         | Δ                    |
|---------------------------------------------|--------------|--------------|----------------------|
| **STEPs vacíos (total_steps == 0)**         | 39 / 100 = **39.0%** | 57 / 200 = **28.5%** | −10.5 pp             |
| **Sub-builds/set (media)**                  | 8.39         | 7.675        | −0.71 (−8.5%)        |
| **Sub-builds/set (mediana)**                | 5.5          | 5            | −0.5                 |
| **parts/STEP (global)**                    | 9.41         | 7.21         | −2.20 (−23%)         |
| **STEPs/set (media)**                       | 19.85        | 29.775       | +9.93 (+50%)         |
| **STEPs/set (mediana)**                     | 7            | 10.5         | +3.5 (+50%)          |

### Lectura

- **STEPs vacíos**: 39% de los sets 80s/90s tienen `total_steps == 0` vs 28.5% en kids. Los models antiguos llegaron a OMR sin la sección STEP del MPD (los autores digitales de los 2000s/2010s añadieron STEPs sistemáticamente).
- **Sub-builds**: contrariamente a la intuición, **80s/90s descompone MÁS** (mean 8.39 vs 7.675). Esto sugiere que los MPDs modernos de kids son más **monolíticos** (un solo gran sub-build principal) mientras los antiguos tienden a romperse en módulos (ruedas, cabinas, chasis por separado).
- **parts/STEP**: kids es **más granular** (7.21 vs 9.41), consistente con manuales digitales modernos que muestran **sub-pasos** y vistas explosionadas más detalladas.

**Conclusión**: la cadencia kids refleja manuales digitales (LDraw Builder, Bricklink Studio) que producen **más pasos, pasos más pequeños, menos descomposición de sub-builds**.

---

## 5. BFC y reflejos

| Métrica                              | 80s/90s           | kids              | Δ                    |
|--------------------------------------|-------------------|-------------------|----------------------|
| **BFC CERTIFY (count)**              | 21 / 100 = **21%**| 73 / 200 = **36.5%** | **+15.5 pp**       |
| **BFC any (CLIP/CERTIFY/NOCLIP)**    | 21 / 100 = 21%    | 74 / 200 = 37%    | +16 pp               |
| **neg_det_count total**              | 50                | 107               | +57                  |
| **neg_det_ratio (per piece)**        | 0.00268           | 0.00249           | −0.00019 (−7%)       |
| **Sets con neg_det > 0**             | 2 / 100 = 2%      | 4 / 200 = 2%      | 0 pp                 |

### Lectura

- **BFC CERTIFY ratio**: kids casi duplica a 80s/90s (36.5% vs 21%). Los OMR modernos se adhieren más a las **mejores prácticas formales** de orientación (BFC CERTIFY + CLIP CW).
- **Reflejos**: sorprendentemente similares. Solo **2 sets 80s/90s y 4 sets kids** usan matrices con determinante negativo (mirroring). El ratio per-piece es prácticamente idéntico (0.00268 vs 0.00249). Los autores de OMR evitan sistemáticamente los reflejos — ambas cohortes son **simétricas por convención**.

**Implicación**: kids refleja ligeramente menos, pero la diferencia es marginal. La simetría se mantiene por **construcción**, no por mirrored geometry.

---

## 6. Custom parts

| Métrica                                       | 80s/90s        | kids           | Δ                |
|-----------------------------------------------|----------------|----------------|------------------|
| **Custom parts totales (`total_custom_parts`)** | 112           | 818            | **+706 (+630%)** |
| **Embedded custom parts (en per-set)**        | 78             | 519            | +441             |
| **Embedded subparts**                         | 34             | 292            | +258             |
| **Embedded hi-res primitives**                | 0              | 7              | +7               |
| **Sets con custom parts > 0**                 | 17 / 100 = 17% | 71 / 200 = **35.5%** | **+18.5 pp** |
| **Custom parts / set (ratio)**                | 1.12           | 4.09           | +2.97            |
| **Custom parts / 1000 parts (ratio)**        | 6.0            | 19.0           | +13.0            |

### Lectura

- **Kids usa 3.65× más custom parts absolutos** (818 vs 112) y casi **el doble proporcionalmente** (4.09/set vs 1.12/set).
- **Embedded subparts** saltan de 34 → 292 (8.6×) y los **hi-res primitives** solo aparecen en kids (7 vs 0).
- Los OMR modernos usan técnicas de **subfiles, primitivas hi-res, y custom geometry** mucho más agresivamente.
- Esto encaja con la diferencia de cadencia: más granularidad + más decoración requieren más sub-partes para evitar duplicación.

**Implicación**: kids = OMR con vocabulario nativo LDraw moderno (subfiles, LOD). 80s/90s = OMR más "plano" (más parts duplicadas, menos geometría especializada).

---

## 7. Reglas específicas por cohorte

1. **Cohorte 80s/90s tiene mayor edad media y menos diversidad temporal**: solo cubre 1980s (25 sets, 3 090 parts) y 1990s (75 sets, 15 580 parts). Kids cubre 5 décadas (1980s=47, 1990s=41, 2000s=44, 2010s=66, 2020s=2). La cohorte 80s/90s es **2 décadas puras**; kids es **5 décadas mezcladas**.

2. **Cohorte kids tiene vocabulario propio moderno**: parts como `3070b.dat` (tile 1×1 con groove, 409 occurrences), `54200.dat` (slope 1×1×45°, 318), `3068b.dat` (tile 2×2, 228), `98283.dat` (tile 1×2 round, 172), `166.dat` (antenna, 426), `30136.dat` (cookie, 205) son **características de los 2000s/2010s** y están **ausentes del top-30 de 80s/90s**.

3. **80s/90s usa más Technic embebido en System**: `3700.dat` (Technic brick 1×2 con hole, 95), `4085c.dat` (plate 1×1 con clip, 93), `3063b.dat` (brick 1×2 con hole, 90), `4624.dat` (plate con hinge, 88), `6091.dat` (86), `6019.dat` (80). Estas 6 parts suman **532 occurrences** — en kids todas están fuera del top-30.

4. **kids descompone menos pero en pasos más pequeños**: sub-builds/set 7.675 (vs 8.39) pero STEPs/set 29.775 (vs 19.85). Los MPDs modernos son **más monolíticos estructuralmente** pero **más granulares en instrucciones**.

5. **kids tiene 1.74× más ratio BFC CERTIFY** (36.5% vs 21%). Los autores modernos son más estrictos con la orientación canónica (CERTIFY + CLIP CW vs NOCLIP legacy).

6. **kids tiene 3.65× más custom parts absolutos** (818 vs 112) y 2× más **proporcionalmente** (4.09/set vs 1.12/set). Incluye 7 hi-res primitives (vs 0 en 80s/90s) y 292 embedded subparts (vs 34).

7. **kids tiene paletas de color más diversas y modernas**: aparecen colores LDraw **71** (2 944 occurrences), **72** (2 024), **70** (1 107), **84** (352), **73** (366), **28** (380), **27** (342), que **no están en el top-20 de 80s/90s**. Estos códigos corresponden a la familia "bluish gray" (71, 72, 73), "reddish brown" (70), "flesh tones" (84), y verdes oscuros modernos (28). La paleta 80s/90s se concentra en códigos legacy: **0** (5 071), **16** (3 300), **7** (2 995), **15** (1 929), **4** (1 615), **14** (1 099) — sin ningún código "bluish gray" en el top-20.

8. **80s/90s tiene ratio más alto de deltas Technic irregulares** (2.61% vs 1.50%): 488 occurrences / 18 670 vs 642 / 42 947. Las rotaciones no enteras (1.5, 1.8, 2.2, 2.8, etc.) son **1.74× más frecuentes proporcionalmente** en models antiguos — Technic embebido es relativamente más prominente.

9. **39% de sets 80s/90s tienen 0 STEPs** en su MPD (39/100), vs 28.5% en kids (57/200). Esto refleja que los MPDs antiguos en OMR suelen venir sin la sección STEP reconstruida (los autores solo modelan geometría, no instrucciones).

10. **Reflejos son raros y similares en ambas cohortes**: solo 2/100 sets 80s/90s y 4/200 sets kids tienen matrices con determinante negativo. neg_det_ratio por parts es prácticamente idéntico (0.00268 vs 0.00249). La simetría se mantiene por convención, no por mirrored geometry, en ambos casos.

11. **kids tiene más "ruido OMR" embedded**: 519 custom parts embebidos vs 78 en 80s/90s. Esto sugiere que los OMR modernos aprovechan más subfiles para decoración (printed tiles, paneles, slopes 1×1) que los antiguos simplemente modelan con primitivas.

12. **Las dos cohortes comparten el "core de bricks"** (22 parts en común en top-30, ~38% del volumen total de cada una), pero divergen completamente en la **larga cola**: Technic embebido + slopes clásicos en 80s/90s; tiles modernas + decorativos + slopes 1×1 en kids.

---

## Síntesis

**El LEGO System cambió estructuralmente entre 1980-1999 y 2000-2020 en tres ejes medibles**:

1. **Vocabulario**: sustitución de slopes/bases clásicas + Technic embebido por tiles modernas (groove tiles, slopes 1×1, paneles curvos, printed).
2. **Cadencia**: manuales digitales modernos producen 50% más STEPs/set con 23% menos parts/step — instrucciones más detalladas.
3. **Técnica OMR**: niños se reconstruyen con 6.5× más embedded subparts y 3.65× más custom parts totales — los autores modernos explotan primitivas LDraw más profundamente.

**El Technic NO migró**: sigue presente en ambas cohortes pero su rol en System se **redujo proporcionalmente** (más parts absolutas en kids pero menor ratio per-piece). Los 80s/90s son los últimos models System donde Technic embebido era rutina.

**La simetría se mantuvo** (reflejos raros en ambos casos), pero la formalización del modelado BFC se duplicó (kids 36.5% vs 80s/90s 21%) — la cultura OMR se profesionalizó.
