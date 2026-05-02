"""
Page header/footer chrome applied to every page of every chapter.
"""

from shared.theme import (
    PRIMARY, BORDER, TEXT_MUTED, PAGE_W, PAGE_H,
    FONT_BOLD, FONT_REG, L_MARGIN, R_MARGIN, B_MARGIN
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
        is_even = (doc.page % 2 == 0)

        # ── Top color strip ──────────────────────────────────────────────────
        canv.setFillColor(PRIMARY)
        canv.rect(0, PAGE_H - 6 * mm, PAGE_W, 6 * mm, fill=1, stroke=0)

        canv.setFillColor('white')
        canv.setFont(FONT_BOLD, 7.2)
        canv.drawString(L_MARGIN, PAGE_H - 4.2 * mm, label)

        canv.setFont(FONT_REG, 7)
        canv.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 4.2 * mm, "ChalkPieceDiary")

        # ── Bottom rule + footer ─────────────────────────────────────────────
        canv.setStrokeColor(BORDER)
        canv.setLineWidth(0.3)
        footer_rule_y = B_MARGIN - 2.5 * mm
        footer_text_y = B_MARGIN - 5.5 * mm
        canv.line(L_MARGIN, footer_rule_y, PAGE_W - R_MARGIN, footer_rule_y)

        canv.setFillColor(TEXT_MUTED)
        canv.setFont(FONT_REG, 6.5)
        left_text = "chalkpiecediary.com" if is_even else "TET Paper II Science Handbook"
        right_text = "TET Paper II Science Handbook" if is_even else "chalkpiecediary.com"
        canv.drawString(L_MARGIN, footer_text_y, left_text)
        canv.drawCentredString(PAGE_W / 2, footer_text_y, f"{chapter_id}.{doc.page}")
        canv.drawRightString(PAGE_W - R_MARGIN, footer_text_y, right_text)

        canv.restoreState()

    return draw
