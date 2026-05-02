"""
Shared paragraph styles for all chapters.
"""

from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from shared.theme import (
    PRIMARY, SECONDARY, ACCENT, DANGER, LIGHT_BG, HIGHLIGHT,
    BORDER, TEXT_DARK, TEXT_MUTED, PURPLE, LIGHT_BG2,
    FONT_REG, FONT_BOLD, FONT_IT, FONT_BIT, USABLE_W
)

_styles = getSampleStyleSheet()


def make_styles():
    """Return dict of all paragraph styles used across chapters."""
    return {

        # ── Section headings ──────────────────────────────────────────────────
        'section': ParagraphStyle(
            'Sec', fontSize=10.5, leading=12, textColor=PRIMARY,
            fontName=FONT_BOLD, spaceBefore=4, spaceAfter=2,
            backColor=None,
        ),
        'section_bar': ParagraphStyle(
            'SecBar', fontSize=10.5, leading=12, textColor='white',
            fontName=FONT_BOLD, spaceBefore=4, spaceAfter=2,
            backColor=PRIMARY, borderPadding=3,
        ),
        'subsec': ParagraphStyle(
            'Sub', fontSize=9.5, leading=11, textColor=PRIMARY,
            fontName=FONT_BOLD, spaceBefore=3, spaceAfter=1,
        ),

        # ── Body text ─────────────────────────────────────────────────────────
        'body': ParagraphStyle(
            'Body', fontSize=8.3, leading=10.5, textColor=TEXT_DARK,
            fontName=FONT_REG, alignment=TA_JUSTIFY, spaceAfter=2,
        ),
        'body_left': ParagraphStyle(
            'BodyL', fontSize=8.3, leading=10.5, textColor=TEXT_DARK,
            fontName=FONT_REG, alignment=TA_LEFT, spaceAfter=2,
        ),
        'bullet': ParagraphStyle(
            'Bul', fontSize=8.3, leading=10.5, textColor=TEXT_DARK,
            fontName=FONT_REG, leftIndent=8, alignment=TA_LEFT, spaceAfter=1,
        ),

        # ── Highlighted fact ──────────────────────────────────────────────────
        'fact': ParagraphStyle(
            'Fact', fontSize=8.2, leading=10.5, textColor=TEXT_DARK,
            fontName=FONT_REG, leftIndent=4, backColor=HIGHLIGHT,
            borderPadding=2, spaceBefore=1, spaceAfter=2,
        ),

        # ── Definition block ──────────────────────────────────────────────────
        'defn': ParagraphStyle(
            'Def', fontSize=8.2, leading=10.5, textColor=TEXT_DARK,
            fontName=FONT_IT, leftIndent=4, backColor=LIGHT_BG,
            borderPadding=2, spaceBefore=1, spaceAfter=2,
        ),

        # ── Glossary (2-column) ───────────────────────────────────────────────
        'gloss_cell': ParagraphStyle(
            'GC', fontSize=7.5, leading=9, fontName=FONT_REG,
            textColor=TEXT_DARK, alignment=TA_LEFT,
        ),

        # ── Table cells ───────────────────────────────────────────────────────
        'th': ParagraphStyle(
            'TH', fontSize=7.8, fontName=FONT_BOLD,
            textColor='white', alignment=TA_CENTER, leading=9.5,
        ),
        'td': ParagraphStyle(
            'TD', fontSize=7.8, fontName=FONT_REG,
            textColor=TEXT_DARK, alignment=TA_LEFT, leading=9.5,
        ),
        'td_center': ParagraphStyle(
            'TDC', fontSize=7.8, fontName=FONT_REG,
            textColor=TEXT_DARK, alignment=TA_CENTER, leading=9.5,
        ),

        # ── Solved problems ───────────────────────────────────────────────────
        'prob_h': ParagraphStyle(
            'PH', fontSize=7.5, fontName=FONT_BOLD,
            textColor='white', alignment=TA_CENTER, leading=9,
        ),
        'prob_b': ParagraphStyle(
            'PB', fontSize=7.5, fontName=FONT_REG,
            textColor=TEXT_DARK, alignment=TA_LEFT, leading=9.5,
        ),

        # ── Banner ────────────────────────────────────────────────────────────
        'banner_id': ParagraphStyle(
            'BID', fontSize=18, textColor='white',
            fontName=FONT_BOLD, leading=18, alignment=TA_CENTER,
        ),
        'banner_title': ParagraphStyle(
            'BT', fontSize=14, textColor='white',
            fontName=FONT_BOLD, leading=15, alignment=TA_LEFT,
        ),
        'banner_sub': ParagraphStyle(
            'BS', fontSize=8, textColor='white',
            fontName=FONT_IT, leading=10, alignment=TA_LEFT,
        ),

        # ── Footer / caption ──────────────────────────────────────────────────
        'footer': ParagraphStyle(
            'Foot', fontSize=6.5, fontName=FONT_REG,
            textColor=TEXT_MUTED, alignment=TA_CENTER,
        ),
    }
