# Cadencia de pasos de construcción (10252 VW Beetle · 10218 Pet Shop)

Análisis de `corpus/10252-1.mpd` (211 STEPs de master, 566 piezas en master) y `corpus/10218-1.mpd` (168 STEPs repartidos en 8 sub-builds de edificio, ~2 034 piezas en total), según `analysis/deep_stats.json` + `analysis/raw_stats.json` + parseo directo.

> Nota: el JSON agrupa `steps_size_distribution` **solo del master**. El parseo completo del archivo confirma que en 10252 hay 462 STEPs totales (master + sub-modelos) y en 10218 hay 188 STEPs totales (master + sub-builds + minifigs). La métrica principal que pide el usuario (211 / 168) coincide con el master de 10252 y con la suma de los 8 sub-builds de edificio de 10218.

---

## 1. Distribución del tamaño de paso (piezas por `0 STEP`)

### 10252 — master (`deep_stats.json` → `steps_size_distribution`)

```
size  count   visual
  0    64    ████████████████████████████ 30.3 %   ← STEPs vacíos
  1    25    ██████████▌                  11.8 %
  2    46    ████████████████████▏        21.8 %   ← MODA
  3    23    ██████████▌                  10.9 %
  4     8    ███▎                          3.8 %
  5     9    ███▉                          4.3 %
  6    13    █████▊                        6.2 %
  7     2    █                             0.9 %
  8     6    ██▎                           2.8 %
  9     6    ██▎                           2.8 %
 10     5    ██                            2.4 %
 12     1    ▌                             0.5 %
 13     1    ▌                             0.5 %
 16     1    ▌                             0.5 %
 18     1    ▌                             0.5 %
───
Σ   211 STEPS · media 2.68 · mediana 2 · mín 0 · máx 18
```

Sobre los **147 STEPs no vacíos**: media **3.85**, mediana **2**, P75 ≈ 6.
El 72 % de los STEPs no vacíos tienen 1–3 piezas; el 94 % tienen ≤ 6 piezas.
Solo **10 STEPs "grandes"** (≥ 10 piezas): tamaños `[16, 10, 10, 12, 18, 11, 10, 13, 10, 10]` y posiciones `[11, 31, 32, 73, 86, 114, 116, 181, 182, 183]` — corresponden al chasis, cabina e interior.

### 10218 — 8 sub-builds de edificio (168 STEPs)

Cada piso es un solo bloque continuo sin STEPs vacíos; los 168 STEPs suman **1 988 piezas** en `Brown/Blue House 1 Basement → 4 Roof`. Distribución por sub-build:

| Sub-build | STEPS | piezas | media | mediana | máx |
|---|---:|---:|---:|---:|---:|
| Brown House 1 Basement | 38 | 456 | 12.0 | 11 | **22** |
| Blue House 1 Basement | 35 | 442 | 12.6 | 13 | **26** |
| Blue House 2 Downstairs | 21 | 302 | 14.4 | 13 | **30** |
| Blue House 3 Upstairs | 21 | 265 | 12.6 | 14 | 21 |
| Brown House 2 Downstairs | 23 | 232 | 10.1 | 10 | 21 |
| Brown House 3 Upstairs | 19 | 203 | 10.7 | 11 | 20 |
| Blue House 4 Roof | 6 | 47 | 7.8 | 9 | 18 |
| Brown House 4 Roof | 5 | 25 | 5.0 | 5 | 9 |
| **Σ** | **168** | **1 972** | **11.7** | — | **30** |

STEP típico de Pet Shop: **10–14 piezas**. Casi nunca 1, casi nunca > 25. Moda ≈ 10–13.

### Comparación inmediata

| | 10252 master | 10218 edificio |
|---|---:|---:|
| Moda por STEP | **2** (22 %) | **10–13** |
| Mediana | **2** | **11** |
| Media (no vacío) | **3.85** | **11.7** |
| % de STEPs con 1 sola pieza | 17 % | < 2 % |
| STEPs ≥ 10 piezas | 4.7 % | **40 %** |
| STEPs vacíos | **30 %** (64/211) | **0 %** |
| STEPs de 30+ piezas | 0 | **varios** (pico 30) |

