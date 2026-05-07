"""
Build an integrated Tamil color handbook PDF.

Usage:
    python build/build_tamil_color_book.py
    python build/build_tamil_color_book.py P1 P2 C1
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.build_tamil_print_bw_book import DEFAULT_CHAPTERS, build_book


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
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
