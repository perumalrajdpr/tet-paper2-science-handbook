"""
Bulk-bump body-content font sizes to a uniform 10.5pt minimum.

Rules:
  - Find every `font-size: <N>pt` declaration
  - If N is between 9.0 and 10.4, bump to 10.5pt
  - SKIP rules belonging to peripheral chrome:
      @page, @top-*, @bottom-*, .footer, .instruction-num,
      .copyright-note, .cover-footer-strip, .back-footer-strip,
      .cv-exam-sub, .cover-band, .back-tag, .foreword-signoff
  - SKIP rules with `th { font-size: < 9pt }` (overrides too aggressive)
  - SKIP table headers that are intentionally compact (table.kv/grid/rapid th < 9pt)

Usage:
    python build/bulk_font_bump.py [--dry-run]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass

ROOT = Path(__file__).resolve().parent.parent
TARGETS = [
    ROOT / "shared" / "css" / "handbook_ta_print_bw.css",
    ROOT / "shared" / "css" / "handbook_ta_color_book.css",
]

MIN_PT = 10.5

# Skip selectors (matched against the current CSS context — selector line)
SKIP_PATTERNS = [
    "@top-", "@bottom-", "@page",
    ".footer", ".instruction-num", ".copyright-note",
    ".cover-footer-strip", ".back-footer-strip",
    ".cv-exam-sub", ".cover-band", ".back-tag", ".foreword-signoff",
    ".pillinline", ".small", ".caption",
]


def _find_selector_context(lines: list[str], line_idx: int) -> str:
    """Walk backwards from line_idx to find the most recent selector line."""
    for j in range(line_idx, max(-1, line_idx - 30), -1):
        ln = lines[j]
        # selector line typically ends with { or has { on the line
        if "{" in ln:
            # take everything before { as selector
            sel = ln.split("{")[0]
            # might span multiple lines (comma-separated)
            extras = []
            for k in range(j - 1, max(-1, j - 5), -1):
                pk = lines[k].rstrip()
                if pk.endswith(",") or pk.endswith("{"):
                    extras.insert(0, lines[k].split("{")[0])
                else:
                    break
            return " ".join(extras + [sel]).strip()
    return ""


def should_skip(selector: str) -> bool:
    for pat in SKIP_PATTERNS:
        if pat in selector:
            return True
    return False


def process_file(path: Path, dry_run: bool) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    pattern = re.compile(r"(font-size:\s*)([0-9]+(?:\.[0-9]+)?)pt")
    changes = 0

    for i, line in enumerate(lines):
        m = pattern.search(line)
        if not m: continue
        pt = float(m.group(2))
        if pt >= MIN_PT or pt < 9.0:
            continue
        selector = _find_selector_context(lines, i)
        if should_skip(selector):
            continue
        new_line = pattern.sub(f"\\g<1>{MIN_PT}pt", line, count=1)
        lines[i] = new_line
        changes += 1
        print(f"  {path.name} L{i+1}: {pt}pt → {MIN_PT}pt  ({selector[:60]})")

    if changes and not dry_run:
        path.write_text("".join(lines), encoding="utf-8")
    return changes


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    total = 0
    print(f"Bulk font bump to {MIN_PT}pt minimum{' (DRY RUN)' if dry_run else ''}:\n")
    for p in TARGETS:
        n = process_file(p, dry_run)
        print(f"  → {p.name}: {n} changes\n")
        total += n
    print(f"Total: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
