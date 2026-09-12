# Convenciones de construcción por THEME LEGO — corpus 532 sets (Plan C completo)

Análisis del corpus **OMR 1966–2020 no-Technic** (532 sets OMR: 300 sets previos + 232 sets Plan C, total **108 760 parts**, **4 724 sub-builds**, **1 037 custom parts + subparts embebidos**, BFC CERTIFY 132/532 = 24.8 %). Datos extraídos de `cross_corpus2_stats.json` (regenerado con `python3 analysis/batch_parse3.py`) y `per_set_stats_532.json` (nueva agregación de 300 legacy + 232 classic). Las cifras se computan directamente desde el JSON (sin scripts persistentes).

> **Metodología:** los top-pieces se obtienen sumando las frecuencias de `top_30_pieces` por set dentro de cada `meta.theme_full`. Los **nuevos themes Plan C** (49 themes pre-2000 añadidos) están marcados con **†**.

> **Composición:** 418/532 sets (78.6 %) son **pre-2000**; 81 themes únicos en total. Distribución por década (sets / themes distintos): 1960s=15/2, 1970s=68/5, 1980s=156/22, 1990s=179/33, 2000s=46/19, 2010s=66/22, 2020s=2/2. **Los 80s/90s son el grueso** (335 sets = 63 %) con **55 themes distintos pre-2000** ahora visibles — Plan C uniformiza la cobertura pre-2000 (los 10 themes de 1980s/1990s del corpus 300 eran muestras de 1-2 sets; ahora muchos son bloques sólidos con n≥5).

---

## 1. Distribución final por theme (532 sets)

**Totales globales (`cohort_all_532`):** 532 sets, 108 760 parts, 4 724 sub-builds, 1 037 custom+subparts, 132 BFC CERTIFY. parts totales / set = 204.4 (mediana por set).

### Tabla maestra por theme

