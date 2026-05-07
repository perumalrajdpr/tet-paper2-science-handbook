"""
Build print-ready Tamil handbook PDFs (black & white profile).

Profile goals:
- Page size: 210mm x 290mm
- Margins: 20mm
- Grayscale, press-friendly styling
- Space-efficient layout for student study + print economy

Usage:
    python build/build_tamil_print_bw.py P1
    python build/build_tamil_print_bw.py ALL
"""

from __future__ import annotations

import importlib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.builders.html_builders import assemble_html

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"
PRINT_CSS_REL = "shared/css/handbook_ta_print_bw.css"
PRINT_SCALE = 170.0 / 174.0


def _load_weasyprint_html():
    """
    Import WeasyPrint HTML with Windows DLL bootstrapping.
    Keeps the script runnable without globally editing PATH.
    """
    if os.name == "nt":
        dll_candidates = [
            Path(r"C:\msys64\mingw64\bin"),
            Path(r"C:\msys64\ucrt64\bin"),
        ]
        for dll_dir in dll_candidates:
            if not dll_dir.exists():
                continue
            os.environ["PATH"] = f"{dll_dir};{os.environ.get('PATH', '')}"
            if hasattr(os, "add_dll_directory"):
                try:
                    os.add_dll_directory(str(dll_dir))
                except OSError:
                    # Skip unusable directories and try next candidate.
                    continue
    from weasyprint import HTML  # pylint: disable=import-outside-toplevel

    return HTML


def discover_tamil_chapters() -> dict[str, tuple[str, str]]:
    """
    Return chapter map:
      chapter_id -> (python_module_name, base_filename_without_extension)
    """
    chapter_map: dict[str, tuple[str, str]] = {}
    for path in sorted(CHAPTERS_DIR.glob("*_ta.py")):
        if path.name == "__init__.py":
            continue
        stem = path.stem
        chapter_id = stem.split("_", 1)[0].upper()
        module_name = f"chapters_ta_html.{stem}"
        chapter_map[chapter_id] = (module_name, stem)
    return chapter_map


def _scale_inline_mm_widths(html: str, scale: float) -> str:
    """
    Scale inline width/max-width mm values inside generated HTML.
    This adapts legacy 174mm table widths to 170mm print area.
    """
    pattern = re.compile(r"(?P<k>max-width|width)\s*:\s*(?P<v>\d+(?:\.\d+)?)mm")

    def repl(match: re.Match[str]) -> str:
        key = match.group("k")
        value = float(match.group("v"))
        scaled = value * scale
        text = f"{scaled:.2f}".rstrip("0").rstrip(".")
        return f"{key}:{text}mm"

    return pattern.sub(repl, html)


def build_print_bw(chapter_id: str, out_dir: str = "output_ta_print_bw", write_html: bool = True) -> tuple[Path, Path | None]:
    chapter_id = chapter_id.upper()
    chapters = discover_tamil_chapters()
    if chapter_id not in chapters:
        valid = ", ".join(sorted(chapters.keys()))
        raise ValueError(f"Unknown chapter '{chapter_id}'. Valid IDs: {valid}")

    module_name, stem = chapters[chapter_id]
    mod = importlib.import_module(module_name)

    if not hasattr(mod, "content"):
        raise AttributeError(f"{module_name} does not expose content()")
    if not hasattr(mod, "CHAPTER_ID") or not hasattr(mod, "CHAPTER_TITLE"):
        raise AttributeError(f"{module_name} is missing CHAPTER_ID/CHAPTER_TITLE")

    fragments = mod.content()
    html = assemble_html(
        title=f"{mod.CHAPTER_ID} · {mod.CHAPTER_TITLE}",
        css_path=PRINT_CSS_REL,
        body_fragments=fragments,
    )
    html = _scale_inline_mm_widths(html, PRINT_SCALE)

    out_path = ROOT / out_dir
    out_path.mkdir(parents=True, exist_ok=True)

    out_pdf = out_path / f"{stem}_print_bw.pdf"
    out_html = out_path / f"{stem}_print_bw.html" if write_html else None

    if out_html is not None:
        out_html.write_text(html, encoding="utf-8")

    HTML = _load_weasyprint_html()
    HTML(string=html, base_url=str(ROOT)).write_pdf(
        str(out_pdf),
        optimize_size=(),  # keep stable glyph rendering behavior
    )
    return out_pdf, out_html


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python build/build_tamil_print_bw.py <CHAPTER_ID|ALL>")
        print(f"Chapters: {', '.join(sorted(discover_tamil_chapters().keys()))}")
        return 1

    target = sys.argv[1].upper()
    chapters = discover_tamil_chapters()
    if not chapters:
        print("No Tamil chapter files found in chapters_ta_html/")
        return 1

    try:
        if target == "ALL":
            for chapter_id in sorted(chapters.keys()):
                out_pdf, _ = build_print_bw(chapter_id)
                size_kb = out_pdf.stat().st_size / 1024
                print(f"Built {chapter_id}: {out_pdf} ({size_kb:.1f} KB)")
        else:
            out_pdf, _ = build_print_bw(target)
            size_kb = out_pdf.stat().st_size / 1024
            print(f"Built {target}: {out_pdf} ({size_kb:.1f} KB)")
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
