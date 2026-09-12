# NEXT_SESSION.md — Plan para continuar el corpus

> Este archivo documenta **exactamente** qué hay que hacer la próxima sesión
> para continuar el análisis cross-corpus de LDraw.
>
> **Estado actual (cierre 2026-09-12)**:
> - 532 sets OMR descargados (108 760 piezas, 3 cohortes).
> - 23 reglas aprendidas (`LEARNED_CONVENTIONS_532.md`).
> - Generador `ldraw_gen.py` con 5 demos validados.
> - **Lo que falta**: ~938 sets OMR no descargados (de 1 470 totales).

---

## TL;DR — Para la próxima sesión

Si el usuario dice "descargá todos los modelos faltantes y analizalos", hacer:

```bash
# 1. Cargar estado actual
cat /home/user/Projects/ldraw/STATE.json

# 2. Generar setlist de los sets faltantes (~938 sets OMR restantes)
#    Estrategia: Plan D — completar OMR al máximo (excluyendo lo que ya tenemos)

# 3. Descargar los nuevos MPDs
mkdir -p /home/user/Projects/ldraw/corpus/mpds_remaining
# (usar xargs con P=24 para paralelizar)

# 4. Re-parsear todo (con el batch parser actualizado)
python3 /home/user/Projects/ldraw/analysis/batch_parse3.py

# 5. Re-despachar subagentes paralelos para actualizar findings

# 6. Actualizar LEARNED_CONVENTIONS_532.md → LEARNED_CONVENTIONS_FINAL.md
# 7. Actualizar el generador
```

---

## 1. Lo que YA está hecho (no repetir)

### Corpus actual: 532 sets en 3 cohortes

| Cohorte | Sets | Piezas | Carpeta | Setlist JSON |
|---------|-----:|-------:|---------|--------------|
| 80s/90s | 100 | 18 670 | `corpus/mpds/` | `corpus/setlist_80s90s.json` |
| Kids | 200 | 42 947 | `corpus/mpds_kids/` | `corpus/setlist_kids.json` |
| Classic (Plan C) | 232 | 47 143 | `corpus/mpds_classic/` | `corpus/setlist_classic.json` |
| **Total** | **532** | **108 760** | — | — |

### Documentos canónicos (NO sobrescribir)
- `LDRAW_GUIDE.md` — spec del formato LDraw.
- `LEARNED_CONVENTIONS_532.md` — **23 reglas aprendidas, CANÓNICO**.
- `README.md` — overview del proyecto.

### Documentos legacy (trazabilidad)
- `LEARNED_CONVENTIONS.md` (2 sets), `_100.md`, `_300.md`.

### Scripts funcionales
- `analysis/batch_parse3.py` — parser principal (corre 532 sets).
- `generator/ldraw_gen.py` — generador con 5 demos.

### Datos
- `analysis/cross_corpus2_stats.json` — stats globales 4 cohortes.
- `analysis/per_set_stats_300.json` — 532 entries por set.
- `corpus/all_omr_themes.json` — catálogo completo de 135 themes OMR.
- `corpus/plan_c_distribution.json` — Plan C con shortfalls documentados.

---

## 2. Lo que FALTA hacer

> **MANDATORY**: cuando el usuario dice "continuar hasta el final" / "todo lo que falta" / "Plan D completo", ejecutar la pipeline completa sin pausar entre etapas. Si un sub-paso falla, reintentarlo. NO preguntar "debería continuar?" — el usuario ya dijo sí.

### 2.1 Sets NO descargados

El OMR tiene ~1 470 sets totales. Tenemos 532. **Faltan ~938 sets**.

URL pattern: `https://library.ldraw.org/library/omr/{SET}-{Q}.mpd`

### 2.2 Themes subrepresentados (Plan C shortfall)

24 themes de los 49 pre-2000 tienen shortfall. Algunos críticos:

| Theme | Shortfall | Razón |
|-------|----------:|-------|
| Pirates > Pirates I | 8 | Todos ya estaban en cohortes previos |
| Castle > Forestmen | 5 | Ya estaban en cohortes previos |
| Castle > Black Knights | 3 | Ya estaban en cohortes previos |
| Castle > Dragon Knights | 2 | Ya estaban en cohortes previos |
| Castle > Knights Kingdom II | 1 | Ya estaban |
| Castle (genérico) | 1 | — |
| Universal Building Set > Basic | 5 | Ya estaban |
| Sports > Soccer | 3 | Ya estaban |
| Town Jr. | 2 | Ya estaban |
| Town > World City | 2 | Ya estaban |
| Adventurers > Desert | 2 | — |
| Adventurers > Orient Expedition | 1 | — |
| Town > Extreme Team | 1 | — |
| Town > Town Plan | 1 | — |
| Znap | 1 | — |

**Recomendación**: verificar si los sets que el shortfall menciona están realmente en los cohortes previos. Si no, agregarlos manualmente.

