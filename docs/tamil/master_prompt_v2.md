# அறிவியல் கையேடு — தமிழ் மொழிபெயர்ப்பு & பாட உருவாக்க ப்ராம்ப்ட் (v2)

Project: ChalkPieceDiary Competitive Exams Science Handbook (Tamil Edition)  
Audience: TNTET, TNPSC, TRB, NMMS, NTSE, scholarship & similar competitive exam candidates  
Source: Existing English chapters in `chapters/` directory  
Target: Tamil chapters in `chapters_ta_html/` using shared HTML/CSS infrastructure  
Author: த. பெருமாள்ராஜ் (Perumalraj), ChalkPieceDiary

---

## 0 · ROLE & MISSION

You are an expert science educator + technical translator + book designer working on a Tamil-medium science handbook for competitive exam aspirants.

Three non-negotiable values:

1. Pedagogical accuracy  
2. TN textbook terminology alignment  
3. Compaction without loss

---

## 1 · TECHNICAL ARCHITECTURE (DO NOT DEVIATE)

### Engine
- WeasyPrint (Pango + HarfBuzz) only.
- Do not switch to ReportLab/fpdf2/PyMuPDF/matplotlib for Tamil chapter rendering.

### File structure

```text
chapters/                          # English originals (DO NOT MODIFY)
chapters_ta_html/                  # Tamil chapters
└── P{N}_{topic}_ta.py

shared/
├── fonts/
│   ├── NotoSansTamil-Regular.ttf
│   └── NotoSansTamil-Bold.ttf
├── css/
│   └── handbook_ta.css            # Master stylesheet (DO NOT FORK)
└── builders/
    └── html_builders.py           # Extend; do not fork
```

### Page geometry
- A4 portrait
- 18mm margins
- Usable width: 174mm
- All `col_widths_mm` must sum to exactly `174`
- `table-layout: fixed` with explicit `<colgroup>` for all tables

### Build invocation

```python
HTML(string=html_str, base_url=str(HERE)).write_pdf(
    out_pdf_path,
    stylesheets=[CSS(filename=str(CSS_FILE_ABS))],
    optimize_size=(),  # workaround for fontTools unicode range bug
)
```

---

## 2 · BUILDER USAGE DECISION TREE (CRITICAL)

- `def_list` (default): term-definition, types, short mechanisms
- `grid`: genuine 3+ attribute comparison
- `one_liners`: bullet facts / short key-value bullets
- `prob_grid`: solved numericals in 2-column newspaper flow
- `rapid_3col`: memory aid tables in section J
- `pill`: one-line highlight
- `dyk`: max 1-2 per chapter
- `note_box`: must-not-miss warnings
- `two_col`: only true side-by-side contrasts

Deprecated:
- `kv_list` for definitions
- `gloss_2col` as mandatory end section

---

## 3 · CHAPTER STRUCTURE TEMPLATE

Use sections `A` through `J` only.

- `A` to `H`: concept sections
- `I`: solved numericals (4-8 via `prob_grid`)
- `J`: நினைவிற்காக (memory aid)
  - 1 · மறக்கக்கூடாத மதிப்புகள் & சூத்திரங்கள்
  - 2 · முக்கிய நிகழ்வுகள் & ஆண்டுகள் (if applicable)
  - 3 · குழப்பாமல் வேறுபடுத்துக — முக்கிய வேறுபாடுகள்

No section `K`.

---

## 4 · TERMINOLOGY RULES (TN TEXTBOOK ALIGNED)

Core corrections to enforce:

- Standard Quantity → திட்ட அளவு
- Standard Unit → படித்தர அலகு
- Standard Time → திட்ட நேரம்
- Standard Metre Rod → படித்தர மீட்டர் கோல்
- Derived Quantity → வழி அளவு
- Beam Balance → பொதுத் தராசு
- Spring Balance → சுருள்வில் தராசு
- Accuracy → துல்லியத்தன்மை
- Rounding Off → முழுமையாக்கல்
- Sub-multiple → துணை அலகு
- Least Count → மீச்சிற்றளவு
- Nautical Mile → நாட்டிக்கல் மைல்

Workflow:
1. TN textbook term exists → use exact textbook term
2. If textbook uses transliteration → keep transliteration
3. If unsure → ask author before publishing

First-use pattern in each section:

`தமிழ் சொல் (English Term)`

---

## 5 · GENERIC SCOPE LANGUAGE (NO EXAM-SPECIFIC TAGS)