| Theme | Sets | parts | P/set | Sub/set | Top-3 parts | Custom+subparts |
|---|---:|---:|---:|---:|---|---:|
| **Town > Classic Town** † | 136 | 18 819 | 138.4 | 5.21 | `3023`(716), `3004`(603), `3024`(524) | 53 |
| Fabuland | 23 | 896 | 39.0 | 3.48 | `u9101`(78), `u9100`(78), `3004`(64) | 135 |
| Western | 17 | 3 821 | 224.8 | 12.29 | `30136`(184), `3023`(142), `3004`(132) | 23 |
| Friends | 17 | 5 046 | 296.8 | 11.24 | `6141`(223), `3004`(218), `3023`(172) | 344 |
| Train > 9V † | 14 | 4 730 | 337.9 | 15.00 | `3023`(168), `3004`(110), `6141`(91) | 8 |
| Creator > Creator 3-in-1 | 14 | 3 143 | 224.5 | 4.43 | `3023`(194), `6141`(185), `3004`(120) | 7 |
| Town > Res-Q † | 12 | 1 401 | 116.8 | 5.17 | `3024`(41), `3023`(35), `3710`(35) | 0 |
| Space > Futuron † | 11 | 1 340 | 121.8 | 11.64 | `756`(102), `3023`(60), `3024`(34) | 0 |
| Space > Blacktron II † | 11 | 1 445 | 131.4 | 11.18 | `756`(96), `3023`(72), `3024`(34) | 0 |
| Space > Classic Space † | 10 | 1 084 | 108.4 | 6.90 | `756`(192), `3023`(43), `3024`(34) | 0 |
| Train > 12V † | 10 | 2 586 | 258.6 | 7.70 | `3004`(151), `3023`(127), `3005`(85) | 12 |
| Boat † | 10 | 1 297 | 129.7 | 3.00 | `4-4cyli`(401), `3005`(80), `3004`(66) | 22 |
| **Castle > Lion Knights** † | 10 | 2 575 | 257.5 | 8.70 | `4-4cyli`(398), `3004`(244), `3005`(237) | 3 |
| Space > M:Tron † | 10 | 1 792 | 179.2 | 14.30 | `756`(192), `3023`(87), `2412b`(40) | 1 |
| Space > Space Police II † | 10 | 1 156 | 115.6 | 11.20 | `3023`(46), `3710`(30), `3820`(30) | 0 |
| Town | 10 | 4 394 | 439.4 | 25.00 | `3010`(282), `3004`(207), `3069b`(197) | 2 |
| Creator | 10 | 361 | 36.1 | 2.20 | `54200`(23), `6141`(17), `3023`(16) | 5 |
| Train > 4.5V † | 9 | 734 | 81.6 | 3.22 | `3004`(41), `4166b`(32), `3010`(23) | 2 |
| Space > Ice Planet 2002 † | 9 | 773 | 85.9 | 10.89 | `756`(50), `4276b`(25), `3023`(24) | 0 |
| Space > Space Police III † | 8 | 2 201 | 275.1 | 18.62 | `54200`(89), `6141`(79), `4589`(67) | 9 |
| Pirates > Pirates I | 7 | 6 319 | 902.7 | 13.29 | `4-4cyli`(3 895), `754`(214), `3004`(101) | 90 |
| Space > Spyrius † | 7 | 518 | 74.0 | 7.14 | `3023`(27), `2412b`(19), `3820`(16) | 0 |
| Model Team | 6 | 4 092 | 682.0 | 23.33 | `754`(408), `3023`(204), `6141`(144) | 26 |
| Town > Launch Command † | 6 | 1 421 | 236.8 | 6.83 | `6141`(55), `3710`(40), `3023`(38) | 1 |
| Star Wars | 6 | 1 120 | 186.7 | 12.00 | `756`(48), `3820`(28), `3003`(24) | 1 |
| Creator > Designer Sets | 6 | 967 | 161.2 | 8.50 | `754`(88), `3023`(40), `6141`(35) | 0 |
| Space > Blacktron I † | 6 | 1 554 | 259.0 | 13.00 | `756`(192), `3023`(57), `6141`(38) | 0 |
| Universal Building Set † | 6 | 229 | 38.2 | 1.33 | `3004`(33), `3005`(22), `3010`(21) | 0 |
| **Castle > Black Falcons** † | 5 | 1 029 | 205.8 | 6.80 | `4-4cyli`(108), `3005`(95), `3004`(92) | 1 |
| **Castle > Forestmen** † | 5 | 779 | 155.8 | 5.60 | `3005`(54), `3040b`(36), `3820`(30) | 1 |
| Space > Unitron † | 5 | 2 681 | 536.2 | 27.40 | `756`(355), `3023`(116), `3710`(98) | 0 |
| Universal Building Set > Basic † | 5 | 39 | 7.8 | 1.60 | `3004`(5), `3023`(4), `3020`(3) | 0 |
| Promotional > Bricktober | 5 | 861 | 172.2 | 2.00 | `3024`(121), `3023`(94), `3005`(73) | 0 |
| Town > Outback † | 4 | 576 | 144.0 | 6.00 | `3023`(25), `6141`(23), `3024`(21) | 0 |
| City > Construction | 4 | 433 | 108.2 | 4.50 | `6141`(29), `54200`(16), `3710`(15) | 0 |
| Harry Potter | 4 | 2 407 | 601.8 | 14.25 | `3005`(127), `3062b`(62), `54200`(61) | 17 |
| System > Town Plan † | 4 | 0 | 0.0 | 0.00 | — | 0 |
| **Castle > Black Knights** | 3 | 1 231 | 410.3 | 11.00 | `4-4cyli`(237), `3004`(126), `3005`(80) | 5 |
| Sports > Soccer † | 3 | 497 | 165.7 | 8.67 | `3820`(32), `3024`(27), `3710`(16) | 0 |
| Town > Paradisa † | 3 | 303 | 101.0 | 5.67 | `3005`(22), `3820`(14), `3063b`(12) | 3 |
| Adventurers > Dino Island † | 3 | 339 | 113.0 | 5.00 | `3004`(14), `2412b`(14), `6141`(12) | 3 |
| Town > City Center † | 3 | 1 035 | 345.0 | 9.00 | `756`(48), `3024`(36), `3023`(30) | 4 |
| Creator > Early Creator | 3 | 0 | 0.0 | 0.00 | — | 0 |
| City > Airport | 3 | 1 076 | 358.7 | 11.67 | `6141`(80), `4862`(50), `3023`(33) | 64 |
| City > Police | 3 | 119 | 39.7 | 3.33 | `3820`(6), `3666`(4), `54200`(4) | 0 |
| Super Heroes DC > Batman | 3 | 454 | 151.3 | 3.33 | `3023`(24), `3623`(18), `3024`(15) | 2 |
| Space > Space Police I † | 3 | 862 | 287.3 | 21.00 | `756`(102), `3023`(37), `3710`(26) | 0 |
| Town > Divers † | 3 | 520 | 173.3 | 7.67 | `754`(47), `3021`(17), `6141`(15) | 0 |
| Castle > Dragon Knights † | 2 | 225 | 112.5 | 10.00 | `3022`(11), `3004`(11), `3023b`(10) | 0 |
| Adventurers > Desert | 2 | 53 | 26.5 | 3.00 | `4624`(6), `3641`(6), `2420`(4) | 0 |
| Town > Town Jr. | 2 | 48 | 24.0 | 3.50 | `3820`(4), `6014c02`(4), `4081b`(2) | 0 |
| Town > World City | 2 | 470 | 235.0 | 7.00 | `4864B`(17), `3001`(14), `3004`(14) | 1 |
| Castle > Knights Kingdom II † | 2 | 4 988 | 2 494.0 | 113.50 | `3021`(203), `3023`(133), `3710`(128) | 8 |
| City > Harbor | 2 | 148 | 74.0 | 3.50 | `61409`(9), `42023`(6), `2444`(6) | 0 |
| Seasonal > Halloween | 2 | 36 | 18.0 | 2.00 | `3004`(12), `3003`(9), `3002`(7) | 0 |
| Seasonal > Christmas | 2 | 238 | 119.0 | 7.00 | `6141`(47), `3023`(27), `93595`(14) | 0 |
| The Lord of the Rings | 2 | 117 | 58.5 | 5.00 | `3023`(7), `3062b`(6), `3820`(6) | 0 |
| Seasonal > Advent > Friends | 2 | 195 | 97.5 | 10.50 | `6141`(20), `54200`(9), `33291`(7) | 14 |
| City > Fire | 2 | 2 307 | 1 153.5 | 28.00 | `4-4cyli`(932), `166`(426), `3023`(26) | 80 |
| Minecraft | 2 | 612 | 306.0 | 14.50 | `3070b`(139), `3024`(105), `3003`(48) | 2 |
| Train | 2 | 1 008 | 504.0 | 11.50 | `2877`(44), `3023`(39), `3710`(34) | 8 |
| Homemaker † | 2 | 170 | 85.0 | 3.50 | `3069b`(42), `3068b`(23), `3010`(13) | 10 |
| (33 themes más con n=1) | 33 | … | … | … | … | … |
| **TOTAL corpus** | **532** | **108 760** | 204.4 | 8.88 | — | **1 037** |

