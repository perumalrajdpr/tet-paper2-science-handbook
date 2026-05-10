"""
Build an integrated Tamil color handbook PDF.

Usage:
    python build/build_tamil_color_book.py
    python build/build_tamil_color_book.py P1 P2 C1
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.build_tamil_print_bw_book import DEFAULT_CHAPTERS, build_book

ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = ROOT / "release" / "color"


def main() -> int:
    requested = [x.upper() for x in sys.argv[1:]] if len(sys.argv) > 1 else DEFAULT_CHAPTERS
    try:
        out_pdf, out_html = build_book(
            requested,
            out_dir="output_ta_color",
            profile="color",
        )
        size_kb = out_pdf.stat().st_size / 1024
        print(f"Built integrated color book: {out_pdf} ({size_kb:.1f} KB)")
        print(f"HTML source: {out_html}")

        RELEASE_DIR.mkdir(parents=True, exist_ok=True)
        release_pdf = RELEASE_DIR / out_pdf.name
        shutil.copy2(out_pdf, release_pdf)
        print(f"\n>>> FINAL RELEASE PDF: {release_pdf}")
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
