"""
TET Paper II Science Handbook — P2: Force, Motion & Pressure  VERSION 3
✓ MCQ Quick-Check boxes REMOVED
✓ Varied formats: tables, def-cards, formula-strips, info-pills,
  contrast-cards, process-flows, note-boxes, did-you-know boxes
✓ All Class 6, 7, 8 sub-topics covered
✓ Key Facts = numbers/years/names only (no repeat)
✓ Glossary = pure definitions only (no repeat)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
import os

CHAPTER_ID = "P2"
CHAPTER_TITLE = "Force, Motion & Pressure"
SUBTITLE = "Physics | Classes 6, 7 & 8 Combined"

# ─── UNICODE SUPERSCRIPT/SUBSCRIPT FIXER ─────────────────────────────────────
_SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4','\u2075':'5',
        '\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9','\u207b':'-','\u207a':'+'}
_SUB = {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4',
        '₅':'5','₆':'6','₇':'7','₈':'8','₉':'9'}

def _fix(text):
    """Replace unicode super/sub with ReportLab XML tags (Helvetica-safe)."""
    import re as _re
    sc = ''.join(_SUP.keys())
    bc = ''.join(_SUB.keys())
    def rs(m): return '<super>'+''.join(_SUP.get(c,c) for c in m.group())+'</super>'
    def rb(m): return '<sub>'  +''.join(_SUB.get(c,c) for c in m.group())+'</sub>'
    t = _re.sub(f'[{_re.escape(sc)}]+', rs, text)
    t = _re.sub(f'[{_re.escape(bc)}]+', rb, t)
    return t


# ─── PALETTE ──────────────────────────────────────────────────────────────────
TEAL        = colors.HexColor('#0F766E')
TEAL_L      = colors.HexColor('#CCFBF1')
TEAL_M      = colors.HexColor('#5EEAD4')
TEAL_D      = colors.HexColor('#134E4A')
CYAN        = colors.HexColor('#0891B2')
CYAN_L      = colors.HexColor('#CFFAFE')
BLUE        = colors.HexColor('#1D4ED8')
BLUE_L      = colors.HexColor('#DBEAFE')
BLUE_D      = colors.HexColor('#1E3A8A')
INDIGO      = colors.HexColor('#4338CA')
INDIGO_L    = colors.HexColor('#E0E7FF')
PURPLE      = colors.HexColor('#7C3AED')
PURPLE_L    = colors.HexColor('#EDE9FE')
PURPLE_D    = colors.HexColor('#4C1D95')
GREEN       = colors.HexColor('#15803D')
GREEN_L     = colors.HexColor('#DCFCE7')
GREEN_D     = colors.HexColor('#14532D')
EMERALD     = colors.HexColor('#059669')
EMERALD_L   = colors.HexColor('#D1FAE5')
ORANGE      = colors.HexColor('#C2410C')
ORANGE_L    = colors.HexColor('#FFEDD5')
RED         = colors.HexColor('#B91C1C')
RED_L       = colors.HexColor('#FEE2E2')
AMBER       = colors.HexColor('#B45309')
AMBER_L     = colors.HexColor('#FEF3C7')
GRAY_L      = colors.HexColor('#F3F4F6')
GRAY_M      = colors.HexColor('#D1D5DB')
GRAY        = colors.HexColor('#6B7280')
GRAY_D      = colors.HexColor('#374151')
SLATE       = colors.HexColor('#1E293B')
WHITE       = colors.white

# ─── PAGE ─────────────────────────────────────────────────────────────────────
PW, PH = 210 * mm, 290 * mm
MAR = 20 * mm
UW = 170 * mm
C_GAP = 6 * mm
CW = 82 * mm

FN, FNB, FNI = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'

def S(nm, **kw): return ParagraphStyle(nm, **kw)

# Core styles
BD   = S('bd',  fontName=FN,  fontSize=10.5, leading=15, textColor=GRAY_D, spaceAfter=2)
BDB  = S('bdb', fontName=FNB, fontSize=10.5, leading=15, textColor=SLATE)
CE   = S('ce',  fontName=FN,  fontSize=11, leading=15, textColor=GRAY_D)
CEB  = S('ceb', fontName=FNB, fontSize=11, leading=15, textColor=SLATE)
CEC  = S('cec', fontName=FNB, fontSize=11, leading=15, textColor=SLATE, alignment=TA_CENTER)
HW   = S('hw',  fontName=FNB, fontSize=9.5, leading=13,   textColor=WHITE)
HWC  = S('hwc', fontName=FNB, fontSize=9.5, leading=13,   textColor=WHITE, alignment=TA_CENTER)
SC   = S('sc',  fontName=FNB, fontSize=11, leading=15,   textColor=WHITE)
MIN  = S('mn',  fontName=FN,  fontSize=9, leading=13, textColor=GRAY_D)
MINB = S('mb',  fontName=FNB, fontSize=9, leading=13, textColor=SLATE)

sp = lambda h: Spacer(1, h*mm)

# ─── PRIMITIVE BUILDERS ───────────────────────────────────────────────────────

def P(text, style=BD): return Paragraph(text, style)

def banner(code, title, sub=''):
    data = [[
        P(f'<font color="white"><b>{code}</b></font>',
          S('bu', fontName=FNB, fontSize=24, leading=28, textColor=WHITE, alignment=TA_CENTER)),
        [P(f'<font color="white"><b>{title}</b></font>',
           S('bt', fontName=FNB, fontSize=15, leading=20, textColor=WHITE)),
         P(f'<font color="#5EEAD4">{sub}</font>' if sub else '',
           S('bs', fontName=FNI, fontSize=9.5, leading=13, textColor=TEAL_M)),
         sp(1),
         P('<font color="#CCFBF1">Classes 6 • 7 • 8  |  TET Paper II Science</font>',
           S('bi', fontName=FN, fontSize=9.5, leading=13, textColor=TEAL_L))]
    ]]
    t = Table(data, colWidths=[26*mm, UW-26*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),TEAL_D),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(0,0),6*mm),
        ('LEFTPADDING',(1,0),(1,0),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),5*mm),
    ]))
    return t

def sec(title, bg=TEAL):
    t = Table([[P(title, SC)]], colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
    ]))
    return t

def sub(title, bg=colors.HexColor('#0D9488')):
    t = Table([[P(title, S('sh', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

def grid(hdrs, rows, ws=None, hbg=TEAL, alt=GRAY_L):
    if not ws:
        ws = [UW / len(hdrs)] * len(hdrs)
    else:
        total = sum(ws)
        if total and abs(total - UW) > 1e-6:
            ws = [w * (UW / total) for w in ws]
    data = [[P(h, HWC) for h in hdrs]]
    for row in rows:
        data.append([P(c, CE) if isinstance(c,str) else c for c in row])
    t = Table(data, colWidths=ws, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),
        ('GRID',(0,0),(-1,-1),0.35,GRAY_M),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),2*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[alt, WHITE]),
    ]))
    return t

def two_col(L, R):
    def mk(items):
        return [P(x) if isinstance(x,str) else x for x in items]
    t = Table([[mk(L), mk(R)]], colWidths=[CW, CW])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('INNERGRID',(0,0),(-1,-1),0,WHITE),
        ('BOX',(0,0),(-1,-1),0,WHITE),
    ]))
    return t

# ── DEFINITION CARD ───────────────────────────────────────────────────────────
def def_card(term, defn, bg_L=TEAL, bg_R=TEAL_L, w_L=40*mm):
    t = Table([[
        P(term, S('dt', fontName=FNB, fontSize=10.5, leading=15, textColor=WHITE)),
        P(defn, S('dd', fontName=FN,  fontSize=8.2, leading=12, textColor=SLATE))
    ]], colWidths=[w_L, UW-w_L])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_L),
        ('BACKGROUND',(1,0),(1,0),bg_R),
        ('BOX',(0,0),(-1,-1),0.8,bg_L),
        ('LINEAFTER',(0,0),(0,-1),0.8,bg_L),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

# ── FORMULA STRIP ─────────────────────────────────────────────────────────────
def fstrip(label, formula, note='', bg=BLUE_D):
    note_txt = f'  <font size="7" color="#94A3B8">({note})</font>' if note else ''
    t = Table([[
        P(label, S('fl', fontName=FNB, fontSize=9.5, leading=13, textColor=TEAL_M)),
        P(f'<b><font color="white">{formula}</font></b>{note_txt}',
          S('ff', fontName=FNB, fontSize=12, leading=16, textColor=WHITE, alignment=TA_CENTER)),
    ]], colWidths=[46*mm, UW-46*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

# ── INFO PILL — single highlight strip for one key fact ───────────────────────
def pill(icon, text, bg=EMERALD_L, fg=GREEN_D):
    """Single-row inline highlight — for a standalone key fact."""
    t = Table([[P(f'{icon}  {text}',
                  S('pi', fontName=FNB, fontSize=10, leading=14, textColor=fg))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('BOX',(0,0),(-1,-1),0.6,fg),
    ]))
    return t

# ── CONTRAST CARD — two concepts side by side ─────────────────────────────────
def contrast(titleL, itemsL, titleR, itemsR, bgL=BLUE_L, bgR=EMERALD_L,
             hbgL=BLUE_D, hbgR=GREEN_D):
    """Side-by-side concept contrast (replaces compare-table for 2-column diff.)"""
    def mk_col(title, items, hbg, bg):
        rows = [[P(title, S('ct', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE))]]
        for item in items:
            rows.append([P(f'• {item}', S('ci', fontName=FN, fontSize=9.5, leading=13.5, textColor=SLATE))])
        t = Table(rows, colWidths=[CW])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(0,0),hbg),
            ('BACKGROUND',(0,1),(-1,-1),bg),
            ('BOX',(0,0),(-1,-1),0.8,hbg),
            ('LINEBELOW',(0,0),(0,0),0.8,hbg),
            ('LEFTPADDING',(0,0),(-1,-1),3*mm),
            ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
            ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
            ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ]))
        return t
    t = Table([[mk_col(titleL,itemsL,hbgL,bgL), mk_col(titleR,itemsR,hbgR,bgR)]],
              colWidths=[CW, CW])
    t.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),
        ('RIGHTPADDING',(0,0),(-1,-1),0),
        ('INNERGRID',(0,0),(-1,-1),0,WHITE),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

# ── PROCESS FLOW — horizontal numbered steps ──────────────────────────────────
def flow(steps, bg=CYAN, fg=WHITE, arrow='→'):
    """Horizontal numbered process strip."""
    n = len(steps)
    w = UW / n
    cells = []
    for i, s in enumerate(steps):
        txt = f'<b><font color="white">{i+1}</font></b>  <font color="white">{s}</font>'
        cells.append(P(txt, S('fl', fontName=FN, fontSize=7.5, leading=11, textColor=WHITE,
                               alignment=TA_CENTER)))
    t = Table([cells], colWidths=[w]*n)
    style = [
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),2*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('BOX',(0,0),(-1,-1),0,WHITE),
    ]
    # Alternate shading per step
    for i in range(0, n, 2):
        style.append(('BACKGROUND',(i,0),(i,0),colors.HexColor('#0E7490')))
    t.setStyle(TableStyle(style))
    return t

# ── NOTE BOX — common misconceptions / important notes ───────────────────────
def note(title, items, bg_h=AMBER, bg_b=AMBER_L, icon='⚠'):
    rows = [[P(f'{icon}  {title}',
               S('nt', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'↳  {item}', S('ni', fontName=FN, fontSize=9.5, leading=13.5, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_h),
        ('BACKGROUND',(0,1),(-1,-1),bg_b),
        ('BOX',(0,0),(-1,-1),1,bg_h),
        ('LINEBELOW',(0,0),(0,0),1,bg_h),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

# ── DID YOU KNOW — textbook science trivia ────────────────────────────────────
def dyk(items, bg=PURPLE_L, hbg=PURPLE_D):
    rows = [[P('💡 Did You Know?  (Textbook Science Facts)',
               S('dk', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'◆  {item}', S('di', fontName=FN, fontSize=9.5, leading=13.5, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),hbg),
        ('BACKGROUND',(0,1),(-1,-1),bg),
        ('BOX',(0,0),(-1,-1),1,hbg),
        ('LINEBELOW',(0,0),(0,0),1,hbg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

# ── SOLVED PROBLEM ────────────────────────────────────────────────────────────
def prob(num, q, given, soln, ans):
    rows = [
        [P(f'Problem {num}', S('pt', fontName=FNB, fontSize=8.5, textColor=BLUE_D)), P(q, BD)],
        [P('Given', CEB), P(given, CE)],
        [P('Solution', CEB), P(soln, CE)],
        [P('Answer', S('pa', fontName=FNB, fontSize=8.5, textColor=GREEN_D)),
         P(f'<b><font color="#14532D">{ans}</font></b>', CE)],
    ]
    t = Table(rows, colWidths=[22*mm, UW-22*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),BLUE_L),
        ('BACKGROUND',(0,-1),(-1,-1),EMERALD_L),
        ('BOX',(0,0),(-1,-1),1,BLUE_D),
        ('INNERGRID',(0,0),(-1,-1),0.3,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

def rapid_nums(rows):
    return grid(['Quantity / Concept','Formula / Value','Unit / Note'], rows,
                ws=[62*mm,72*mm,40*mm], hbg=TEAL_D)

def rapid_ppl(rows):
    return grid(['Scientist','Contribution','Year / Class'], rows,
                ws=[48*mm,88*mm,38*mm], hbg=PURPLE_D)

def gloss_2col(terms):
    rows = []
    for i in range(0, len(terms), 2):
        L = P(f'<b>{terms[i][0]}</b> — {terms[i][1]}', MIN)
        R = P(f'<b>{terms[i+1][0]}</b> — {terms[i+1][1]}', MIN) if i+1<len(terms) else P('', MIN)
        rows.append([L, R])
    t = Table(rows, colWidths=[CW, CW])
    t.setStyle(TableStyle([
        ('GRID',(0,0),(-1,-1),0.3,GRAY_M),
        ('ROWBACKGROUNDS',(0,0),(-1,-1),[GRAY_L,WHITE]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t


# ═══════════════════════════════════════════════════════════════════════════════
def content():
    s = []

    # ── BANNER ────────────────────────────────────────────────────────────────
    s += [banner('P2','Force, Motion & Pressure','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  FORCE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  FORCE — Definition, Types & Effects'), sp(2)]

    s += [
        def_card('Force',
                 'A <b>push or pull</b> by an animate or inanimate agency — causes motion, stops motion, changes direction, or changes shape of an object.'),
        sp(1),
        def_card('Force',
                 'External agency that changes or tends to change the state of rest, uniform motion, direction, or shape of a body. Force is a <b>vector quantity</b> (has magnitude AND direction).'),
        sp(2),
    ]

    s += [
        fstrip('SI Unit of Force', 'Newton  (N)', 'CGS unit = dyne  |  1 N = 10<super>5</super> dyne', BLUE_D),
        sp(1),
        fstrip('Force Formula', 'F = m × a', "Newton's 2nd Law  |  m in kg, a in m/s<super>2</super>", TEAL_D),
        sp(1),
        fstrip('Weight Formula', 'W = m × g', 'g = 9.8 m/s<super>2</super> ≈ 10 m/s<super>2</super> at Earth\'s surface', GREEN_D),
        sp(3),
    ]

    s += [sub('Contact & Non-Contact Forces'), sp(1)]
    s += [contrast(
        '⚡ Contact Forces',
        ['Act only when bodies physically touch',
         'Muscular force — muscles exert push/pull',
         'Friction — opposes sliding/rolling',
         'Applied force — push a book, kick a ball',
         'Tension in a rope, Normal reaction',
         'Examples: kicking ball, pulling cart, wind on grass'],
        '🧲 Non-Contact Forces',
        ['Act without any physical contact (at a distance)',
         'Gravity — Earth pulls every object downward',
         'Magnetic force — magnet attracts iron nail',
         'Electrostatic force — charged body attracts paper',
         'Examples: falling coconut, compass needle deflecting',
         'A magnet attracts iron without touching it'],
        bgL=BLUE_L, bgR=EMERALD_L, hbgL=BLUE_D, hbgR=GREEN_D
    ), sp(3)]

    s += [sub('Effects of Force'), sp(1)]
    s += [grid(
        ['Effect on Object','Explanation','Real Example'],
        [
            ['Rest → Motion',           'Stationary body begins to move when force applied',         'Kicking a ball at rest'],
            ['Motion → Rest',           'Moving body slows down and stops',                          'Braking a bicycle'],
            ['Change speed',            'Velocity increases (acceleration) or decreases (deceleration)', 'Car speeding up / slowing down'],
            ['Change direction',        'Direction of moving body changes on applying force',        'Batsman deflects cricket ball'],
            ['Change shape / size',     'Object compressed, stretched, bent, or deformed',           'Squeezing balloon; pulling rubber band'],
            ['Effect ∝ force magnitude','Greater the force → greater the change in motion',          'Harder bat hit → ball travels farther'],
        ],
        ws=[38*mm,72*mm,64*mm]
    ), sp(2)]

    s += [note('Common Misconceptions — Force', [
        'Force does NOT always produce motion — balanced forces keep object at rest.',
        'Weight (W = mg) is a FORCE (in Newtons), NOT the same as mass (in kg).',
        'A body can be in motion even with ZERO net force — uniform velocity needs no force.',
    ], bg_h=AMBER, icon='⚠'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  MOTION — CLASS 6
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  MOTION — Rest, Types & Speed'), sp(2)]

    s += [
        def_card('Motion',
                 'Change in <b>position</b> of an object with respect to time and a reference point (surroundings).'),
        sp(1),
        def_card('Rest',
                 'No change in position with respect to time and surroundings.  <i>Both rest and motion are RELATIVE — not absolute.</i>'),
        sp(2),
    ]

    s += [pill('🔁', 'REST & MOTION ARE RELATIVE — An object at rest for one observer may be in motion for another.', INDIGO_L, INDIGO)]
    s += [sp(2)]

    s += [sub('Types of Motion Based on Path'), sp(1)]
    s += [grid(
        ['Type of Motion','Path Description','Class 6 Textbook Examples','More Examples'],
        [
            ['Linear (Rectilinear)','Straight-line path',             'Person walking on straight road; falling stone','Car on straight highway'],
            ['Curvilinear',         'Curved path (direction changes)','Thrown paper aeroplane',                       'Javelin throw; ball rolled off table'],
            ['Circular',            'Circular path around fixed centre','Stone on rope swirled in circles',           'Earth revolving around Sun; fan blade tip'],
            ['Rotatory',            'Spinning about own axis',        'Spinning top; pencil in sharpener',            "Earth's rotation; ceiling fan; motor shaft"],
            ['Oscillatory',        'To-and-fro about mean position', 'Pendulum; pencil held between fingers swung',  'Swing; vibrating guitar string; sewing machine needle'],
            ['Zigzag (Irregular)', 'No fixed path or direction',      'Fly buzzing in room',                          'Brownian motion; people in crowd'],
        ],
        ws=[36*mm,42*mm,56*mm,40*mm]
    ), sp(2)]

    s += [contrast(
        '🔄 Periodic Motion',
        ['Repeats after a fixed time interval (time period)',
         'Oscillatory motion → always periodic',
         'Circular motion → periodic (Earth\'s revolution: 365 days)',
         'Rotatory motion → periodic (Earth\'s rotation: 24 hours)',
         'Pendulum swings every fixed interval'],
        '🔀 Non-Periodic Motion',
        ['No fixed time pattern — does not repeat regularly',
         'Zigzag / Irregular motion (fly in room)',
         'Curvilinear motion (thrown ball)',
         'Linear motion may be non-periodic',
         'Walking, running in general'],
        bgL=CYAN_L, bgR=ORANGE_L, hbgL=CYAN, hbgR=ORANGE
    ), sp(2)]

    # Speeds += [sub('Speed'), sp(1)]
    s += [
        fstrip('Speed', 's = d / t', 'Distance ÷ Time  |  SCALAR  |  SI unit: m/s', TEAL_D),
        sp(1),
    ]
    s += [grid(
        ['Speed Type','Definition','Example'],
        [
            ['Uniform Speed',     'Equal distances in equal time intervals',     'Light through vacuum (3×10<super>8</super> m/s)'],
            ['Non-uniform Speed', 'Unequal distances in equal time intervals',   'Bus in city traffic'],
            ['Average Speed',     'Total distance ÷ total time taken',           'Overall trip when speed varies'],
        ],
        ws=[40*mm,80*mm,54*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  DISTANCE, DISPLACEMENT, VELOCITY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  Distance, Displacement & Velocity'), sp(2)]

    s += [contrast(
        '📏 Distance',
        ['Total length of path from start to end',
         'SCALAR — magnitude only, no direction',
         'SI unit: metre (m)',
         'Always positive (≥ 0)',
         'Can never be zero unless object never moved',
         'Symbol: d'],
        '↗ Displacement',
        ['Shortest straight-line path from start to end',
         'VECTOR — has both magnitude AND direction',
         'SI unit: metre (m)',
         'Can be positive, negative, or ZERO',
         'Zero when object returns to starting point',
         'Symbol: s  (or Δx)'],
        bgL=BLUE_L, bgR=EMERALD_L, hbgL=BLUE_D, hbgR=GREEN_D
    ), sp(2)]

    s += [pill('⚡', 'Distance = Displacement ONLY when object moves in a STRAIGHT LINE from start to end without turning back.', CYAN_L, CYAN)]
    s += [sp(1)]
    s += [pill('⚡', 'Displacement = 0 means the object RETURNED to its starting point (e.g., one complete circular trip).', ORANGE_L, ORANGE)]
    s += [sp(2)]

    s += [def_card('Nautical Mile',
                   '1 nautical mile = 1.852 km — unit for sea/air navigation. <b>Knot</b> = 1 nautical mile/hour — speed unit for ships and aircraft.'), sp(3)]

    s += [sub('Speed vs Velocity'), sp(1)]
    s += [grid(
        ['','Speed','Velocity'],
        [
            ['Definition', 'Rate of change of distance',          'Rate of change of displacement'],
            ['Type',       'Scalar (magnitude only)',              'Vector (magnitude + direction)'],
            ['Formula',    'speed = distance / time',             'velocity = displacement / time'],
            ['SI Unit',    'm/s',                                  'm/s'],
            ['Uniform',    'Equal distances in equal time',        'Equal displacement in equal time in same direction'],
            ['Can be zero?','Only if not moving',                  'Yes — if displacement = 0 in that interval'],
            ['Example',    'Car speedometer reading',              'Car at 60 km/h heading NORTH'],
        ],
        ws=[30*mm,72*mm,72*mm]
    ), sp(2)]

    s += [
        fstrip('Average Speed',    'v_avg = Total Distance / Total Time',        'Scalar', TEAL_D),
        sp(1),
        fstrip('Average Velocity', 'v_avg = Total Displacement / Total Time',    'Vector — direction matters', BLUE_D),
        sp(1),
        fstrip('Unit Conversion',  '1 km/h = 5/18 m/s  |  1 m/s = 3.6 km/h',  'Multiply km/h by 5/18 to get m/s', SLATE),
        sp(3),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # D  ACCELERATION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  Acceleration — All Types'), sp(2)]

    s += [def_card('Acceleration',
                   'Rate of change of velocity. If a body changes its speed OR direction, it is said to be accelerated. SI unit: m/s<super>2</super>'), sp(1)]
    s += [fstrip('Acceleration Formula', 'a = (v − u) / t', 'v = final velocity, u = initial velocity, t = time  |  SI: m/s<super>2</super>', BLUE_D), sp(2)]

    s += [grid(
        ['Type (Section)','Definition','Sign','Textbook Example'],
        [
            ['Positive Acceleration\n(2.3.1)',
             'Velocity INCREASES with time','+ve',
             'Car at rest reaches 12 m/s in 4 s → a = 3 m/s<super>2</super>'],
            ['Negative Acceleration\n/ Deceleration / Retardation\n(2.3.2)',
             'Velocity DECREASES with time','−ve',
             'Golf ball: 8 m/s → 2 m/s in 10 s → a = −0.6 m/s<super>2</super>'],
            ['Uniform Acceleration\n(2.3.3)',
             'Change in velocity is SAME each second','±',
             'Bus velocity: 20, 40, 60, 80… m/s — increases by 20 m/s every second'],
            ['Non-uniform Acceleration\n(2.3.4)',
             'Change in velocity is DIFFERENT each second','±',
             'Velocity sequence: 0, 10, 40, 60, 70, 50 m/s — change varies'],
        ],
        ws=[44*mm,58*mm,14*mm,58*mm]
    ), sp(2)]

    s += [dyk([
        'Cheetah accelerates from 0 to 20 m/s in just 2 seconds — acceleration = 10 m/s<super>2</super> (Class 7 textbook).',
        'Usain Bolt runs 100 m in 9.58 s → average speed ≈ 10.44 m/s (discussed in Class 7).',
        'Tortoise speed: 0.1 m/s | Person walking: 1.4 m/s | Falling raindrop: 9–10 m/s (Class 7 textbook data).',
        'Badminton smash speed: 80–90 m/s | Rocket: 5200 m/s | Passenger jet: 180 m/s.',
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  GRAPHS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  Distance–Time & Speed–Time Graphs'), sp(2)]

    s += [sub('Distance–Time Graph — Section 2.4 (4 Cases)'), sp(1)]
    s += [grid(
        ['Case','Graph Shape','Gradient / Slope','Motion Represented'],
        [
            ['1','Horizontal line','Zero (flat)','Object at REST — distance does not change'],
            ['2','Straight line rising','Constant (positive)','Uniform speed — equal distance per second'],
            ['3','Curve — concave (bending upward)','Increasing','Speed INCREASING — acceleration'],
            ['4','Curve — convex (flattening)','Decreasing','Speed DECREASING — deceleration'],
        ],
        ws=[12*mm,42*mm,30*mm,90*mm]
    ), sp(2)]

    s += [sub('Speed–Time Graph — Section 2.5 (6 Cases)'), sp(1)]
    s += [grid(
        ['Case','Graph Shape','What it Means'],
        [
            ['1','Horizontal line at speed = 0',          'Object at rest (zero speed, zero acceleration)'],
            ['2','Horizontal line at speed > 0',          'Uniform speed — zero acceleration'],
            ['3','Straight line RISING (constant slope)', 'Uniform acceleration — speed increases at constant rate'],
            ['4','Straight line FALLING (constant slope)','Uniform deceleration — speed decreases at constant rate'],
            ['5','Rising CURVE with increasing slope',    'Non-uniform acceleration — acceleration itself is increasing'],
            ['6','Rising CURVE with decreasing slope',    'Non-uniform acceleration — acceleration is decreasing (speed still rising but slower)'],
        ],
        ws=[12*mm,56*mm,106*mm]
    ), sp(2)]

    s += [sub('D–T vs S–T Graph Comparison — Section 2.5.1'), sp(1)]
    s += [grid(
        ['Journey Phase','Distance–Time Graph','Speed–Time Graph'],
        [
            ['Accelerating uniformly from rest','Concave curve (gradient increases)','Straight line rising (positive constant slope)'],
            ['Moving at constant speed',         'Straight line (constant gradient)',  'Horizontal line (slope = 0 = zero acceleration)'],
            ['Decelerating uniformly to stop',   'Convex curve (gradient decreases)', 'Straight line falling (negative constant slope)'],
            ['Important: Area under graph',      'Not directly useful',               '= Distance travelled (area of triangle/rectangle)'],
        ],
        ws=[46*mm,64*mm,64*mm]
    ), sp(2)]

    s += [note('Graph Reading Tips', [
        'D–T and S–T graphs may look similar — always check the Y-axis label first.',
        'Slope of D–T graph = speed  |  Slope of S–T graph = acceleration.',
        'Area under S–T graph = distance travelled (calculate as triangle / trapezium area).',
    ], bg_h=AMBER, icon='📌'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  CENTRE OF GRAVITY & STABILITY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  Centre of Gravity & Stability'), sp(2)]

    s += [def_card('Centre of Gravity (CG)',
                   'The point through which the <b>entire weight of an object appears to act</b>. For regular shapes, CG lies at the geometric centre.'), sp(2)]

    s += [sub('CG of Regular-Shaped Objects — Section 2.6.1'), sp(1)]
    s += [grid(
        ['Shape','Location of Centre of Gravity','How to find for irregular shapes'],
        [
            ['Square / Rectangle','Intersection of diagonals','—'],
            ['Circle / Disc',     'Centre of the circle',     '—'],
            ['Triangle',          'Centroid — where three medians intersect','—'],
            ['Ring / Hollow circle','Centre (may be in empty space)','—'],
            ['Uniform ruler / rod','Midpoint of the ruler',   '—'],
            ['Irregular lamina',  'Found experimentally',     'Suspend from 3 holes; draw plumb-line each time; intersection = CG'],
        ],
        ws=[38*mm,68*mm,68*mm]
    ), sp(2)]

    s += [sub('Types of Equilibrium / Stability — Section 2.7'), sp(1)]

    # Stability grid with color-coded rows
    hdr = [P(h, HWC) for h in ['Type','When Displaced...','CG change','Returns?','Example']]
    stable_rows = [
        hdr,
        [P('Stable\nEquilibrium', S('se', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE)),
         P('CG rises; weight-line stays WITHIN base area', CE),
         P('Rises ↑', CEB),
         P('YES ✓', S('y', fontName=FNB, fontSize=10, textColor=GREEN_D)),
         P('Frustum on wide base; Thanjavur doll; racing car', CE)],
        [P('Unstable\nEquilibrium', S('ue', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE)),
         P('CG lowers; weight-line falls OUTSIDE base area', CE),
         P('Falls ↓', CEB),
         P('NO ✗', S('n', fontName=FNB, fontSize=10, textColor=RED)),
         P('Frustum balanced on tip; pencil on tip', CE)],
        [P('Neutral\nEquilibrium', S('ne', fontName=FNB, fontSize=9.5, leading=13, textColor=WHITE)),
         P('CG remains at SAME height; body rolls without toppling', CE),
         P('No change', CEB),
         P('Stays in\nnew pos.', CEB),
         P('Frustum on its curved side; sphere on flat surface', CE)],
    ]
    st = Table(stable_rows, colWidths=[28*mm,52*mm,28*mm,22*mm,44*mm])
    st.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),TEAL_D),
        ('BACKGROUND',(0,1),(0,1),GREEN_D), ('BACKGROUND',(1,1),(-1,1),EMERALD_L),
        ('BACKGROUND',(0,2),(0,2),RED),     ('BACKGROUND',(1,2),(-1,2),RED_L),
        ('BACKGROUND',(0,3),(0,3),BLUE_D),  ('BACKGROUND',(1,3),(-1,3),BLUE_L),
        ('TEXTCOLOR',(0,1),(0,-1),WHITE),
        ('GRID',(0,0),(-1,-1),0.4,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    s += [st, sp(2)]

    s += [sub('Conditions & Applications of Stability — Section 2.7.1 & 2.7.2'), sp(1)]
    s += [two_col(
        ['<b>Stability INCREASES by:</b>',
         '1. <b>Lowering the Centre of Gravity</b>',
         '   → Use a heavy base (base absorbs weight)',
         '2. <b>Increasing the base area</b>',
         '   → Wider base = more stable',
         '',
         '<b>Thanjavur Doll:</b>',
         '• Traditional Thanjavur terracotta toy',
         '• CG concentrated at <b>bottommost point</b>',
         '• Returns to upright on any tilt → stable equilibrium',
         '• Shows slow oscillatory dance-like motion'],
        ['<b>Real-Life Applications:</b>',
         '• Tour bus: luggage stored at <b>BOTTOM</b> (not on roof)',
         '• Double-decker bus: extra passengers NOT on upper deck',
         '• Racing cars: built <b>low and broad</b>',
         '• Table lamps / fans: <b>large heavy base</b>',
         '',
         '<b>Finding CG of irregular shape:</b>',
         'Step 1 → Make 3 holes in the lamina',
         'Step 2 → Suspend from each hole + hang plumb-line',
         'Step 3 → Draw lines along plumb-line on lamina',
         'Step 4 → Intersection of 3 lines = Centre of Gravity']
    ), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  PRESSURE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  Pressure — Thrust, Atmospheric & Liquid'), sp(2)]

    s += [
        def_card('Thrust',
                 'Force acting <b>perpendicularly</b> on a given surface area. Unit: Newton (N). A given force on a smaller area produces greater thrust effect.'),
        sp(1),
        def_card('Pressure',
                 'Amount of thrust (force) acting on <b>unit area</b> of surface. SI unit: <b>Pascal (Pa) = 1 Nm<super>-2</super></b> — named after French scientist Blaise Pascal.'),
        sp(1),
        fstrip('Pressure Formula', 'P = F / A  =  Thrust / Area', '1 Pascal = 1 Nm<super>-2</super>  |  CGS: dyne/cm<super>2</super>', BLUE_D),
        sp(2),
    ]

    s += [sub('Pressure — Effect of Area on Practical Situations'), sp(1)]
    s += [grid(
        ['Situation','Force','Area','Pressure Effect','Reason'],
        [
            ['Sharp knife / nail',  'Same','Very small (tip)','Very HIGH','Small area → concentrates force → penetrates easily'],
            ['Injection needle',    'Same','Tiny tip',        'Very HIGH','Concentrated force → pierces skin without large force'],
            ['Camel\'s padded feet','Body weight','Large',    'LOW',       'Large feet area spreads weight → no sinking in sand'],
            ['Heavy truck wheels',  'Body weight','Many tyres (large total)','LOW','Many wheels increase contact area → less road pressure'],
            ['Broad bag strap',     'Bag weight','Wide strap','LOW',       'Wide strap spreads load → comfortable on shoulder'],
            ['Dam wall — wider base','Water','Larger at bottom','Withstands high pressure','Liquid pressure increases with depth → thicker wall needed at base'],
        ],
        ws=[38*mm,24*mm,30*mm,22*mm,60*mm]
    ), sp(3)]

    s += [sub('Atmospheric Pressure'), sp(1)]
    s += [
        def_card('Atmospheric Pressure',
                 'Weight of the column of atmospheric air above <b>unit area</b> of Earth\'s surface. It acts in ALL directions — not just downward.'),
        sp(1),
    ]
    s += [grid(
        ['Parameter','Value / Explanation'],
        [
            ['Standard value (sea level)',  '1 atm = 76 cm Hg = 760 mmHg = 1,01,325 Pa ≈ 1.01 × 10<super>5</super> Nm<super>-2</super>'],
            ['Measuring instrument',        'Barometer (mercury barometer) — invented by Evangelista Torricelli (1643)'],
            ['Pressure with altitude',      'Atmospheric pressure DECREASES as altitude increases above Earth\'s surface'],
            ['Tilting the barometer tube',  'Mercury level remains the same — proof that air pressure acts equally in all directions'],
            ['Aneroid barometer',           'No liquid — uses elastic metal box deformation; used in aircraft as altimeter'],
            ['Cooking at high altitude',    'Lower atmospheric pressure → boiling point of water drops (even 80°C) → food does not cook properly'],
            ['Pressure cooker',             'Sealed vessel → increased internal pressure → boiling point of water rises → food cooks faster'],
        ],
        ws=[54*mm,120*mm]
    ), sp(3)]

    s += [sub('Liquid Pressure'), sp(1)]
    s += [
        fstrip('Liquid Pressure', 'P = ρ × g × h', 'ρ = density (kg/m<super>3</super>), g = 9.8 m/s<super>2</super>, h = depth below surface (m)', colors.HexColor('#0369A1')),
        sp(1),
    ]
    s += [grid(
        ['Property','Explanation','Textbook Experiment / Example'],
        [
            ['Increases with depth',          'Greater depth → more liquid weight above → more pressure',   'Spouting can: lowest hole shoots water farthest'],
            ['Same in ALL directions at a given depth','Liquid exerts equal pressure sideways, upward, downward at same depth','Rubber ball with holes: water shoots equally from all holes'],
            ['Depends only on height of liquid column','Not on shape/width of container — only vertical height (h) matters','Balloon at bottom of tube bulges more as water height increases'],
            ['Buoyant Force (Archimedes)',     'Upward force on submerged body = weight of liquid displaced',       'Ship floats; submarine; hydrometer measures density'],
            ['Object floats if...',           'Weight of object < Buoyant force (upward force)',            'Cork floats in water'],
            ['Object sinks if...',            'Weight of object > Buoyant force',                           'Iron ball sinks in water'],
            ['Scuba diver suits',             'Withstand enormous water pressure at great ocean depths',    'Pressure increases with depth — special suit prevents body compression'],
        ],
        ws=[44*mm,66*mm,64*mm]
    ), sp(3)]

    s += [sub('Pascal\'s Law'), sp(1)]
    s += [def_card('Pascal\'s Law',
                   'Pressure applied at any point of a <b>liquid at rest in a closed container</b> is transmitted equally in all directions throughout the liquid. (Blaise Pascal, 1648)'), sp(1)]

    # Process flow for Pascal's Law mechanism
    s += [flow(['Apply small force on small piston',
                'Pressure = F₁/A₁ created',
                'Pressure transmitted equally to ALL points',
                'Same pressure acts on large piston (A₂)',
                'Large force F₂ = P × A₂ produced'], bg=CYAN)]
    s += [sp(2)]

    s += [grid(
        ['Application','Working Principle','Where Used'],
        [
            ['Hydraulic Lift / Jack', 'F₁/A₁ = F₂/A₂ → small force on small piston → large force lifts vehicle',     'Car service stations; aircraft jacks'],
            ['Hydraulic Brakes',      'Brake fluid transmits force equally to all four wheel cylinders simultaneously', 'Cars, buses, motorcycles'],
            ['Hydraulic Press',       'Large mechanical advantage → compress materials',                               'Cotton/paper bale compression'],
            ['Syringe / Pump',        'Pressure on liquid transmitted uniformly to needle outlet',                     'Medical injections; pumps'],
        ],
        ws=[38*mm,88*mm,48*mm]
    ), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  SURFACE TENSION & VISCOSITY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  Surface Tension & Viscosity'), sp(2)]

    s += [
        def_card('Surface Tension',
                 'Property of liquid surface molecules to contract and minimize surface area. Defined as <b>force per unit length</b> acting on the surface. Unit: <b>Nm<super>-1</super></b>.',
                 bg_L=PURPLE, bg_R=PURPLE_L),
        sp(1),
        def_card('Viscosity / Viscous Force',
                 'Frictional force between <b>successive moving layers</b> of a liquid that opposes their relative motion. CGS unit: <b>Poise</b>. SI unit: <b>kg m<super>-1</super> s<super>-1</super> = N s m<super>-2</super></b>.',
                 bg_L=PURPLE, bg_R=PURPLE_L),
        sp(2),
    ]

    s += [contrast(
        '💧 Surface Tension',
        ['Acts at the SURFACE / boundary of liquid',
         'Contracts surface to MINIMUM area',
         'Unit: Nm<super>-1</super> (Newton per metre)',
         'Decreases when temperature rises',
         'Decreased by detergent/soap',
         'Causes: spherical drops, capillary rise, insects on water'],
        '🌊 Viscosity (Viscous Force)',
        ['Acts BETWEEN LAYERS of a moving liquid',
         'Opposes relative motion of layers (internal friction)',
         'CGS: poise  |  SI: kg m<super>-1</super> s<super>-1</super>',
         'Also decreases when temperature rises',
         'Honey > Oil > Water — more viscous = flows slower',
         'Causes: slow flow of thick liquids; engine oil lubricates'],
        bgL=PURPLE_L, bgR=INDIGO_L, hbgL=PURPLE, hbgR=INDIGO
    ), sp(2)]

    s += [sub('Applications of Surface Tension — Section 2.5.1'), sp(1)]
    s += [two_col(
        ['<b>Surface Tension Applications:</b>',
         '• <b>Rain drops spherical</b> — liquid contracts to minimum surface area for given volume',
         '• <b>Water strider insect</b> walks on water without sinking',
         '• <b>Paper clip / needle floats</b> — though denser than water',
         '• <b>Capillary action in plants</b> — water rises in narrow xylem vessels against gravity',
         '• <b>Soap bubble</b> formation — liquid film holds shape due to surface tension'],
        ['<b>Practical Consequences:</b>',
         '• <b>Detergent reduces surface tension</b> — water spreads into cloth fibres → better cleaning',
         '• <b>Sailors pour oil on rough sea</b> — reduces surface tension → calms waves and protects ship',
         '• <b>Water spreads on glass</b> (wets glass) because adhesion > cohesion',
         '• <b>Mercury beads up on glass</b> (does not wet) because cohesion > adhesion',
         '• <b>Mosquito larvae</b> breathe through water surface — surface tension supports them']
    ), sp(3)]

    s += [dyk([
        'Surface tension of water = 0.073 N/m at 20°C — pure water has higher surface tension than soapy water.',
        'Water strider insect has waxy legs — increases contact angle, prevents wetting, allows walking on water surface.',
        'Blood viscosity is about 3–4 times that of water — important for cardiovascular health.',
        'Viscosity of honey: ~2000–10,000 times that of water — why it flows very slowly at room temperature.',
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  FRICTION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  Friction — Types, Factors & Control'), sp(2)]

    s += [def_card('Friction',
                   'Force arising between two bodies in contact that <b>opposes relative motion</b>. Caused by geometrical dissimilarities (roughness/irregularities) on surfaces. Always acts <b>opposite to direction of motion</b>.'), sp(2)]

    s += [sub('Types of Friction — Section 2.7.1'), sp(1)]
    s += [grid(
        ['Type','When it Acts','Magnitude Order','Class 8 Example'],
        [
            ['Static Friction',          'Body at REST; external force applied but no motion yet',       'LARGEST',   'Book resting on table; parked car; wall before pushing'],
            ['Sliding Friction (Kinetic)','During SLIDING of one surface over another',                 'MODERATE',  'Box dragged on floor; chalk on blackboard; braking'],
            ['Rolling Friction',          'When body ROLLS over another surface',                        'SMALLEST',  'Ball rolling on ground; bicycle/car tyre rolling on road'],
            ['Fluid Friction (Viscosity)','Object moving through liquid or gas (air/water resistance)',  'Varies',    'Ship in water; aeroplane in air; swimming'],
        ],
        ws=[38*mm,56*mm,24*mm,56*mm]
    ), sp(1)]
    s += [pill('📌', 'Order of friction magnitude:  Rolling < Sliding < Static  (rolling friction is smallest → ball bearings used in machines)', EMERALD_L, GREEN_D)]
    s += [sp(3)]

    s += [sub('Factors Affecting Friction — Section 2.7.2'), sp(1)]
    s += [grid(
        ['Factor','Effect','Textbook Example'],
        [
            ['Nature of surface (rough vs smooth)',
             'Rough surface → MORE friction; Smooth/polished → LESS friction',
             'Walking on wet surface is slippery; polished marble floor more slippery than rough road'],
            ['Weight / Mass of body',
             'Greater mass/weight → GREATER frictional force',
             'Loaded trolley harder to push than empty trolley; cyclist with heavy load pedals harder'],
            ['Area of contact',
             'Greater contact area → greater friction (for same weight)',
             'Road roller (broad drum) offers more friction; cycle tyre (narrow) offers less'],
        ],
        ws=[48*mm,64*mm,62*mm]
    ), sp(3)]

    s += [sub('Advantages vs Disadvantages of Friction — Sections 2.7.3 & 2.7.4'), sp(1)]
    s += [contrast(
        '✅ Advantages of Friction',
        ['We walk without slipping on ground',
         'Vehicles brake and stop safely',
         'We write with pen/pencil on paper',
         'Knots, nails, bolts, screws hold firmly',
         'Matchstick lights when struck on box',
         'Climbing, gripping, stitching clothes possible',
         'Brakes on cycle/car work due to friction'],
        '❌ Disadvantages of Friction',
        ['Wears out surfaces — shoe soles, tyres, gear teeth',
         'Wastes energy — extra effort to overcome friction',
         'Produces HEAT — damages machines and bearings',
         'Moving parts make noise due to friction',
         'Vehicles slow down due to air and road friction',
         'Engine parts wear out → frequent maintenance needed',
         'Reduces efficiency of all machines'],
        bgL=EMERALD_L, bgR=RED_L, hbgL=GREEN_D, hbgR=RED
    ), sp(1)]
    s += [def_card('Friction is a "Necessary Evil"',
                   'Essential for daily life (walking, braking, writing) yet also destructive (wears surfaces, wastes energy). Hence called a <b>necessary evil</b>.'), sp(3)]

    s += [sub('Increasing & Decreasing Friction — Section 2.7.5'), sp(1)]
    s += [grid(
        ['Method','Effect on Friction','How it Works','Example'],
        [
            ['Increase area of contact','INCREASES','More contact area → more surface irregularities engaged', 'Brake shoes pressed close to wheel rim'],
            ['Lubricants (oil/grease)', 'DECREASES','Fills gaps in rough surfaces; smooth layer prevents direct contact', 'Engine oil, grease, coconut oil, castor oil, graphite'],
            ['Ball Bearings',           'DECREASES','Converts sliding → rolling friction (rolling much smaller)', 'Cycle hub, electric motors, axles, wheels'],
            ['Streamlining body shape', 'DECREASES fluid friction','Smooth shape reduces air/water resistance', 'Aircraft, ships, sports cars, fish body'],
            ['Polishing / smoothing surfaces','DECREASES','Removes surface irregularities → smoother contact', 'Sports tracks, machine parts, bearings'],
            ['Using rough grooved surface','INCREASES','More grip needed for safety', 'Tyre treads, brake pads, shoe soles, stair nosing'],
        ],
        ws=[36*mm,30*mm,60*mm,48*mm]
    ), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Solved Numerical Problems'), sp(2)]

    ps = [
        ('1','A vehicle covers 400 km in 5 hours. Find speed.',
         'd = 400 km = 4,00,000 m; t = 5 h = 18,000 s',
         'Speed = d/t = 400/5 = 80 km/h  OR  = 4,00,000/18,000 = 22.22 m/s',
         '80 km/h  =  22.22 m/s'),
        ('2','A car starts from rest and reaches 20 m/s in 10 s. Find acceleration.',
         'u = 0 m/s, v = 20 m/s, t = 10 s',
         'a = (v−u)/t = (20−0)/10 = 2 m/s<super>2</super>',
         'Acceleration = 2 m/s<super>2</super>'),
        ('3','Golf ball decelerates from 8 m/s to 2 m/s in 10 s. Find deceleration.',
         'u = 8 m/s, v = 2 m/s, t = 10 s',
         'a = (v−u)/t = (2−8)/10 = −6/10 = −0.6 m/s<super>2</super>',
         'Deceleration = 0.6 m/s<super>2</super>'),
        ('4','Elephant weight = 4000 N, one foot area = 0.1 m<super>2</super>. Find pressure on one foot.',
         'Force on one foot = 4000 ÷ 4 = 1000 N; A = 0.1 m<super>2</super>',
         'P = F/A = 1000/0.1 = 10,000 Nm<super>-2</super>',
         '10,000 Pa  =  10<super>4</super> Nm<super>-2</super>'),
        ('5','Stone weighs 500 N, contact area = 25 cm<super>2</super>. Find pressure.',
         'F = 500 N; A = 25 cm<super>2</super> = 25×10<super>-4</super> m<super>2</super> = 0.0025 m<super>2</super>',
         'P = F/A = 500/0.0025 = 2,00,000 Nm<super>-2</super>',
         '2 × 10<super>5</super> Pa'),
        ('6','Geetha cycles at 2 m/s for 15 min. Find distance to school.',
         'v = 2 m/s; t = 15 min = 15×60 = 900 s',
         'Distance = v × t = 2 × 900 = 1800 m',
         '1800 m  =  1.8 km'),
    ]

    for i, p_args in enumerate(ps):
        s += [prob(*p_args), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  KEY FACTS — RAPID REVISION (numbers/years/names ONLY, no definitions)
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]
    s += [P('<b>Formulas, Values & Units</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Force',                'F = m × a',                                'Newton (N)  |  CGS: dyne'],
        ['1 Newton',             '= 10<super>5</super> dyne',                               'Unit conversion'],
        ['Weight',               'W = m × g  (g = 9.8 m/s<super>2</super> ≈ 10)',          'Newton (N)'],
        ['Speed',                'distance ÷ time',                          'm/s (scalar)'],
        ['Velocity',             'displacement ÷ time',                      'm/s (vector)'],
        ['Acceleration',         'a = (v − u) / t',                          'm/s<super>2</super> (vector)'],
        ['1 km/h',               '= 5/18 m/s  ≈ 0.278 m/s',                 'Unit conversion'],
        ['1 m/s',                '= 3.6 km/h  (multiply by 3.6)',            'Unit conversion'],
        ['Pressure',             'P = F/A  = Thrust ÷ Area',                 'Pascal (Pa) = Nm<super>-2</super>'],
        ['1 atmosphere',         '= 76 cm Hg = 760 mmHg = 1.01×10<super>5</super> Pa',    'Standard sea-level value'],
        ['Liquid pressure',      'P = ρ × g × h',                           'Pa (Nm<super>-2</super>)'],
        ['Surface tension unit', 'Nm<super>-1</super> (Newton per metre)',                  'Force per unit length on liquid surface'],
        ['Viscosity (CGS)',       'Poise',                                    'CGS unit'],
        ['Viscosity (SI)',        'kg m<super>-1</super> s<super>-1</super>  =  N s m<super>-2</super>',               'SI unit'],
        ['1 Nautical mile',       '= 1.852 km',                              'Sea/air navigation; 1 knot = 1 nmi/h'],
        ['Cheetah speed',         '25–30 m/s  |  0→20 m/s in 2 s = 10 m/s<super>2</super> acc.', 'Class 7 textbook data'],
        ['Speed of light',        '3 × 10<super>8</super> m/s (vacuum)',                    'Uniform velocity example'],
        ['Tortoise speed',        '0.1 m/s  |  Person walking: 1.4 m/s',    'Class 7 textbook data'],
        ['Friction order',        'Rolling < Sliding < Static',              'Smallest to largest friction'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoverers & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['Isaac Newton',           'Laws of Motion; Law of Gravitation; unit "Newton" named after him', '1687  '],
        ['Blaise Pascal',          'Pascal\'s Law of fluid pressure; unit "pascal" named after him',   '1648  '],
        ['Evangelista Torricelli', 'Invented the mercury barometer to measure atmospheric pressure',   '1643  '],
        ['Galileo Galilei',        'Law of falling bodies; studied motion, velocity, acceleration',    '1638  '],
        ['Archimedes',             'Archimedes\' Principle: buoyant force = weight of fluid displaced','287–212 BC '],
        ['Aryabhata',              'Observed rest and motion are RELATIVE (star/river bank example)',  '5th century CE '],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # L  GLOSSARY (pure one-line definitions ONLY — no values, no applications)
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('L  ·  Glossary — Definitions  (one-line definitions only)'), sp(2)]

    g = [
        ('Force',               'Push or pull by animate/inanimate agency; vector quantity; SI unit: Newton'),
        ('Thrust',              'Force acting perpendicularly on a surface area; unit: Newton'),
        ('Pressure',            'Thrust per unit area (P = F/A); SI unit: Pascal (Pa)'),
        ('Newton (N)',          'SI unit of force; 1 N = force that gives 1 kg an acceleration of 1 m/s<super>2</super>'),
        ('Pascal (Pa)',         'SI unit of pressure; 1 Pa = 1 Nm<super>-2</super>; named after Blaise Pascal'),
        ('Motion',              'Change in position of a body with respect to time and a reference point'),
        ('Rest',                'No change in position with respect to time and a reference point'),
        ('Distance',            'Total length of path travelled; scalar quantity; unit: metre'),
        ('Displacement',        'Shortest straight-line path from initial to final position with direction; vector'),
        ('Speed',               'Rate of change of distance; scalar; unit: m/s'),
        ('Velocity',            'Rate of change of displacement; vector; unit: m/s'),
        ('Acceleration',        'Rate of change of velocity; a = (v−u)/t; unit: m/s<super>2</super>'),
        ('Deceleration',        'Negative acceleration; velocity decreasing with time; also called retardation'),
        ('Linear Motion',       'Motion along a straight-line path'),
        ('Circular Motion',     'Motion along a circular path around a fixed centre or axis'),
        ('Rotatory Motion',     'Spinning of a body about its own axis'),
        ('Oscillatory Motion',  'Repeated to-and-fro motion about a mean (equilibrium) position'),
        ('Curvilinear Motion',  'Motion along a curved path where direction continuously changes'),
        ('Periodic Motion',     'Motion that repeats identically after a fixed time interval (time period)'),
        ('Uniform Motion',      'Motion with equal distances covered in equal time intervals'),
        ('Average Speed',       'Total distance divided by total time taken for a journey'),
        ('Average Velocity',    'Total displacement divided by total time taken for a journey'),
        ('Atmospheric Pressure','Weight of atmospheric air acting per unit area of Earth\'s surface'),
        ('Barometer',           'Instrument to measure atmospheric pressure; mercury barometer invented by Torricelli'),
        ('Buoyant Force',       'Upward force exerted by a fluid on an immersed or floating object'),
        ('Pascal\'s Law',       'Pressure applied to a confined liquid is transmitted equally in all directions'),
        ('Hydraulic Machine',   'Device using Pascal\'s Law to multiply force via liquid pressure transmission'),
        ('Surface Tension',     'Property of liquid surfaces to contract to minimum area; unit: Nm<super>-1</super>'),
        ('Viscosity',           'Property of a liquid to resist flow; internal friction between moving liquid layers'),
        ('Viscous Force',       'Frictional force between adjacent layers of a liquid moving at different velocities'),
        ('Friction',            'Force opposing relative motion between surfaces in contact; due to surface irregularities'),
        ('Static Friction',     'Friction on a body at rest; attains maximum value just before motion begins'),
        ('Sliding Friction',    'Kinetic friction during sliding motion of one surface over another'),
        ('Rolling Friction',    'Friction when a body rolls over a surface; less than sliding friction'),
        ('Lubricant',           'Substance that reduces friction by forming smooth layer between surfaces (oil, grease)'),
        ('Centre of Gravity',   'Point through which total weight of an object appears to act'),
        ('Stable Equilibrium',  'Object returns to original position when slightly displaced; CG rises on displacement'),
        ('Unstable Equilibrium','Object topples further when displaced; CG lowers on displacement'),
        ('Neutral Equilibrium', 'Object stays in displaced position; CG height unchanged on displacement'),
        ('Capillarity',         'Rise or fall of liquid in a narrow tube due to surface tension and adhesion'),
        ('Knot',                'Unit of speed: 1 knot = 1 nautical mile per hour; used in sea and air navigation'),
    ]

    s += [gloss_2col(g), sp(3)]

    # ── FOOTER ────────────────────────────────────────────────────────────────
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL),
        sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P2: Force, Motion & Pressure  |  Classes 6 • 7 • 8',
          S('ft', fontName=FNI, fontSize=7, textColor=TEAL, alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 7)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P2  |  Force, Motion & Pressure  |  Page {doc.page}')
        cv.restoreState()

    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=18*mm,
        title='TET Handbook P2 Force Motion Pressure',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P2_Force_Motion_Pressure.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