### 2.3 Themes NO descargados (grandes oportunidades)

| Theme | Sets en OMR | ¿Descargado? |
|-------|------------:|:------------:|
| Technic | 158 | ❌ NO (excluido) |
| Brickheadz | 76 | ❌ NO (specialty) |
| Racers | 76 | ❌ NO |
| Star Wars | 64 | ❌ NO (parcialmente en 80s/90s) |
| Architecture | 36 | ❌ NO |
| Modular Buildings | 14 | ❌ NO |

**Decisión recomendada**: si el usuario quiere "todo", incluir Technic + Brickheadz + Architecture + Modular Buildings como 4ª cohorte ("modernos/coleccionista"). Excluir Racers (es oficial pero redundante con Creator 3-in-1).

---

## 3. Plan D — "Todo lo que falta"

Si el usuario pide "descargá todo lo faltante":

### 3.1 Estrategia

1. **Generar setlist completo** de OMR:
   - Partir de `all_omr_themes.json` (135 themes).
   - Para cada theme, generar URLs plausibles para los sets en `set_count`.
   - Excluir sets ya en `STATE.json:corpus.downloaded_set_numbers`.
   - Verificar cada URL con `curl -sI` (HEAD).

2. **Distribución objetivo**:
   - +600-800 sets nuevos.
   - Mantener coherencia con las cohortes existentes (no fragmentar).
   - Nueva 4ª cohorte: **Modern/Collector** (Technic + Brickheadz + Architecture + Modular Buildings).

3. **Distribución sugerida** (ajustable):

| Cohorte nueva | Sets | Themes |
|---------------|-----:|--------|
| Modern Official | ~300 | Technic, Brickheadz, Architecture, Modular Buildings, Icons, Racers |
| Remaining Official | ~300 | Star Wars restantes, Ideas, Mixels, Elves, etc. |
| Specialty | ~100 | Promotional, Seasonal, Hobby Sets |

4. **Output esperado**:
   - `corpus/setlist_modern.json` (~300 sets).
   - `corpus/setlist_remaining.json` (~400 sets).
   - `corpus/mpds_modern/` y `corpus/mpds_remaining/` con los MPDs descargados.

### 3.2 Estimación de tiempo

- Scraping de URLs: ~5-10 min (1 subagente).
- Descarga en paralelo (24 workers): ~10-15 min para ~700 archivos (~50 MB).
- Parsing: ~5 min.
- Análisis: ~30 min (4 subagentes paralelos).
- Síntesis docs: ~15 min.

**Total**: ~1-1.5 horas wall-clock.

---

## 4. Pipeline exacto (paso a paso para la próxima sesión)

> **REGLA**: ejecutar todos los pasos sin pausar. NO preguntar entre etapas. Si un paso falla, reintentarlo antes de parar.

### Paso 1: Verificar estado (30 segundos)

```bash
cat /home/user/Projects/ldraw/STATE.json | head -30
ls /home/user/Projects/ldraw/corpus/mpds*/ 2>/dev/null | head
python3 -c "import json; s=json.load(open('/home/user/Projects/ldraw/STATE.json')); print(f\"Corpus: {s['corpus']['total_sets']}/{s['omr_metadata']['total_sets_in_omr']} sets, faltan {s['omr_metadata']['total_sets_in_omr']-s['corpus']['total_sets']}\")"
```

### Paso 2: Identificar themes a ampliar (solo si el usuario NO especificó)

- Si el usuario no especifica, preguntar brevemente con 3 opciones:
  - (A) **Plan D completo**: terminar todo el OMR (~938 sets nuevos, 4 cohortes adicionales).
  - (B) **Plan D gaps**: solo themes subrepresentados en cohortes actuales.
  - (C) **Plan D temático**: el usuario elige 3-5 themes específicos.
- Si el usuario dice "lo que sea" / "vos decidí" / "todo", ir con (A) por defecto.

### Paso 3: Generar URLs (subagente, ~5 min)

Despachar subagente para:
- Leer `corpus/all_omr_themes.json`.
- Para cada theme objetivo, generar setlist con URLs del OMR.
- Verificar cada URL con HEAD.
- Devolver JSON con metadata completa.

### Paso 4: Descargar

```bash
mkdir -p corpus/mpds_newcohort
cd corpus
cat setlist_newcohort.txt | xargs -I {} -P 24 sh -c '
  url="$1"
  fname=$(basename "$url")
  curl -sL --max-time 60 -o "mpds_newcohort/$fname" "$url" 2>/dev/null
' _ {}
```

### Paso 5: Actualizar parser

Modificar `analysis/batch_parse3.py` para incluir el nuevo directorio. O crear `batch_parse4.py`.

