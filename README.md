# TET Paper II Science Handbook

> **Comprehensive TN-TET Paper II Science preparation handbook**  
> Covering Classes 6, 7 & 8 syllabus across 23 TET-aligned chapters.  
> Memorization-focused, fact-dense PDFs built with Python + ReportLab.  
> **By [ChalkPieceDiary](https://chalkpiecediary.com)**

---

## 📚 Chapter Structure (23 Chapters)

### ⚡ Physics (P1–P8)
| ID | Chapter | Status |
|----|---------|--------|
| P1 | Measurement | ✅ Complete |
| P2 | Force, Motion & Pressure | ✅ Complete |
| P3 | Heat & Temperature | ✅ Complete |
| P4 | Light | ✅ Complete |
| P5 | Electricity | ✅ Complete |
| P6 | Magnetism | ✅ Complete |
| P7 | Sound | ✅ Complete |
| P8 | Universe & Space Science | ✅ Complete |

### ⚗️ Chemistry (C1–C7)
| ID | Chapter | Status |
|----|---------|--------|
| C1 | Matter & Its Properties | ⏳ Planned |
| C2 | Atomic Structure | ⏳ Planned |
| C3 | Changes Around Us | ⏳ Planned |
| C4 | Air | ⏳ Planned |
| C5 | Water | ⏳ Planned |
| C6 | Acids, Bases & Salts | ⏳ Planned |
| C7 | Chemistry in Daily Life | ⏳ Planned |

### 🌱 Biology (B1–B8)
| ID | Chapter | Status |
|----|---------|--------|
| B1 | Plant Kingdom | ⏳ Planned |
| B2 | Animal Kingdom & Movements | ⏳ Planned |
| B3 | Cell & Organisation of Life | ⏳ Planned |
| B4 | Microorganisms | ⏳ Planned |
| B5 | Health, Hygiene & Adolescence | ⏳ Planned |
| B6 | Crop Production & Management | ⏳ Planned |
| B7 | Environment & Ecology | ⏳ Planned |
| B8 | Environment & Conservation | ⏳ Planned |

---

## 🗂️ Project Structure

```
tet-paper2-science-handbook/
├── shared/
│   ├── theme.py          # Colors, fonts, page size (central config)
│   ├── styles.py         # All paragraph styles
│   ├── components.py     # Reusable UI elements (tables, banners, fact boxes)
│   └── page_chrome.py    # Header / footer for every page
├── chapters/
│   ├── P1_measurement.py # ✅ Chapter module (one per chapter)
│   ├── P2_force_motion_pressure.py
│   ├── P3_heat_temperature.py
│   └── ...
├── build/
│   ├── build_chapter.py  # Build a single chapter
│   ├── build_all.py      # Build all 22 chapters
│   └── combine.py        # Merge all into master PDF
├── output/               # English working PDFs (gitignored)
├── output_ta/            # Tamil per-chapter color PDFs (gitignored)
├── output_ta_web/        # Tamil web/HTML bundle (gitignored)
├── output_ta_color/      # Tamil full-book color PDF (gitignored)
├── output_ta_print_bw/   # Tamil full-book B/W print PDF (gitignored)
├── release/
│   ├── web/              # Final Tamil web bundle
│   ├── color/            # Final Tamil color PDF
│   └── print/            # Final Tamil B/W print PDF
├── requirements.txt
└── .github/workflows/
    └── build.yml         # GitHub Actions auto-build
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.9+
pip install -r requirements.txt

# Linux: Install DejaVu fonts (for proper Unicode rendering)
sudo apt-get install fonts-dejavu-core

# macOS:
brew install --cask font-dejavu-sans
```

### Build a single chapter

```bash
python build/build_chapter.py P1    # Output: output/P1_Measurement.pdf
python build/build_chapter.py C2    # Output: output/C2_Atomic_Structure.pdf
```

### Tamil edition — three output formats

The Tamil pipeline (HTML/CSS → WeasyPrint) produces **three distinct deliverables**
from the same chapter sources in `chapters_ta_html/`:

| # | Format | Purpose | Build script | Stylesheet | Working dir | Final release |
|---|--------|---------|--------------|------------|-------------|---------------|
| 1 | **Web** (HTML) | வலைத்தளம் / WordPress publishing | `build/build_tamil_wordpress.py` | `shared/css/handbook_ta_web.css` | `output_ta_web/` | `release/web/` |
| 2 | **Color PDF** | படிக்க — on-screen / e-reader (Scholar Modern palette: Indigo / Burnt-Orange / Forest) | `build/build_tamil_color_book.py` | `shared/css/handbook_ta_color_book.css` | `output_ta_color/` | `release/color/` |
| 3 | **B/W Print PDF** | அச்சுக்காக — cost-effective print (210 × 290 mm, grayscale ramp) | `build/build_tamil_print_bw_book.py` (whole book) / `build/build_tamil_print_bw.py` (single chapter) | `shared/css/handbook_ta_print_bw.css` | `output_ta_print_bw/` | `release/print/` |

The color stylesheet `@import`s the print B/W stylesheet and overlays only the
subject palette — pagination, cover, and front-matter are identical between
the color and print editions, so layout proofing can be done on either.

```bash
# 1. Web (HTML bundle for WordPress)
python build/build_tamil_wordpress.py

# 2. Color PDF (full book)
python build/build_tamil_color_book.py

# 3. B/W Print PDF (full book)
python build/build_tamil_print_bw_book.py

# Single chapter (color PDF, default pipeline)
python build/build_tamil_chapter.py P1     # → output_ta/P1_measurement_ta.pdf

# Single chapter (B/W print)
python build/build_tamil_print_bw.py P1    # → output_ta_print_bw/P1_measurement_ta.pdf
```

When a build is final, copy the artifact from its `output_ta_*` working dir
into the matching `release/<format>/` folder.

Tamil pipeline docs:
- `docs/tamil/master_prompt_v2.md`
- `docs/tamil/chapter_execution_checklist_ta.md`
- `docs/tamil/weasyprint_windows_setup.md`

### Build all chapters

```bash
python build/build_all.py
```

### Combine into master handbook

```bash
python build/combine.py
# Output: output/TET_Handbook_Paper2_Science_Master.pdf
```

---

## 🎨 Design System

| Element | Value |
|---------|-------|
| Page size | 210 × 290 mm (custom, near A4) — two-column layout, 20 mm margins |
| Primary color | `#0F766E` (Deep teal-green) |
| Accent | `#F59E0B` (Amber — ★ fact boxes) |
| Font | DejaVu Sans (full Unicode support) |
| Body size | 8.3pt |
| TET focus | Memorization-first — years, names, numbers |

### Content philosophy

Each chapter contains:
- **Fact tables** — all key data in scannable format
- **★ Highlighted facts** — years, scientists, specific values for TET MCQs
- **Comparison tables** — side-by-side Class 6 / 7 / 8 progression
- **Solved problems** — numbered, tabular format
- **2-column glossary** — all terms alphabetically

---

## 📦 CI/CD

On every push to `main`, GitHub Actions:
1. Installs dependencies
2. Builds all available chapter PDFs
3. Combines into master handbook
4. Uploads as a downloadable artifact

On tag push (e.g., `v1.0`), it also creates a GitHub Release with the master PDF attached.

---

## 📝 License

MIT License — see [LICENSE](LICENSE)

**Note:** The PDF outputs may be used/distributed for free under this license, or
sold commercially — as permitted by MIT. TN Govt textbook content is public domain.

---

## 🙏 Credits

- **Author**: [ChalkPieceDiary](https://chalkpiecediary.com) — Perumalraj
- **Source material**: TN SCERT Textbooks (Class 6, 7, 8 — Science)
- **TET Syllabus reference**: [TRB Tamil Nadu](https://trb.tn.gov.in/)
- **Built with**: Python, ReportLab, pypdf, DejaVu fonts