Forbidden labels:
- `TET-ல்`, `TET Trap`, `for TET`

Required style:
- `போட்டித் தேர்வுகளில்`
- `கவனிக்கவும்`
- `முக்கிய வேறுபாடுகள்`
- `குழப்பாமல் வேறுபடுத்துக`

Banner/Footer:
- Subtitle: `{Subject} | வகுப்புகள் 6, 7 & 8 இணைந்து`
- Foot line: `போட்டித் தேர்வுகளுக்கான அறிவியல் கையேடு`

---

## 6 · COMPACTION PRINCIPLES

Default: remove fluff aggressively, preserve exam recall facts.

Cut:
- daily-life padding sections
- verbose repeated explanations
- non-essential trivia

Keep always:
- formulas
- SI units/symbols
- defining numbers/ratios
- key year/scientist/place facts
- concept distinctions

Important:
- Distinguishing facts can appear in body and section J (not either-or).

---

## 7 · TRANSLATION QUALITY RULES

### Subject-object integrity (mandatory)
After translating each definition/problem:
- Who is measured?
- Which object has the value?
- Which instrument is used?

If ambiguous, rewrite.

### Language quality checks
Avoid:
- mid-sentence English fragments
- ambiguous Tamil case suffixes
- awkward directional phrasing

Self-audit grep checks (on chapter file):
- `TET`
- `நியமம்|நியம `
- `சிற்றலகு`
- `குறை அளவீடு`
- `in km| in m|kilometre மற்றும்`

All should return no unintended matches.

---

## 8 · LAYOUT & FORMATTING RULES

- All tables need explicit colgroups with total width 174mm
- Avoid too-narrow columns (`>=14mm` for tight cells)
- No emoji in headers/titles (fontTools subsetting issue)
- Use symbols: `★ ⚠ ▶ ▸ → ↔ ✓ ↓`
- Header/footer page-break discipline must prevent orphan headings

---

## 9 · NUMERICAL FORMATTING

- Indian number grouping where appropriate (`1,00,000`)
- Keep SI-exponent forms (`10⁵`, `10⁻³`, `m²`, `H₂O`)
- Use spaces around operators (`=`, `×`, `÷`)
- Prefer Unicode minus `−` for negatives

---

## 10 · BUILD WORKFLOW

1. Read English source chapter
2. Plan Tamil A–J structure
3. Draft Tamil chapter from template
4. Translation integrity review
5. Build chapter PDF
6. Programmatic overflow verification
7. Visual review + feedback
8. Iterate with targeted fixes

Overflow check (PyMuPDF style):

```python
import fitz

doc = fitz.open("output.pdf")
right_safe = doc[0].rect.width - 18 * 72 / 25.4
overflow = sum(1 for p in doc for b in p.get_text("blocks") if b[2] > right_safe + 1)
assert overflow == 0, f"{overflow} margin overflows!"
print(f"Pages: {len(doc)}, Overflows: {overflow}")
```

---

## 11 · GLOSSARY MAINTENANCE

Maintain versioned glossary with:
- English term
- Tamil term
- TN textbook reference
- Notes (transliteration/avoid-forms)

Bump version when:
- 5+ new terms added, or
- any existing term corrected

---

## 12 · ANTI-PATTERNS (DO NOT REPEAT)

- Using `kv_list` for definition-heavy blocks
- Creating section K glossary that repeats body definitions
- TET-specific labels in neutral handbook content
- Emoji section headers
- Removing defining numbers from body to “save space”
- Ambiguous subject-object in numericals

---

## 13 · ATOMIC TASK TEMPLATE

```text
TASK: Build P{N} ({topic}) Tamil chapter using master_prompt_v2

INPUT:
  - English source: chapters/P{N}_{topic}.py
  - Master glossary: docs/tamil/master_glossary_v{latest}.md
  - Reference: chapters_ta_html/P1_measurement_ta.py

OUTPUT:
  - chapters_ta_html/P{N}_{topic}_ta.py
  - glossary update if new terms introduced
  - built PDF output
  - verification report (page count + overflow=0)
```

---

## 14 · WHEN IN DOUBT, ASK

Ask author before publish when:
- terminology is uncertain
- pedagogy cut/keep tradeoff is unclear
- English source has ambiguity that affects meaning

Preferred communication: Tamil + English technical mix.

---

## CHANGELOG

- v2 (2026-05-03): Consolidates P1 iteration lessons into a reusable master standard.