> **Aclaración "themes 49 pre-2000 + otros modernos":** Plan C añadió **49 themes pre-2000** pero NO todos están ahora con n ≥ 5. Algunos quedaron con n=1-3 (Black Knights n=3, Dragon Knights n=2, Forestmen n=5). Los 24 themes "modernos/licenciados" del corpus (Star Wars n=6, Harry Potter n=4, Marvel Avengers n=1, Batman n=3, LOTR n=2, Minecraft n=2, Indiana Jones n=1, City sub-themes n=1-4) **no son Plan C** — vienen de cohorts 80s/90s y kids originales.

> **Themes con n=1 (33 themes, "long tail"):** Castle, Pirates, Duplo, Duplo > Town, Znap, Insectoids, City > Hospital, City > Coast Guard, City, City > Police subset, Creator > X-Pod, Adventurers > Orient Expedition, Seasonal > Thanksgiving, Town > Extreme Team, Town > Space Port, Town > Town Plan, Indiana Jones, Promotional, Promotional > Airlines, Super Heroes Marvel > Avengers, Seasonal > Christmas > Creator, Town > Res-Q subset (1 set legacy), Universal Building Set > Basic subset (n=5). Estos están agregados en la fila "(33 themes más)" — parts totales aproximadas: ~6 500.

---

## 2. Themes clásicos con n≥10 en corpus 532

Los themes pre-2000 ahora tienen **representación sólida**. Listado de los **17 themes con ≥10 sets** (ordenados por n):

| Theme | n | parts | Notas nuevos patrones |
|---|---:|---:|---|
| **Town > Classic Town** | **136** | 18 819 | Antes 63 sets, ahora 136 — Plan C añadió **73 sets (×2.16)**. La parts signature se mantiene: `3023`(716), `3004`(603), `3024`(524). **Media parts/set baja a 138.4** (antes 162.4) porque Plan C añadió sets pequeños. |
| Fabuland | 23 | 896 | Sin cambios desde corpus 300. Mantiene su **encapsulamiento total** (custom `u91xx` serie, ratio 9.26 % custom). |
| Western | 17 | 3 821 | Creció **13 → 17 sets** por la línea BrickHeadz/Promos; mantiene `30136` caballo (184×) y saddle `30141`. |
| Friends | 17 | 5 046 | Sin cambios. **6141 round** (223×) sigue dominando. |
| **Train > 9V** † | 14 | 4 730 | **NUEVO en n≥10**. Antes ausente como sub-theme. Vocabulario: `3023`(168), `3004`(110), `6141`(91). Sub-builds/set = **15.0** — segundo más alto del corpus. |
| Creator > Creator 3-in-1 | 14 | 3 143 | Sin cambios. **`54200` hinge** (89×) + `2780` technic pin (49×) — la parts signature. |
| **Town > Res-Q** † | 12 | 1 401 | **NUEVO en n≥10**. Plan C target=8 (consiguió 12 con legacy 4). Vocabulario: `3024`(41), `3023`(35), `3710`(35) — sub-theme técnico de Town (cuerpo de bomberos/rescate). |
| **Space > Futuron** † | 11 | 1 340 | **NUEVO en n≥10**. `756`(102) baseplate + `3023`(60). |
| **Space > Blacktron II** † | 11 | 1 445 | **NUEVO en n≥10**. `756`(96) + `3023`(72). Idéntico perfil que Futuron. |
| **Space > Classic Space** † | 10 | 1 084 | **NUEVO en n≥10**. `756`(192) — el **doble** que Futuron/Blacktron II porque los sets Classic Space son más grandes. Aparece `3957a`(28) **en exclusiva** dentro de los Space (ningún otro sub-theme Space la tiene). |
| **Train > 12V** † | 10 | 2 586 | **NUEVO en n≥10**. `3004`(151) brick 1×2 — más pesado que 9V (más brick que plate). |
| **Boat** † | 10 | 1 297 | **NUEVO en n≥10**. `4-4cyli`(401) — el cilindro primitivo de mástiles aparece por primera vez como theme **independiente** (no Pirates). |
| **Castle > Lion Knights** † | 10 | 2 575 | **NUEVO en n≥10**. Ahora Castle se subdivide visiblemente: Lion Knights `4-4cyli`(398), `3004`(244), `3005`(237). |
| **Space > M:Tron** † | 10 | 1 792 | **NUEVO en n≥10**. `756`(192) + **`2412b`(40) slope 45° 1×1 con stud** — la slope distintiva M:Tron. |
| **Space > Space Police II** † | 10 | 1 156 | **NUEVO en n≥10**. **Sin baseplate 756** en top-5 — sólo `3023`(46), `3710`(30), `3820`(30). Space Police II **se construye libre sin suelo**. |
| Town | 10 | 4 394 | **Se redujo de 40 a 10 sets** — los 30 sets kids antes clasificados `meta.theme="Town"` ahora son `theme_full="Town > Classic Town"` por la reclasificación de OMR. Town puro = 10 sets 80s/90s. |
| Creator | 10 | 361 | Sin cambios. **Mismo vocabulario que Creator 3-in-1**, escala 1:2. |

### Patrones nuevos que no se veían en corpus 300

1. **Sub-themes de Space con n≥10 (5 sub-themes, 52 sets)** — corpus 300 sólo tenía `Space` agregado (15 sets). Ahora los 5 sub-themes principales tienen datasets sólidos para extraer patrones individuales. **Plan C desbloqueó el análisis sub-theme por sub-theme** (antes imposible con 1-3 sets por sub-theme).