La diferencia es enorme: 10252 construye **pieza a pieza** (un ladrillo aquí, una placa allá); 10218 construye **lienzos enteros** (10–14 piezas por STEP, técnicas de "sembrado" típicas de los Modular Buildings).

---

## 2. Sub-modelos vs master — la diferencia arquitectónica

### `sub_model_count` en JSON: **81 (10252)** vs **17 (10218)**

Inspección directa del MPD (parseando bloques `0 FILE`) revela que:

**10252** (101 bloques totales, 462 STEPs totales)
- `main.ldr`: **211 STEPs · 566 piezas** (toda la construcción atómica: chasis, carrocería, interiores, ventanas, ruedas — paso a paso).
- 74 sub-modelos `subModel-*.ldr`: **1–9 STEPs cada uno, 2–18 piezas**. Media ≈ 3.4 STEPs / 5.7 piezas. Algunos son **ruedas, techos, tubos de escape, manijas, asientos** — pequeñas pre-construcciones que se insertan luego en el master.
- 6 mangueras/bandas elásticas (`pneumaticHoseLQ`, `technicflexSysHose`, `rubberBandRound`): STEPs vacíos usados como placeholders visuales.
- 17 partes embebidas (`.dat` decorativos): towel, wheel covers, hub caps — STEPs con 1 STEP de 22, 19, 40 piezas.

→ **Arquitectura "atómica"**: el master hace casi todo el modelo pieza a pieza, y los 74 sub-modelos son **piezas pre-ensambladas que se añaden como bloques compactos**.

**10218** (20 bloques totales, 188 STEPs totales)
- `main.ldr`: **1 STEP · 5 piezas** (solo referencias a sub-builds). Es esencialmente vacío.
- 8 sub-builds de edificio (4 pisos × 2 casas): Brown/Blue House 1 Basement → 4 Roof. **Toda la construcción está aquí**, organizada por piso arquitectónico.
- 4 minifigs: `MiniFig1.ldr`…`MiniFig4.ldr` — cada uno 1–3 STEPs, 8–12 piezas (cuerpo + accesorios).
- 1 escalera (`Corkskrew Stair`): 1 STEP, 4 piezas.
- 2 mangueras y 3 piezas decorativas embebidas.
- 2 archivos "assembler" (`Brown House.ldr`, `Blue House.ldr`): cada uno 4 STEPs, 4 piezas — son referencias finales a las casas completas.

→ **Arquitectura "por pisos"**: master es solo índice, y la **construcción real vive en los sub-builds**, cada uno = un piso. Refleja el manual real del Modular Building, donde cada piso es una "fase" de la construcción.

**Conclusión arquitectónica**:
- **10252 hace el coche entero en el master**, y los sub-modelos son "trozos pequeños ya cocinados" que se añaden al master como puntos discretos. La atomización es fina (mediana 2 piezas/STEP).
- **10218 descompone por pisos físicos** (sótano, planta baja, primer piso, tejado × 2 casas) porque el manual real se lee así. La atomización es gruesa (mediana 11 piezas/STEP), más cercana a colocar un rectángulo de fachada que a colocar un brick suelto.

---

## 3. STEPs con 0 piezas

### 10252 master — **64 STEPs vacíos** (30.3 %)

Distribución de las posiciones revela **5 racimos densos** (≥ 3 STEPs vacíos consecutivos), no están dispersos al azar:

| Rango de posiciones | # vacíos seguidos | Interpretación probable |
|---|---:|---|
| 42–51 | **10 seguidos** | cambio de subsección grande (transición a techo/cabina) |
| 70–72 | 3 | rotación 180° / punto de inflexión |
| 76–79 | 4 | cierre de sección |
| 186–191 | **6 seguidos** | tramo final antes de remates |
| 205, 207, 208 | sueltos | cierre del modelo |

