"""
Build WordPress-friendly HTML output from Tamil chapters.

Outputs:
- output_ta_web/Tamil_Science_<SPAN>_wordpress_bundle.html
- output_ta_web/chapters/<CHAPTER_ID>.html (chapter fragments)
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.build_tamil_print_bw_book import DEFAULT_CHAPTERS

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"
WEB_CSS_REL = "shared/css/handbook_ta_web.css"


def discover_tamil_chapters() -> dict[str, tuple[str, str]]:
    chapter_map: dict[str, tuple[str, str]] = {}
    for path in sorted(CHAPTERS_DIR.glob("*_ta.py")):
        if path.name == "__init__.py":
            continue
        stem = path.stem
        chapter_id = stem.split("_", 1)[0].upper()
        chapter_map[chapter_id] = (f"chapters_ta_html.{stem}", stem)
    return chapter_map


def _subject_class(chapter_id: str) -> str:
    prefix = chapter_id[:1].upper()
    if prefix == "P":
        return "subject-p"
    if prefix == "C":
        return "subject-c"
    if prefix == "B":
        return "subject-b"
    return "subject-generic"


def _chapter_span_label(chapter_ids: list[str]) -> str:
    if not chapter_ids:
        return "BOOK"
    if len(chapter_ids) == 1:
        return chapter_ids[0]
    return f"{chapter_ids[0]}_{chapter_ids[-1]}"


def build_wordpress_bundle(
    chapter_ids: list[str] | None = None,
    out_dir: str = "output_ta_web",
) -> tuple[Path, Path]:
    chapter_ids = [c.upper() for c in (chapter_ids or DEFAULT_CHAPTERS)]
    chapter_map = discover_tamil_chapters()
    out_path = ROOT / out_dir
    chapter_out_dir = out_path / "chapters"
    out_path.mkdir(parents=True, exist_ok=True)
    chapter_out_dir.mkdir(parents=True, exist_ok=True)

    chapter_sections: list[str] = []
    for chapter_id in chapter_ids:
        if chapter_id not in chapter_map:
            valid = ", ".join(sorted(chapter_map.keys()))
            raise ValueError(f"Unsupported chapter ID: {chapter_id}. Valid IDs: {valid}")
        module_name, _stem = chapter_map[chapter_id]
        mod = importlib.import_module(module_name)
        title = getattr(mod, "CHAPTER_TITLE", chapter_id)
        body = "".join(mod.content())
        section = (
            f'<section class="wp-chapter {_subject_class(chapter_id)}" id="chapter-{chapter_id.lower()}">\n'
            f'  <h2 class="wp-chapter-title">{chapter_id} · {title}</h2>\n'
            f"{body}\n"
            "</section>\n"
        )
        chapter_sections.append(section)
        (chapter_out_dir / f"{chapter_id}.html").write_text(section, encoding="utf-8")

    span = _chapter_span_label(chapter_ids)
    bundle = (
        "<!DOCTYPE html>\n"
        '<html lang="ta">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        f'  <title>Tamil Science WordPress Bundle ({span})</title>\n'
        f'  <link rel="stylesheet" href="{WEB_CSS_REL}">\n'
        "</head>\n"
        "<body>\n"
        f'  <h1 class="wp-book-title">Tamil Science Handbook — WordPress Bundle ({span})</h1>\n'
        f"{''.join(chapter_sections)}"
        "</body>\n"
        "</html>\n"
    )
    out_html = out_path / f"Tamil_Science_{span}_wordpress_bundle.html"
    out_fragment = out_path / f"Tamil_Science_{span}_wordpress_fragment.html"
    out_html.write_text(bundle, encoding="utf-8")
    out_fragment.write_text("".join(chapter_sections), encoding="utf-8")
    return out_html, out_fragment


def main() -> int:
    requested = [x.upper() for x in sys.argv[1:]] if len(sys.argv) > 1 else DEFAULT_CHAPTERS
    try:
        out_html, out_fragment = build_wordpress_bundle(requested)
        print(f"Built WordPress bundle: {out_html}")
        print(f"Built WordPress fragment: {out_fragment}")

        import shutil
        release_dir = ROOT / "release" / "web"
        release_dir.mkdir(parents=True, exist_ok=True)
        for src in (out_html, out_fragment):
            shutil.copy2(src, release_dir / src.name)
        print(f"\n>>> FINAL RELEASE BUNDLE: {release_dir}")
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