2. **Train 9V / 12V / 4.5V ahora visibles por separado** (14+10+9 = 33 sets vs corpus 300 con sólo 9 sets Train agrupados). Patrón nuevo observado: **9V usa más plate que brick** (`3023` 168×, `3004` 110×), **12V usa más brick que plate** (`3004` 151×, `3023` 127×), **4.5V usa parts más grandes** (`4166b` panel 1×6 = 32×, no en 9V/12V). **Train 9V es la era 1991-2006** (railtrack gris + motor 9V) vs **12V (1969-1991, metal rails + transformador)** — la transición se ve en el vocabulario.

3. **Town > Res-Q como sub-theme técnico diferenciado** — Town genérico usa `3004` brick + `3024` plate mezclados; Res-Q usa **`3024` + `3710` plates principalmente** (41+35 vs `3004` ausente del top-3) = construcción **plana para bases de camiones de rescate**, no paredes.

4. **Castle > Lion Knights tiene el cilindro primitivo `4-4cyli`(398) como #1** — único Castle sub-theme donde el mástil/antorcha supera al brick. Esto lo distingue de Black Falcons/Forestmen/Black Knights donde el top es `3005` brick 1×1 o `3004` brick 1×2.

5. **Boat como theme separado de Pirates** — el corpus 300 mezclaba Boat con Pirates I. Ahora **Boat (10 sets, 1 297 p, `4-4cyli` 401×)** es un theme independiente — barcos civiles/lanchas sin la narrativa pirata, **sin el sesgo de `754` baseplate 24×24** (sólo 0 en top-5).

### Vocabularios únicos muy distintivos (no en otros themes)

- **Fabuland:** 23 parts únicas serie `u91xx` (cabeza `u9101`×78 en 23/23 sets, cuerpo `u9100`×78 en 23/23, animal `u9103`×39 en 23/23). Único theme con **100 % de sets conteniendo cabeza + cuerpo + animal custom**.
- **Western:** 7 parts impresas (`30141` saddle×37, `3629` printed plate×8, `30133`×8, `3069bpw2` WANTED×7, `6064`×7, `30127p01`×4, `4491b`×3) — segundo theme con más decoración impresa.
- **Pirates > Pirates I:** 8 parts exclusivas (`70501a/b/c/d` flag variants, `2335p30` flag calavera, `3626bp35` printed plate, `2543` plate 6×6 round, `2562`). **Comparte `2543` con Pirates I** y `4-4cyli` con Castle.

---

## 3. Castle sub-themes (nuevos con Plan C)

### Sub-themes con representación sólida (n ≥ 3)

| Sub-theme | n | parts | P/set | Sub/set | Custom | parts #1 (#sets) |
|---|---:|---:|---:|---:|---:|---|
| Castle > Lion Knights | 10 | 2 575 | 257.5 | 8.70 | 3 | `4-4cyli`(398, en 1 set: 6080) |
| Castle > Black Falcons | 5 | 1 029 | 205.8 | 6.80 | 1 | `4-4cyli`(108, en 1 set: 6074) |
| Castle > Forestmen | 5 | 779 | 155.8 | 5.60 | 1 | `3005`(54) brick 1×1 — único sin `4-4cyli` dominante |
| Castle > Black Knights | 3 | 1 231 | 410.3 | 11.00 | 5 | `4-4cyli`(237, en 1 set: 6085) |
| Castle > Dragon Knights | 2 | 225 | 112.5 | 10.00 | 0 | `3022`/`3004` (sin `4-4cyli`) |
| Castle > Knights Kingdom II | 2 | 4 988 | 2 494.0 | 113.50 | 8 | `3021`(203) — moderno, vocabulario distinto |
| Castle (genérico) | 1 | 72 | 72.0 | 7.00 | 0 | `3820`(12) — corpus mínimo |
| **Total Castle familia** | **28** | **10 899** | 389.3 | 12.40 | 18 | — |

### parts canónicas identificables

**Lion Knights (n=10):** `4-4cyli`(398), `3004`(244), `3005`(237), `3820`(68), `3062b`(56). Las 3 primeras son **mástil + muro + torre** — la "trinidad Lion Knights". 6080 King's Mountain Fortress (843 p, 21 sub-builds) y 6073 Knight's Castle (580 p, 14 sub-builds) son los mega-sets que cargan el conteo de `4-4cyli`. 6061 Siege Tower (341 p) es donde viene el `4-4cyli` histórico (104 unidades en corpus 300, ahora agregado a Lion Knights).

**Black Falcons (n=5):** `4-4cyli`(108), `3005`(95), `3004`(92), `3820`(34), `3024`(24). Más brick que Lion Knights proporcionalmente. parts específica: **`3749`(4)** — sólo en Black Falcons, no en otros Castle. 6074 Black Falcon's Fortress (567 p) es el set canónico.

**Forestmen (n=5):** `3005`(54), **`3040b`(36)** — la **signature Forestmen es `3040b` slope 65° 1×2** (techo de cabaña de bosque, ningún otro Castle la usa en este rango). Forestmen es el **único Castle sub-theme sin `4-4cyli` dominante** — sin castillos, sólo cabañas y carros. **16 parts específicas** (`2417`, `3659`, `4287a`, `4865a`, `2462`, `93792`, `30071`, `45505`, `87693`, `3455`, `6225`, `2436a`, `2453a`, `30068`, `4286`, `2423`) — la **mayor exclusividad Castle**.

