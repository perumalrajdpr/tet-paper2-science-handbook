"""
Page header/footer chrome applied to every page of every chapter.
"""

from shared.theme import (
    PRIMARY, BORDER, TEXT_MUTED, PAGE_W, PAGE_H,
    FONT_BOLD, FONT_REG
)


def make_page_chrome(chapter_id: str, chapter_title: str):
    """
    Returns a function compatible with ReportLab's onFirstPage/onLaterPages.

    Usage:
        chrome = make_page_chrome("P1", "MEASUREMENT")
        doc.build(story, onFirstPage=chrome, onLaterPages=chrome)
    """
    label = f"TET PAPER II SCIENCE  ·  {chapter_id} {chapter_title}"

    def draw(canv, doc):
        from reportlab.lib.units import mm
        canv.saveState()

        # ── Top color strip ──────────────────────────────────────────────────
        canv.setFillColor(PRIMARY)
        canv.rect(0, PAGE_H - 5*mm, PAGE_W, 5*mm, fill=1, stroke=0)

        canv.setFillColor('white')
        canv.setFont(FONT_BOLD, 7)
        canv.drawString(10*mm, PAGE_H - 3.5*mm, label)

        canv.setFont(FONT_REG, 7)
        canv.drawRightString(PAGE_W - 10*mm, PAGE_H - 3.5*mm, "ChalkPieceDiary")

        # ── Bottom rule + footer ─────────────────────────────────────────────
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(0.3)
        canv.line(10*mm, 7*mm, PAGE_W - 10*mm, 7*mm)

        canv.setFillColor(TEXT_MUTED)
        canv.setFont(FONT_REG, 6.5)
        canv.drawString(10*mm,           4.5*mm, "TET Paper II Science Handbook")
        canv.drawCentredString(PAGE_W/2, 4.5*mm, f"{chapter_id}.{doc.page}")
        canv.drawRightString(PAGE_W - 10*mm, 4.5*mm, "chalkpiecediary.com")

        canv.restoreState()

    return draw
