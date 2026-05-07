# Tamil-First Workflow

இந்த repository-யில் final output தமிழ் PDF ஆக இருப்பதால், authoring மற்றும் review flow-ஐ **Tamil-first** ஆக lock செய்கிறோம்.

## Source of Truth

- Primary content source: `chapters_ta_html/`
- Final outputs:
  - `output_ta/` (color Tamil chapter PDFs)
  - `output_ta_color/` (integrated color book output)
  - `output_ta_print_bw/` (print B/W chapter + book outputs)
  - `output_ta_web/` (WordPress HTML bundle)
  - `release/` (curated final compiled PDFs only)
- English chapters (`chapters/`) are reference/back-sync targets, not release source.

## Working Rule (Must Follow)

1. எல்லா புதிய content edits-மும் முதலில் `chapters_ta_html/`-ல் செய்ய வேண்டும்.
2. Render/layout-only edits மட்டும் shared layer-ல் செய்ய வேண்டும்:
   - `shared/builders/html_builders.py`
   - `shared/css/handbook_ta.css`
   - `shared/css/handbook_ta_print_bw.css`
3. Concept/content மாற்றம் செய்தால், short sync note பதிவு செய்ய வேண்டும்.
4. English back-sync same session-ல் வேண்டிய அவசியம் இல்லை; batch-ஆக செய்யலாம்.

## Per-Change Checklist

- [ ] Tamil chapter content updated in `chapters_ta_html/`
- [ ] `python build/check_tamil_sync.py` passed
- [ ] Tamil color chapter build tested
- [ ] Tamil print B/W chapter build tested
- [ ] Tamil print B/W book build tested (when relevant)
- [ ] Sync note recorded (if concept/data changed)

## Suggested Commands

```bash
python build/check_tamil_sync.py
python build/build_tamil_chapter.py P1
python build/build_tamil_print_bw.py P1
python build/build_tamil_print_bw_book.py
python build/build_tamil_color_book.py
python build/build_tamil_wordpress.py
```

## Sync Note Template

Use this in PR description or commit body:

```text
SYNC_NOTE:
- Chapter: P?
- Type: concept update / value correction / terminology / structure
- Tamil source updated: yes
- English back-sync: pending / completed
- Impacted outputs: color / print-chapter / print-book
```

## Guardrail

If a quick fix is applied only in output/build layer and not in `chapters_ta_html/`, it will drift over time. Always fix at source first, then rebuild formats.
