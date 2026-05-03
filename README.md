# TET Paper II Science Handbook

> **Comprehensive TN-TET Paper II Science preparation handbook**  
> Covering Classes 6, 7 & 8 syllabus across 22 TET-aligned chapters.  
> Memorization-focused, fact-dense PDFs built with Python + ReportLab.  
> **By [ChalkPieceDiary](https://chalkpiecediary.com)**

---

## 📚 Chapter Structure (22 Chapters)

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

### 🌱 Biology (B1–B7)
| ID | Chapter | Status |
|----|---------|--------|
| B1 | Plant Kingdom | ⏳ Planned |
| B2 | Animal Kingdom & Movements | ⏳ Planned |
| B3 | Cell & Organisation of Life | ⏳ Planned |
| B4 | Microorganisms | ⏳ Planned |
| B5 | Health, Hygiene & Adolescence | ⏳ Planned |
| B6 | Crop Production & Management | ⏳ Planned |
| B7 | Environment & Ecology | ⏳ Planned |

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
├── output/               # Generated PDFs (gitignored)
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

### Build a Tamil chapter (HTML/CSS pipeline)

```bash
python build/build_tamil_chapter.py P1   # Output: output_ta/P1_measurement_ta.pdf
```

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
| Page size | A5 (148 × 210 mm) |
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