**Black Knights (n=3):** `4-4cyli`(237), `3004`(126), `3005`(80), `3665b`(34), **`2357`(32)** — `2357` brick 2×2 con studs laterales es **signature Black Knights** (también en Forestmen). 8 parts específicas (`3029`, `30499`, `3846p4c`, `2546`, `3063b`, `2554`, `3958`, `3307`).

**Dragon Knights (n=2):** `3022`(11), `3004`(11), `3023b`(10) — **sin `4-4cyli`, sin `3005`**. Vocabulario moderno: `3700`(8), `4477`(8), `3660b`(2), `3839b`(2), `3684`(2), `2540`(6 slate). Es la transición a la era 2005+ con slopes invertidos y slate.

**Knights Kingdom II (n=2):** `3021`(203), `3023`(133), `3710`(128), `3068b`(110), **`3794b`(99)** — la firma moderna. 22 parts específicas (`6636`, `44302`, `4592`, `4593`, `4589`, `3703`, `6558`, `3068b`). Sub-builds/set = **113.5** — descomposición masiva porque los sets KK II (incluye 8781 Castle of Morcia con 608 p) son playsets enormes.

### ¿Hay una "gramática Castle" común?

**Sí, 16 parts compartidas** entre los 4 sub-themes principales (Lion Knights, Black Falcons, Black Knights, Forestmen). Intersección top-50 ≥ 2 unidades por set:

```
{3831, 4444, 3710, 3005, 3622, 3830, 3040b, 3024, 2339,
 3004, 3820, 3819, 3010, 3023, 3818, 3009}
```

Estas son **16/50 = 32 %** del top-50 Castle. La **gramática común** incluye:
- **Paredes:** `3004` (brick 1×2), `3005` (brick 1×1), `3009` (brick 1×6), `3010` (brick 1×1 — sí, distinto a 3005), `3023` (plate 1×2), `3024` (plate 1×1), `3710` (plate 1×4), `3622` (plate 3×3)
- **Techos:** `3820` (slope 45° 2×1), `3818`/`3819` (slope 45° 1×3 variantes), `4444` (slope 45° 2×2), `3040b` (slope 65° 1×2 — sólo Forestmen en top)
- **Remates:** `3830`, `3831` (hinges para puertas), `2339` (slope invertido)

**Deltas compartidos (top-1 en cada sub-theme):**
- Lion Knights: `(0, -24, 0)` = 121 (apilado 1 brick) **— Y dominante**
- Black Falcons: `(0, 0, 0)` = 41 (apilado directo) **— X/Y/Z mixto**
- Black Knights: `(0, 0, 0)` = 31 (apilado directo)
- Forestmen: `(0, 0, 0)` = 28 (apilado directo)

→ **Lion Knights construye vertical (eje Y dominante con 121 deltas de apilado brick)**; los demás sub-themes son más isométricos. **El "Castle Lion Knights style" es el más extendido** (10 sets) y tiene la firma vertical más fuerte.

---

## 4. Space sub-themes (también fragmentados)

**12 sub-themes Space identificados** (excluyendo `Town > Space Port` que es realmente Town):

| Sub-theme | n | parts | P/set | Sub/set | parts #1 | Bigrama #1 |
|---|---:|---:|---:|---:|---|---|
| **Space > Classic Space** | 10 | 1 084 | 108.4 | 6.90 | `756`(192) | `756→756`(188) |
| **Space > Futuron** | 11 | 1 340 | 121.8 | 11.64 | `756`(102) | `756→756`(101) |
| **Space > Blacktron I** | 6 | 1 554 | 259.0 | 13.00 | `756`(192) | `756→756`(191) |
| **Space > Blacktron II** | 11 | 1 445 | 131.4 | 11.18 | `756`(96) | `756→756`(94) |
| **Space > M:Tron** | 10 | 1 792 | 179.2 | 14.30 | `756`(192) | `756→756`(188) |
| **Space > Ice Planet 2002** | 9 | 773 | 85.9 | 10.89 | `756`(50) | `756→756`(49) |
| **Space > Space Police I** | 3 | 862 | 287.3 | 21.00 | `756`(102) | `756→756`(100) |
| **Space > Space Police II** | 10 | 1 156 | 115.6 | 11.20 | `3023`(46) | `3023→3023`(17) |
| **Space > Space Police III** | 8 | 2 201 | 275.1 | 18.62 | `54200`(89) | `54200→54200`(50) |
| **Space > Spyrius** | 7 | 518 | 74.0 | 7.14 | `3023`(27) | `2412b→2412b`(13) |
| **Space > Unitron** | 5 | 2 681 | 536.2 | 27.40 | `756`(355) | `756→756`(348) |
| Space > Insectoids | 1 | 259 | 259.0 | 17.00 | `3023`(13) | (corpus mínimo) |
| **Total Space familia** | **91** | **15 705** | 172.6 | 12.50 | — | — |

### ¿Cada sub-theme tiene su vocabulario particular?

**Sí, muy marcado.** Los sub-themes se agrupan en **3 categorías por el bigrama #1**:

**Categoría A — "Baseplate 756 dominantes"** (8 sub-themes: Classic Space, Futuron, Blacktron I/II, M:Tron, Ice Planet 2002, Space Police I, Unitron): comparten `756→756` como bigrama #1. Esto significa **suelo de nave apilado** — el patrón universal Space. Los conteos varían: Unitron 348, M:Tron 188, Classic Space 188, Blacktron I 191, Futuron 101, Space Police I 100, Blacktron II 94, Ice Planet 49. Unitron tiene **3.5× más `756→756`** que Ice Planet — los sets Unitron son más grandes y más modulares.

