"""
ChalkPieceDiary Theme — TET Handbook
Central color, font, and spacing definitions.
Import this in every chapter file.
"""

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily, Font
from pathlib import Path

# ─── PAGE ─────────────────────────────────────────────────────────────────────
# InDesign export spec:
# page = 210 x 290 mm, margins = 20 mm, two columns = 82 mm + 6 mm + 82 mm
PAGE_SIZE   = (210 * mm, 290 * mm)
PAGE_W, PAGE_H = PAGE_SIZE
L_MARGIN    = 20 * mm
R_MARGIN    = 20 * mm
T_MARGIN    = 20 * mm
B_MARGIN    = 20 * mm
USABLE_W    = PAGE_W - L_MARGIN - R_MARGIN

FACING_PAGES = True

# Two-column text geometry (inside full-width content area)
COL_GAP = 6 * mm
COL_W = 82 * mm

# ─── COLORS ───────────────────────────────────────────────────────────────────
PRIMARY     = HexColor('#0F766E')   # Deep teal-green  — main brand
SECONDARY   = HexColor('#0EA5E9')   # Sky blue          — accent
TERTIARY    = HexColor('#14B8A6')   # Light teal        — class 6 labels
ACCENT      = HexColor('#F59E0B')   # Amber             — ★ fact boxes
DANGER      = HexColor('#DC2626')   # Red               — warnings
PURPLE      = HexColor('#7C3AED')   # Violet            — TET focus boxes
LIGHT_BG    = HexColor('#F0FDFA')   # Light teal bg     — table alternates
LIGHT_BG2   = HexColor('#ECFEFF')   # Light cyan bg     — info boxes
HIGHLIGHT   = HexColor('#FEF3C7')   # Amber tint        — fact highlights
BORDER      = HexColor('#CBD5E1')   # Slate-300         — table borders
TEXT_DARK   = HexColor('#0F172A')   # Slate-900         — body text
TEXT_MUTED  = HexColor('#475569')   # Slate-600         — footer text

# ─── FONTS ────────────────────────────────────────────────────────────────────
_FONTS_REGISTERED = False

def register_fonts():
    global _FONTS_REGISTERED
    if _FONTS_REGISTERED:
        return

    candidates = [
        Path('/usr/share/fonts/truetype/dejavu'),
        Path('/usr/local/share/fonts/dejavu'),
        Path('C:/Windows/Fonts'),
    ]
    dv = next((p for p in candidates if (p / 'DejaVuSans.ttf').exists()), None)

    if dv:
        pdfmetrics.registerFont(TTFont('DV',        str(dv / 'DejaVuSans.ttf')))
        pdfmetrics.registerFont(TTFont('DV-Bold',   str(dv / 'DejaVuSans-Bold.ttf')))
        pdfmetrics.registerFont(TTFont('DV-Italic', str(dv / 'DejaVuSans-Oblique.ttf')))
        pdfmetrics.registerFont(TTFont('DV-BoldIt', str(dv / 'DejaVuSans-BoldOblique.ttf')))
        pdfmetrics.registerFont(TTFont('DVCond',    str(dv / 'DejaVuSansCondensed.ttf')))
        pdfmetrics.registerFont(TTFont('DVCond-B',  str(dv / 'DejaVuSansCondensed-Bold.ttf')))
    else:
        # Fallback for environments where DejaVu is not installed.
        pdfmetrics.registerFont(Font('DV', 'Helvetica', 'WinAnsiEncoding'))
        pdfmetrics.registerFont(Font('DV-Bold', 'Helvetica-Bold', 'WinAnsiEncoding'))
        pdfmetrics.registerFont(Font('DV-Italic', 'Helvetica-Oblique', 'WinAnsiEncoding'))
        pdfmetrics.registerFont(Font('DV-BoldIt', 'Helvetica-BoldOblique', 'WinAnsiEncoding'))
        pdfmetrics.registerFont(Font('DVCond', 'Helvetica', 'WinAnsiEncoding'))
        pdfmetrics.registerFont(Font('DVCond-B', 'Helvetica-Bold', 'WinAnsiEncoding'))

    registerFontFamily('DV',     normal='DV',     bold='DV-Bold',
                       italic='DV-Italic', boldItalic='DV-BoldIt')
    registerFontFamily('DVCond', normal='DVCond', bold='DVCond-B')
    _FONTS_REGISTERED = True

FONT_REG  = 'DV'
FONT_BOLD = 'DV-Bold'
FONT_IT   = 'DV-Italic'
FONT_BIT  = 'DV-BoldIt'
