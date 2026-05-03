"""
TET Paper II Science Handbook — P3: Heat & Temperature  VERSION 1
Style: One-liner / cheat-sheet guide format
Tables ≤ 50-60% of page space
All Class 6 (Term II, Unit 1), Class 7 (Term II, Unit 1), Class 8 (Unit 4) sub-topics
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

CHAPTER_ID = "P3"
CHAPTER_TITLE = "Heat & Temperature"
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

def S(nm, **kw): return ParagraphStyle(nm, **kw)

BD   = S('bd',  fontName=FN,  fontSize=8.5, leading=12.5, textColor=GRAY_D, spaceAfter=2)
BDB  = S('bdb', fontName=FNB, fontSize=8.5, leading=12.5, textColor=SLATE)
CE   = S('ce',  fontName=FN,  fontSize=7.8, leading=11.5, textColor=GRAY_D)
CEB  = S('ceb', fontName=FNB, fontSize=7.8, leading=11.5, textColor=SLATE)
HWC  = S('hwc', fontName=FNB, fontSize=7.5, leading=10,   textColor=WHITE, alignment=TA_CENTER)
SC   = S('sc',  fontName=FNB, fontSize=10,  leading=14,   textColor=WHITE)
MIN  = S('mn',  fontName=FN,  fontSize=7.3, leading=10.5, textColor=GRAY_D)
MINB = S('mb',  fontName=FNB, fontSize=7.3, leading=10.5, textColor=SLATE)

sp = lambda h: Spacer(1, h*mm)
P  = lambda t, st=BD: Paragraph(t, st)

# ── UNICODE FIXER ─────────────────────────────────────────────────────────────
_SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4',
        '\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9',
        '\u207b':'-','\u207a':'+'}
_SUB = {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4',
        '\u2085':'5','\u2086':'6','\u2087':'7','\u2088':'8','\u2089':'9'}
def _fix(text):
    import re as _re
    sc = ''.join(_SUP.keys()); bc = ''.join(_SUB.keys())
    def rs(m): return '<super>'+''.join(_SUP.get(c,c) for c in m.group())+'</super>'
    def rb(m): return '<sub>'  +''.join(_SUB.get(c,c) for c in m.group())+'</sub>'
    t = _re.sub(f'[{_re.escape(sc)}]+', rs, text)
    t = _re.sub(f'[{_re.escape(bc)}]+', rb, t)
    return t

# ─── PRIMITIVE BUILDERS ───────────────────────────────────────────────────────

def banner(code, title, sub=''):
    data = [[
        P(f'<font color="white"><b>{code}</b></font>',
          S('bu', fontName=FNB, fontSize=24, leading=28, textColor=WHITE, alignment=TA_CENTER)),
        [P(f'<font color="white"><b>{title}</b></font>',
           S('bt', fontName=FNB, fontSize=15, leading=20, textColor=WHITE)),
         P(f'<font color="#5EEAD4">{sub}</font>' if sub else '',
           S('bs', fontName=FNI, fontSize=8.5, leading=11, textColor=TEAL_M)),
         sp(1),
         P('<font color="#CCFBF1">Classes 6 • 7 • 8  |  TET Paper II Science</font>',
           S('bi', fontName=FN, fontSize=7.5, leading=10, textColor=TEAL_L))]
    ]]
    t = Table(data, colWidths=[26*mm, UW-26*mm])
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
    t = Table([[P(title, S('sh', fontName=FNB, fontSize=8.5, leading=11.5, textColor=WHITE))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
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
        data.append([P(_fix(c), CE) if isinstance(c,str) else c for c in row])
    t = Table(data, colWidths=ws, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),('GRID',(0,0),(-1,-1),0.35,GRAY_M),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),2*mm),('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[alt,WHITE]),
    ]))
    return t

# ONE-LINER LIST — the signature format of this chapter
def one_liners(items, bg_bullet=TEAL, bg_body=TEAL_L, key_w=52*mm):
    """Compact one-liner rows.
    Plain string  -> [▶ bullet (5mm)] [text]
    Tuple (k, v)  -> [bold key (key_w)] [value]  — separate widths to avoid vertical text
    """
    # Separate pure-bullet rows from key-value rows and build two tables
    # This avoids mixing column widths in one Table (which forces all rows to same widths)
    result_tables = []
    current_bullet_rows = []
    current_kv_rows = []

    def flush_bullets():
        if not current_bullet_rows:
            return
        t = Table(current_bullet_rows, colWidths=[5*mm, UW-5*mm])
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),1.5*mm),('RIGHTPADDING',(0,0),(-1,-1),2*mm),
            ('TOPPADDING',(0,0),(-1,-1),1*mm),('BOTTOMPADDING',(0,0),(-1,-1),1*mm),
            ('LINEBELOW',(0,0),(-1,-2),0.25,GRAY_M),
        ]))
        result_tables.append(t)

    def flush_kvs():
        if not current_kv_rows:
            return
        t = Table(current_kv_rows, colWidths=[key_w, UW-key_w])
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(0,-1),TEAL),
            ('BACKGROUND',(1,0),(1,-1),TEAL_L),
            ('BOX',(0,0),(-1,-1),0.6,TEAL),
            ('LINEAFTER',(0,0),(0,-1),0.6,TEAL),
            ('LINEBELOW',(0,0),(-1,-2),0.25,GRAY_M),
            ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
            ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ]))
        result_tables.append(t)

    prev_type = None
    for item in items:
        if isinstance(item, tuple):
            if prev_type == 'bullet':
                flush_bullets()
                current_bullet_rows = []
            key, val = item
            current_kv_rows.append([
                P(f'<b>{key}</b>', S('ok', fontName=FNB, fontSize=8, leading=11, textColor=WHITE)),
                P(_fix(val),        S('ov', fontName=FN,  fontSize=8, leading=11, textColor=SLATE)),
            ])
            prev_type = 'kv'
        else:
            if prev_type == 'kv':
                flush_kvs()
                current_kv_rows = []
            current_bullet_rows.append([
                P('▶', S('ob', fontName=FNB, fontSize=8, leading=11, textColor=bg_bullet, alignment=TA_CENTER)),
                P(_fix(item), S('oi', fontName=FN, fontSize=8, leading=11, textColor=SLATE)),
            ])
            prev_type = 'bullet'

    flush_bullets()
    flush_kvs()

    # If only one table, return it directly; else wrap in a container
    if len(result_tables) == 1:
        return result_tables[0]
    # Wrap multiple tables in a single-col Table
    wrapper = Table([[t] for t in result_tables], colWidths=[UW])
    wrapper.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),1*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return wrapper

def kv_list(items, bg_L=TEAL, bg_R=TEAL_L, w_L=48*mm):
    """Key-Value rows: coloured label | value — compact cheat style"""
    rows = []
    for key, val in items:
        rows.append([
            P(key, S('kl', fontName=FNB, fontSize=8, leading=11, textColor=WHITE)),
            P(_fix(val), S('kr', fontName=FN, fontSize=8, leading=11, textColor=SLATE)),
        ])
    t = Table(rows, colWidths=[w_L, UW-w_L])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,-1),bg_L),
        ('BACKGROUND',(1,0),(1,-1),bg_R),
        ('BOX',(0,0),(-1,-1),0.6,bg_L),
        ('LINEAFTER',(0,0),(0,-1),0.6,bg_L),
        ('LINEBELOW',(0,0),(-1,-2),0.25,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def fstrip(label, formula, note='', bg=BLUE_D):
    note_t = f'  <font size="7" color="#94A3B8">({_fix(note)})</font>' if note else ''
    t = Table([[
        P(label, S('fl', fontName=FNB, fontSize=8, leading=11, textColor=TEAL_M)),
        P(f'<b><font color="white">{_fix(formula)}</font></b>{note_t}',
          S('ff', fontName=FNB, fontSize=10, leading=13, textColor=WHITE, alignment=TA_CENTER)),
    ]], colWidths=[46*mm, UW-46*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def pill(icon, text, bg=GREEN_L, fg=GREEN_D):
    t = Table([[P(f'{icon}  {_fix(text)}',
                  S('pi', fontName=FNB, fontSize=8.2, leading=11.5, textColor=fg))]],
              colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOX',(0,0),(-1,-1),0.6,fg),
    ]))
    return t

def note_box(title, items, bg_h=AMBER, bg_b=AMBER_L, icon='📌'):
    rows = [[P(f'{icon}  {title}',
               S('nt', fontName=FNB, fontSize=8.5, leading=11.5, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'↳  {_fix(item)}', S('ni', fontName=FN, fontSize=8, leading=11.5, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_h),('BACKGROUND',(0,1),(-1,-1),bg_b),
        ('BOX',(0,0),(-1,-1),1,bg_h),('LINEBELOW',(0,0),(0,0),1,bg_h),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

def dyk(items, hbg=PURPLE_D, bg=PURPLE_L):
    rows = [[P('💡 Did You Know?',
               S('dk', fontName=FNB, fontSize=8.5, leading=11.5, textColor=WHITE))]]
    for item in items:
        rows.append([P(f'◆  {_fix(item)}', S('di', fontName=FN, fontSize=8, leading=11.5, textColor=SLATE))])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),hbg),('BACKGROUND',(0,1),(-1,-1),bg),
        ('BOX',(0,0),(-1,-1),1,hbg),('LINEBELOW',(0,0),(0,0),1,hbg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
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
        [P(f'Problem {num}', S('pt', fontName=FNB, fontSize=8.5, textColor=BLUE_D)), P(q, BD)],
        [P('Given', CEB), P(_fix(given), CE)],
        [P('Solution', CEB), P(_fix(soln), CE)],
        [P('Answer', S('pa', fontName=FNB, fontSize=8.5, textColor=GREEN_D)),
         P(f'<b><font color="#14532D">{_fix(ans)}</font></b>', CE)],
    ]
    t = Table(rows, colWidths=[22*mm, UW-22*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),BLUE_L),('BACKGROUND',(0,-1),(-1,-1),GREEN_L),
        ('BOX',(0,0),(-1,-1),1,BLUE_D),('INNERGRID',(0,0),(-1,-1),0.3,GRAY_M),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

def rapid_nums(rows):
    return grid(['Quantity / Concept','Formula / Value','Unit / Note'], rows,
                ws=[60*mm,74*mm,40*mm], hbg=TEAL_D)

def rapid_ppl(rows):
    return grid(['Scientist','Contribution','Year / Class'], rows,
                ws=[46*mm,92*mm,36*mm], hbg=PURPLE_D)

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
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t


# ═══════════════════════════════════════════════════════════════════════════════
def content():
    s = []

    # BANNER
    s += [banner('P3','Heat & Temperature','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  HEATTerm II, Sections 1.1–1.3
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  HEAT — Definition, Sources & Flow'), sp(2)]

    s += [kv_list([
        ('Heat',          'Total Kinetic Energy of all constituent particles of an object — form of energy, not matter'),
        ('SI Unit',       'Joule (J)  |  also measured in calorie  |  1 calorie = 4.186 J'),
        ('Temperature',   'Average Kinetic Energy of molecules — measures warmness or coldness of a substance'),
        ('SI Unit (Temp)','Kelvin (K)  |  also °C (Celsius) and °F (Fahrenheit)'),
        ('Flow of Heat',  'Always flows from HIGHER temperature → LOWER temperature (like water from high to low level)'),
        ('Thermal Contact','Two bodies that can exchange heat energy with each other'),
        ('Thermal Equilibrium','Two bodies in thermal contact that NO longer affect each other\'s temperature — same temp reached'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Sources of Heat (Class 6 — Section 1.1)'), sp(1)]
    s += [one_liners([
        ('Sun',         'Primary source — gives heat besides light; barefoot walking on sunny afternoon is difficult'),
        ('Combustion',  'Burning of fuels: wood, kerosene, coal, charcoal, petrol, LPG → produces heat energy'),
        ('Friction',    'Rubbing two surfaces → heat generated (e.g., ancient humans rubbed stones to make fire)'),
        ('Electricity', 'Current through conductor → heat (water heater, iron box, electric kettle work on this principle)'),
    ]), sp(2)]

    # Heat vs Temperature
    s += [sub_h('Heat vs Temperature — The Key Distinction (Class 6 — Section 1.5)'), sp(1)]
    s += [one_liners([
        'Heat = TOTAL KE of all molecules  |  Temperature = AVERAGE KE of molecules',
        'Same temperature (100°C) — 5L boiling water has MORE HEAT than 1L boiling water (more molecules)',
        'Pond water has more HEAT than a hot cup of tea (despite tea\'s higher temperature) — much larger volume',
        'Heat depends on: (1) Temperature of substance  (2) Number of molecules present (mass/volume)',
        'Sense of touch is NOT reliable to measure temperature — use a thermometer',
        'Neela\'s mistake: 80°C + 80°C ≠ 160°C — mixing equal volumes gives ~80°C (not additive)',
    ]), sp(2)]

    s += [note_box('Common Exam Traps — Heat & Temperature', [
        'Heat and temperature are NOT the same — different units, different definitions.',
        'Heat flows from high temperature → low temperature, NOT from more heat → less heat.',
        'When two bodies reach thermal equilibrium, heat flow STOPS — both at same temperature.',
        'Adding two volumes of 80°C water does NOT give 160°C — temperature stays ~80°C.',
    ], icon='⚠')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  THERMOMETERTerm II, Sections 1.3–1.5
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  THERMOMETER — Types, Scales & Conversion'), sp(2)]

    s += [sub_h('Thermometric Liquids — Mercury vs Alcohol'), sp(1)]
    s += [grid(
        ['Property','Mercury (Hg)','Alcohol'],
        [
            ['Appearance',       'Opaque, shining silver',           'Transparent — coloured brightly for visibility'],
            ['Boiling Point',    '357°C (high — wide range)',        '78°C (low — cannot measure high temperatures)'],
            ['Freezing Point',   '-39°C',                            '-100°C or lower (ideal for very cold temperatures)'],
            ['Stickiness',       'Does NOT stick to glass walls',    'May slightly wet glass'],
            ['Expansion',        'Uniform expansion (equal per °C)','Larger expansion per °C (more sensitive to change)'],
            ['Heat conduction',  'Good conductor of heat',           'Poor conductor of heat'],
            ['Suitable for',     'Wide range; clinical & lab use',  'Very low temperatures (Arctic, polar regions)'],
        ],
        ws=[34*mm,70*mm,70*mm]
    ), sp(2)]

    s += [sub_h('Types of Thermometers (Class 7 — Section 1.4.1 & 1.4.2)'), sp(1)]
    s += [one_liners([
        ('Clinical Thermometer',   'Measures human body temperature | range: 35°C to 42°C (94°F to 108°F)'),
        ('Kink in Clinical Therm.','Prevents mercury from flowing back into bulb after removal from patient\'s mouth'),
        ('Reading clinical therm.','Body temperature normally measured in °F (Fahrenheit more sensitive than Celsius)'),
        ('Lab Thermometer',        'Measures higher temperatures for scientific research and industry — longer stem/bulb'),
        ('Precaution',             'Never hold thermometer by bulb | Jerk it down before use | Do not heat in flame/sun'),
    ]), sp(2)]

    s += [sub_h('Temperature Scales — Celsius, Fahrenheit & Kelvin (Class 7 — Section 1.5)'), sp(1)]

    # Scale comparison table
    s += [grid(
        ['Scale','Inventor / Named After','Freezing Pt of Water','Boiling Pt of Water','Notes'],
        [
            ['Celsius (°C)',    'Anders Celsius (Swedish astronomer, 1742); earlier called Centigrade\n(centium=100, gradus=step)',
             '0°C','100°C','Centigrade = 100 steps; SI preferred unit for everyday use'],
            ['Fahrenheit (°F)', 'Daniel Gabriel Fahrenheit (German physicist)',
             '32°F','212°F','Used for body temperature; more sensitive scale (180 divisions vs 100 in Celsius)'],
            ['Kelvin (K)',      'Lord Kelvin; SI unit of temperature — absolute scale',
             '273.15 K','373.15 K','No negative values; starts from absolute zero (-273.15°C); used in science'],
        ],
        ws=[22*mm,52*mm,22*mm,22*mm,56*mm]
    ), sp(2)]

    s += [fstrip('°C to °F', '(F - 32) / 9 = C / 5  →  F = (9/5 × C) + 32', 'or use: F = 1.8C + 32', BLUE_D)]
    s += [sp(1)]
    s += [fstrip('°C to K',  'K = 273.15 + C  (or K = 273 + C approximately)', '', TEAL_D)]
    s += [sp(2)]

    # Important values table
    s += [grid(
        ['Reference Point','Celsius (°C)','Fahrenheit (°F)','Kelvin (K)'],
        [
            ['Freezing point of water',        '0',    '32',    '273.15'],
            ['Boiling point of water',         '100',  '212',   '373.15'],
            ['Normal human body temperature',  '37',   '98.6',  '310.15'],
            ['Average room temperature',       '23',   '72',    '296.15'],
            ['Hottest natural temp (Earth)',    '56.7', '134.06','329.85'],
            ['Coldest natural temp (Earth)',    '-89',  '-128.2','184.15'],
            ['Absolute zero',                  '-273.15','-459.67','0'],
        ],
        ws=[60*mm,30*mm,34*mm,30*mm]
    ), sp(2)]

    s += [dyk([
        'Celsius invented thermometer calibration in 1742 — original scale was reversed (100=freeze, 0=boil); later flipped by Linnaeus.',
        'Fahrenheit scale was first published in 1724 — based on brine (salt+ice) as 0°F and human body as 96°F originally.',
        'Lord Kelvin (William Thomson) proposed absolute temperature scale in 1848 — 0 K = absolute zero (no thermal motion).',
        'Hottest temperature ever recorded on Earth: 56.7°C in Libya, Africa (1922). Coldest: -89°C in Antarctica.',
    ])]
    s += [sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  EXPANSION — Classes 6 & 8
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  THERMAL EXPANSION — Solids, Liquids & Gases  (Class 6 Sec. 1.7–1.9, Class 8 Sec. 4.1.1)'), sp(2)]

    s += [pill('🔑', 'Thermal Expansion: Most substances EXPAND on heating and CONTRACT on cooling — same mass, more volume.', CYAN_L, CYAN)]
    s += [sp(1)]

    s += [one_liners([
        'Molecules gain heat energy → move faster → spread apart → substance expands',
        'Expansion maximum in GASES > LIQUIDS > SOLIDS (order of expansion)',
        ('Linear Expansion',   'Increase in LENGTH of a solid when heated'),
        ('Cubical Expansion',  'Increase in VOLUME (in all 3 directions) of a solid when heated'),
        ('Areal Expansion',    'Increase in AREA of a solid when heated (2D expansion)'),
        'Heated metal ball does not pass through ring → cubical expansion (Class 6 Activity 6 / Class 8 Activity 1)',
        'Cycle spoke heating → length increases → bulb lights (circuit completed) → linear expansion proof',
        'Electric wires sag in summer (expand), become taut in winter (contract) → left slack intentionally',
    ]), sp(2)]

    s += [sub_h('Applications of Thermal Expansion (Class 6 — Section 1.9)'), sp(1)]
    s += [one_liners([
        ('Railway track gaps',    'Small gaps between rail sections prevent buckling when rails expand in summer heat'),
        ('Concrete bridge joints','Expansion joints allow bridge to expand/contract without cracking'),
        ('Iron rim on wheel',     'Iron rim heated → expands → slipped onto wooden wheel → cools & contracts → holds tightly'),
        ('Riveting',              'Hot rivet driven through hole in metal plates → head formed → cools & contracts → grips plates tightly'),
        ('Glass cracking',        'Thick glass tumbler cracks — inner surface expands with hot liquid but outer surface stays cool'),
        ('Borosilicate (Pyrex)',  'Very low thermal expansion → does not crack → used in kitchenware and laboratory glassware'),
        ('Loose electric wires',  'Wires left slack intentionally so they can contract in winter without snapping'),
    ]), sp(2)]

    s += [note_box('Expansion Order — Critical TET Fact', [
        'Expansion: Gas > Liquid > Solid (gases expand most for same temperature change)',
        'All three types occur in solids: Linear (length), Areal (area), Cubical (volume)',
        'In liquids and gases: only volume (cubical) expansion is significant',
    ], icon='📌')]
    s += [sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  CHANGE OF STATE'D  ·  CHANGE OF STATE — All 6 Processes'), sp(2)]

    s += [grid(
        ['Process','Change of State','Heat','Example'],
        [
            ['Melting (Fusion)',      'Solid → Liquid',  'Absorbed ↑', 'Ice → Water at 0°C'],
            ['Freezing (Solidification)','Liquid → Solid','Released ↓','Water → Ice at 0°C'],
            ['Vaporisation (Evaporation/Boiling)','Liquid → Gas','Absorbed ↑','Water → Steam at 100°C'],
            ['Condensation',          'Gas → Liquid',    'Released ↓', 'Steam → Water; dew on cold surface'],
            ['Sublimation',           'Solid → Gas (directly)','Absorbed ↑','Camphor, Dry ice (CO<sub>2</sub>), Naphthalene'],
            ['Deposition',            'Gas → Solid (directly)','Released ↓','Frost formation on window pane'],
        ],
        ws=[44*mm,36*mm,24*mm,70*mm]
    ), sp(2)]

    s += [one_liners([
        'Melting point of ice = 0°C | Boiling point of water = 100°C (at standard atmospheric pressure)',
        'Dry ice = solid CO<sub>2</sub> (carbon dioxide) sublimes at -57°C — used to refrigerate fish/meat in transit',
        'Water is the ONLY substance naturally found on Earth in all three states (solid, liquid, gas)',
        'Change of state is a PHYSICAL change — composition does not change, only state changes',
        'During change of state, temperature remains CONSTANT even though heat is being added/removed',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  HEAT TRANSFER'E  ·  HEAT TRANSFER — Conduction, Convection & Radiation'), sp(2)]

    # Big comparison table
    s += [grid(
        ['Method','Medium','Mechanism','Daily Life Examples'],
        [
            ['Conduction',
             'Solids (metals best) — also works between two touching solids',
             'Heat passes from hot end to cold end by vibration of atoms — NO actual movement of atoms',
             'Cooking in metal vessels; iron box heating cloth; wooden/plastic handles on utensils; igloo warm (snow = insulator)'],
            ['Convection',
             'Liquids and Gases (fluids) — NOT in solids',
             'Hot fluid rises (less dense), cold fluid sinks — ACTUAL movement of molecules creates currents',
             'Land breeze & sea breeze; hot air balloon rises; refrigerator cooling; room heater warms air; heating water in vessel'],
            ['Radiation',
             'No medium needed — works even through VACUUM',
             'Energy travels as electromagnetic waves at speed of light — does not need matter',
             'Sunlight warming Earth; feeling warmth of fire; black cooking vessel base absorbs more heat; white clothes in summer'],
        ],
        ws=[24*mm,32*mm,58*mm,60*mm]
    ), sp(2)]

    s += [sub_h('Conductors vs Insulators (Conduction)'), sp(1)]
    s += [two_col(
        ['<b>Good Conductors of Heat:</b>',
         '▶ All metals — copper, aluminium, iron, silver',
         '▶ Used for: cooking vessels, iron box soleplate, heat exchangers',
         '▶ Silver = best conductor of heat among metals',
         '▶ Faster heat transfer → cooking quicker'],
        ['<b>Poor Conductors (Insulators):</b>',
         '▶ Wood, cork, cotton, wool, glass, rubber, plastic',
         '▶ Used for: handles of utensils, oven mitts, building insulation',
         '▶ Snow = poor conductor → inside igloo stays warm despite Arctic cold',
         '▶ Air (still) = excellent insulator → woollen clothes trap air → warm'],
    ), sp(2)]

    s += [sub_h('Land Breeze & Sea Breeze — Convection in Nature'), sp(1)]
    s += [grid(
        ['','Land Breeze','Sea Breeze'],
        [
            ['When it occurs','Night',                                    'Day'],
            ['Why',           'Land cools faster than sea at night → sea air warmer → rises → land air blows to sea',
             'Land heats faster than sea during day → land air rises → cool sea breeze blows inland'],
            ['Wind direction', 'Land → Sea (outward from coast)',         'Sea → Land (inward toward coast)'],
        ],
        ws=[30*mm,72*mm,72*mm]
    ), sp(2)]

    s += [sub_h('Radiation — Black & White Surfaces'), sp(1)]
    s += [one_liners([
        ('Black surface',   'Absorbs MORE heat radiation — bottom of cooking vessels painted black for faster heating'),
        ('White surface',   'Reflects heat radiation — white clothes in summer keep body cool'),
        ('Visible radiation','When substance heated to ~500°C, radiation becomes visible as dull red glow'),
        ('Good absorber',   'Also a good emitter of radiation (black body radiates more than white body)'),
        'Heat energy from Sun reaches Earth by RADIATION — travels 150 million km through vacuum',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  CALORIMETRY'F  ·  CALORIMETRY — Heat Capacity & Specific Heat'), sp(2)]

    s += [sub_h('Units of Heat (Class 8 — Section 4.3.2)'), sp(1)]
    s += [kv_list([
        ('Joule (J)',    'SI unit of heat energy  |  heat is a form of energy → measured in joules'),
        ('Calorie (cal)','Amount of heat to raise 1 gram of water by 1°C  |  1 calorie = 4.186 J'),
        ('Kilocalorie',  '1 kcal = 4200 J (approximately)  |  food energy is measured in kilocalories'),
    ], bg_L=BLUE_D, bg_R=BLUE_L), sp(2)]

    s += [sub_h('Heat Capacity vs Specific Heat Capacity (Class 8 — Sections 4.3.3 & 4.3.4)'), sp(1)]
    s += [grid(
        ['','Heat Capacity (C\')','Specific Heat Capacity (C)'],
        [
            ['Definition',
             'Amount of heat required to raise temperature of a GIVEN substance by 1°C or 1K',
             'Amount of heat required to raise temperature of 1 kg of substance by 1°C or 1K'],
            ['Symbol',  'C\' (C prime)',  'C'],
            ['Formula', 'C\' = Q / ΔT',  'C = Q / (m × ΔT)   →   Q = m × C × ΔT'],
            ['SI Unit',  'JK<super>-1</super>  (Joule per Kelvin)',  'J kg<super>-1</super> K<super>-1</super>  (Joule per kilogram per Kelvin)'],
            ['CGS Unit', 'cal/°C',        'cal g<super>-1</super> °C<super>-1</super>'],
        ],
        ws=[30*mm,72*mm,72*mm]
    ), sp(2)]

    s += [pill('🔑', 'Specific Heat of Water = 4200 J kg⁻¹ K⁻¹  |  Water has the HIGHEST specific heat among common substances.', CYAN_L, CYAN)]
    s += [sp(1)]

    s += [one_liners([
        'High specific heat of water → used as coolant in radiators, nuclear reactors, and engine cooling systems',
        '100 g of water carries away MORE heat than 100 g of oil (water has higher heat capacity)',
        'Cooking oil heats up FASTER than water (lower specific heat capacity than water)',
        '3 factors that affect heat gained/lost: (1) Mass of substance  (2) Temperature change  (3) Nature of material',
        'Specific heat capacity is a material property — different for every substance',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  CALORIMETER, THERMOSTAT & THERMOS FLASK'G  ·  Calorimeter, Thermostat & Thermos Flask'), sp(2)]

    s += [grid(
        ['Device','What it Does','Key Features','Inventor / Year'],
        [
            ['Calorimeter',
             'Measures amount of heat gained or lost by a substance — used in calorimetry',
             'Metal vessel (copper/aluminium) in insulating jacket + thermometer + stirrer + heating element',
             'First ice-calorimeter: Antoine Lavoisier & Pierre-Simon Laplace (1782)'],
            ['Thermostat',
             'Maintains temperature of a place or device at a constant set value',
             'Senses temperature → switches appliance ON or OFF when set temp reached; "thermo"=heat + "static"=same',
             'Used in: AC, refrigerator, oven, water heater, iron box, room heater'],
            ['Thermos Flask\n(Vacuum Flask)',
             'Keeps contents hotter or cooler than surroundings for extended period',
             'Double walls with vacuum between them; silvered inner walls reflect radiated heat back; conduction only at neck',
             'Sir James Dewar (Scottish scientist, 1892) — also called Dewar Flask / Dewar Bottle'],
        ],
        ws=[28*mm,46*mm,66*mm,34*mm]
    ), sp(2)]

    s += [sub_h('How Thermos Flask Prevents All Three Modes of Heat Transfer'), sp(1)]
    s += [one_liners([
        ('Conduction prevented',  'Vacuum between double walls — no atoms/molecules to conduct heat'),
        ('Convection prevented',  'Vacuum — no liquid or gas present to form convection currents'),
        ('Radiation prevented',   'Silvered inner walls REFLECT radiated heat back into liquid — heat stays inside'),
        ('Minor conduction path', 'Only at the glass neck (top) and insulated support at bottom — unavoidable but minimal'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  Solved Numerical Problems'), sp(2)]

    problems = [
        ('1', 'Convert 37°C (normal body temperature) to Fahrenheit and Kelvin.',
         'C = 37°C',
         'F = (9/5 × 37) + 32 = 66.6 + 32 = 98.6°F  |  K = 273.15 + 37 = 310.15 K',
         '98.6°F  |  310.15 K'),
        ('2', 'Convert 212°F (boiling point) to Celsius.',
         'F = 212°F',
         'C = (F - 32) × 5/9 = (212 - 32) × 5/9 = 180 × 5/9 = 100°C',
         '100°C (boiling point of water confirmed)'),
        ('3', 'A metal ball at 30°C receives 3000 J. Temperature rises to 40°C. Find heat capacity.',
         'Q = 3000 J; T1 = 30°C; T2 = 40°C; ΔT = 40 - 30 = 10°C = 10 K',
         'C\' = Q / ΔT = 3000 / 10 = 300 JK<super>-1</super>',
         'Heat Capacity = 300 J K<super>-1</super>'),
        ('4', '84000 J raises 2 kg of water from 60°C to 70°C. Find specific heat capacity.',
         'Q = 84000 J; m = 2 kg; ΔT = 70 - 60 = 10°C = 10 K',
         'C = Q / (m × ΔT) = 84000 / (2 × 10) = 84000 / 20 = 4200 J kg<super>-1</super>K<super>-1</super>',
         'Specific Heat Capacity = 4200 J kg<super>-1</super>K<super>-1</super>'),
        ('5', 'Heat capacity of a vessel is 500 JK⁻¹. Find heat needed to raise temperature by 20 K.',
         'C\' = 500 JK<super>-1</super>; ΔT = 20 K',
         'Q = C\' × ΔT = 500 × 20 = 10,000 J',
         'Q = 10,000 J = 10 kJ'),
        ('6', 'Specific heat of metal = 160 J kg⁻¹K⁻¹. Find heat for 500 g metal, 125°C to 325°C.',
         'C = 160 J kg<super>-1</super>K<super>-1</super>; m = 500 g = 0.5 kg; ΔT = 325 - 125 = 200 K',
         'Q = C × m × ΔT = 160 × 0.5 × 200 = 16,000 J',
         'Q = 16,000 J = 16 kJ'),
    ]

    for p in problems:
        s += [prob(*p), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Formulas, Values & Units</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Heat (energy)',           'Total KE of all molecules',                              'Joule (J)'],
        ['Temperature',             'Average KE of molecules',                                'Kelvin (K); also °C, °F'],
        ['1 calorie',               '= 4.186 J  (heat to raise 1g water by 1°C)',            'CGS unit of heat'],
        ['1 kcal (food energy)',    '= 4200 J (approximately)',                               'Dietary calorie'],
        ['°C to °F',               'F = (9/5 × C) + 32   OR   C = (F - 32) × 5/9',         'Conversion formula'],
        ['°C to K',                'K = 273.15 + C',                                         'Conversion formula'],
        ['Body temp',              '37°C = 98.6°F = 310.15 K',                               'Normal human'],
        ['Boiling pt of water',    '100°C = 212°F = 373.15 K',                              'At 1 atm pressure'],
        ['Freezing pt of water',   '0°C = 32°F = 273.15 K',                                 'At 1 atm pressure'],
        ['Heat Capacity (C\')',    'C\' = Q / ΔT',                                           'J K<super>-1</super>'],
        ['Specific Heat (C)',       'C = Q / (m × ΔT)  →  Q = m × C × ΔT',                 'J kg<super>-1</super> K<super>-1</super>'],
        ['Specific heat of water',  '4200 J kg<super>-1</super> K<super>-1</super>  (highest common substance)',  'J kg<super>-1</super> K<super>-1</super>'],
        ['Clinical therm. range',   '35°C to 42°C  =  94°F to 108°F',                       'Human body only'],
        ['Expansion order',         'Gas > Liquid > Solid',                                   'Thermal expansion'],
        ['Heat transfer order',     'Conduction (solid) | Convection (liquid/gas) | Radiation (vacuum)', 'Medium needed'],
        ['Absolute zero',           '-273.15°C  =  -459.67°F  =  0 K',                      'No thermal motion'],
        ['Hottest on Earth',        '56.7°C (Libya, Africa, 1922)',                          'Natural record'],
        ['Coldest on Earth',        '-89°C (Antarctica)',                                    'Natural record'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoveries & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['Anders Celsius',          'Invented Celsius (Centigrade) temperature scale',                              '1742 '],
        ['Daniel G. Fahrenheit',    'Invented Fahrenheit scale; first mercury thermometer',                         '1724 '],
        ['Lord Kelvin (W. Thomson)','Proposed absolute (Kelvin) temperature scale; SI unit named after him',        '1848 '],
        ['Antoine Lavoisier',       'First ice-calorimeter (with Laplace); identified oxygen role in combustion',   '1782 '],
        ['Pierre-Simon Laplace',    'Co-invented ice-calorimeter with Lavoisier',                                   '1782 '],
        ['Sir James Dewar',         'Invented vacuum (thermos) flask — also called Dewar flask / Dewar bottle',     '1892 '],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Heat',                 'Total kinetic energy of all constituent particles of a body; form of energy; SI unit: Joule'),
        ('Temperature',          'Measure of average kinetic energy of molecules; measures hotness/coldness; SI unit: Kelvin'),
        ('Thermal Contact',      'State of two bodies that can exchange heat energy between them'),
        ('Thermal Equilibrium',  'State when two bodies in thermal contact no longer transfer heat — same temperature'),
        ('Calorie',              'Amount of heat to raise 1 gram of water by 1°C; 1 cal = 4.186 J'),
        ('Thermometer',          'Instrument used to measure temperature accurately and quantitatively'),
        ('Clinical Thermometer', 'Thermometer for human body temperature; range 35°C to 42°C; has a kink'),
        ('Lab Thermometer',      'Thermometer for scientific/industrial use; wider temperature range than clinical'),
        ('Celsius Scale (°C)',   'Temperature scale: 0°C = freezing point, 100°C = boiling point of water; named after Anders Celsius'),
        ('Fahrenheit Scale (°F)','Temperature scale: 32°F = freezing, 212°F = boiling; named after Daniel G. Fahrenheit'),
        ('Kelvin Scale (K)',     'SI absolute temperature scale; 0 K = absolute zero; named after Lord Kelvin'),
        ('Absolute Zero',        'The lowest possible temperature: 0 K = -273.15°C; no thermal motion of molecules'),
        ('Thermal Expansion',    'Expansion of a substance when heated — most substances expand on heating'),
        ('Linear Expansion',     'Increase in length of a solid on heating'),
        ('Cubical Expansion',    'Increase in volume (in all three dimensions) of a substance on heating'),
        ('Melting (Fusion)',      'Change of state from solid to liquid; heat is absorbed; e.g., ice → water at 0°C'),
        ('Freezing',             'Change of state from liquid to solid; heat is released; e.g., water → ice at 0°C'),
        ('Vaporisation',         'Change of state from liquid to gas; heat is absorbed; e.g., water → steam at 100°C'),
        ('Condensation',         'Change of state from gas to liquid; heat is released; e.g., steam → water'),
        ('Sublimation',          'Direct change of state from solid to gas without passing through liquid; e.g., camphor, dry ice'),
        ('Deposition',           'Direct change of state from gas to solid; reverse of sublimation; e.g., frost formation'),
        ('Conduction',           'Heat transfer in solids from hot to cold region — NO actual movement of atoms/molecules'),
        ('Convection',           'Heat transfer in liquids and gases by actual movement of molecules from hot to cold regions'),
        ('Radiation',            'Heat transfer as electromagnetic waves — can travel through vacuum; e.g., solar energy'),
        ('Calorimetry',          'Technique to measure the amount of heat involved in a physical or chemical process'),
        ('Calorimeter',          'Device to measure heat capacity of substances; metal vessel in insulating jacket'),
        ('Heat Capacity (C\')',  'Heat needed to raise temperature of given substance by 1°C or 1K; unit: JK<super>-1</super>'),
        ('Specific Heat Cap. (C)','Heat needed to raise temperature of 1 kg of substance by 1°C or 1K; unit: J kg<super>-1</super> K<super>-1</super>'),
        ('Thermostat',           'Device that maintains constant temperature by switching appliance ON/OFF at set temperature'),
        ('Thermos Flask',        'Insulating vessel with vacuum between double walls; keeps contents hot or cold; invented by Dewar'),
        ('Dry Ice',              'Solid CO2 (carbon dioxide) — sublimes directly at -57°C; used to refrigerate perishables'),
        ('Borosilicate Glass',   'Glass with very low thermal expansion; does not crack when heated; used in lab/kitchen'),
        ('Igloo',                'Snow house; warm inside because snow is a poor conductor of heat (insulator)'),
    ]

    s += [gloss_2col(g), sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P3: Heat & Temperature  |  Classes 6 • 7 • 8',
          S('ft', fontName=FNI, fontSize=7, textColor=TEAL, alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 7)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P3  |  Heat & Temperature  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=18*mm,
        title='TET Handbook P3 Heat Temperature',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P3_heat_temperature.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