Los otros ~38 vacíos están intercalados cada 9–15 STEPs. **Doble función inferida**:
1. **Marcador de rotación** ("gira 180° el modelo") — muy común en manuales LEGO, equivale a "step de solo-rotación".
2. **Cierre de inserción de sub-modelo**: cada vez que el master referencia un `subModel-N.ldr` (hay 108 referencias a sub-modelos en master), el editor suele poner un STEP vacío justo después para que el LPub/editor separe visualmente "lo construido en línea" de "lo añadido como bloque".

### 10218 sub-builds — **0 STEPs vacíos** en los 168 STEPs de edificio

Los 8 sub-builds están **completamente densos**. No hay STEPs de rotación ni marcadores intermedios. Esto se explica porque cada sub-build es una "vista continua" sin rotaciones forzadas — la rotación se hace entre archivos (al cambiar de sub-build).

### STEPs vacíos totales

| | 10252 | 10218 |
|---|---:|---:|
| STEPs vacíos en master/sub-builds principales | **64** (30 %) | **0** (0 %) |
| STEPs vacíos en sub-modelos auxiliares (mangueras, bandas) | 8 | 5 |
| **STEPs vacíos totales en el MPD** | **~72** | **~7** |

→ El **30 % de vacíos en 10252 master** es coherente con un modelo de "transiciones frecuentes entre sub-piezas atómicas + rotaciones". El **0 % en 10218** es coherente con "vista continua por piso, sin rotaciones intermedias".

---

## 4. Patrones de agrupación reconocidos

### a) Piezas consecutivas sin STEP antes del primer STEP

- **10252 master**: STEP 0 ya tiene 5 piezas (no hay "preludio" sin STEP). El primer STEP agrupa las 5 piezas iniciales directamente. → **0 piezas huérfanas antes del primer STEP**.
- **10218 master**: STEP 0 tiene 5 piezas (las 4 referencias a Brown/Blue House + escaleras).
- **10218 Brown House 1 Basement**: STEP 0 ya tiene 4 piezas.
- **10252 sub-models**: STEP 0 suele tener 1–3 piezas (no hay preludios largos).

→ **Convención detectada**: ningún sub-build arranca con "muchas piezas sueltas antes del primer STEP". El primer STEP **siempre** lleva piezas — el STEP vacío nunca abre un bloque.

### b) Ración de un sub-modelo completo

| Métrica | 10252 (74 sub-models) | 10218 (8 edificios) |
|---|---:|---:|
| STEPs/sub-build (media) | 3.4 | 21.0 |
| piezas/sub-build (media) | **5.7** | **246.5** |
| piezas/STEP (media dentro del sub-build) | **2.0** | **11.7** |

→ En 10252 un sub-modelo es **un mini-ensamble de ~6 piezas en 3–4 pasos**. En 10218 un sub-build de piso es **~250 piezas en 21 pasos** — 40× más grande.

### c) STEPs que cierran secciones lógicas

- **10252**: STEPs vacíos en posiciones `[42–51, 76–79, 186–191]` (los racimos) **cierran secciones del master** (chasis → cabina, cabina → techo, techo → remates).
- **10218**: cada sub-build de piso **se cierra solo** (el último STEP del sub-build = última pieza, no un STEP vacío). El "cierre de piso" es la frontera del archivo, no un STEP dentro del archivo.
- **STEP final del modelo**:
  - 10252 master: STEPS 209 y 210 son piezas (2 y 4), no vacíos. El último STEP NO es vacío.
  - 10218: igual — los archivos terminan con piezas, no con un STEP ceremonial.

→ **No hay "STEP ceremonial de fin"** en estos sets: el último STEP siempre lleva la última pieza, no es un marcador.

### d) STEPs "ancla" (de 1 sola pieza)

- 10252 master tiene **25 STEPs de 1 pieza** (12 %): típicamente colocar 1 plate estratégico antes de añadir un racimo encima.
- 10218 edificios tienen **0 STEPs de 1 pieza** y muy pocos de 2. Esto encaja con la técnica "construyo todo el rectángulo de fachada de una vez".

### e) Concentración de piezas pesadas (≥ 10)

