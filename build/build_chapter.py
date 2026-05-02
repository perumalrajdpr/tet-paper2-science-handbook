"""
Build a single chapter PDF.

Usage:
    python build/build_chapter.py P1
    python build/build_chapter.py C3
    python build/build_chapter.py B1

Output: output/P1_Measurement.pdf  (etc.)
"""

import sys
import os
import importlib

# Make sure project root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.theme import register_fonts

# ── Chapter registry ──────────────────────────────────────────────────────────
# Maps chapter_id → (module_name, output_filename)
CHAPTERS = {
    # ── Physics ───────────────────────────────────────────────────────────────
    'P1': ('chapters.P1_measurement',       'P1_Measurement.pdf'),
    'P2': ('chapters.P2_force_motion',      'P2_Force_Motion_Pressure.pdf'),
    'P3': ('chapters.P3_heat',              'P3_Heat_Temperature.pdf'),
    'P4': ('chapters.P4_light',             'P4_Light.pdf'),
    'P5': ('chapters.P5_electricity',       'P5_Electricity.pdf'),
    'P6': ('chapters.P6_magnetism',         'P6_Magnetism.pdf'),
    'P7': ('chapters.P7_sound',             'P7_Sound.pdf'),
    'P8': ('chapters.P8_universe',          'P8_Universe_Space.pdf'),

    # ── Chemistry ─────────────────────────────────────────────────────────────
    'C1': ('chapters.C1_matter',            'C1_Matter_Properties.pdf'),
    'C2': ('chapters.C2_atomic_structure',  'C2_Atomic_Structure.pdf'),
    'C3': ('chapters.C3_changes',           'C3_Changes_Around_Us.pdf'),
    'C4': ('chapters.C4_air',               'C4_Air.pdf'),
    'C5': ('chapters.C5_water',             'C5_Water.pdf'),
    'C6': ('chapters.C6_acids_bases',       'C6_Acids_Bases_Salts.pdf'),
    'C7': ('chapters.C7_chemistry_daily',   'C7_Chemistry_Daily_Life.pdf'),

    # ── Biology ───────────────────────────────────────────────────────────────
    'B1': ('chapters.B1_plants',            'B1_Plant_Kingdom.pdf'),
    'B2': ('chapters.B2_animals',           'B2_Animal_Kingdom.pdf'),
    'B3': ('chapters.B3_cell',              'B3_Cell_Organisation.pdf'),
    'B4': ('chapters.B4_microorganisms',    'B4_Microorganisms.pdf'),
    'B5': ('chapters.B5_health',            'B5_Health_Hygiene_Adolescence.pdf'),
    'B6': ('chapters.B6_crop_production',   'B6_Crop_Production.pdf'),
    'B7': ('chapters.B7_environment',       'B7_Environment_Ecology.pdf'),
}


def build(chapter_id: str, out_dir: str = 'output'):
    chapter_id = chapter_id.upper()
    if chapter_id not in CHAPTERS:
        print(f"❌ Unknown chapter: {chapter_id}")
        print(f"   Valid IDs: {', '.join(sorted(CHAPTERS.keys()))}")
        sys.exit(1)

    module_name, filename = CHAPTERS[chapter_id]
    out_path = os.path.join(out_dir, filename)
    os.makedirs(out_dir, exist_ok=True)

    print(f"📖 Building {chapter_id}  →  {out_path}")

    # Register fonts once
    register_fonts()

    # Dynamically import the chapter module and call its build() function
    try:
        mod = importlib.import_module(module_name)
        mod.build(out_path)
    except ModuleNotFoundError:
        print(f"⚠️  Chapter module not yet created: {module_name}.py")
        print(f"   Create chapters/{chapter_id.lower()}_*.py with a build(out_path) function.")
        sys.exit(1)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"✅ Done  →  {out_path}  ({size_kb:.1f} KB)")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python build/build_chapter.py <CHAPTER_ID>")
        print(f"Chapters: {', '.join(sorted(CHAPTERS.keys()))}")
        sys.exit(1)
    build(sys.argv[1])
