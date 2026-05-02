"""
Reusable UI components for chapter building.
Every chapter imports from here — ensures consistent look.
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.colors import HexColor
from shared.theme import (
    PRIMARY, SECONDARY, ACCENT, LIGHT_BG, HIGHLIGHT,
    BORDER, TEXT_DARK, TEXT_MUTED, PURPLE, LIGHT_BG2,
    FONT_BOLD, FONT_REG, USABLE_W, COL_W, COL_GAP
)
from shared.styles import make_styles

S = make_styles()


# ─── BANNER ──────────────────────────────────────────────────────────────────

def chapter_banner(chapter_id: str, title: str, subtitle: str):
    """Slim 10mm chapter banner — P1/C1/B1 + title + subject info."""
    data = [[
        Paragraph(f"<b>{chapter_id}</b>", S['banner_id']),
        Paragraph(f"<b>{title}</b>",      S['banner_title']),
        Paragraph(subtitle,               S['banner_sub']),
    ]]
    t = Table(
        data,
        colWidths=[12*_mm(), USABLE_W*0.55, USABLE_W - 12*_mm() - USABLE_W*0.55],
        rowHeights=[10*_mm()]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), PRIMARY),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING',   (0,0), (-1,-1), 4),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('TOPPADDING',    (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LINEAFTER',     (0,0), (0,0), 0.5, HexColor('#FFFFFF80')),
    ]))
    return t


def _mm():
    from reportlab.lib.units import mm
    return mm


# ─── SECTION HEADINGS ────────────────────────────────────────────────────────

def section(num, title):
    """Full-width colored bar section heading."""
    text = Paragraph(f"<b>{num}.  {title}</b>", S['section_bar'])
    t = Table([[text]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PRIMARY),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


def subsec(num, title):
    return Paragraph(f"<b>{num}</b>  {title}", S['subsec'])


# ─── TEXT HELPERS ────────────────────────────────────────────────────────────

def p(text):
    return two_col_body(text)


def pl(text):
    return Paragraph(text, S['body_left'])


def b(text):
    return Paragraph(f"• {text}", S['bullet'])


def fact(text):
    """Amber highlighted memorization fact box."""
    para = Paragraph(f"<b>★</b>  {text}", S['fact'])
    t = Table([[para]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HIGHLIGHT),
        ('BOX', (0, 0), (-1, -1), 0.4, ACCENT),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


def defn(text):
    """Italic definition block on light teal background."""
    return Paragraph(text, S['defn'])


def two_col_body(left_text, right_text=''):
    """Two-column body text row (82mm + 6mm gap + 82mm)."""
    left = Paragraph(left_text, S['body'])
    right = Paragraph(right_text, S['body']) if right_text else Paragraph('', S['body'])
    t = Table([[left, right]], colWidths=[COL_W, COL_W])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
        ('RIGHTPADDING', (0, 0), (0, -1), COL_GAP / 2),
        ('LEFTPADDING', (1, 0), (1, -1), COL_GAP / 2),
        ('RIGHTPADDING', (1, 0), (1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    return t


def two_col_paragraphs(paragraphs):
    """Pack paragraph strings into paired 2-column rows."""
    rows = []
    for i in range(0, len(paragraphs), 2):
        right = paragraphs[i + 1] if i + 1 < len(paragraphs) else ''
        rows.append(two_col_body(paragraphs[i], right))
    return rows


def sp(h=1.5):
    """Small spacer. h in mm."""
    from reportlab.lib.units import mm
    return Spacer(1, h*mm)


# ─── TABLES ──────────────────────────────────────────────────────────────────

def dense_table(header, rows, col_widths=None, font_size=7.8,
                header_color=PRIMARY):
    """
    Standard compact table.

    Args:
        header: list of column header strings
        rows:   list of lists (each row)
        col_widths: list of widths in pts; auto-distributes if None
        font_size: body cell font size (default 7.8)
        header_color: header background color
    """
    if col_widths is None:
        col_widths = [USABLE_W / len(header)] * len(header)

    h_sty = S['th']
    b_sty = S['td']

    # Allow per-cell font size override
    if font_size != 7.8:
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_LEFT, TA_CENTER
        h_sty = ParagraphStyle('TH_', fontSize=font_size, fontName=FONT_BOLD,
                                textColor='white', alignment=TA_CENTER,
                                leading=font_size+1.5)
        b_sty = ParagraphStyle('TD_', fontSize=font_size, fontName=FONT_REG,
                                textColor=TEXT_DARK, alignment=TA_LEFT,
                                leading=font_size+2)

    tdata = [[Paragraph(str(h), h_sty) for h in header]]
    for row in rows:
        tdata.append([Paragraph(str(c), b_sty) for c in row])

    t = Table(tdata, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  header_color),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), ['white', LIGHT_BG]),
        ('GRID',          (0,0), (-1,-1), 0.3,  BORDER),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING',   (0,0), (-1,-1), 3),
        ('RIGHTPADDING',  (0,0), (-1,-1), 3),
        ('TOPPADDING',    (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t


def problems_table(problems):
    """
    Table for solved numerical problems.

    Args:
        problems: list of (question_str, answer_str) tuples
    """
    rows = [[str(i), q, a] for i, (q, a) in enumerate(problems, 1)]
    header = ['#', 'Problem', 'Solution']
    col_widths = [6*_mm(), USABLE_W*0.55, USABLE_W*0.45 - 6*_mm()]

    tdata = [[Paragraph(c, S['prob_h']) for c in header]]
    for row in rows:
        tdata.append([Paragraph(c, S['prob_b']) for c in row])

    t = Table(tdata, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  PRIMARY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), ['white', LIGHT_BG]),
        ('GRID',          (0,0), (-1,-1), 0.3,  BORDER),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING',   (0,0), (-1,-1), 3),
        ('RIGHTPADDING',  (0,0), (-1,-1), 3),
        ('TOPPADDING',    (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t


def two_col_glossary(items):
    """
    Two-column glossary.

    Args:
        items: list of (term, definition) tuples
    """
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT

    cell_sty = S['gloss_cell']

    def cell(term, defn):
        return Paragraph(
            f'<font name="{FONT_BOLD}" color="#0F766E">{term}:</font> {defn}',
            cell_sty
        )

    cells = [cell(t, d) for t, d in items]

    rows = []
    for i in range(0, len(cells), 2):
        right = cells[i+1] if i+1 < len(cells) else Paragraph('', cell_sty)
        rows.append([cells[i], right])

    t = Table(rows, colWidths=[(USABLE_W - COL_GAP) / 2, (USABLE_W - COL_GAP) / 2])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (0,-1), 0),
        ('RIGHTPADDING',  (0,0), (0,-1), COL_GAP / 2),
        ('LEFTPADDING',   (1,0), (1,-1), COL_GAP / 2),
        ('RIGHTPADDING',  (1,0), (1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LINEBELOW',     (0,0), (-1,-2), 0.2, BORDER),
    ]))
    return t