- 10252 master: 10 STEPs ≥ 10 piezas, **distribuidos a lo largo** (posiciones `[11, 31, 32, 73, 86, 114, 116, 181, 182, 183]`) — repartidos por todo el master, no concentrados.
- 10218 Blue House 2 Downstairs: tiene los 3 STEPs más grandes del set (`[30, 22, 28]` justo al final) — corresponde probablemente al ático/tejado de un piso completo en pocos pasos.

---

## 5. Reglas inferidas sobre cadencia (con números del JSON)

1. **"STEP vacío = cierre de sección o marcador de rotación, no marcador de inicio"**. El primer STEP de cada sub-build nunca es vacío (5/4/2 piezas en los masters de ambos sets). En 10252, los 64 STEPs vacíos se concentran en 5 racimos (≥ 3 seguidos), sugiriendo transiciones de fase, no dispersión aleatoria.

2. **"STEPS típicos según granularidad del set"**:
   - Set de vehículo atomizado (10252): **1–3 piezas** por STEP (72 % de los no-vacíos), media 3.85, mediana 2.
   - Set arquitectónico (10218): **8–14 piezas** por STEP, media 11.7, mediana 11.
   - Regla práctica: un STEP "normal" tiene entre **media × 0.5** y **media × 2** piezas.

3. **"STEPs grandes (≥ 10 piezas) son momentos críticos del manual"**: 10252 master tiene solo 10 de 211 (4.7 %), pero marcan hitos constructivos (chasis en pos 11, cabina en pos 31–32, interior en pos 73, 86, 114, 116, techos en pos 181–183). 10218 Blue House 2 Downstairs tiene los STEPs más grandes del corpus (`[30, 22, 28]`) justo al final del sub-build — **construir el ático de una sola vez**.

4. **"Sub-modelos reflejan la modularidad del set"**:
   - **10252**: 74 sub-modelos pequeños (media 5.7 piezas, 3.4 STEPs cada uno) = atomización fina; cada sub-modelo es 1 wheel arch / 1 handle / 1 wheel.
   - **10218**: 8 sub-builds grandes (media 246 piezas, 21 STEPs) = modularidad gruesa por pisos arquitectónicos.

5. **"El último STEP no es ceremonial, lleva piezas"**: ambos masters terminan con STEPs no-vacíos (10252 master termina con tamaños `[2, 4]` en sus últimos 2 STEPs; 10218 sub-builds terminan con piezas). Esto rompe la convención típica de algunos editores que ponen un STEP vacío al final.

6. **"Media de piezas/STEP correlaciona inversamente con el número de sub-modelos"**:
   - 10252: 2.68 piezas/STEP × 81 sub-modelos = atomización.
   - 10218: 11.7 piezas/STEP × 17 sub-modelos = pocos pero grandes.
   - Ratio: ≈ 1 STEP de 10218 equivale a ≈ 4.4 STEPs de 10252.

7. **"Una sección lógica del master 10252 se cierra con 1 STEP vacío"** (no más, no menos): los racimos de 4–10 STEPs vacíos consecutivos son infrecuentes (5 ocurrencias en 211 = 2.4 %); predominan vacíos aislados (38/64 = 59 %), separados por 9–15 STEPs útiles. Esto encaja con la práctica editorial de marcar una rotación o un punto de pivote **a la mitad** de la sesión constructiva.

### Conclusión sintética

Los dos sets representan **dos filosofías de manual LEGO**:

| | 10252 VW Beetle | 10218 Pet Shop |
|---|---|---|
| Manual = | "una pieza, otra pieza, conecto" | "una pared, luego la otra, luego el techo" |
| STEPs no-vacíos/STEPs totales | 147/211 = 70 % | 168/168 = **100 %** |
| STEPs vacíos | 30 % (transiciones/rotaciones) | 0 % (todo se hace dentro del sub-build) |
| Ratio sub-modelos/master | 81/1 = **muchos auxiliares** | 17/1 = pocos pero **completos por piso** |
| Piezas/STEP media | 3.85 | 11.7 |
| "Cierre" de sección | STEP vacío | Frontera del archivo |

El **10252 master está estructurado como una secuencia larga con hitos**, mientras que el **10218 está estructurado como una constelación de módulos grandes e independientes**.