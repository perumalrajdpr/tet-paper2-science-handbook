"""
TET Paper II Science Handbook — P1: Measurement
Style: P3 one-liner cheat-sheet
Font: 10.5pt body, 10pt cells (print-friendly A4)
All sub-topics: Class 6 (Term I, Unit 1), Class 7 (Term I, Unit 1), Class 8 (Unit 1)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

CHAPTER_ID = "P1"
CHAPTER_TITLE = "Measurement"
SUBTITLE = "Physics | Classes 6, 7 & 8 Combined"

# ─── PALETTE ──────────────────────────────────────────────────────────────────
TEAL   = colors.HexColor('#0F766E')
TEAL_L = colors.HexColor('#CCFBF1')
TEAL_M = colors.HexColor('#5EEAD4')
TEAL_D = colors.HexColor('#134E4A')
BLUE   = colors.HexColor('#1D4ED8')
BLUE_L = colors.HexColor('#DBEAFE')
BLUE_D = colors.HexColor('#1E3A8A')
CYAN   = colors.HexColor('#0891B2')
CYAN_L = colors.HexColor('#CFFAFE')
GREEN  = colors.HexColor('#15803D')
GREEN_L= colors.HexColor('#DCFCE7')
GREEN_D= colors.HexColor('#14532D')
ORANGE = colors.HexColor('#C2410C')
ORANGE_L=colors.HexColor('#FFEDD5')
RED    = colors.HexColor('#B91C1C')
RED_L  = colors.HexColor('#FEE2E2')
AMBER  = colors.HexColor('#B45309')
AMBER_L= colors.HexColor('#FEF3C7')
PURPLE = colors.HexColor('#7C3AED')
PURPLE_L=colors.HexColor('#EDE9FE')
PURPLE_D=colors.HexColor('#4C1D95')
GRAY_L = colors.HexColor('#F3F4F6')
GRAY_M = colors.HexColor('#D1D5DB')
GRAY_D = colors.HexColor('#374151')
SLATE  = colors.HexColor('#1E293B')
WHITE  = colors.white

PW, PH = 210 * mm, 290 * mm
MAR = 20 * mm
UW = 170 * mm
C_GAP = 6 * mm
CW = 82 * mm

FN, FNB, FNI = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'

# ── FONT SIZES — print-friendly ───────────────────────────────────────────────
FS_BODY  = 10.5   # main body text
FS_CELL  = 10.0   # table cells
FS_SMALL = 9.5    # secondary text
FS_MINI  = 9.0    # glossary / sub-labels
FS_SEC   = 11.0   # section headings
FS_FORM  = 12.0   # formula strip main text

def S(nm, **kw): return ParagraphStyle(nm, **kw)

BD   = S('bd',  fontName=FN,  fontSize=FS_BODY,  leading=15,   textColor=GRAY_D, spaceAfter=2)
BDB  = S('bdb', fontName=FNB, fontSize=FS_BODY,  leading=15,   textColor=SLATE)
CE   = S('ce',  fontName=FN,  fontSize=FS_CELL,  leading=14,   textColor=GRAY_D)
CEB  = S('ceb', fontName=FNB, fontSize=FS_CELL,  leading=14,   textColor=SLATE)
HWC  = S('hwc', fontName=FNB, fontSize=FS_SMALL, leading=13,   textColor=WHITE, alignment=TA_CENTER)
SC   = S('sc',  fontName=FNB, fontSize=FS_SEC,   leading=15,   textColor=WHITE)
MIN  = S('mn',  fontName=FN,  fontSize=FS_MINI,  leading=13,   textColor=GRAY_D)
MINB = S('mb',  fontName=FNB, fontSize=FS_MINI,  leading=13,   textColor=SLATE)

sp = lambda h: Spacer(1, h*mm)
P  = lambda t, st=BD: Paragraph(t, st)

# ── UNICODE FIXER ─────────────────────────────────────────────────────────────
_SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4',
        '\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9',
        '\u207b':'-','\u207a':'+'}
_SUB = {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4'}
def _fix(text):
    import re as _re
    sc = ''.join(_SUP.keys()); bc = ''.join(_SUB.keys())
    def rs(m): return '<super>'+''.join(_SUP.get(c,c) for c in m.group())+'</super>'
    def rb(m): return '<sub>'  +''.join(_SUB.get(c,c) for c in m.group())+'</sub>'
    t = _re.sub(f'[{_re.escape(sc)}]+', rs, text)
    t = _re.sub(f'[{_re.escape(bc)}]+', rb, t)
    return t

# ─── BUILDERS ─────────────────────────────────────────────────────────────────

def banner(code, title, sub=''):
    data = [[
        P(f'<font color="white"><b>{code}</b></font>',
          S('bu', fontName=FNB, fontSize=26, leading=30, textColor=WHITE, alignment=TA_CENTER)),
        [P(f'<font color="white"><b>{title}</b></font>',
           S('bt', fontName=FNB, fontSize=16, leading=21, textColor=WHITE)),
         P(f'<font color="#5EEAD4">{sub}</font>' if sub else '',
           S('bs', fontName=FNI, fontSize=9.5, leading=12, textColor=TEAL_M)),
         sp(1),
         P('<font color="#CCFBF1">Classes 6 • 7 • 8  |  TET Paper II Science</font>',
           S('bi', fontName=FN, fontSize=8.5, leading=11, textColor=TEAL_L))]
    ]]
    t = Table(data, colWidths=[28*mm, UW-28*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),TEAL_D),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(0,0),6*mm),('LEFTPADDING',(1,0),(1,0),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),5*mm),('BOTTOMPADDING',(0,0),(-1,-1),5*mm),
    ]))
    return t

def sec(title, bg=TEAL):
    t = Table([[P(title, SC)]], colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),5*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
    ]))
    return t

def sub_h(title, bg=colors.HexColor('#0D9488')):
    t = Table([[P(title, S('sh', fontName=FNB, fontSize=FS_SMALL, leading=13, textColor=WHITE))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t

def grid(hdrs, rows, ws=None, hbg=TEAL, alt=GRAY_L):
    if not ws:
        ws = [UW / len(hdrs)] * len(hdrs)
    else:
        # Keep table layouts stable after migrating to the locked 170mm usable width.
        total = sum(ws)
        if total and abs(total - UW) > 1e-6:
            ws = [w * (UW / total) for w in ws]
    data = [[P(h, HWC) for h in hdrs]]
    for row in rows:
        data.append([P(_fix(c), CE) if isinstance(c,str) else c for c in row])
    t = Table(data, colWidths=ws, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),('GRID',(0,0),(-1,-1),0.4,GRAY_M),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[alt,WHITE]),
    ]))
    return t

def one_liners(items, bg_bullet=TEAL, key_w=55*mm):
    """Compact one-liner rows — plain string: bullet row | tuple: KV row."""
    result_tables = []
    cur_b = []; cur_kv = []; prev = None

    def flush_b():
        if not cur_b: return
        t = Table(cur_b, colWidths=[6*mm, UW-6*mm])
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),2*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
            ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
            ('LINEBELOW',(0,0),(-1,-2),0.25,GRAY_M),
        ]))
        result_tables.append(t)

    def flush_kv():
        if not cur_kv: return
        t = Table(cur_kv, colWidths=[key_w, UW-key_w])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(0,-1),TEAL),
            ('BACKGROUND',(1,0),(1,-1),TEAL_L),
            ('BOX',(0,0),(-1,-1),0.6,TEAL),
            ('LINEAFTER',(0,0),(0,-1),0.6,TEAL),
            ('LINEBELOW',(0,0),(-1,-2),0.3,GRAY_M),
            ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
            ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ]))
        result_tables.append(t)

    for item in items:
        if isinstance(item, tuple):
            if prev == 'b': flush_b(); cur_b = []
            key, val = item
            cur_kv.append([
                P(f'<b>{key}</b>', S('ok', fontName=FNB, fontSize=FS_CELL, leading=14, textColor=WHITE)),
                P(_fix(val),       S('ov', fontName=FN,  fontSize=FS_CELL, leading=14, textColor=SLATE)),
            ])
            prev = 'kv'
        else:
            if prev == 'kv': flush_kv(); cur_kv = []
            cur_b.append([
                P('▶', S('ob', fontName=FNB, fontSize=FS_CELL, leading=14, textColor=bg_bullet, alignment=TA_CENTER)),
                P(_fix(item), S('oi', fontName=FN, fontSize=FS_CELL, leading=14, textColor=SLATE)),
            ])
            prev = 'b'

    flush_b(); flush_kv()

    if len(result_tables) == 1: return result_tables[0]
    wrap = Table([[t] for t in result_tables], colWidths=[UW])
    wrap.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return wrap

def kv_list(items, bg_L=TEAL, bg_R=TEAL_L, w_L=50*mm):
    rows = []
    for key, val in items:
        rows.append([
            P(key, S('kl', fontName=FNB, fontSize=FS_CELL, leading=14, textColor=WHITE)),
            P(_fix(val), S('kr', fontName=FN, fontSize=FS_CELL, leading=14, textColor=SLATE)),
        ])
    t = Table(rows, colWidths=[w_L, UW-w_L])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,-1),bg_L),('BACKGROUND',(1,0),(1,-1),bg_R),
        ('BOX',(0,0),(-1,-1),0.6,bg_L),('LINEAFTER',(0,0),(0,-1),0.6,bg_L),
        ('LINEBELOW',(0,0),(-1,-2),0.3,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def fstrip(label, formula, note='', bg=BLUE_D):
    note_t = f'  <font size="8.5" color="#94A3B8">({_fix(note)})</font>' if note else ''
    t = Table([[
        P(label, S('fl', fontName=FNB, fontSize=FS_SMALL, leading=13, textColor=TEAL_M)),
        P(f'<b><font color="white">{_fix(formula)}</font></b>{note_t}',
          S('ff', fontName=FNB, fontSize=FS_FORM, leading=16, textColor=WHITE, alignment=TA_CENTER)),
    ]], colWidths=[48*mm, UW-48*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),3*mm),('BOTTOMPADDING',(0,0),(-1,-1),3*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def pill(icon, text, bg=GREEN_L, fg=GREEN_D):
    t = Table([[P(f'{icon}  {_fix(text)}',
                  S('pi', fontName=FNB, fontSize=FS_SMALL, leading=13, textColor=fg))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('BOX',(0,0),(-1,-1),0.6,fg),
    ]))
    return t

def note_box(title, items, bg_h=AMBER, bg_b=AMBER_L, icon='📌'):
    rows = [[P(f'{icon}  {title}',
               S('nt', fontName=FNB, fontSize=FS_SMALL, leading=13, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'↳  {_fix(item)}', S('ni', fontName=FN, fontSize=FS_CELL, leading=14, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_h),('BACKGROUND',(0,1),(-1,-1),bg_b),
        ('BOX',(0,0),(-1,-1),1,bg_h),('LINEBELOW',(0,0),(0,0),1,bg_h),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t

def dyk(items, hbg=PURPLE_D, bg=PURPLE_L):
    rows = [[P('💡 Did You Know?',
               S('dk', fontName=FNB, fontSize=FS_SMALL, leading=13, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'◆  {_fix(item)}', S('di', fontName=FN, fontSize=FS_CELL, leading=14, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),hbg),('BACKGROUND',(0,1),(-1,-1),bg),
        ('BOX',(0,0),(-1,-1),1,hbg),('LINEBELOW',(0,0),(0,0),1,hbg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t

def two_col(L, R):
    def mk(items):
        return [P(_fix(x)) if isinstance(x,str) else x for x in items]
    t = Table([[mk(L), mk(R)]], colWidths=[CW, CW])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('INNERGRID',(0,0),(-1,-1),0,WHITE),('BOX',(0,0),(-1,-1),0,WHITE),
    ]))
    return t

def prob(num, q, given, soln, ans):
    rows = [
        [P(f'Problem {num}', S('pt', fontName=FNB, fontSize=FS_CELL, textColor=BLUE_D)), P(q, BD)],
        [P('Given', CEB), P(_fix(given), CE)],
        [P('Solution', CEB), P(_fix(soln), CE)],
        [P('Answer', S('pa', fontName=FNB, fontSize=FS_CELL, textColor=GREEN_D)),
         P(f'<b><font color="#14532D">{_fix(ans)}</font></b>', CE)],
    ]
    t = Table(rows, colWidths=[24*mm, UW-24*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),BLUE_L),('BACKGROUND',(0,-1),(-1,-1),GREEN_L),
        ('BOX',(0,0),(-1,-1),1,BLUE_D),('INNERGRID',(0,0),(-1,-1),0.3,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

def rapid_nums(rows):
    return grid(['Quantity / Concept','Formula / Value','Unit / Note'], rows,
                ws=[60*mm,74*mm,40*mm], hbg=TEAL_D)

def rapid_ppl(rows):
    return grid(['Scientist / Event','Contribution / Fact','Year / Class'], rows,
                ws=[50*mm,86*mm,38*mm], hbg=PURPLE_D)

def gloss_2col(terms):
    rows = []
    for i in range(0, len(terms), 2):
        L = P(f'<b>{terms[i][0]}</b> — {terms[i][1]}', MIN)
        R = P(f'<b>{terms[i+1][0]}</b> — {terms[i+1][1]}', MIN) if i+1<len(terms) else P('',MIN)
        rows.append([L, R])
    t = Table(rows, colWidths=[CW, CW])
    t.setStyle(TableStyle([
        ('GRID',(0,0),(-1,-1),0.3,GRAY_M),('ROWBACKGROUNDS',(0,0),(-1,-1),[GRAY_L,WHITE]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t


# ═══════════════════════════════════════════════════════════════════════════════
def content():
    s = []

    # BANNER
    s += [banner('P1','Measurement','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  MEASUREMENT — Definition & Need
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  MEASUREMENT — Definition & Need'), sp(2)]

    s += [kv_list([
        ('Measurement',         'Comparison of an unknown quantity with a known standard quantity — result has TWO parts: a number and a unit'),
        ('Need for Measurement','For uniformity and accuracy across countries, scientists adopted a common system (SI System)'),
        ('Physical Quantity',   'Any quantity that can be measured — e.g., length, mass, time, temperature, current'),
        ('Fundamental Quantity','Independent physical quantity that cannot be derived from others — 7 in SI system'),
        ('Derived Quantity',    'Quantity derived from fundamental quantities — e.g., area = length × length; speed = length/time'),
        ('Unit',                'Known standard used for comparison in measurement — e.g., metre, kilogram, second'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  UNIT SYSTEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  UNIT SYSTEMS — FPS, CGS, MKS & SI'), sp(2)]

    s += [grid(
        ['System','Full Form','Length','Mass','Time','Type / Notes'],
        [
            ['FPS','Foot-Pound-Second','Foot (ft)','Pound (lb)','Second (s)','British system — NOT a metric system'],
            ['CGS','Centimetre-Gram-Second','Centimetre (cm)','Gram (g)','Second (s)','Metric system'],
            ['MKS','Metre-Kilogram-Second','Metre (m)','Kilogram (kg)','Second (s)','Metric system — precursor to SI'],
            ['SI','Systeme International\n(International System)','Metre (m)','Kilogram (kg)','Second (s)','Metric — universally accepted; adopted in 1960 at Paris'],
        ],
        ws=[14*mm,46*mm,26*mm,24*mm,18*mm,46*mm]
    ), sp(2)]

    s += [pill('⚠', 'FPS = British system (NOT metric). CGS, MKS, SI = metric systems. TET exams test this difference!', ORANGE_L, ORANGE)]
    s += [sp(2)]

    s += [dyk([
        'In December 1998, NASA\'s Mars Climate Orbiter (worth $125 million) was lost because one team used FPS units and another used MKS units — unit mismatch caused the spacecraft to approach Mars at wrong altitude and crash.',
        'SI stands for "Systeme International" — French words. The system was established at the 11th General Conference on Weights and Measures in Paris, France in 1960.',
        'The metric system was created by the French in 1790.',
    ])]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  SI BASE QUANTITIES — All 7
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  SI BASE QUANTITIES — All 7 Fundamental Units'), sp(2)]

    s += [grid(
        ['Quantity','SI Unit','Symbol','Measuring Instrument','Class'],
        [
            ['Length',             'metre',    'm',   'Ruler / Scale / Metre rod / Vernier calliper / Screw gauge', '6,7,8'],
            ['Mass',               'kilogram', 'kg',  'Beam balance / Electronic balance / Spring balance',         '6,7,8'],
            ['Time',               'second',   's',   'Clock / Stopwatch / Pendulum',                               '6,7,8'],
            ['Temperature',        'kelvin',   'K',   'Thermometer (clinical, lab, digital)',                       '8'],
            ['Electric Current',   'ampere',   'A',   'Ammeter',                                                    '8'],
            ['Amount of Substance','mole',     'mol', 'Calculated from mass and molar mass',                        '8'],
            ['Luminous Intensity', 'candela',  'cd',  'Photometer (Luminous Intensity Meter)',                      '8'],
        ],
        ws=[36*mm,26*mm,16*mm,68*mm,16*mm]
    ), sp(2)]

    s += [sub_h('Supplementary Quantities — Plane Angle & Solid Angle'), sp(1)]
    s += [grid(
        ['Quantity','Definition','SI Unit','Symbol','Dimension'],
        [
            ['Plane Angle', 'Angle at intersection of two straight lines or planes',
             'radian','rad','2D — two dimensional'],
            ['Solid Angle', 'Angle at intersection of three or more planes at a common point; also = angle at vertex of a cone',
             'steradian','sr','3D — three dimensional'],
        ],
        ws=[30*mm,68*mm,24*mm,18*mm,34*mm]
    ), sp(1)]

    s += [one_liners([
        'π radian = 180°  |  1 radian = 180°/π  |  1° = π/180 radian',
        'Radian: angle at centre of circle where arc length = radius of circle',
        'Steradian: solid angle at centre of sphere where surface area = (radius)²',
        'Until 1995, plane angle and solid angle were "supplementary quantities" — reclassified as derived quantities in 1995',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  LENGTH — Conversions, Instruments, Errors
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  LENGTH — Units, Conversions & Measurement'), sp(2)]

    s += [sub_h('Length Conversions — Memorise All'), sp(1)]
    s += [grid(
        ['Conversion','Value','Direction'],
        [
            ['1 km  →  m',      '1,000 m (10<super>3</super> m)',         'km to m: × 1000'],
            ['1 m   →  cm',     '100 cm (10<super>2</super> cm)',          'm to cm: × 100'],
            ['1 cm  →  mm',     '10 mm',                                   'cm to mm: × 10'],
            ['1 m   →  mm',     '1,000 mm',                               'm to mm: × 1000'],
            ['1 km  →  cm',     '1,00,000 cm (10<super>5</super> cm)',    'km to cm: × 100,000'],
            ['1 km  →  mm',     '10,00,000 mm (10<super>6</super> mm)',   'km to mm: × 1,000,000'],
            ['1 nautical mile', '= 1.852 km',                              'Sea/air navigation'],
        ],
        ws=[40*mm,60*mm,74*mm]
    ), sp(2)]

    s += [sub_h('SI Prefixes — Multiples & Submultiples'), sp(1)]
    s += [grid(
        ['Prefix','Symbol','Meaning','Value','For Metre'],
        [
            ['Nano',  'n', 'Submultiple: 1/10<super>9</super>', '10<super>-9</super>',  '1,000,000,000 nm = 1 m'],
            ['Micro', 'μ', 'Submultiple: 1/10<super>6</super>', '10<super>-6</super>',  '10,00,000 μm = 1 m'],
            ['Milli', 'm', 'Submultiple: 1/1,000',              '10<super>-3</super>',  '1,000 mm = 1 m'],
            ['Centi', 'c', 'Submultiple: 1/100',                '10<super>-2</super>',  '100 cm = 1 m'],
            ['Deci',  'd', 'Submultiple: 1/10',                 '10<super>-1</super>',  '10 dm = 1 m'],
            ['Kilo',  'k', 'Multiple: 1,000',                   '10<super>3</super>',   '1 km = 1,000 m'],
            ['Mega',  'M', 'Multiple: 10,00,000',               '10<super>6</super>',   '1 Mm = 10<super>6</super> m'],
        ],
        ws=[24*mm,18*mm,50*mm,28*mm,54*mm]
    ), sp(2)]

    s += [sub_h('Measuring Instruments for Length'), sp(1)]
    s += [one_liners([
        ('Metre Scale / Ruler',   'Measures straight lengths — range: 0 to 15 cm (small) or 0 to 30 cm (large) or 1 metre'),
        ('Measuring Tape',        'Flexible tape for curved body measurements (chest, waist) — used by tailors; not for straight lines'),
        ('Divider Method',        'Measures curved lines by stepping equal segments along the curve then counting segments × length'),
        ('String Method',         'Place string along curved line, straighten it, then measure with ruler — finds length of curved line'),
        ('Vernier Callipers',     'Precise measurement of small lengths, inner/outer diameters — least count = 0.1 mm'),
        ('Screw Gauge',           'Very precise measurement of thin wires, thickness of paper — least count = 0.01 mm'),
        ('Odometer',              'Device on automobiles that indicates total distance travelled by the vehicle'),
    ]), sp(2)]

    s += [sub_h('Measurement Errors & Corrections'), sp(1)]
    s += [one_liners([
        ('Parallax Error',     'Error due to incorrect eye position — eye must be VERTICALLY ABOVE the measurement point, not tilted'),
        ('Zero Error',         'Error when the instrument does not read zero when nothing is measured — must be corrected before use'),
        ('Correct method',     'Head of object at zero of scale | Eye vertically above | Count cm then mm from the end'),
        'Never hold the thermometer by the bulb; never heat it in flame or sun (for temperature instruments)',
        'Always keep object PARALLEL to the scale when measuring length',
        'Standard metre rod: made of platinum-iridium alloy at Bureau of Weights and Measures, Paris, France',
        'India\'s copy of standard metre rod is at the National Physical Laboratory (NPL), New Delhi',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  MASS — Units, Instruments
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  MASS — Definition, Units & Instruments'), sp(2)]

    s += [kv_list([
        ('Mass',          'Measure of the amount of matter in an object — SI unit: kilogram (kg) — does NOT change with location'),
        ('Weight',        'Gravitational pull experienced by matter — Weight = mass × g — changes with location (moon vs earth)'),
        ('Key Difference','Mass = constant everywhere | Weight = varies (1/6 on Moon vs Earth)'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Mass Conversions'), sp(1)]
    s += [grid(
        ['Conversion','Value'],
        [
            ['1 kg  →  g',    '1,000 g'],
            ['1 g   →  mg',   '1,000 mg'],
            ['1 tonne → kg',  '1,000 kg'],
            ['1 quintal → kg','100 kg'],
            ['Standard 1 kg', 'Mass of platinum-iridium bar at International Bureau of Weights and Measures, Sèvres, France (since 1889)'],
        ],
        ws=[40*mm,134*mm]
    ), sp(2)]

    s += [sub_h('Instruments for Mass Measurement'), sp(1)]
    s += [one_liners([
        ('Beam Balance',      'Compares unknown mass with known standard masses — works by equilibrium principle'),
        ('Electronic Balance','Precise digital measurement — used in laboratories for chemicals, in shops for groceries and jewellery'),
        ('Spring Balance',    'Uses spring extension to measure weight (in Newtons) — not for precise mass measurement'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  TIME — Units, Clocks
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  TIME — Units, Instruments & Clock Types'), sp(2)]

    s += [sub_h('Time Units & Conversions'), sp(1)]
    s += [grid(
        ['Conversion','Value'],
        [
            ['1 minute',  '= 60 seconds'],
            ['1 hour',    '= 60 minutes = 3,600 seconds'],
            ['1 day',     '= 24 hours = 86,400 seconds'],
            ['1 year',    '= 365 days = 8,760 hours'],
            ['SI Unit',   'Second (s) — represented as \'s\''],
        ],
        ws=[36*mm,138*mm]
    ), sp(2)]

    s += [sub_h('Types of Clocks (Class 8 — Section 1.3)'), sp(1)]

    s += [two_col(
        ['<b>By Display Type:</b>',
         '',
         '<b>Analog Clock</b>',
         '▶ Classic clock with three hands',
         '▶ Hours hand — short and thick',
         '▶ Minutes hand — long and thin',
         '▶ Seconds hand — long, very thin; makes 1 rotation per minute; 60 rotations per hour',
         '▶ Driven by mechanical or electronic mechanism',
         '',
         '<b>Digital Clock</b>',
         '▶ Shows time directly in numerals or symbols',
         '▶ May display 12-hour or 24-hour format',
         '▶ Modern digital clocks show date, day, month, year, temperature'],
        ['<b>By Working Mechanism:</b>',
         '',
         '<b>Quartz Clock</b>',
         '▶ Uses electronic oscillations controlled by a quartz crystal (SiO2)',
         '▶ Crystal vibration frequency is very precise',
         '▶ More accurate than mechanical clocks',
         '▶ Accuracy: 1 second error per 10<super>9</super> seconds',
         '',
         '<b>Atomic Clock</b>',
         '▶ Uses periodic vibrations occurring within atoms',
         '▶ Most accurate clock ever made',
         '▶ Accuracy: 1 second error per 10<super>13</super> seconds',
         '▶ Used in GPS, GLONASS, International Time Distribution Services']
    ), sp(2)]

    s += [sub_h('Historical & Special Timekeeping'), sp(1)]
    s += [one_liners([
        'Ancient time measurement: sand clock (hourglass) and sundial — used during daytime',
        'Pulse measurement: counting heartbeats (≈75/min) gives approximate time elapsed',
        ('GMT', 'Greenwich Mean Time — mean solar time at Royal Observatory, Greenwich, London (0° longitude)'),
        ('IST', 'Indian Standard Time = GMT + 5:30 hours | Reference: Mirzapur, Uttar Pradesh (82.5°E longitude)'),
        ('Time Zones', 'Earth divided into 24 zones × 15° longitude each | Difference between adjacent zones = 1 hour'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  ADDITIONAL SI BASE QUANTITIES
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  Additional Base Quantities — Temperature, Current, Mole, Candela'), sp(2)]

    s += [one_liners([
        ('Temperature',        'Measure of average KE of particles — degree of hotness/coldness — SI unit: kelvin (K) — measured by thermometer'),
        ('Electric Current (I)','Flow of electric charges in a direction | I = Q/t (charge/time) — SI unit: ampere (A) — measured by ammeter'),
        ('1 Ampere',           'If 1 coulomb of charge flows through conductor in 1 second → current = 1 ampere'),
        ('Amount of Substance','Measure of number of entities (atoms, molecules, ions) — SI unit: mole (mol)'),
        ('1 Mole',             '= 6.023 × 10<super>23</super> entities — known as Avogadro Number — mole is used because atoms are too small to count individually'),
        ('Luminous Intensity', 'Measure of power of emitted light in a particular direction per unit solid angle — SI unit: candela (cd)'),
        ('1 Candela',          '≈ light emitted by one common wax candle — measured by photometer (Luminous Intensity Meter)'),
        ('Luminous Flux',      'Measure of total perceived power of light — SI unit: lumen (lm)'),
        ('Calibration',        'Process of configuring an instrument to measure accurately within a specific range'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  ACCURACY, PRECISION & APPROXIMATION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  Accuracy, Precision, Approximation & Rounding Off'), sp(2)]

    s += [grid(
        ['Concept','Definition','Example / Remember'],
        [
            ['Error',        'Difference between the real (true) value and the observed (measured) value',
             'Every measurement has some uncertainty — cannot be completely eliminated'],
            ['Accuracy',     'Closeness of a measured value to the actual/true value',
             'Arrows all hitting bullseye = accurate AND precise (best case)'],
            ['Precision',    'Closeness of two or more measurements to EACH OTHER (repeatability)',
             'Arrows all hitting same spot (but not centre) = precise but NOT accurate'],
            ['Approximation','Finding a number acceptably close to exact value by estimation — used when data is inadequate',
             'Heart beats ≈ 75/min → in a day ≈ 75 × 60 × 24 = 1,08,000 beats (approximate)'],
            ['Rounding Off', 'Technique to reduce digits in a result to manageable number',
             '1.864 → 1.86 (next digit < 5, keep 6) | 1.868 → 1.87 (next digit > 5, increase 6 to 7)'],
        ],
        ws=[28*mm,72*mm,74*mm]
    ), sp(2)]

    s += [sub_h('Rules for Rounding Off'), sp(1)]
    s += [one_liners([
        'Step 1: Decide which is the LAST DIGIT to keep',
        'Step 2: If the NEXT digit is less than 5 → keep last digit SAME',
        'Step 3: If the NEXT digit is 5 or greater than 5 → INCREASE last digit by 1',
        'Example: Round 4.582 to 2 decimal places → last digit = 8, next = 2 (< 5) → answer: 4.58',
        'Example: Round 4.586 to 2 decimal places → last digit = 8, next = 6 (> 5) → answer: 4.59',
    ]), sp(2)]

    s += [note_box('Accuracy vs Precision — TET Trap', [
        'Accurate = close to TRUE value | Precise = close to EACH OTHER (can be precise but wrong!)',
        'Good precision + good accuracy = all arrows at bullseye (ideal measurement)',
        'Good precision + poor accuracy = arrows clustered together but far from centre',
        'Poor precision + poor accuracy = arrows scattered AND far from centre',
    ], icon='📌')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  Solved Numerical Problems'), sp(2)]

    probs = [
        ('1', 'The distance between two cities is 43.65 km. Convert to metres and centimetres.',
         'd = 43.65 km',
         'In metres: 43.65 × 1000 = 43,650 m  |  In cm: 43,650 × 100 = 43,65,000 cm',
         '43,650 m  =  43,65,000 cm'),
        ('2', 'Length of pencil: scale reading at one end = 2.0 cm, other end = 12.1 cm. Find length.',
         'Reading 1 = 2.0 cm; Reading 2 = 12.1 cm',
         'Length = 12.1 – 2.0 = 10.1 cm',
         '10.1 cm  =  101 mm'),
        ('3', 'Distance from school to home = 2250 m. Express in kilometres.',
         'd = 2250 m',
         'd in km = 2250 / 1000 = 2.250 km',
         '2.25 km'),
        ('4', 'Convert 60° into radians.',
         '1° = π/180 radian',
         '60° = π/180 × 60 = π/3 radian = 3.14/3 ≈ 1.047 rad',
         'π/3 radian  ≈  1.047 rad'),
        ('5', 'If 2 coulombs of charge flows through a circuit for 10 seconds, calculate the current.',
         'Q = 2 C; t = 10 s',
         'I = Q/t = 2/10 = 0.2 A',
         'Current = 0.2 Ampere'),
        ('6', 'Round off 7875 cm to km and m.',
         '7875 cm',
         '7875 cm ÷ 100 = 78.75 m  →  78 m 75 cm  |  78.75 m ÷ 1000 = 0.07875 km',
         '78 m 75 cm  =  0.07875 km'),
    ]

    for p in probs:
        s += [prob(*p), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Values, Formulas & Unit Conversions</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Measurement',              'Number + Unit (two parts)',                           'e.g., 5 kg; 3 metres'],
        ['1 km',                     '= 1,000 m = 1,00,000 cm = 10,00,000 mm',            'Length'],
        ['1 m',                      '= 100 cm = 1,000 mm',                                'Length'],
        ['1 kg',                     '= 1,000 g  |  1,000 kg = 1 tonne',                  'Mass'],
        ['1 hour',                   '= 3,600 s  |  1 day = 86,400 s',                    'Time'],
        ['π radian',                 '= 180°  →  1° = π/180 rad',                         'Plane angle'],
        ['Avogadro Number',          '6.023 × 10<super>23</super> per mole',               'Amount of substance'],
        ['1 candela',                '≈ light of one common wax candle',                   'Luminous intensity'],
        ['Electric current',         'I = Q/t  (charge/time)',                             'Ampere (A)'],
        ['1 Ampere',                 '= 1 coulomb per second',                             'Definition'],
        ['Quartz clock accuracy',    '1 second error per 10<super>9</super> seconds',      'Class 8'],
        ['Atomic clock accuracy',    '1 second error per 10<super>13</super> seconds',     'Class 8 — most accurate'],
        ['IST',                      'GMT + 5:30 hours  |  Reference: 82.5°E longitude',  'Mirzapur, UP'],
        ['Time zone width',          '15° longitude = 1 hour difference',                  '24 zones for 360°'],
        ['Body temperature',         '37°C = 98.6°F = 310.15 K',                          'Normal human'],
        ['Rounding: next digit < 5', 'Keep last digit SAME',                               'Rule'],
        ['Rounding: next digit ≥ 5', 'Increase last digit by 1',                           'Rule'],
    ]), sp(3)]

    s += [P('<b>Scientists, Events & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['SI System established',  '11th General Conference on Weights & Measures, Paris, France', '1960 '],
        ['Metric system created',  'French scientists established the metric system',              '1790 '],
        ['Standard metre rod',     'Platinum-iridium alloy at Bureau of Weights & Measures, Paris; India\'s copy at NPL, New Delhi', 'Cl. 6'],
        ['Standard 1 kg',          'Platinum-iridium bar at International Bureau of Weights & Measures, Sèvres, France',             '1889 '],
        ['Ruler inventor',         'William Bedwell invented the ruler in the 16th century',       '16th century '],
        ['Odometer',               'Device indicating distance travelled by automobile',            'Cl. 6'],
        ['Mars Orbiter disaster',  'NASA lost $125M Mars Climate Orbiter due to FPS vs MKS unit mismatch between two teams', 'Sept 23, 1999 '],
        ['GMT reference',          'Greenwich Mean Time at Royal Observatory, Greenwich, London at 0° longitude', 'Cl. 8'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Measurement',          'Comparison of unknown quantity with known standard; result has number + unit'),
        ('Physical Quantity',    'Any quantity that can be measured — e.g., length, mass, time, temperature'),
        ('Fundamental Quantity', 'Independent physical quantity — 7 in SI: length, mass, time, temp, current, amount, luminous intensity'),
        ('Derived Quantity',     'Quantity derived from fundamental quantities — e.g., area, volume, density, speed'),
        ('SI System',            'International System of Units — "Systeme International" — adopted in 1960 at Paris'),
        ('FPS System',           'British system: Foot, Pound, Second — NOT a metric system'),
        ('CGS System',           'Metric system: Centimetre, Gram, Second'),
        ('MKS System',           'Metric system: Metre, Kilogram, Second — precursor to SI'),
        ('Metre (m)',             'SI unit of length'),
        ('Kilogram (kg)',         'SI unit of mass'),
        ('Second (s)',            'SI unit of time'),
        ('Kelvin (K)',            'SI unit of temperature'),
        ('Ampere (A)',            'SI unit of electric current — 1 A = 1 coulomb per second'),
        ('Mole (mol)',            'SI unit of amount of substance — 1 mol = 6.023 × 10<super>23</super> entities (Avogadro Number)'),
        ('Candela (cd)',          'SI unit of luminous intensity — ≈ light from one wax candle'),
        ('Radian (rad)',          'SI unit of plane angle — angle where arc length = radius of circle'),
        ('Steradian (sr)',        'SI unit of solid angle — 3D angle at vertex of cone / intersection of 3+ planes'),
        ('Parallax Error',       'Error due to eye not being directly above measurement point — eye displacement causes wrong reading'),
        ('Zero Error',           'Instrument error when it does not read zero before measurement begins — must be subtracted or added'),
        ('Accuracy',             'Closeness of measured value to the true value'),
        ('Precision',            'Closeness of two or more measurements to each other — repeatability'),
        ('Approximation',        'Process of finding a value acceptably close to exact value by estimation'),
        ('Rounding Off',         'Reducing digits in a number: if next digit < 5, keep same; if ≥ 5, increase by 1'),
        ('Calibration',          'Process of configuring an instrument to measure accurately within a specific range'),
        ('Beam Balance',         'Instrument to measure mass by comparing unknown mass with known standard masses'),
        ('Electronic Balance',   'Precise digital instrument for measuring mass — used in labs and shops'),
        ('Vernier Callipers',    'Precise instrument to measure small lengths — least count = 0.1 mm'),
        ('Screw Gauge',          'Very precise instrument for measuring thin wires — least count = 0.01 mm'),
        ('Odometer',             'Device in automobiles that records total distance travelled'),
        ('Quartz Clock',         'Clock using electronic oscillations from quartz crystal — accuracy: 1s error per 10<super>9</super> s'),
        ('Atomic Clock',         'Most accurate clock using atomic vibrations — accuracy: 1s error per 10<super>13</super> s; used in GPS'),
        ('GMT',                  'Greenwich Mean Time — mean solar time at Royal Observatory, London, at 0° longitude'),
        ('IST',                  'Indian Standard Time = GMT + 5:30 hours; reference: Mirzapur (82.5°E), Uttar Pradesh'),
        ('Avogadro Number',      '6.023 × 10<super>23</super> — number of atoms/molecules in one mole of any substance'),
        ('Photometer',           'Instrument to measure luminous intensity in candela'),
        ('Ammeter',              'Instrument to measure electric current in ampere — connected in series in a circuit'),
    ]

    s += [gloss_2col(g), sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P1: Measurement  |  Classes 6 • 7 • 8',
          S('ft', fontName=FNI, fontSize=8.5, textColor=TEAL, alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P1  |  Measurement  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P1 Measurement',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P1_Measurement.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
