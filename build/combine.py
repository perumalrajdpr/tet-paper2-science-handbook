"""
Combine all chapter PDFs into a single master TET Handbook PDF.

Usage:
    python build/combine.py

Output: output/TET_Handbook_Paper2_Science_Master.pdf
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pypdf import PdfWriter, PdfReader


CHAPTER_ORDER = [
    'P1_Measurement.pdf',
    'P2_Force_Motion_Pressure.pdf',
    'P3_Heat_Temperature.pdf',
    'P4_Light.pdf',
    'P5_Electricity.pdf',
    'P6_Magnetism.pdf',
    'P7_Sound.pdf',
    'P8_Universe_Space.pdf',
    'C1_Matter_Properties.pdf',
    'C2_Atomic_Structure.pdf',
    'C3_Changes_Around_Us.pdf',
    'C4_Air.pdf',
    'C5_Water.pdf',
    'C6_Acids_Bases_Salts.pdf',
    'C7_Chemistry_Daily_Life.pdf',
    'B1_Plant_Kingdom.pdf',
    'B2_Animal_Kingdom.pdf',
    'B3_Cell_Organisation.pdf',
    'B4_Microorganisms.pdf',
    'B5_Health_Hygiene_Adolescence.pdf',
    'B6_Crop_Production.pdf',
    'B7_Environment_Ecology.pdf',
]

MASTER_FILENAME = 'TET_Handbook_Paper2_Science_Master.pdf'


def combine(out_dir='output'):
    writer = PdfWriter()
    total_pages = 0
    found = []
    missing = []

    for fname in CHAPTER_ORDER:
        fpath = os.path.join(out_dir, fname)
        if not os.path.exists(fpath):
            missing.append(fname)
            continue
        reader = PdfReader(fpath)
        n = len(reader.pages)
        for page in reader.pages:
            writer.add_page(page)
        total_pages += n
        found.append((fname, n))
        print(f"  ✅ {fname}  ({n} pages)")

    if missing:
        print(f"\n  ⏳ Not yet built: {len(missing)} chapters")
        for m in missing:
            print(f"     — {m}")

    if not found:
        print("❌ No chapter PDFs found. Run build_all.py first.")
        return

    # Set metadata
    writer.add_metadata({
        '/Title':    'TN TET Paper II Science Handbook',
        '/Author':   'ChalkPieceDiary',
        '/Subject':  'TET Paper II Science — Classes 6, 7, 8',
        '/Keywords': 'TET, Tamil Nadu, Science, Handbook, ChalkPieceDiary',
        '/Creator':  'Python ReportLab',
    })

    out_path = os.path.join(out_dir, MASTER_FILENAME)
    with open(out_path, 'wb') as f:
        writer.write(f)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"\n{'═'*50}")
    print(f"📚 Master Handbook: {out_path}")
    print(f"   Chapters: {len(found)} / {len(CHAPTER_ORDER)}")
    print(f"   Pages:    {total_pages}")
    print(f"   Size:     {size_kb:.1f} KB  ({size_kb/1024:.2f} MB)")
    print(f"{'═'*50}")


if __name__ == '__main__':
    combine()