Agregar:
```python
newcohort = []
for meta in setlist_newcohort:
    path = Path('corpus/mpds_newcohort') / f"{num}-{q}.mpd"
    if path.exists():
        try:
            r = analyze_one(path, meta, cohort='newcohort_name')
            newcohort.append(r)
        except: pass
```

### Paso 6: Re-correr análisis

```bash
python3 analysis/batch_parse3.py  # o 4.py
```

### Paso 7: Despachar 4 subagentes paralelos

- (a) chaining cross-corpus con nueva cohorte.
- (b) comparison cohortes (incluir nueva).
- (c) themes específicos de la nueva cohorte (Technic, Brickheadz, etc.).
- (d) update generador con nuevas reglas.

### Paso 8: Sintetizar documento

- `LEARNED_CONVENTIONS_FINAL.md` (reemplaza `_532.md`).
- O `LEARNED_CONVENTIONS_532_PLUS.md` (extiende el anterior).
- Actualizar README con nueva cohorte.

### Paso 9: Validar

- Todos los demos del generador pasan `validate()` con 0 errores.
- El corpus actualizado aparece en `STATE.json`.

---

## 5. Convenciones de nombres

| Cosa | Convención |
|------|------------|
| Cohortes | `<era>_<style>` ej: `80s90s`, `kids`, `classic`, `modern`, `remaining` |
| Carpetas | `corpus/mpds_<cohort>/` |
| Setlists | `corpus/setlist_<cohort>.{txt,json}` |
| Scripts parser | `analysis/batch_parse<N>.py` (N=1, 2, 3, ...) |
| Stats JSON | `analysis/cross_corpus<N>_stats.json` |
| Findings | `analysis/findings_<topic>.md` |
| Convenciones doc | `LEARNED_CONVENTIONS_<N>.md` donde N es el conteo de sets |

---

## 6. Estado persistente

`STATE.json` contiene:
- Lista de todos los sets descargados (532 numbers).
- Lista de URLs de cada setlist.
- Estadísticas por cohorte.
- Rutas a scripts y outputs.

**Regla**: actualizar `STATE.json` después de cada sesión exitosa.

---

## 7. Si el usuario pide algo diferente a "todo"

### "Solo Technic"
- Despachar subagente para encontrar 50-100 sets Technic.
- Crear `cohort_technic`.
- Re-parsear, re-analizar.

### "Solo Star Wars faltantes"
- Filtrar `all_omr_themes.json` por Star Wars + sub-themes.
- Excluir los 6 sets ya descargados.
- Generar URLs, descargar, parsear.

### "Solo una categoría temática"
- El usuario debe especificar.
- Despachar subagente con la categoría.

---

## 8. Riesgos conocidos

1. **OMR tiene rate limits**: descargar ~700 archivos en paralelo puede triggerear. Si pasa, agregar `--max-time 60` (ya está) y reducir a `-P 8`.

2. **Sets con `sub_model` suffix**: `XXX-1_Helicopter.mpd` (no `XXX-1.mpd`). El parser actual no los maneja bien. Si aparece, ajustar.

3. **OMR puede haber añadido sets nuevos** desde la sesión anterior. Re-verificar contra `all_omr_themes.json`.

4. **BFC CERTIFY ratio puede cambiar** con sets nuevos. Si baja de 20 %, probablemente el corpus se vuelve menos formal.

5. **Generador puede romperse** con nuevas constantes. Mantener backwards-compat con demos existentes.

---

## 9. Comando de reanudación completo (para copy-paste)

```bash
# Verificar estado
cat /home/user/Projects/ldraw/STATE.json | python3 -c "import json,sys; d=json.load(sys.stdin); print('Sets:', len(d['corpus']['downloaded_set_numbers']), 'Pieces:', d['corpus']['total_pieces'])"

# Identificar gaps
python3 -c "
import json
themes = json.load(open('/home/user/Projects/ldraw/corpus/all_omr_themes.json'))
state = json.load(open('/home/user/Projects/ldraw/STATE.json'))
downloaded = set(state['corpus']['downloaded_set_numbers'])
# Show themes not yet downloaded
print('Themes available in OMR not yet covered:')
for t in themes['themes']:
    print(f'  {t[\"theme_full\"]}: {t[\"set_count\"]} sets, category={t.get(\"category\")}')"
```

---

## 10. TL;DR final

**Para la próxima sesión**:
1. Leer `STATE.json` y `NEXT_SESSION.md` (este archivo).
2. Preguntar al usuario: ¿Plan D completo, enfocado en gaps, o temático?
3. Despachar subagente para generar URLs de los themes objetivo.
4. Descargar en paralelo.
5. Actualizar parser.
6. Re-analizar con 4 subagentes paralelos.
7. Sintetizar nuevo documento de convenciones.
8. Actualizar `STATE.json`.

**Output esperado**: corpus de ~1 200-1 400 sets, 28-30 reglas aprendidas (con ajustes), generador con nuevos templates.

**Tiempo**: 1-2 horas wall-clock.
