"""
Convert short grids (≤3 rows, ≤3 cols) into lighter def_list format.

Rules — applied per grid, preserving ALL information:

  • 2-column grid → def_list:
        row [a, b]  →  (a, b)

  • 3-column grid with col3 header in {எடுத்துக்காட்டு, எ.கா, ...}:
        row [a, b, c]  →  (a, "b. <b>எ.கா.</b> c")

  • 3-column grid with col1 header == "அம்சம்" (parallel comparison) — SKIP
    (these compare two parallel concepts and can't flatten without losing structure)

  • Anything else with ≥4 rows or >3 cols — SKIP

Usage:
    python build/convert_short_grids.py [--dry-run]
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters_ta_html"

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

# Header tokens that indicate "this column is an example, not a parallel value"
EXAMPLE_HEADERS = {"எடுத்துக்காட்டு", "எ.கா", "எ.கா.", "உதாரணம்"}

# Skip these col1 patterns — they signal parallel comparison
SKIP_COL1 = {"அம்சம்"}


def get_arg(call, name, pos):
    for kw in call.keywords:
        if kw.arg == name: return kw.value
    if len(call.args) > pos: return call.args[pos]
    return None


def get_str(node) -> str:
    """Concatenate string content of a node (handles BinOp string concat)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    parts = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
            parts.append(sub.value)
    return "".join(parts)


def get_strs(node) -> list[str]:
    if not isinstance(node, ast.List): return []
    return [get_str(elt) for elt in node.elts]


def _esc_py_string(s: str) -> str:
    """Escape a string for safe Python single-quote literal."""
    s = s.replace("\\", "\\\\").replace("'", "\\'")
    # Keep readable for multiline by joining
    s = s.replace("\n", " ").replace("\r", "")
    return s


def grid_to_def_list_source(rows: list[list[str]], col_count: int, col3_is_example: bool, indent: str = "    ") -> str | None:
    """Build def_list(...) source string from grid row data. Returns None if can't convert."""
    items = []
    for row in rows:
        if len(row) < 2:
            return None
        col1 = row[0].strip()
        if col_count == 2:
            defn = row[1].strip()
        elif col_count == 3 and col3_is_example:
            col2 = row[1].strip()
            col3 = row[2].strip()
            defn = f"{col2}. <b>எ.கா.</b> {col3}"
        elif col_count == 3:
            col2 = row[1].strip()
            col3 = row[2].strip()
            defn = f"{col2}. {col3}"
        else:
            return None
        items.append((col1, defn))

    inner = ",\n".join(
        f"{indent}    ('{_esc_py_string(t)}',\n{indent}     '{_esc_py_string(d)}')"
        for t, d in items
    )
    return f"def_list([\n{inner},\n{indent}])"


def find_grid_calls_in_source(src: str) -> list[tuple[int, int, ast.Call]]:
    """Return (start_byte_offset, end_byte_offset, call_node) for f.append(grid(...)) calls."""
    tree = ast.parse(src)
    out = []
    # Find all f.append(grid(...)) statements
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            outer = node.value
            if (isinstance(outer.func, ast.Attribute) and outer.func.attr == "append"
                and len(outer.args) == 1 and isinstance(outer.args[0], ast.Call)):
                inner = outer.args[0]
                if isinstance(inner.func, ast.Name) and inner.func.id == "grid":
                    out.append((node.lineno, node.end_lineno, inner))
    return out


def process_chapter(path: Path, dry_run: bool) -> tuple[int, int]:
    src = path.read_text(encoding="utf-8")
    lines = src.splitlines(keepends=True)

    try:
        calls = find_grid_calls_in_source(src)
    except SyntaxError as e:
        print(f"  SYNTAX ERROR in {path.name}: {e}")
        return 0, 0

    converted = 0
    skipped = 0

    # Process in reverse line order to keep line numbers stable
    for stmt_lineno, stmt_end_lineno, grid_call in reversed(calls):
        h_arg = get_arg(grid_call, "headers", 0)
        r_arg = get_arg(grid_call, "rows", 1)
        if not isinstance(h_arg, ast.List) or not isinstance(r_arg, ast.List):
            continue
        headers = get_strs(h_arg)
        n_cols = len(headers)
        n_rows = len(r_arg.elts)

        if n_rows > 3 or n_cols > 3 or n_cols < 2:
            continue

        col1_header = headers[0].strip() if headers else ""
        if col1_header in SKIP_COL1:
            skipped += 1
            continue

        col3_is_example = (n_cols == 3 and headers[2].strip() in EXAMPLE_HEADERS)
        if n_cols == 3 and not col3_is_example:
            # Conservatively skip — non-example 3rd cols may be parallel
            skipped += 1
            continue

        # Extract row data
        rows_data: list[list[str]] = []
        for row_node in r_arg.elts:
            if isinstance(row_node, ast.List):
                rows_data.append(get_strs(row_node))
        if not rows_data:
            continue

        new_src = grid_to_def_list_source(rows_data, n_cols, col3_is_example)
        if not new_src:
            continue

        # Build the replacement statement: f.append(def_list([...]))
        # Preserve indent of original
        original_first_line = lines[stmt_lineno - 1]
        leading_ws = original_first_line[:len(original_first_line) - len(original_first_line.lstrip())]
        replacement = f"{leading_ws}f.append({new_src})\n"

        if not dry_run:
            # Replace lines [stmt_lineno-1, stmt_end_lineno) with replacement
            new_lines = lines[:stmt_lineno - 1] + [replacement] + lines[stmt_end_lineno:]
            lines = new_lines

        converted += 1
        print(f"    [{path.name.split('_')[0]} L{stmt_lineno:4d}] {n_cols}c×{n_rows}r → def_list  ({headers[0][:25]}...)")

    if converted and not dry_run:
        path.write_text("".join(lines), encoding="utf-8")

    return converted, skipped


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    print(f"Converting short grids → def_list{' (DRY RUN)' if dry_run else ''}:")
    total_conv = total_skip = 0
    for f in sorted(CHAPTERS.glob("*_ta.py")):
        c, s = process_chapter(f, dry_run)
        total_conv += c
        total_skip += s
    print(f"\nConverted: {total_conv}   |   Skipped (parallel comparison): {total_skip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
