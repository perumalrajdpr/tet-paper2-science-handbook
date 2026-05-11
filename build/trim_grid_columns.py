"""
Trim non-essential columns from specific grids.

Each TRIM entry says: "in chapter <cid>, find the grid whose headers contain
all of <signature_substrings>, and remove columns at indices <cols_to_remove>".

Removes from headers, all rows, and col_widths_mm (if present).
Preserves col_widths_mm proportions by redistributing removed widths to
the most relevant remaining column.

Usage:
    python build/trim_grid_columns.py [--dry-run]
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters_ta_html"

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

# Each: (chapter_id, header_signature_strings_to_match, col_indices_to_remove_0based, label)
TRIMS: list[tuple[str, list[str], list[int], str]] = [
    ("C2", ["துகள்", "குறியீடு", "கண்டுபிடித்தவர்", "நிறை"], [2],
     "C2 atomic particles: drop discoverer/year column"),
    ("P1", ["அமைப்பு", "விரிவாக்கம்", "நீளம்", "நிறை", "காலம்"], [5],
     "P1 unit systems: drop type/note column"),
    ("P1", ["முன்னொட்டு", "குறியீடு", "மதிப்பு", "மீட்டருக்கு"], [4],
     "P1 SI prefixes: drop 'per metre' column (derivable)"),
    ("P3", ["அளவை", "கண்டுபிடித்தவர்", "உறை", "கொதி"], [1, 4],
     "P3 temperature scales: drop discoverer + remarks columns"),
    ("P3", ["சாதனம்", "பணி", "முக்கிய அமைப்பு", "கண்டுபிடித்தவர்"], [3],
     "P3 thermal devices: drop discoverer column"),
    ("P2", ["சூழ்நிலை", "விசை", "பரப்பளவு", "அழுத்தம்", "காரணம்"], [4],
     "P2 pressure scenarios: drop reasoning column"),
    ("P2", ["வகை", "பெயர்ச்சி", "CG", "திரும்புமா"], [3],
     "P2 equilibrium: drop yes/no return column"),
    ("C7", ["எண்", "கி/லிட்டர்", "சதவீதம்"], [2],
     "C7 ORS recipe: drop g/L column (% kept)"),
]


def get_arg(call: ast.Call, name: str, pos: int):
    for kw in call.keywords:
        if kw.arg == name: return kw, "kw"
    if len(call.args) > pos: return call.args[pos], "pos"
    return None, None


def strs_of_list(node: ast.List) -> list[str]:
    out = []
    for elt in node.elts:
        if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
            out.append(elt.value)
        else:
            parts = [s.value for s in ast.walk(elt)
                     if isinstance(s, ast.Constant) and isinstance(s.value, str)]
            out.append("".join(parts))
    return out


def find_target_grid(tree: ast.Module, sig: list[str]) -> ast.Call | None:
    """Find first grid() Call whose headers contain all signature substrings."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "grid":
            h_node, _ = get_arg(node, "headers", 0)
            h_value = h_node.value if h_node and hasattr(h_node, "value") and isinstance(h_node, ast.keyword) else h_node
            if not isinstance(h_value, ast.List):
                continue
            headers = strs_of_list(h_value)
            joined = " || ".join(headers)
            if all(s in joined for s in sig):
                return node
    return None


def get_node_segment(src: str, node) -> str:
    return ast.get_source_segment(src, node)