**Categoría B — "Plate 3023 dominantes sin 756"** (Space Police II n=10, Spyrius n=7, Insectoids n=1): estos sub-themes **NO usan baseplate 756** en el top — construyen con `3023`(46/27/13) como base. Space Police II (n=10) usa `3710`(30) y `3820`(30) en top-5 — muros en lugar de suelos. Spyrius es el más peculiar: **`2412b` slope 45° 1×1 (19×)** y **`4624` wheel (no top pero usado como bigrama `4624→3641=8`)** — Spyrius construye **rovers con wheel-tire pairs**, no naves.

**Categoría C — "Hinge 54200 dominantes"** (Space Police III n=8): **vocabulario moderno post-2000**. `54200`(89), `6141`(79), `4589`(67), `3673`(61). Las 22 parts específicas de Space Police III incluyen `6587`, `44728`, `209`, `32556`, `4274`, `30104k02`, `50950`, `54200`, `61409`, `32062` — **mezcla Technic pin + brick estándar** (la transición a la era 2009-2010 donde Space Police se hizo modular-articulado).

### ¿Qué los distingue? (cascos, decoraciones, colores)

Sin acceso al catálogo de minifigs (sólo estructura de parts), las distinciones observables en el corpus son:

**Por pendientes (slopes):**
- **M:Tron:** `2412b` slope 45° 1×1 = 40 unidades — la **micro-slope más frecuente del corpus Space**. Patente M:Tron.
- **Spyrius:** `2412b` = 19 unidades — mismo elemento.
- **Space Police II:** `3820`(30) — slope 45° 2×1 estándar.
- **Space Police III:** `4589` cone 1×1 = 67 unidades — la **signature** (toberas).

**Por cilindros (mástiles/antenas):**
- `4-4cyli` **no aparece en el top-15 de ningún Space sub-theme** — el cilindro primitivo es de Castle/Pirates/Boat/City Fire, no Space. (Confirma observación: cilindros = mástil/barco/antena terrestre.)

**Por Technic pin (articulación):**
- **Space Police III:** `54200` hinge = 89 unidades, `6141` round = 79 — **el único Space con hinges en top-3**. Esto lo distingue de los Space pre-2000 que construyen sin articulación Technic.

**Por bigramas únicos:**
- **M:Tron:** `2412b→2412b = 16` — micro-slopes apilados para cascos angulares M:Tron.
- **Futuron:** `4592→4593 = 16` — **par canónico Futuron** (`4592` cylinder 2×2 + `4593` cone 2×2 = tobera de nave). Único Space con este bigrama en top.
- **Ice Planet 2002:** `4275b→4275b = 12`, `4276b→4276b = 12` — **parts específicas Ice Planet** (`4275b` slope 45° 1×2 mod con stud, `4276b` slope 33° 1×2 con stud) — los **"ice tracks"** azules del theme.
- **Spyrius:** `4624→3641 = 8` y `3641→4624 = 7` — **wheel/tyre bidireccional** = rover Spyrius.
- **Space Police I:** `3666`(26) — plate 1×6 — muros largos para la prisión espacial.
- **Unitron:** `756→756 = 348` + `754→754 = 88` — **doble baseplate** (756 stack 348 + 754 stack 88). Unitron es el **único Space que combina ambos baseplates** — son las naves circulares UFO Unitron.

### parts específicas de cada sub-theme (no en otros Space)

| Sub-theme | parts específica | Frec. | Notas |
|---|---|---:|---|
| Classic Space | (ninguna exclusiva en top-30) | — | Vocabulario universal Space pre-1990 |
| Futuron | (ninguna exclusiva en top-30) | — | Universal |
| Blacktron I | `4073` | — | Plate 1×1 round — único |
| Blacktron II | `2515a` | — | Wheel 8×4 — único |
| M:Tron | `2959c01` | — | Slope curvo 2×1 — único |
| Ice Planet 2002 | (ninguna exclusiva en top-30) | — | Usa 4275b/4276b (compartidos con otros Space) |
| Spyrius | `3297` | — | Slope 33° 2×1 — único |
| Space Police I | `2362a` | — | Panel 1×2×1 — único |
| Space Police II | `3298p69`, `4215a`, `6061` | — | 3 parts específicas |
| Space Police III | `6587`, `44728`, `209`, `32556`, `4274`, `30104k02`, `50950`, `54200`, `61409`, `32062` | — | **10 parts específicas** — el más moderno y Technic |
| Unitron | `993`, `754`, `2681` | — | 754 baseplate + 993 + 2681 — UFO specific |
| Insectoids | `30211`, `3665b`, `6249`, `6232`, `2456` | — | 5 parts específicas |

→ **Space Police III es el más diferenciado** (10 parts únicas) — refleja el salto generacional a Technic-pin + custom hinges. **Los sub-themes pre-1995 (Classic Space, Futuron, Ice Planet, Blacktron I/II) comparten vocabulario universal** porque están construidos con el mismo System set pre-Castle/post-Castle.

---

## 5. Pirates (reducido en Plan C)

**Corpus Pirates final: 7 sets, 6 319 parts.** El shortfall Plan C fue **0/8 sets nuevos** — el corpus Pirates **no creció**.

### Sets en corpus

