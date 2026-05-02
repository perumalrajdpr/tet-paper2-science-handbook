"""
Build all 22 chapters sequentially.

Usage:
    python build/build_all.py

Output: output/P1_Measurement.pdf, output/P2_*.pdf, ... (22 files)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from build.build_chapter import build, CHAPTERS


def build_all(out_dir='output'):
    order = [
        'P1','P2','P3','P4','P5','P6','P7','P8',  # Physics
        'C1','C2','C3','C4','C5','C6','C7',         # Chemistry
        'B1','B2','B3','B4','B5','B6','B7',         # Biology
    ]
    success, skipped, failed = [], [], []

    for cid in order:
        try:
            build(cid, out_dir)
            success.append(cid)
        except SystemExit:
            skipped.append(cid)
        except Exception as e:
            print(f"❌ {cid} failed: {e}")
            failed.append(cid)

    print(f"\n{'═'*50}")
    print(f"✅ Built:   {len(success):2d} chapters  →  {', '.join(success)}")
    if skipped:
        print(f"⏳ Pending: {len(skipped):2d} chapters  →  {', '.join(skipped)}")
    if failed:
        print(f"❌ Failed:  {len(failed):2d} chapters  →  {', '.join(failed)}")
    print(f"{'═'*50}")


if __name__ == '__main__':
    build_all()
