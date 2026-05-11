"""
Cross-chapter redundancy checker for the Tamil science textbook.

Walks chapters_ta_html/*.py and extracts:
  - Definition terms (first arg of (term, defn) tuples in def_list / kv_list)
  - Section / sub-section headers (sec, subh)
  - Years (4-digit, 1500-2100 range)
  - Scientist / proper-noun mentions (Tamil + English-in-parens pattern)

Then builds inverted indexes (item -> chapters) and writes a markdown report
to docs/redundancy_report.md highlighting items that appear in 2+ chapters.

Usage:
    python build/check_redundancy.py
"""

from __future__ import annotations

import ast
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"
OUT_PATH = ROOT / "docs" / "redundancy_report.md"

CHAPTER_ORDER = [
    "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
]


def _normalize(text: str) -> str:
    """Strip HTML tags, collapse whitespace, lowercase ASCII."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _term_key(text: str) -> str:
    """Canonical key for a definition term: Tamil only (drop trailing English-in-parens)."""
    text = _normalize(text)
    # Strip "(English)" suffix
    text = re.sub(r"\s*\([^)]*\)\s*$", "", text).strip()
    return text


def _extract_strings_from_node(node) -> list[str]:
    """Collect all string literals inside an ast node."""
    out = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
            out.append(sub.value)
        elif isinstance(sub, ast.JoinedStr):
            for v in sub.values:
                if isinstance(v, ast.Constant) and isinstance(v.value, str):
                    out.append(v.value)
    return out


def parse_chapter(path: Path) -> dict:
    """Extract redundancy-relevant items from one chapter file."""
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"defs": [], "secs": [], "subhs": [], "years": [], "names": []}

    defs: list[str] = []
    secs: list[str] = []
    subhs: list[str] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name):
            continue
        fname = node.func.id

        if fname == "sec" and node.args:
            s = _extract_strings_from_node(node.args[0])
            if s:
                secs.append(_normalize(" ".join(s)))
        elif fname == "subh" and node.args:
            s = _extract_strings_from_node(node.args[0])
            if s:
                subhs.append(_normalize(" ".join(s)))
        elif fname in ("def_list", "kv_list") and node.args:
            arg = node.args[0]
            if isinstance(arg, ast.List):
                for elt in arg.elts:
                    if isinstance(elt, ast.Tuple) and elt.elts:
                        first = elt.elts[0]
                        s = _extract_strings_from_node(first)
                        if s:
                            term = _normalize(" ".join(s))
                            if term:
                                defs.append(term)

    # Year & name extraction from raw source (string literals only)
    year_pattern = re.compile(r"\b(1[5-9]\d{2}|20\d{2})\b")
    years = year_pattern.findall(src)

    # Scientist/proper-noun pattern: Tamil word + "(English)" e.g. "ஆர்கிமிடிஸ் (Archimedes)"
    name_pattern = re.compile(
        r"([஀-௿][஀-௿\s]{2,}?)\s*\(\s*([A-Z][A-Za-z\s.\-]{2,})\s*\)"
    )
    names = []
    for m in name_pattern.finditer(src):
        ta = _normalize(m.group(1))
        en = _normalize(m.group(2))
        # Filter common non-name capitals (e.g. "Note", "Example")
        skip = {"Measurement", "Unit", "Quantity", "Note", "Example", "Definition",
                "Important", "Standard", "Numerical", "Atomic", "Molecule",
                "Cell", "Force", "Motion", "Energy", "Heat", "Temperature",
                "Light", "Sound", "Magnetism", "Electricity", "Universe",
                "Matter", "Air", "Water", "Element", "Compound", "Solution",
                "Acid", "Base", "Salt", "Plant", "Animal", "Microbe",
                "Health", "Crop", "Environment", "Ecology", "Chemistry",
                "Physics", "Biology", "Science", "System", "Property"}
        if any(en.startswith(s) for s in skip):
            continue
        if len(en) > 2 and len(ta) > 2:
            # Heuristic: typical scientist names are 1-3 words
            if 1 <= len(en.split()) <= 4:
                names.append(f"{en} ({ta})")

    return {
        "defs": list(dict.fromkeys(defs)),       # de-dup within chapter
        "secs": list(dict.fromkeys(secs)),
        "subhs": list(dict.fromkeys(subhs)),
        "years": sorted(set(years)),
        "names": list(dict.fromkeys(names)),
    }


def build_index(by_chapter: dict[str, dict]) -> dict[str, dict[str, set]]:
    """Inverted index: category -> item -> set of chapter ids."""
    idx = {
        "defs": defaultdict(set),
        "secs": defaultdict(set),
        "subhs": defaultdict(set),
        "years": defaultdict(set),
        "names": defaultdict(set),
    }
    for cid, data in by_chapter.items():
        for term in data["defs"]:
            idx["defs"][_term_key(term)].add(cid)
        for h in data["secs"]:
            idx["secs"][_term_key(h)].add(cid)
        for h in data["subhs"]:
            idx["subhs"][_term_key(h)].add(cid)
        for y in data["years"]:
            idx["years"][y].add(cid)
        for n in data["names"]:
            idx["names"][n].add(cid)
    return idx


def write_report(by_chapter: dict[str, dict], idx: dict) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append("# Cross-chapter Redundancy Report")
    lines.append("")
    lines.append(
        "Generated by `build/check_redundancy.py`. Items appearing in **2 or more chapters** "
        "are listed below — review and decide: keep as strategic repetition, "
        "consolidate to primary chapter, or cross-reference."
    )
    lines.append("")

    # --- Per-chapter summary
    lines.append("## Per-chapter counts")
    lines.append("")
    lines.append("| Chapter | Definitions | Sections | Sub-headers | Years | Names |")
    lines.append("|---|---|---|---|---|---|")
    for cid in CHAPTER_ORDER:
        if cid not in by_chapter:
            continue
        d = by_chapter[cid]
        lines.append(
            f"| {cid} | {len(d['defs'])} | {len(d['secs'])} | "
            f"{len(d['subhs'])} | {len(d['years'])} | {len(d['names'])} |"
        )
    lines.append("")

    def _section(title: str, key: str, threshold: int = 2) -> None:
        items = [(t, sorted(c)) for t, c in idx[key].items() if len(c) >= threshold]
        items.sort(key=lambda x: (-len(x[1]), x[0]))
        lines.append(f"## {title} ({len(items)} duplicated)")
        lines.append("")
        if not items:
            lines.append("_No duplicates found._")
            lines.append("")
            return
        lines.append("| Item | # | Chapters |")
        lines.append("|---|---|---|")
        for term, chs in items:
            lines.append(f"| {term} | {len(chs)} | {', '.join(chs)} |")
        lines.append("")

    _section("Definitions repeated", "defs")
    _section("Section headers repeated", "secs")
    _section("Sub-headers repeated", "subhs")
    _section("Years referenced in multiple chapters", "years", threshold=2)
    _section("Scientist / proper-noun mentions", "names", threshold=2)

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written: {OUT_PATH}")


def main() -> int:
    by_chapter: dict[str, dict] = {}
    for cid in CHAPTER_ORDER:
        # find file matching <cid>_*.py
        matches = list(CHAPTERS_DIR.glob(f"{cid}_*.py"))
        if not matches:
            print(f"WARNING: no source file for {cid}", file=sys.stderr)
            continue
        by_chapter[cid] = parse_chapter(matches[0])

    idx = build_index(by_chapter)
    write_report(by_chapter, idx)

    # Print summary stats
    for cat in ("defs", "secs", "subhs", "names"):
        dup = sum(1 for v in idx[cat].values() if len(v) >= 2)
        total = len(idx[cat])
        print(f"  {cat}: {dup}/{total} appear in 2+ chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
