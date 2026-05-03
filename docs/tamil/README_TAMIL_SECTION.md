# Tamil Edition — தமிழ் பதிப்பு

> அறிவியல் கையேடு — போட்டித் தேர்வுகளுக்கான தமிழ் பதிப்பு  
> TNTET, TNPSC, TRB, NMMS, NTSE மற்றும் scholarship தேர்வுகளுக்கான வடிவமைப்பு.

---

## Architecture

| Aspect | English Edition | Tamil Edition |
|---|---|---|
| Engine | ReportLab | WeasyPrint (Pango + HarfBuzz) |
| Sources | `chapters/` | `chapters_ta_html/` |
| Output | `output/P{N}_*.pdf` | `output_ta/P{N}_*_ta.pdf` |
| Builders | inline/chapter-specific | `shared/builders/html_builders.py` |
| Styling | ReportLab styles | `shared/css/handbook_ta.css` |

---

## Build

```bash
pip install -r requirements.txt
python build/build_tamil_chapter.py P1
```

---

## Notes

- Tamil shaping correctness காக WeasyPrint stack பயன்படுத்தப்படுகிறது.
- Full prompt/reference:
  - `docs/tamil/master_prompt_v2.md`
  - `docs/tamil/chapter_execution_checklist_ta.md`
  - `docs/tamil/weasyprint_windows_setup.md`

