# Tamil Edition — தமிழ் பதிப்பு

> **அறிவியல் கையேடு — போட்டித் தேர்வுகளுக்கான தமிழ் பதிப்பு**
> Tamil-medium science handbook for competitive exam aspirants
> (TNTET, TNPSC, TRB, NMMS, NTSE, scholarship exams)
> Authored by **த. பெருமாள்ராஜ்** ([ChalkPieceDiary](https://chalkpiecediary.com))

---

## 🏗 Architecture

The Tamil edition uses a **separate HTML/CSS pipeline** from the English edition (which uses ReportLab):

| Aspect | English Edition | Tamil Edition |
|---|---|---|
| Engine | ReportLab | **WeasyPrint** (Pango + HarfBuzz) |
| Sources | `chapters/` | `chapters_ta_html/` |
| Output | `output/P{N}_*.pdf` | `output/P{N}_*_ta.pdf` |
| Builders | inline per-chapter | shared in `shared/builders/html_builders.py` |
| Styling | inline ReportLab | shared in `shared/css/handbook_ta.css` |

**Why WeasyPrint?** ReportLab cannot properly shape Tamil ligatures (வீ, ணை, கொ/கோ, ஸ்ரீ). WeasyPrint uses Pango+HarfBuzz which renders Tamil correctly.

---

## 📁 Tamil Edition File Structure

```
chapters_ta_html/                     # Tamil chapter sources
└── P1_measurement_ta.py              # P1 அளவீடு (Measurement)

shared/                               # Shared infrastructure
├── fonts/
│   ├── NotoSansTamil-Regular.ttf
│   └── NotoSansTamil-Bold.ttf
├── css/
│   └── handbook_ta.css               # Master stylesheet
└── builders/
    ├── __init__.py
    └── html_builders.py              # Builder library
```

---

## 🚀 Building Tamil Chapters

### Setup
```bash
pip install weasyprint fonttools PyMuPDF
```

### Build a chapter (color PDF)
```bash
cd /path/to/repo
python3 chapters_ta_html/P1_measurement_ta.py
```

Output PDF: `output/P1_measurement_ta.pdf`

### Build print-ready B/W chapter (press profile)
```bash
python build/build_tamil_print_bw.py P1
```

Output files:
- `output_ta_print_bw/P1_measurement_ta_print_bw.pdf`
- `output_ta_print_bw/P1_measurement_ta_print_bw.html`

Print profile spec:
- Page size: `210mm x 290mm`
- Margins: `20mm` (usable width `170mm`)
- Grayscale styling optimized for black-and-white printing

### Build integrated print B/W book (with cover/front-matter/back-cover)
```bash
python build/build_tamil_print_bw_book.py P1 P2 P3 P4 P5 P6 P7 P8 C1 C2 C3 C4 C5 C6 C7 B1 B2 B3 B4
```

Output files:
- `output_ta_print_bw/Tamil_Science_<SPAN>_print_bw_book.pdf`
- `output_ta_print_bw/Tamil_Science_<SPAN>_print_bw_book.html`

### Build integrated color book (subject-wise color scheme)
```bash
python build/build_tamil_color_book.py P1 P2 P3 P4 P5 P6 P7 P8 C1 C2 C3 C4 C5 C6 C7 B1 B2 B3 B4
```

Output files:
- `output_ta_color/Tamil_Science_<SPAN>_color_book.pdf`
- `output_ta_color/Tamil_Science_<SPAN>_color_book.html`

### Build WordPress-friendly HTML bundle
```bash
python build/build_tamil_wordpress.py P1 P2 P3 P4 P5 P6 P7 P8 C1 C2 C3 C4 C5 C6 C7 B1 B2 B3 B4
```

Output files:
- `output_ta_web/Tamil_Science_<SPAN>_wordpress_bundle.html` (full page preview)
- `output_ta_web/Tamil_Science_<SPAN>_wordpress_fragment.html` (paste-ready content)
- `output_ta_web/chapters/<CHAPTER_ID>.html` (per-chapter fragments)

---

## 📚 Tamil Chapter Status

### ⚡ இயற்பியல் (Physics)
| ID | Tamil Title | English Title | Status |
|----|-------------|---------------|--------|
| P1 | அளவீடு | Measurement | ✅ முடிந்தது (12 pages) |
| P2 | விசை, இயக்கம் & அழுத்தம் | Force, Motion & Pressure | ⏳ திட்டமிடப்பட்டது |
| P3 | வெப்பம் & வெப்பநிலை | Heat & Temperature | ⏳ திட்டமிடப்பட்டது |
| ... | ... | ... | ⏳ |

---

## 🎯 Design Principles (Tamil Edition)

1. **TN textbook terminology alignment** — மாணவர்கள் பாடநூலில் கற்ற கலைச்சொற்களையே தேர்வுக்குப் படிப்பதால், supplementary handbook-உம் same terminology use செய்ய வேண்டும்.

2. **Generic competitive-exam scope** — TET-specific அல்லாமல், TNTET / TNPSC / TRB / NMMS / NTSE போன்ற அனைத்து போட்டித் தேர்வுகளுக்கும் பொதுவான content.

3. **Compact + dense** — ஒவ்வொரு pageஉம் exam-relevant content-ஆல் நிரப்பப்பட வேண்டும். "Daily life" / "Why measurement matters" போன்ற non-exam sections-ஐ தவிர்த்தல்.

4. **Section J நினைவிற்காக** — பாரம்பரிய glossary section-க்குப் பதிலாக, 3 sub-blocks-கொண்ட Memory Aid section: (1) values & formulas, (2) events & years, (3) confusion-pair distinctions.

5. **Newspaper column-flow for problems** — solved problems vertical column-by-column reading order, not zigzag rows.

For full design specification, see `master_prompt_v2.md`.

---

## 🔤 Key Terminology Standards

(TN textbook alignment — DO NOT deviate)

| English | Tamil | Notes |
|---|---|---|
| Standard Quantity | திட்ட அளவு | NOT நியமம் |
| Standard Unit | படித்தர அலகு | NOT நியம அலகு |
| Standard Time | திட்ட நேரம் | — |
| Derived Quantity | வழி அளவு | NOT வழியாக்கப்பட்ட அளவு |
| Beam Balance | பொதுத் தராசு | NOT தட்டு தராசு |
| Spring Balance | சுருள்வில் தராசு | NOT சுருள் தராசு |
| Accuracy | துல்லியத்தன்மை | NOT just துல்லியம் |
| Precision | நுட்பம் | — |
| Rounding Off | முழுமையாக்கல் | NOT வட்டமிடல் |
| Sub-multiple | துணை அலகு | NOT சிற்றலகு |
| Least Count | மீச்சிற்றளவு | NOT குறை அளவீடு |
| Nautical Mile | நாட்டிக்கல் மைல் | Transliteration (not கடல் மைல்) |

---

## 📜 License

Same as parent project — see `LICENSE`.
