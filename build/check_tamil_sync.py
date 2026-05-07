"""
Quick sync checker for Tamil chapter coverage.

Validates which expected chapter IDs are currently available in chapters_ta_html.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"

EXPECTED = {
    "P": [f"P{i}" for i in range(1, 9)],
    "C": [f"C{i}" for i in range(1, 8)],
    "B": [f"B{i}" for i in range(1, 8)],
}


def _available_ids() -> set[str]:
    ids: set[str] = set()
    for path in CHAPTERS_DIR.glob("*_ta.py"):
        if path.name == "__init__.py":
            continue
        ids.add(path.stem.split("_", 1)[0].upper())
    return ids


def main() -> int:
    available = _available_ids()
    missing_total: list[str] = []
    print("Tamil chapter sync status:")
    for subject, expected_ids in EXPECTED.items():
        missing = [cid for cid in expected_ids if cid not in available]
        present = [cid for cid in expected_ids if cid in available]
        missing_total.extend(missing)
        print(f"- {subject}: {len(present)}/{len(expected_ids)} present")
        if missing:
            print(f"  missing -> {', '.join(missing)}")
    if missing_total:
        return 1
    print("All expected Tamil chapter IDs are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