| Set | Año | parts | Sub | Custom |
|---|---|---:|---:|---:|
| 6235-1 Buried Treasure | 1989 | 31 | 3 | 0 |
| **6286-1 Skull's Eye Schooner** | 1993 | **2 834** | 33 | 21 |
| 1713-1 Shipwrecked Pirate | 1994 | 29 | 3 | 0 |
| 6279-1 Skull Island | 1995 | 383 | 14 | 2 |
| 6232-1 Skeleton Crew | 1996 | 37 | 4 | 0 |
| 6245-1 Harbor Sentry | 1989 | 30 | 3 | 1 |
| **6285-1 Black Seas Barracuda** | 1989 | **2 975** | 33 | 18 |
| **Total** | — | **6 319** | 93 | 90 |

### Sesgo extremo confirmado

- **Sin 6286 + 6285 (los dos mega-ships):** 6 319 − 2 834 − 2 975 = **510 parts en 5 sets = 102 p/set** (modiano 30).
- **Con ellos:** **5 809/6 319 = 91.9 % de las parts** están en sólo 2 sets.
- **Bigrama `4-4cyli→4-4cyli`:** corpus 532 = 6 093, **Pirates = 3 895 = 63.9 %** del total corpus `4-4cyli`.
- **El cilindro primitivo de Pirates (3 895 unidades) supera a todo el resto del corpus combinado** (2 198 unidades en Castle Lion Knights 398 + Black Knights 237 + Black Falcons 108 + Boat 401 + City Fire 932 + Friends 88 + Town Plan 34).

### ¿Sigue siendo un outlier por `4-4cyli` y Technic embebido?

**Sí, ambos confirmados:**

1. **`4-4cyli` outlier:** Pirates monopoliza el cilindro primitivo. Los 2 mega-ships tienen **mastiles multi-segmento** (Sch Barracuda 33 sub-builds incluye mástil cilíndrico entero, Schooner 33 sub-builds idem). Bigrama `4-4cyli→4-4cyli` = 3 789 (en 2 sets, principalmente).

2. **Technic embebido:** los 2 mega-ships tienen **21 + 18 = 39 custom parts embebidos** (highest del corpus Pirates). Pirates > Pirates I tiene **90 custom+subparts totales** — el **3.er theme con más custom** después de Fabuland (135) y Friends (344). Custom ratio 90/6 319 = 1.42 % — **el más alto entre themes Town/Space/Castle** (que rondan 0.0-0.7 %).

3. **Subparts:** Pirates > Pirates I tiene **26 subparts embebidos** — concentra velas, banderas, cañones como subparts en los mega-ships.

### ¿Los sets sesgan las estadísticas?

**Sí, completamente.** Sin los 2 mega-ships (5 809 parts), el corpus Pirates real es **510 parts en 5 sets** = comparable a Castle > Dragon Knights (225 p en 2 sets) o Castle > Forestmen (779 p en 5 sets). Las estadísticas de Pirates son **las del Schooner + Barracuda**, no las de un theme representativo.

**Implicación:** Pirates es **el theme menos generalizable** del corpus 532. Cualquier inferencia sobre "cómo construye Pirates" es realmente "cómo construye el Schooner y el Barracuda". Los 5 sets pequeños (6235, 1713, 6232, 6245, 6279) confirman el vocabulario base (`4-4cyli` reducido, `3004`/`3023`/`3062b`/`3820`) pero el conteo de parts está dominado por los 2 mega-ships.

**Comparación con corpus 300:**
- Corpus 300: 5 sets (sólo el Schooner como mega, 86 % del theme).
- Corpus 532: 7 sets (Schooner + Barracuda, 91.9 % del theme).
- **El sesgo se amplió** — añadir 1713 (29 p) y 6279 Skull Island (383 p) no compensa el segundo mega-ship.

---

## 6. Reglas cross-theme (10 reglas del corpus 532)

1. **Town + Town > Classic Town = 146 sets (27.4 % del corpus 532) y 23 213 parts (21.3 %)** — **el bloque dominante por volumen**. Pero **sólo 55 custom parts** (0.24 % ratio). Town **no innova en vocabulario**, recombina `3023` (832 unidades totales), `3004` (810), `3024` (645), `3010` (590), `3005` (567). La parts **única signature** de Town genérico (no compartida con Space/Castle/Friends) es **`3010` brick 1×1** que aparece en 282 unidades en sólo Town genérico (10 sets), pero es estándar LEGO así que "exclusivo" no aplica en sentido estricto.

2. **Space baseplate `756` es la parts signature de la familia Space pre-2000** — **1 281 unidades en 92 sets** (los 11 sub-themes Space agregados). Sub-themes Space Police II, Spyrius, Insectoids y Space Police III **no usan `756`** (Space Police III usa `54200` hinges en su lugar; los otros son modulares o pre-baseplate). El sub-theme **Unitron combina `756`(355) + `754`(92)** — único Space con ambos baseplates. **Boat** (10 sets, theme separado) **NO usa `756` en top** — usa `4-4cyli`(401) en su lugar.

3. **Castle sub-themes comparten una "gramática Castle" de 16 parts** = {3831, 4444, 3710, 3005, 3622, 3830, 3040b, 3024, 2339, 3004, 3820, 3819, 3010, 3023, 3818, 3009} — 32 % del top-50 Castle. **Lion Knights es el más extenso** (n=10) y tiene la firma vertical más fuerte (delta `(0,-24,0)` = 121). **Forestmen es el más distintivo** (16 parts específicas: `2417`, `4287a`, `4865a`, `93792`, `3455`, `2436a`, `2453a`, etc.) — los animales y cabañas de bosque. **Black Knights tiene 8 parts específicas** (`30499`, `3846p4c`, `3063b`, `2554`, `3958`). **Dragon Knights (n=2) y Knights Kingdom II (n=2)** son outliers modernos con vocabularios distintos (slate `2540`, hinges `3794b`, `6636`).