def trim_grid_in_source(src: str, grid_call: ast.Call, cols_to_remove: list[int]) -> tuple[str, dict] | None:
    """Return (new_source, info) with the specified column indices removed
    from headers, rows, and col_widths_mm of the given grid Call. Operates
    by reading the original Call's source segment, parsing it, modifying
    AST literals, and unparsing."""
    seg = ast.get_source_segment(src, grid_call)
    if seg is None:
        return None

    # Re-parse the segment to get a clean tree we can manipulate
    parsed = ast.parse(seg, mode="eval")
    call_node = parsed.body
    if not isinstance(call_node, ast.Call):
        return None

    info = {"trimmed_headers": []}

    def trim_list(list_node: ast.List, dropped_collector: list = None) -> None:
        new_elts = []
        for i, elt in enumerate(list_node.elts):
            if i in cols_to_remove:
                if dropped_collector is not None and isinstance(elt, ast.Constant):
                    dropped_collector.append(elt.value)
                continue
            new_elts.append(elt)
        list_node.elts = new_elts

    # Find headers / rows / col_widths_mm by keyword first, then positional
    h_node = r_node = w_node = None
    for kw in call_node.keywords:
        if kw.arg == "headers": h_node = kw.value
        elif kw.arg == "rows": r_node = kw.value
        elif kw.arg == "col_widths_mm": w_node = kw.value
    args = call_node.args
    if h_node is None and len(args) >= 1: h_node = args[0]
    if r_node is None and len(args) >= 2: r_node = args[1]
    if w_node is None and len(args) >= 3: w_node = args[2]

    if not isinstance(h_node, ast.List):
        return None

    dropped_headers: list[str] = []
    trim_list(h_node, dropped_headers)
    info["trimmed_headers"] = dropped_headers

    if isinstance(r_node, ast.List):
        for row_elt in r_node.elts:
            if isinstance(row_elt, ast.List):
                trim_list(row_elt)

    if isinstance(w_node, ast.List):
        # Capture removed widths total to redistribute (proportionally)
        removed_total = 0.0
        keep = []
        for i, elt in enumerate(w_node.elts):
            if isinstance(elt, ast.Constant) and isinstance(elt.value, (int, float)):
                if i in cols_to_remove:
                    removed_total += float(elt.value)
                else:
                    keep.append(elt)
            else:
                if i not in cols_to_remove:
                    keep.append(elt)
        w_node.elts = keep
        # Add removed_total to the LAST remaining column proportionally
        if removed_total and keep:
            kept_widths = [e.value for e in keep if isinstance(e, ast.Constant)
                          and isinstance(e.value, (int, float))]
            if kept_widths:
                kept_sum = sum(kept_widths)
                for i, elt in enumerate(keep):
                    if isinstance(elt, ast.Constant) and isinstance(elt.value, (int, float)):
                        share = elt.value / kept_sum * removed_total
                        elt.value = round(elt.value + share, 1)

    new_seg = ast.unparse(call_node)
    # Replace the segment in src
    new_src = src.replace(seg, new_seg, 1)
    return new_src, info


def process_chapter(path: Path, trims_for_cid: list[tuple], dry_run: bool) -> int:
    src = path.read_text(encoding="utf-8")
    applied = 0
    for sig, cols, label in trims_for_cid:
        try:
            tree = ast.parse(src)
        except SyntaxError as e:
            print(f"  SYNTAX ERROR in {path.name}: {e}")
            return applied

        target = find_target_grid(tree, sig)
        if target is None:
            print(f"  ⚠  not found: {label}")
            continue

        result = trim_grid_in_source(src, target, cols)
        if result is None:
            print(f"  ⚠  could not trim: {label}")
            continue
        new_src, info = result
        if not dry_run:
            src = new_src
        applied += 1
        dropped = " + ".join(info["trimmed_headers"]) or "(unnamed cols)"
        print(f"  ✓  {label}  [dropped: {dropped[:50]}]")

    if applied and not dry_run:
        path.write_text(src, encoding="utf-8")
    return applied


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    by_cid: dict[str, list] = {}
    for cid, sig, cols, label in TRIMS:
        by_cid.setdefault(cid, []).append((sig, cols, label))
    total = 0
    print(f"Trimming low-value columns from wide grids{' (DRY RUN)' if dry_run else ''}:\n")
    for cid, trims in by_cid.items():
        files = list(CHAPTERS.glob(f"{cid}_*.py"))
        if not files:
            print(f"  no source for {cid}")
            continue
        print(f"[{cid}]")
        n = process_chapter(files[0], trims, dry_run)
        total += n
        print()
    print(f"Total trims: {total}/{len(TRIMS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
