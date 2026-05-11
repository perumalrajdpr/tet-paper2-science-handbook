"""
Remove non-essential comparison rows from each chapter's
"3 · ஒப்பிடுக, வேறுபடுத்துக" grid section.

Uses AST to locate the grid() call that follows the subh('3 · ஒப்பிடுக...') call,
identifies rows whose first two string columns match the REMOVE_PAIRS set
(per chapter), and physically deletes those source lines.

Usage:
    python build/prune_compare_rows.py [--dry-run]
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

# Force UTF-8 stdout for Tamil output on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters_ta_html"

# (chapter_id, term1_substring, term2_substring) — match by substring
# of the first two cells (case- and whitespace-insensitive).
# Substrings should be Tamil-only (English-in-parens stripped during match).
REMOVE_PAIRS: list[tuple[str, str, str]] = [
    # C1
    ("C1", "திண்மம்", "திரவம்"),
    ("C1", "விரிவடைதல்", "நிலை மாற்றம்"),
    # P1
    ("P1", "FPS", "மெட்ரிக்"),
    ("P1", "திட்ட அளவு", "படித்தர அலகு"),
    ("P1", "குவார்ட்ஸ்", "அணு கடிகாரம்"),
    ("P1", "GMT", "IST"),
    # P2
    ("P2", "நிறை", "எடை"),
    ("P2", "பரப்பு இழுவிசை", "பாகுநிலை"),
    # P3
    ("P3", "கலோரி", "ஜூல்"),
    ("P3", "மருத்துவ", "ஆய்வக"),
    ("P3", "கலோரிமீட்டர்", "தெர்மோஸ்டேட்"),
    ("P3", "நல்ல கடத்தி", "நல்ல தடுப்பான்"),
    # P4
    ("P4", "கலைடாஸ்கோப்", "பெரிஸ்கோப்"),
    ("P4", "ஒளி ஊடுருவும்", "பகுதி ஊடுருவும்"),
    # P5
    ("P5", "மின் உருகி", "MCB"),
    ("P5", "நிக்ரோம்", "டங்ஸ்டன்"),
    # P6
    ("P6", "காந்தவியல் கடினம்", "மென்"),
    ("P6", "சீரான", "சீரற்ற காந்தப்புலம்"),
    ("P6", "கவரும்", "திசை சார்ந்த"),
    ("P6", "கூலூம்", "காஸ்"),
    # P7
    ("P7", "இசை", "இரைச்சல்"),
    ("P7", "ஆண்", "பெண் குரல்"),
    # P8
    ("P8", "திரவ", "திண்ம இயக்குப்பொருள்"),
    ("P8", "கிரையோஜெனிக்", "வழக்கமான"),
    ("P8", "அப்போலோ-8", "அப்போலோ-11"),
    ("P8", "Lander", "Rover"),
    ("P8", "ISRO", "NASA"),
    ("P8", "கல்பனா", "சுனிதா"),
]


def _strip(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _string_value(node) -> str:
    """Return the concatenated string value of a Constant or implicit-concat string."""
    parts = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
            parts.append(sub.value)
    return _strip(" ".join(parts))


def find_compare_rows_lists(tree: ast.Module) -> list[ast.List]:
    """Find the rows-list (List node) inside the one_liners() / grid() call that
    follows a subh('3 · ஒப்பிடுக...') call. Returns list of List nodes."""
    out: list[ast.List] = []
    found_subh = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "subh" and node.args:
                txt = _string_value(node.args[0])
                if "ஒப்பிடுக" in txt and "வேறுபடுத்துக" in txt:
                    found_subh = True
                    continue
            if found_subh and node.func.id in ("one_liners", "grid") and node.args:
                # one_liners(rows) — rows is first arg
                # grid(headers, rows) — rows is second arg
                rows_arg = node.args[0] if node.func.id == "one_liners" else (
                    node.args[1] if len(node.args) >= 2 else None
                )
                if isinstance(rows_arg, ast.List):
                    out.append(rows_arg)
                    found_subh = False
    return out


def prune_chapter(path: Path, pairs_for_chapter: list[tuple[str, str]], dry_run: bool) -> int:
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        print(f"  SYNTAX ERROR in {path.name}: {e}")
        return 0

    rows_lists = find_compare_rows_lists(tree)
    if not rows_lists:
        return 0

    lines = src.splitlines(keepends=True)
    removed = 0

    for rows_list in rows_lists:
        for row in rows_list.elts:
            # Each row may be a Tuple (one_liners) or List (grid)
            if not isinstance(row, (ast.Tuple, ast.List)) or len(row.elts) < 1:
                continue
            # one_liners format: (title, content) — title contains "X vs Y"
            # grid format: [col1, col2, ...] — cols separate
            title = _string_value(row.elts[0])
            second = _string_value(row.elts[1]) if len(row.elts) >= 2 else ""
            search_text = f"{title} || {second}"
            for t1, t2 in pairs_for_chapter:
                if t1 in search_text and t2 in search_text:
                    start = row.lineno - 1
                    end = row.end_lineno
                    if not dry_run:
                        for i in range(start, end):
                            lines[i] = ""
                    print(f"    [{path.name.split('_')[0]}] removing: {title[:50]}")
                    removed += 1
                    break

    if removed and not dry_run:
        path.write_text("".join(lines), encoding="utf-8")
    return removed


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    by_cid: dict[str, list[tuple[str, str]]] = {}
    for cid, t1, t2 in REMOVE_PAIRS:
        by_cid.setdefault(cid, []).append((t1, t2))

    total_removed = 0
    print(f"Pruning compare-section rows{' (DRY RUN)' if dry_run else ''}:")
    for cid, pairs in by_cid.items():
        matches = list(CHAPTERS.glob(f"{cid}_*.py"))
        if not matches:
            print(f"  WARNING: no source for {cid}")
            continue
        n = prune_chapter(matches[0], pairs, dry_run)
        total_removed += n
    print(f"\nTotal rows removed: {total_removed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
