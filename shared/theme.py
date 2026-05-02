"""
ChalkPieceDiary Theme — TET Handbook
Central color, font, and spacing definitions.
Import this in every chapter file.
"""

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A5
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ─── PAGE ─────────────────────────────────────────────────────────────────────
PAGE_SIZE   = A5
PAGE_W, PAGE_H = A5
L_MARGIN    = 10 * mm
R_MARGIN    = 10 * mm
T_MARGIN    = 11 * mm
B_MARGIN    = 10 * mm
USABLE_W    = PAGE_W - L_MARGIN - R_MARGIN

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
    dv = '/usr/share/fonts/truetype/dejavu'
    pdfmetrics.registerFont(TTFont('DV',        f'{dv}/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DV-Bold',   f'{dv}/DejaVuSans-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('DV-Italic', f'{dv}/DejaVuSans-Oblique.ttf'))
    pdfmetrics.registerFont(TTFont('DV-BoldIt', f'{dv}/DejaVuSans-BoldOblique.ttf'))
    pdfmetrics.registerFont(TTFont('DVCond',    f'{dv}/DejaVuSansCondensed.ttf'))
    pdfmetrics.registerFont(TTFont('DVCond-B',  f'{dv}/DejaVuSansCondensed-Bold.ttf'))
    registerFontFamily('DV',     normal='DV',     bold='DV-Bold',
                       italic='DV-Italic', boldItalic='DV-BoldIt')
    registerFontFamily('DVCond', normal='DVCond', bold='DVCond-B')
    _FONTS_REGISTERED = True

FONT_REG  = 'DV'
FONT_BOLD = 'DV-Bold'
FONT_IT   = 'DV-Italic'
FONT_BIT  = 'DV-BoldIt'