4. **Pirates es un outlier estadístico confirmado** — **91.9 % de las 6 319 parts Pirates están en 2 mega-ships** (6286 Schooner 2 834 p + 6285 Barracuda 2 975 p). El cilindro primitivo `4-4cyli` suma **3 895 unidades** = **63.9 % del total corpus de esa parts** (6 093). Sin los mega-ships, Pirates sería un theme de **102 p/set comparable a Castle Forestmen** (155 p/set). Pirates es **el theme menos generalizable** del corpus.

5. **Train 9V vs 12V vs 4.5V distinción clara por vocabulario** (33 sets en 3 sub-themes): **9V (n=14) usa más plate** (`3023` 168×, `3004` 110×, ratio plate/brick ≈ 1.5); **12V (n=10) usa más brick** (`3004` 151×, `3023` 127×, ratio ≈ 1.0, más pesado); **4.5V (n=9) usa parts grandes** (`4166b` panel 1×6 = 32×, no en 9V/12V). **Train genérico (n=2) tiene `2877` printed plate 1×6 = 44×** — firma moderna única. **Sub-builds/set varía:** 9V = 15.0, 12V = 7.7, 4.5V = 3.22 — 9V es el más subdividido (sets 1991-2006 con instrucciones detalladas).

6. **Space Police III (n=8) es el Space sub-theme más diferenciado y moderno** — **`54200` hinge = 89 unidades** (bigrama `54200→54200 = 50`) + `6141` round = 79 + `4589` cone = 67 + `3673` = 61. **10 parts específicas** (`6587`, `44728`, `209`, `32556`, `4274`, `30104k02`, `50950`, `54200`, `61409`, `32062`) — **el doble que cualquier otro Space sub-theme**. Space Police III es **el único Space con Technic pin en top-3** — refleja la transición 2009-2010 donde Space Police se hizo articulado (vs naves rígidas pre-2000).

7. **Friends (n=17) y Fabuland (n=23) son gemelos en custom density** — Fabuland **9.26 %** (135 custom+subparts / 896 parts, 23 parts únicas `u91xx`), Friends **4.12 %** (344 custom+subparts / 5 046 parts, 3 parts decorativas pastel). **Estrategias opuestas**: Fabuland 100 % serie custom `u91xx` (cabeza+cuerpo+animal bloquean cada set), Friends 100 % estándar + decoración pastel (`59349`, `92244`, `92245`). **No comparten ninguna parts exclusiva entre sí.**

8. **Boat (n=10) absorbe el vocabulario Pirates sin la narrativa** — `4-4cyli`(401) + `3005`(80) + `3004`(66). parts signature: **cilindro primitivo para mástiles de barcos civiles**. **Boat NO usa `754` baseplate 24×24** (sólo 0 en top-5) — al revés que Pirates donde `754` = 214 unidades (todo del Schooner+Barracuda). **Boat es la "Pirates sin skull"** — barcode del cilindro sin la decoración pirata.

9. **Western es bimodal signature-caballo + saloon** (n=17): `30136` cabeza caballo = **184 unidades** (bigrama `30136→30136 = 137` en 4/17 sets), `30137` cuerpo = 103, `30141` saddle = 37 — el trío equino. Para saloon/carro: `3004` brick 1×2 (132×) + `3820` slope 45° 2×1 (76×, **12/17 sets**) + `3818`/`3819` slopes (38 c/u). **7 parts impresas exclusivas** (saddle, WANTED plate, horse accessory) — **segundo theme con más decoración impresa** después de Pirates. Delta signature `(31, 0, 0)` = 24 — offset no-1-stud para cuellos movibles.

10. **Themes con vocabulario 100 % estándar (sin parts exclusivas en top-30):** **Town, Town > Classic Town, Creator 3-in-1, Creator, Space Police II, Train genérico, Universal Building Set, Model Team**. Estos themes **no innovan en vocabulario**, sólo recombinan System estándar. Los themes con parts exclusivas son los **temáticos** (Fabuland 23, Pirates 8, Western 7, Friends 3, Space Police III 10, Castle Forestmen 16, Castle Black Knights 8, Castle Dragon Knights 12, Castle Knights Kingdom II 22, Insectoids 5, Spyrius 1, etc.) — **la exclusividad de vocabulario es el marcador de identidad temática**.

---

## Resumen ejecutivo

- **532 sets, 108 760 parts, 81 themes, 1 037 custom+subparts (0.95 % ratio global), BFC CERTIFY 24.8 %.**
- **78.6 % de sets son pre-2000** (418/532) — Plan C logró el target de uniformización.
- **Town > Classic Town (136 sets) y Train > 9V (14 sets)** son los beneficiaries más grandes — Theme dominante + sub-theme técnico emergente.
- **Castle familia (28 sets)** ahora tiene 6 sub-themes con n≥2; Lion Knights (n=10) es el bloque principal, Forestmen (n=5) el más distintivo.
- **Space familia (91 sets)** tiene 12 sub-themes con n≥1; 5 con n≥10. Space Police III es el más moderno/Techic, Classic Space el más "puro".
- **Pirates (7 sets)** sigue siendo un outlier dominado por 2 mega-ships — corpus sesgado, no generalizable.
- **Fabuland + Friends** son los únicos themes con custom density > 4 % — encapsulamiento temático vía parts exclusivas.
- **16 parts compartidas** = la "gramática Castle"; **12 sub-themes Space** sin gramática común pero con baseplate `756` como signature de los pre-2000.