"""
Build a single Tamil HTML chapter PDF (WeasyPrint).

Usage:
    python build/build_tamil_chapter.py P1
"""

import importlib
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"


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


def _bootstrap_windows_gtk():
    """Make GTK DLLs discoverable for WeasyPrint on Windows."""
    if os.name != "nt":
        return
    candidates = [
        Path(r"C:\msys64\mingw64\bin"),
        Path(r"C:\msys64\ucrt64\bin"),
    ]
    for dll_dir in candidates:
        if not dll_dir.exists():
            continue
        os.environ["PATH"] = f"{dll_dir};{os.environ.get('PATH', '')}"
        if hasattr(os, "add_dll_directory"):
            try:
                os.add_dll_directory(str(dll_dir))
            except OSError:
                continue


def build(chapter_id: str, out_dir: str = "output_ta"):
    chapter_id = chapter_id.upper()
    chapters = discover_tamil_chapters()
    if chapter_id not in chapters:
        print(f"ERROR: Unknown Tamil chapter: {chapter_id}")
        print(f"Valid IDs: {', '.join(sorted(chapters.keys()))}")
        sys.exit(1)

    module_name, stem = chapters[chapter_id]
    filename = f"{stem}.pdf"
    out_path = os.path.join(out_dir, filename)
    os.makedirs(out_dir, exist_ok=True)

    print(f"Building Tamil {chapter_id} -> {out_path}")
    _bootstrap_windows_gtk()
    try:
        mod = importlib.import_module(module_name)
    except (ModuleNotFoundError, OSError) as exc:
        print("\nTamil HTML build stack is not fully available on this machine.")
        print("Install WeasyPrint runtime dependencies and retry.")
        print("Guide: docs/tamil/weasyprint_windows_setup.md\n")
        raise exc
    if hasattr(mod, "build"):
        mod.build(out_path)
    elif hasattr(mod, "build_pdf"):
        mod.build_pdf(out_path)
    else:
        raise AttributeError(
            f"Module '{module_name}' has neither build() nor build_pdf()"
        )

    if os.path.exists(out_path):
        size_kb = os.path.getsize(out_path) / 1024
        print(f"Done -> {out_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    chapters = discover_tamil_chapters()
    if len(sys.argv) < 2:
        print("Usage: python build/build_tamil_chapter.py <CHAPTER_ID>")
        print(f"Chapters: {', '.join(sorted(chapters.keys()))}")
        sys.exit(1)
    build(sys.argv[1])
