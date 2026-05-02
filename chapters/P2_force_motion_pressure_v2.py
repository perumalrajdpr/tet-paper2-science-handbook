"""
TET Paper II Science Handbook
P2: Force, Motion & Pressure — VERSION 2
✓ All sub-topics from Classes 6, 7, 8 covered
✓ Varied formats: tables, definition cards, formula strips, MCQ grids, CG/stability cards
✓ No content repeat between Key Facts and Glossary
✓ Glossary = pure definitions only
✓ Key Facts = exam-ready numbers, years, names only
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import os, re

# ─── COLORS ───────────────────────────────────────────────────────────────────
TEAL        = colors.HexColor('#0F766E')
TEAL_LIGHT  = colors.HexColor('#CCFBF1')
TEAL_MID    = colors.HexColor('#5EEAD4')
TEAL_DARK   = colors.HexColor('#134E4A')
AMBER       = colors.HexColor('#D97706')
AMBER_LIGHT = colors.HexColor('#FEF3C7')
AMBER_DARK  = colors.HexColor('#78350F')
RED_LIGHT   = colors.HexColor('#FEE2E2')
RED_DARK    = colors.HexColor('#7F1D1D')
BLUE_LIGHT  = colors.HexColor('#DBEAFE')
BLUE_DARK   = colors.HexColor('#1E3A8A')
GREEN_LIGHT = colors.HexColor('#D1FAE5')
GREEN_DARK  = colors.HexColor('#064E3B')
PURPLE_LIGHT= colors.HexColor('#EDE9FE')
PURPLE_DARK = colors.HexColor('#4C1D95')
ORANGE_LIGHT= colors.HexColor('#FFEDD5')
ORANGE_DARK = colors.HexColor('#7C2D12')
GRAY_LIGHT  = colors.HexColor('#F3F4F6')
GRAY_MID    = colors.HexColor('#D1D5DB')
GRAY_DARK   = colors.HexColor('#374151')
SLATE       = colors.HexColor('#1E293B')
WHITE       = colors.white

# ─── PAGE SETUP ───────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN   = 18*mm
USABLE_W = PAGE_W - 2*MARGIN   # ~174mm
COL_W    = (USABLE_W - 5*mm) / 2   # ~84.5mm

FN  = 'Helvetica'
FNB = 'Helvetica-Bold'
FNI = 'Helvetica-Oblique'

def S(name, **kw):
    return ParagraphStyle(name, **kw)

BODY   = S('B',  fontName=FN,  fontSize=8.5, leading=12, textColor=GRAY_DARK, spaceAfter=3)
BODYB  = S('BB', fontName=FNB, fontSize=8.5, leading=12, textColor=SLATE)
CELL   = S('C',  fontName=FN,  fontSize=7.8, leading=11, textColor=GRAY_DARK)
CELLB  = S('CB', fontName=FNB, fontSize=7.8, leading=11, textColor=SLATE)
CELLC  = S('CC', fontName=FNB, fontSize=7.8, leading=11, textColor=SLATE, alignment=TA_CENTER)
HDR    = S('H',  fontName=FNB, fontSize=7.5, leading=10, textColor=WHITE)
HDRC   = S('HC', fontName=FNB, fontSize=7.5, leading=10, textColor=WHITE, alignment=TA_CENTER)
SEC    = S('SC', fontName=FNB, fontSize=10,  leading=14, textColor=WHITE)
MINI   = S('MI', fontName=FN,  fontSize=7.2, leading=10, textColor=GRAY_DARK)
MINIB  = S('MB', fontName=FNB, fontSize=7.2, leading=10, textColor=SLATE)
MINIR  = S('MR', fontName=FNB, fontSize=7.2, leading=10, textColor=SLATE, alignment=TA_RIGHT)

sp = lambda h: Spacer(1, h*mm)

def super_p(text, style=CELL):
    return Paragraph(text, style)

# ─── REUSABLE BUILDERS ────────────────────────────────────────────────────────

def banner(code, title, sub=''):
    data = [[
        Paragraph(f'<font color="white"><b>{code}</b></font>',
                  S('bu', fontName=FNB, fontSize=24, leading=28, textColor=WHITE, alignment=TA_CENTER)),
        [
            Paragraph(f'<font color="white"><b>{title}</b></font>',
                      S('bt', fontName=FNB, fontSize=15, leading=19, textColor=WHITE)),
            Paragraph(f'<font color="#5EEAD4">{sub}</font>' if sub else '',
                      S('bs', fontName=FNI, fontSize=8.5, leading=11, textColor=TEAL_MID)),
            sp(1),
            Paragraph('<font color="#CCFBF1">Classes 6 • 7 • 8 | TET Paper II Science</font>',
                      S('bi', fontName=FN, fontSize=7.5, leading=10, textColor=TEAL_LIGHT)),
        ]
    ]]
    t = Table(data, colWidths=[26*mm, USABLE_W-26*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),TEAL_DARK),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(0,0),6*mm),
        ('LEFTPADDING',(1,0),(1,0),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),5*mm),
    ]))
    return t

def sec_head(title, bg=TEAL):
    t = Table([[Paragraph(title, SEC)]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
    ]))
    return t

def sub_head(title, bg=colors.HexColor('#0D9488')):
    t = Table([[Paragraph(title, S('sh', fontName=FNB, fontSize=8.5, leading=11, textColor=WHITE))]],
              colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

def grid(headers, rows, widths=None, hbg=TEAL, alt=GRAY_LIGHT):
    if not widths:
        n = len(headers)
        widths = [USABLE_W/n]*n
    data = [[Paragraph(h, HDRC) for h in headers]]
    for i, row in enumerate(rows):
        cells = [Paragraph(c, CELL) if isinstance(c,str) else c for c in row]
        data.append(cells)
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),
        ('GRID',(0,0),(-1,-1),0.35,GRAY_MID),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),2*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[alt, WHITE]),
    ]))
    return t

def two_col(left_items, right_items, gap=5*mm):
    def make(items):
        out = []
        for x in items:
            out.append(Paragraph(x, BODY) if isinstance(x, str) else x)
        return out
    t = Table([[make(left_items), make(right_items)]],
              colWidths=[COL_W, COL_W], hAlign='LEFT')
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

# Definition card — used for key definitions
def def_card(term, definition, bg_left=TEAL, bg_right=TEAL_LIGHT):
    data = [[
        Paragraph(term, S('dt', fontName=FNB, fontSize=8.5, leading=12, textColor=WHITE)),
        Paragraph(definition, S('dd', fontName=FN, fontSize=8.2, leading=12, textColor=SLATE))
    ]]
    t = Table(data, colWidths=[40*mm, USABLE_W-40*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_left),
        ('BACKGROUND',(1,0),(1,0),bg_right),
        ('BOX',(0,0),(-1,-1),0.8,TEAL),
        ('LINEAFTER',(0,0),(0,-1),0.8,TEAL),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

# Formula strip — highlight single formula
def formula_strip(label, formula, note='', bg=BLUE_DARK):
    note_text = f'  <font size="7" color="#94A3B8">({note})</font>' if note else ''
    data = [[
        Paragraph(label, S('fl', fontName=FNB, fontSize=8, leading=11, textColor=TEAL_MID)),
        Paragraph(f'<b><font color="white">{formula}</font></b>{note_text}',
                  S('ff', fontName=FNB, fontSize=10, leading=13, textColor=WHITE, alignment=TA_CENTER)),
    ]]
    t = Table(data, colWidths=[45*mm, USABLE_W-45*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

# MCQ-style quick-check box
def mcq_box(title, qas, bg_title=AMBER_DARK, bg_body=AMBER_LIGHT):
    """qas = list of (question, answer) tuples"""
    rows = [[Paragraph(f'⚡ {title}',
                       S('mct', fontName=FNB, fontSize=8.5, leading=11, textColor=WHITE))]]
    for q, a in qas:
        rows.append([Paragraph(f'<b>Q:</b> {q}<br/><font color="#065F46"><b>Ans: {a}</b></font>',
                               S('mcq', fontName=FN, fontSize=8, leading=12, textColor=SLATE))])
    t = Table(rows, colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_title),
        ('BACKGROUND',(0,1),(-1,-1),bg_body),
        ('BOX',(0,0),(-1,-1),1,AMBER),
        ('LINEBELOW',(0,0),(0,0),1,AMBER),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t

# Stability card (for CG & Stability section)
def stability_card(stype, description, cg_change, returns, example, bg):
    data = [[
        Paragraph(stype, S('st', fontName=FNB, fontSize=8.5, leading=11, textColor=WHITE)),
        Paragraph(description, S('sd', fontName=FN, fontSize=8, leading=11, textColor=SLATE)),
        Paragraph(cg_change, S('sc', fontName=FN, fontSize=8, leading=11, textColor=SLATE)),
        Paragraph(returns, S('sr', fontName=FNB, fontSize=8, leading=11, textColor=SLATE)),
        Paragraph(example, S('se', fontName=FN, fontSize=8, leading=11, textColor=SLATE)),
    ]]
    t = Table(data, colWidths=[30*mm, 42*mm, 38*mm, 22*mm, 42*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg),
        ('BACKGROUND',(1,0),(-1,-1),colors.HexColor('#F8FAFC')),
        ('BOX',(0,0),(-1,-1),0.8,bg),
        ('INNERGRID',(0,0),(-1,-1),0.3,GRAY_MID),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def num_problem(num, question, given, solution, ans):
    rows = [
        [Paragraph(f'Problem {num}', S('pt', fontName=FNB, fontSize=8.5, textColor=BLUE_DARK)),
         Paragraph(question, BODY)],
        [Paragraph('Given', CELLB), Paragraph(given, CELL)],
        [Paragraph('Solution', CELLB), Paragraph(solution, CELL)],
        [Paragraph('Answer', S('pa', fontName=FNB, fontSize=8.5, textColor=GREEN_DARK)),
         Paragraph(f'<b><font color="#064E3B">{ans}</font></b>', CELL)],
    ]
    t = Table(rows, colWidths=[22*mm, USABLE_W-22*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),BLUE_LIGHT),
        ('BACKGROUND',(0,-1),(-1,-1),GREEN_LIGHT),
        ('BOX',(0,0),(-1,-1),1,BLUE_DARK),
        ('INNERGRID',(0,0),(-1,-1),0.3,GRAY_MID),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t

def rapid_numbers(rows):
    return grid(
        ['Quantity / Concept', 'Formula / Value', 'Unit / Remark'],
        rows,
        widths=[60*mm, 70*mm, 44*mm],
        hbg=TEAL_DARK
    )

def rapid_people(rows):
    return grid(
        ['Scientist / Person', 'Contribution', 'Year / Class'],
        rows,
        widths=[50*mm, 88*mm, 36*mm],
        hbg=PURPLE_DARK
    )

def glossary_2col(terms):
    """Pure definition-only glossary, no facts or applications."""
    rows = []
    for i in range(0, len(terms), 2):
        left = Paragraph(f'<b>{terms[i][0]}</b> — {terms[i][1]}', MINI)
        right = Paragraph(f'<b>{terms[i+1][0]}</b> — {terms[i+1][1]}', MINI) if i+1<len(terms) else Paragraph('', MINI)
        rows.append([left, right])
    t = Table(rows, colWidths=[COL_W, COL_W])
    t.setStyle(TableStyle([
        ('GRID',(0,0),(-1,-1),0.3,GRAY_MID),
        ('ROWBACKGROUNDS',(0,0),(-1,-1),[GRAY_LIGHT, WHITE]),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),1.5*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
    ]))
    return t


# ═══════════════════════════════════════════════════════════════════════════════
# CHAPTER BUILD
# ═══════════════════════════════════════════════════════════════════════════════

def content():
    story = []

    # ── BANNER ────────────────────────────────────────────────────────────────
    story += [
        banner('P2', 'Force, Motion & Pressure', 'Physics | Classes 6, 7 & 8 Combined'),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # A. FORCE (Class 6 & 8)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('A  ·  FORCE — Definition, Types & Effects  (Cl. 6 & 8)'), sp(2)]

    # Key definition cards
    story += [
        def_card('Force (Class 6)',
                 'A push or pull by an animate or inanimate agency that causes or tends to cause motion, stop motion, change direction, or change shape of an object.'),
        sp(1),
        def_card('Force (Class 8)',
                 'An external agency which changes or tends to change the state of rest or uniform motion of a body, its direction, or its shape. Force is a <b>vector quantity</b>.'),
        sp(2),
    ]

    # Formula strips
    story += [
        formula_strip('SI Unit', 'Newton (N)', 'CGS unit = dyne ; 1 N = 10⁵ dyne', BLUE_DARK),
        sp(1),
        formula_strip('Force = ', 'F = m × a', "Newton's 2nd Law; m in kg, a in m/s²", TEAL_DARK),
        sp(1),
        formula_strip('Weight = ', 'W = m × g', 'g = 9.8 m/s² ≈ 10 m/s² on Earth\'s surface', colors.HexColor('#065F46')),
        sp(3),
    ]

    # Contact vs Non-contact (Class 6 focus)
    story += [sub_head('Contact & Non-Contact Forces (Class 6)'), sp(1)]
    story += [
        grid(
            ['Type', 'Acts when...', 'Class 6 Examples', 'Class 8 Addition'],
            [
                ['Contact Force',     'Physical touch required',     'Kicking ball, pulling cart, wind on grass', 'Applied force, Normal force, Tension, Friction'],
                ['Non-contact Force', 'No physical contact needed',  'Gravity (coconut falls), Magnet attracts iron', 'Electrostatic force, Magnetic force'],
                ['Muscular Force',    'Muscles exert force (contact)','Lifting bag, swimming, cycling', 'Type of contact force'],
            ],
            widths=[36*mm, 44*mm, 58*mm, 36*mm]
        ),
        sp(3),
    ]

    # Effects of Force (Class 8 section 2.1.1)
    story += [sub_head('Effects of Force (Class 8 — Section 2.1.1)'), sp(1)]
    story += [
        grid(
            ['Effect of Force', 'Explanation', 'Example'],
            [
                ['Set object in motion',    'Stationary body begins to move',           'Kick a ball at rest'],
                ['Stop moving object',      'Moving body brought to rest',              'Braking a bicycle'],
                ['Change speed',            'Velocity increases or decreases',          'Accelerating car'],
                ['Change direction',        'Direction of moving object changes',       'Batsman deflects ball'],
                ['Change shape/size',       'Object compressed, stretched, or deformed','Squeezing balloon, pulling rubber band'],
                ['Effect ∝ Force magnitude','Greater force → greater effect',           'Hard bat-hit → ball goes farther'],
            ],
            widths=[42*mm, 68*mm, 64*mm]
        ),
        sp(3),
    ]

    story += [
        mcq_box('FORCE — TET MCQ Quick-Check', [
            ('What is the SI unit of force?', 'Newton (N)'),
            ('1 Newton = ? dyne', '10⁵ dyne'),
            ('Force is a _____ quantity', 'Vector (has magnitude + direction)'),
            ('Gravity is an example of _____ force', 'Non-contact force'),
            ('Formula: Force = ?', 'F = m × a (mass × acceleration)'),
        ]),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # B. MOTION — Rest, Types, Distance vs Displacement (Class 6 & 7)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('B  ·  MOTION — Rest, Types & Kinematics  (Cl. 6 & 7)'), sp(2)]

    story += [
        def_card('Motion (Class 6)',
                 'When there is a <b>change in position</b> of an object with respect to time and its surroundings, the object is said to be in motion.'),
        sp(1),
        def_card('Rest (Class 6)',
                 'An object is at <b>rest</b> when its position does NOT change with respect to its surroundings. <i>Note: Rest and Motion are RELATIVE — not absolute.</i>'),
        sp(2),
    ]

    # Types of Motion (Class 6 — 2.2)
    story += [sub_head('Types of Motion Based on Path (Class 6 — Section 2.2)'), sp(1)]
    story += [
        grid(
            ['Type', 'Description', 'Class 6 Examples', 'Additional Examples'],
            [
                ['Linear (Rectilinear)', 'Straight-line path',                    'Person walking on straight road; Falling stone', 'Car on highway'],
                ['Curvilinear',          'Curved path (moving but changing dir.)','Thrown paper aeroplane',                         'Ball thrown at angle'],
                ['Circular',             'Circular path around a fixed centre',   'Swirling stone on rope',                         'Earth around Sun, fan blade tip'],
                ['Rotatory',             'Spinning on its own axis',              'Spinning top; sharpening pencil in sharpener',   'Earth\'s rotation; motor'],
                ['Oscillatory',         'To-and-fro about a mean position',      'Pendulum; pencil held between fingers',          'Swing; vibrating string'],
                ['Zigzag (Irregular)',   'Random directions; no fixed path',      'Fly buzzing in room',                            'People in crowded street'],
            ],
            widths=[36*mm, 46*mm, 54*mm, 38*mm]
        ),
        sp(2),
    ]

    story += [sub_head('Periodic vs Non-Periodic Motion (Class 6)'), sp(1)]
    story += [
        two_col(
            [
                '<b>Periodic Motion</b> — repeats after a fixed time interval.',
                '• Oscillatory motion → always periodic (pendulum)',
                '• Circular motion → periodic (Earth\'s revolution)',
                '• Rotatory motion → periodic (Earth\'s rotation)',
            ],
            [
                '<b>Non-Periodic Motion</b> — no fixed time pattern.',
                '• Zigzag / Irregular motion (fly, crowd)',
                '• Curvilinear motion (thrown ball)',
                '• Linear motion may be non-periodic',
            ]
        ),
        sp(3),
    ]

    # Distance vs Displacement (Class 7 — 2.1)
    story += [sub_head('Distance & Displacement (Class 7 — Section 2.1)'), sp(1)]
    story += [
        grid(
            ['', 'Distance', 'Displacement'],
            [
                ['Definition', 'Total length of path travelled from start to end', 'Shortest straight-line path from start to end point'],
                ['Type', 'Scalar (no direction)', 'Vector (has direction)'],
                ['SI Unit', 'metre (m)', 'metre (m)'],
                ['Can it be zero?', 'Only if object never moved', 'Yes — if object returns to start (circular trip)'],
                ['Equal when?', '—', 'When object moves in a straight line without turning'],
                ['Symbol', 'd', 's (or Δx)'],
            ],
            widths=[30*mm, 72*mm, 72*mm]
        ),
        sp(2),
    ]

    story += [
        def_card('Nautical Mile',
                 '1 nautical mile = 1.852 km — used in aviation and sea transport. <b>Knot</b> = 1 nautical mile/hour — speed unit for ships and aircraft.'),
        sp(3),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # C. SPEED, VELOCITY & ACCELERATION (Class 6 & 7)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('C  ·  Speed, Velocity & Acceleration  (Cl. 6 & 7)'), sp(2)]

    # Speed (Class 6)
    story += [sub_head('Speed (Class 6 — Section 2.3 & Class 7 — Section 2.2.1)'), sp(1)]
    story += [
        formula_strip('Speed', 's = d / t', 'Distance ÷ Time | scalar quantity | SI unit: m/s', TEAL_DARK),
        sp(1),
        formula_strip('Average Speed', 'v_avg = Total Distance / Total Time', 'Used when speed varies', colors.HexColor('#0369A1')),
        sp(1),
        formula_strip('Conversion', '1 km/h = 5/18 m/s  |  1 m/s = 18/5 km/h = 3.6 km/h', '', SLATE),
        sp(2),
    ]

    story += [
        grid(
            ['Speed Type', 'Definition', 'Class', 'Example'],
            [
                ['Uniform Speed',     'Equal distances in equal time intervals',         '6 & 7', 'Light through vacuum (3×10⁸ m/s)'],
                ['Non-uniform Speed', 'Unequal distances in equal time intervals',       '6 & 7', 'Bus in city traffic'],
                ['Average Speed',     'Total distance ÷ total time taken',              '7',     'Total trip with varying speeds'],
            ],
            widths=[38*mm, 68*mm, 18*mm, 50*mm]
        ),
        sp(2),
    ]

    # Velocity (Class 7 — 2.2.2)
    story += [sub_head('Velocity (Class 7 — Section 2.2.2)'), sp(1)]
    story += [
        formula_strip('Velocity', 'v = Displacement / Time', 'vector | SI unit: m/s', colors.HexColor('#7C3AED')),
        sp(1),
        formula_strip('Average Velocity', 'v_avg = Total Displacement / Total Time', 'positive/negative based on direction', PURPLE_DARK),
        sp(2),
    ]

    story += [
        grid(
            ['Velocity Type', 'Definition', 'Example'],
            [
                ['Uniform Velocity',     'Equal displacement in equal time in same direction', 'Light through vacuum; ideal uniform circular motion'],
                ['Non-uniform Velocity', 'Speed OR direction changes (or both)',               'Train leaving station; vehicle turning corner'],
                ['Average Velocity',     'Total displacement ÷ total time taken',              'Car going east 5 km then west 7 km'],
            ],
            widths=[40*mm, 80*mm, 54*mm]
        ),
        sp(3),
    ]

    # Acceleration (Class 7 — 2.3)
    story += [sec_head('C.2  ·  Acceleration — Types  (Class 7, Section 2.3)'), sp(2)]

    story += [
        formula_strip('Acceleration', 'a = (v − u) / t', 'v=final velocity, u=initial velocity, t=time | SI unit: m/s²', BLUE_DARK),
        sp(2),
    ]

    story += [
        grid(
            ['Acceleration Type', 'Definition (Class 7)', 'Sign', 'Example'],
            [
                ['Positive Acceleration',
                 'Velocity INCREASES with time (Section 2.3.1)',
                 '+ve', 'Car speeding up; Cheetah sprinting 0→20 m/s in 2 s'],
                ['Negative Acceleration\n(Deceleration / Retardation)',
                 'Velocity DECREASES with time (Section 2.3.2)',
                 '−ve', 'Golf ball slowing down; braking bus'],
                ['Uniform Acceleration',
                 'Change in velocity is SAME per unit time (Section 2.3.3)',
                 '+ve/−ve', 'Bus velocity increasing 20 m/s every second'],
                ['Non-uniform Acceleration',
                 'Change in velocity is DIFFERENT per unit time (Section 2.3.4)',
                 'Varies', 'City traffic vehicle; velocity 0,10,40,60,70,50 m/s'],
            ],
            widths=[46*mm, 68*mm, 14*mm, 46*mm]
        ),
        sp(2),
    ]

    story += [
        mcq_box('MOTION — TET MCQ Quick-Check', [
            ('Cheetah speed = 25–30 m/s. It goes 0 → 20 m/s in 2 s. Acceleration = ?', '10 m/s²'),
            ('What is the SI unit of acceleration?', 'm/s² (metre per second squared)'),
            ('Displacement = 0 means...', 'Object returned to starting point'),
            ('1 nautical mile = ?', '1.852 km'),
            ('Speed is a _____ quantity; velocity is a _____ quantity', 'Scalar; Vector'),
        ]),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # D. DISTANCE-TIME & SPEED-TIME GRAPHS (Class 7 — 2.4 & 2.5)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('D  ·  Distance–Time & Speed–Time Graphs  (Class 7, Sections 2.4 & 2.5)'), sp(2)]

    story += [sub_head('Distance–Time Graph (Section 2.4) — 4 Cases'), sp(1)]
    story += [
        grid(
            ['Graph Shape / Slope', 'What it Means', 'Motion Type'],
            [
                ['Horizontal line (zero slope)',    'Distance constant — object NOT moving',          'Rest'],
                ['Straight line, constant slope',   'Distance increases uniformly — constant speed',  'Uniform speed'],
                ['Curve with INCREASING slope',     'Distance increases faster — speed is rising',    'Acceleration'],
                ['Curve with DECREASING slope',     'Distance increase slowing — speed is falling',   'Deceleration'],
            ],
            widths=[56*mm, 78*mm, 40*mm]
        ),
        sp(2),
    ]

    story += [sub_head('Speed–Time Graph (Section 2.5) — 6 Cases'), sp(1)]
    story += [
        grid(
            ['Graph Shape', 'What it Means', 'Motion Type'],
            [
                ['Horizontal line at speed = 0',       'Bus not moving',                           'Rest (zero speed)'],
                ['Horizontal line at speed > 0',       'Constant speed, zero acceleration',        'Uniform speed'],
                ['Straight line RISING (const. slope)', 'Speed increasing at constant rate',       'Uniform acceleration'],
                ['Straight line FALLING (const. slope)','Speed decreasing at constant rate',       'Uniform deceleration'],
                ['Rising curve with INCREASING slope', 'Acceleration itself is increasing',        'Non-uniform acceleration (increasing)'],
                ['Rising curve with DECREASING slope', 'Acceleration itself is decreasing',        'Non-uniform acceleration (decreasing)'],
            ],
            widths=[58*mm, 74*mm, 42*mm]
        ),
        sp(2),
    ]

    story += [sub_head('D–T vs S–T Graph Comparison (Section 2.5.1)'), sp(1)]
    story += [
        grid(
            ['Journey Phase', 'Distance–Time Graph', 'Speed–Time Graph'],
            [
                ['Accelerating uniformly from rest', 'Concave curve (gradient increasing)',    'Straight line rising (constant positive slope)'],
                ['Constant speed',                   'Straight line (constant gradient)',       'Horizontal line (zero slope = zero acceleration)'],
                ['Decelerating uniformly to stop',   'Convex curve (gradient decreasing)',     'Straight line falling (constant negative slope)'],
                ['Area under graph',                 'Not directly useful',                    '= Distance travelled'],
            ],
            widths=[50*mm, 62*mm, 62*mm]
        ),
        sp(3),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # E. CENTRE OF GRAVITY & STABILITY (Class 7 — 2.6 & 2.7)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('E  ·  Centre of Gravity & Stability  (Class 7, Sections 2.6 & 2.7)'), sp(2)]

    story += [
        def_card('Centre of Gravity (CG)',
                 'The single point through which the <b>entire weight of an object appears to act</b>. For regular-shaped objects, CG lies at the geometric centre.'),
        sp(1),
    ]

    # CG of regular shapes
    story += [
        grid(
            ['Shape', 'Location of Centre of Gravity'],
            [
                ['Square / Rectangle',  'Intersection of diagonals (geometric centre)'],
                ['Circle / Disc',       'Centre of the circle'],
                ['Triangle',            'Centroid (intersection of medians)'],
                ['Ring / Hollow circle','Centre of the ring (may be in empty space)'],
                ['Uniform ruler',       'Midpoint of the ruler'],
            ],
            widths=[50*mm, 124*mm]
        ),
        sp(2),
    ]

    story += [sub_head('Types of Equilibrium / Stability (Class 7 — Section 2.7)'), sp(1)]

    # Stability header row manually
    hdr_row = [
        Paragraph('Type', HDRC), Paragraph('When Displaced...', HDRC),
        Paragraph('CG change', HDRC), Paragraph('Returns?', HDRC), Paragraph('Example', HDRC),
    ]
    stab_rows = [
        hdr_row,
        [Paragraph('Stable\nEquilibrium', S('se', fontName=FNB, fontSize=8, textColor=WHITE)),
         Paragraph('CG rises briefly; weight-line stays WITHIN base', MINI),
         Paragraph('CG rises', MINIB),
         Paragraph('YES ✓', S('yr', fontName=FNB, fontSize=8, textColor=GREEN_DARK)),
         Paragraph('Frustum resting on wide base; Thanjavur doll; Racing car', MINI)],
        [Paragraph('Unstable\nEquilibrium', S('ue', fontName=FNB, fontSize=8, textColor=WHITE)),
         Paragraph('CG falls; weight-line falls OUTSIDE base', MINI),
         Paragraph('CG lowers', MINIB),
         Paragraph('NO ✗', S('nr', fontName=FNB, fontSize=8, textColor=RED_DARK)),
         Paragraph('Inverted frustum balanced on tip; pencil balanced on tip', MINI)],
        [Paragraph('Neutral\nEquilibrium', S('ne', fontName=FNB, fontSize=8, textColor=WHITE)),
         Paragraph('CG stays at SAME height; object rolls but does not topple', MINI),
         Paragraph('No change', MINIB),
         Paragraph('Same\nposition', MINIB),
         Paragraph('Frustum on its side (rolls); sphere on flat surface', MINI)],
    ]
    stab_bgs = [TEAL_DARK, GREEN_DARK, RED_DARK, colors.HexColor('#0369A1')]
    t = Table(stab_rows, colWidths=[28*mm, 48*mm, 30*mm, 22*mm, 46*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),TEAL_DARK),
        ('BACKGROUND',(0,1),(0,1),GREEN_DARK),
        ('BACKGROUND',(0,2),(0,2),RED_DARK),
        ('BACKGROUND',(0,3),(0,3),colors.HexColor('#0369A1')),
        ('BACKGROUND',(1,1),(-1,1),GREEN_LIGHT),
        ('BACKGROUND',(1,2),(-1,2),RED_LIGHT),
        ('BACKGROUND',(1,3),(-1,3),BLUE_LIGHT),
        ('GRID',(0,0),(-1,-1),0.4,GRAY_MID),
        ('TEXTCOLOR',(0,1),(0,-1),WHITE),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),2*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),
        ('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    story += [t, sp(2)]

    story += [sub_head('Increasing Stability — Conditions (Section 2.7.1)'), sp(1)]
    story += [
        two_col(
            [
                '<b>Stability INCREASES by:</b>',
                '1. <b>Lowering the Centre of Gravity</b> (heavy base)',
                '2. <b>Increasing the base area</b> (broad base)',
                '',
                '<b>Application examples (Class 7):</b>',
                '• Tour bus luggage at <b>bottom</b> (not on roof)',
                '• Racing cars built <b>low and broad</b>',
                '• Table lamps have <b>large heavy base</b>',
                '• Extra passengers NOT on upper deck of double-decker bus',
            ],
            [
                '<b>Thanjavur Doll — Stable Equilibrium:</b>',
                '• Made of terracotta material',
                '• CG and total weight concentrated at <b>bottommost point</b>',
                '• Even when tilted, returns to upright position',
                '• Produces slow oscillatory dance-like movement',
                '',
                '<b>Finding CG of irregular shapes:</b>',
                'Suspend shape from 3 different holes; draw plumb-line each time.',
                'Intersection of three lines = Centre of Gravity.',
            ]
        ),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # F. PRESSURE (Class 8 — 2.2, 2.3, 2.4)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('F  ·  Pressure — Thrust, Air, Liquid & Pascal\'s Law  (Class 8)'), sp(2)]

    story += [
        def_card('Thrust',
                 'Force acting <b>perpendicularly</b> on a surface — unit: Newton (N). A large force over a small area creates very high pressure.'),
        sp(1),
        def_card('Pressure',
                 'Amount of thrust (force) acting on <b>unit area</b> of a surface. P = F/A. SI unit: <b>Pascal (Pa) = Nm⁻²</b> — named after Blaise Pascal.'),
        sp(1),
        formula_strip('Pressure', 'P = F / A  (Thrust ÷ Area)', 'SI: Pascal (Pa) = 1 Nm⁻² | CGS: dyne/cm²', BLUE_DARK),
        sp(2),
    ]

    story += [sub_head('Pressure — Practical Examples (Class 8)'), sp(1)]
    story += [
        grid(
            ['Situation', 'Area', 'Pressure', 'Why?'],
            [
                ['Sharp knife cuts easily',        'Small (sharp edge)', 'HIGH', 'Same force, tiny area → huge pressure → penetrates easily'],
                ['Injection needle pierces skin',  'Very small tip',     'HIGH', 'Concentrated force on tiny area'],
                ['Camel walks on sand',            'Large padded feet',  'LOW',  'Large area distributes weight → low pressure → no sinking'],
                ['Heavy truck → many wheels',      'Large (many tyres)', 'LOW',  'More wheels = more contact area = less road pressure'],
                ['Broad bag straps',               'Wide strap',         'LOW',  'Wider strap spreads force over shoulder → comfortable'],
                ['Nail hammered into wall',        'Sharp tip',          'HIGH', 'Small tip area creates very high pressure → penetrates'],
            ],
            widths=[46*mm, 30*mm, 20*mm, 78*mm]
        ),
        sp(3),
    ]

    # Atmospheric Pressure (Class 8 — 2.3)
    story += [sub_head('Atmospheric Pressure (Class 8 — Section 2.3)'), sp(1)]
    story += [
        grid(
            ['Parameter', 'Value / Fact'],
            [
                ['Definition',          'Weight of the entire column of air above unit area of Earth\'s surface'],
                ['Standard value',      '1 atm = 76 cm Hg = 760 mmHg = 1,01,325 Pa ≈ 1.01 × 10⁵ Nm⁻²'],
                ['Measurement instrument', 'Barometer (mercury barometer) — invented by Evangelista Torricelli (1643)'],
                ['Pressure vs Altitude','Atmospheric pressure DECREASES as altitude increases above Earth'],
                ['Why tilting barometer doesn\'t change reading', 'Level of mercury column remains the same regardless of tilt angle'],
                ['Cooking at high altitude', 'Lower atm. pressure → boiling point decreases (water boils even at 80°C) → cooking difficult'],
                ['Pressure cooker principle', 'Sealed vessel → increased pressure inside → boiling point rises → food cooks faster'],
            ],
            widths=[54*mm, 120*mm]
        ),
        sp(3),
    ]

    # Liquid Pressure (Class 8 — 2.4.1)
    story += [sub_head('Liquid Pressure (Class 8 — Section 2.4.1)'), sp(1)]
    story += [
        formula_strip('Liquid Pressure', 'P = ρ × g × h', 'ρ=density (kg/m³), g=9.8 m/s², h=depth (m)', colors.HexColor('#0369A1')),
        sp(1),
    ]
    story += [
        grid(
            ['Property of Liquid Pressure', 'Explanation'],
            [
                ['Increases with depth',         'Pressure at bottom of container > pressure at top (spouting can experiment)'],
                ['Same in all directions at same depth', 'Liquid exerts equal pressure sideways, up, down at a given depth'],
                ['Depends on height of liquid column', 'Not on shape or volume of container — only height (h) matters'],
                ['Buoyant Force',                'Upward force on submerged/floating object = weight of liquid displaced (Archimedes)'],
                ['Object floats if...',          'Weight of object < Buoyant force (upward force)'],
                ['Object sinks if...',           'Weight of object > Buoyant force'],
                ['Why dams wider at base?',      'Water pressure increases with depth → greater force at bottom → needs thicker wall'],
                ['Why scuba divers wear suits?', 'To withstand high water pressure at great ocean depths'],
            ],
            widths=[60*mm, 114*mm]
        ),
        sp(3),
    ]

    # Pascal's Law (Class 8 — 2.4.2)
    story += [sub_head('Pascal\'s Law (Class 8 — Section 2.4.2)'), sp(1)]
    story += [
        def_card('Pascal\'s Law',
                 'Pressure applied at any point of a <b>liquid at rest in a closed system</b> is distributed equally through all directions of the liquid. (Blaise Pascal, 1648)'),
        sp(1),
        grid(
            ['Application', 'Working Principle', 'Where Used'],
            [
                ['Hydraulic Lift / Jack', 'Small force on small piston → same pressure → large force on large piston (F₁/A₁ = F₂/A₂)', 'Car service stations, elevators'],
                ['Hydraulic Brakes',      'Brake fluid transmits pressure from pedal equally to all four wheel brake cylinders', 'Automobiles (bikes, cars, trucks)'],
                ['Hydraulic Press',       'High pressure applied to compress materials into smaller volume', 'Cotton/paper bale compression'],
                ['Syringe / Pump',        'Pressure on liquid transmitted to outlet nozzle', 'Medical injections, pumps'],
            ],
            widths=[38*mm, 88*mm, 48*mm]
        ),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # G. SURFACE TENSION & VISCOSITY (Class 8 — 2.5 & 2.6)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('G  ·  Surface Tension & Viscosity  (Class 8, Sections 2.5 & 2.6)'), sp(2)]

    story += [
        def_card('Surface Tension',
                 'Property of liquid surface molecules to contract and minimize surface area. Defined as <b>force per unit length</b> on the liquid surface. Unit: <b>Nm⁻¹</b>'),
        sp(1),
        def_card('Viscosity / Viscous Force',
                 'Frictional force between successive <b>layers of a moving liquid</b> that opposes their relative motion. Unit: <b>poise</b> (CGS) or <b>kgm⁻¹s⁻¹ = Nsm⁻²</b> (SI)'),
        sp(2),
    ]

    story += [
        grid(
            ['Property', 'Surface Tension', 'Viscosity'],
            [
                ['Acts on', 'Surface of liquid (boundary layer)', 'Between moving liquid layers (throughout)'],
                ['Unit', 'Nm⁻¹', 'Poise (CGS) | kgm⁻¹s⁻¹ (SI)'],
                ['Effect of temperature', 'Decreases when temperature rises', 'DECREASES when temperature rises (honey flows faster when hot)'],
                ['Practical use', 'Capillary action in plants, drops become spherical', 'Engine oil lubrication, blood flow, ink flow'],
                ['Reduced by', 'Adding detergent/soap → spreads better → cleans', 'Heating the liquid; adding lubricants'],
            ],
            widths=[36*mm, 69*mm, 69*mm]
        ),
        sp(2),
    ]

    story += [sub_head('Applications of Surface Tension (Class 8 — Section 2.5.1)'), sp(1)]
    story += [
        two_col(
            [
                '• <b>Rain drops spherical</b> — liquid contracts to minimum surface area',
                '• <b>Capillary action</b> in xylem tissue of plants — water rises against gravity',
                '• <b>Water strider insect</b> walks on water surface',
                '• <b>Paper clip floats</b> on water surface (heavier than water)',
                '• <b>Needle floats</b> on carefully placed on water',
            ],
            [
                '• <b>Detergent lowers surface tension</b> → water spreads into cloth fibers → better cleaning',
                '• <b>Sailors pour oil on rough sea</b> to reduce surface tension and calm waves',
                '• <b>Soap bubbles</b> form because of liquid film surface tension',
                '• <b>Mosquito larvae</b> breathe through the water surface (surface tension supports them)',
            ]
        ),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # H. FRICTION (Class 8 — 2.7)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('H  ·  Friction — Types, Factors, Pros, Cons & Control  (Class 8)'), sp(2)]

    story += [
        def_card('Friction',
                 'Force arising between two or more bodies in contact that <b>opposes relative motion</b>. Caused by geometrical dissimilarities (roughness) of surfaces. Acts opposite to direction of motion.'),
        sp(2),
    ]

    # Types (2.7.1)
    story += [sub_head('Types of Friction (Class 8 — Section 2.7.1)'), sp(1)]
    story += [
        grid(
            ['Type', 'When it Occurs', 'Magnitude', 'Class 8 Example'],
            [
                ['Static Friction',  'Body at REST; external force applied but no motion yet', 'LARGEST (max. just before motion)', 'Book resting on table, parked vehicle'],
                ['Sliding Friction\n(Kinetic)', 'One surface SLIDES over another during motion', 'MODERATE', 'Box dragged on floor; chalk on blackboard; braking car'],
                ['Rolling Friction', 'Body ROLLS over a surface', 'SMALLEST (least)', 'Ball rolling on ground; bicycle wheel; car tyre'],
                ['Fluid Friction\n(Viscosity)', 'Object moving through liquid or gas', 'Depends on speed & viscosity', 'Ship in water; bird in air; swimming'],
            ],
            widths=[38*mm, 52*mm, 34*mm, 50*mm]
        ),
        sp(1),
    ]
    story += [
        formula_strip('Order of Friction',
                      'Rolling < Sliding < Static',
                      'That is why ball bearings (rolling) used in machines to reduce friction', ORANGE_DARK),
        sp(3),
    ]

    # Factors (2.7.2)
    story += [sub_head('Factors Affecting Friction (Class 8 — Section 2.7.2)'), sp(1)]
    story += [
        grid(
            ['Factor', 'Effect on Friction', 'Example'],
            [
                ['Nature of surface (rough vs smooth)', 'Rough surface → MORE friction; Smooth surface → LESS friction', 'Sand road vs polished marble floor'],
                ['Weight / Mass of body',               'Greater weight → GREATER friction', 'Loaded trolley harder to push than empty one'],
                ['Area of contact',                     'For given weight: greater area → greater friction', 'Road roller (broad base) vs cycle tyre (narrow)'],
            ],
            widths=[54*mm, 70*mm, 50*mm]
        ),
        sp(3),
    ]

    # Advantages (2.7.3) and Disadvantages (2.7.4) — side by side
    story += [sub_head('Advantages (2.7.3) vs Disadvantages (2.7.4) of Friction'), sp(1)]
    story += [
        grid(
            ['Advantages of Friction ✅', 'Disadvantages of Friction ❌'],
            [
                ['We can walk without slipping',             'Wears out surfaces — soles, tyres, gears, machine parts'],
                ['Vehicles brake and stop safely',           'Wastes energy — extra effort needed to overcome friction'],
                ['We write with pen/pencil on paper',        'Produces HEAT — damages machines and causes wear'],
                ['Knots, nails, bolts, screws hold tight',   'Noise produced in machines by friction'],
                ['Matchstick lights when struck',            'Vehicles slow down due to air/road friction → fuel wasted'],
                ['Climbing, gripping, stitching possible',   'Moving parts need frequent maintenance due to friction'],
            ],
            widths=[87*mm, 87*mm]
        ),
        sp(1),
    ]
    story += [
        def_card('Friction is a "Necessary Evil"',
                 'It is necessary (we cannot live without it) yet evil (it wastes energy and causes wear). Therefore called a <b>necessary evil</b>.'),
        sp(3),
    ]

    # Increasing/Decreasing Friction (2.7.5)
    story += [sub_head('Increasing & Decreasing Friction (Class 8 — Section 2.7.5)'), sp(1)]
    story += [
        grid(
            ['Method', 'Increases or Decreases?', 'How it Works', 'Example'],
            [
                ['Increasing area of contact', 'INCREASES friction', 'More surface → more contact irregularities', 'Brake shoes adjusted close to wheel rim'],
                ['Lubricants (oil/grease)',    'DECREASES friction', 'Fills gaps in rough surfaces; smooth layer prevents direct contact', 'Engine oil, coconut oil, castor oil, grease, graphite'],
                ['Ball Bearings',              'DECREASES friction', 'Converts sliding friction to rolling friction (rolling < sliding)', 'Cycle hub, electric motors, axles, wheels'],
                ['Streamlining',               'DECREASES fluid friction', 'Smooth body shape reduces air/water resistance', 'Aircraft, ships, sports cars, fish body shape'],
                ['Polishing surfaces',         'DECREASES friction', 'Removes surface irregularities → smoother contact', 'Sports tracks, machine parts'],
                ['Using rough / grooved surface', 'INCREASES friction', 'More grip required for safety',              'Tyre treads, brake pads, shoe soles, stair mats'],
            ],
            widths=[40*mm, 32*mm, 58*mm, 44*mm]
        ),
        sp(3),
    ]

    story += [
        mcq_box('FRICTION — TET MCQ Quick-Check', [
            ('Which friction is LEAST?', 'Rolling friction (smallest of all three types)'),
            ('Why are ball bearings used in cycle hub?', 'To convert sliding friction to rolling friction (rolling < sliding)'),
            ('What is the unit of viscosity in SI system?', 'kg m⁻¹ s⁻¹ (= N s m⁻²)'),
            ('Friction is called a "necessary evil" because...', 'It is essential for daily life BUT wastes energy and causes wear'),
            ('Which factor does NOT affect friction?', 'Color / material color of the surfaces'),
        ]),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # I. SOLVED NUMERICAL PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('I  ·  Solved Numerical Problems'), sp(2)]

    probs = [
        ('1', 'A vehicle covers 400 km in 5 hours. Calculate its speed. (Class 6)',
         'Distance d = 400 km = 4,00,000 m; Time t = 5 h = 5 × 3600 = 18,000 s',
         'Speed = d/t = 4,00,000 / 18,000 = 22.22 m/s  OR  in km/h: 400/5 = 80 km/h',
         '80 km/h = 22.22 m/s'),
        ('2', 'A car accelerates from rest to 20 m/s in 10 seconds. Find acceleration. (Class 7)',
         'Initial velocity u = 0 m/s; Final velocity v = 20 m/s; Time t = 10 s',
         'a = (v – u) / t = (20 – 0) / 10 = 2 m/s²',
         'Acceleration = 2 m/s²'),
        ('3', 'A golf ball decelerates from 8 m/s to 2 m/s in 10 s. Find deceleration. (Class 7)',
         'u = 8 m/s; v = 2 m/s; t = 10 s',
         'a = (v – u) / t = (2 – 8) / 10 = –6/10 = –0.6 m/s²',
         'Deceleration = 0.6 m/s² (retardation)'),
        ('4', 'An elephant weighs 4000 N. Area of one foot sole = 0.1 m². Find pressure on one foot. (Class 8)',
         'Force on one foot = 4000 ÷ 4 = 1000 N; Area A = 0.1 m²',
         'P = F/A = 1000 / 0.1 = 10,000 Nm⁻²',
         '10,000 Pa = 10⁴ Nm⁻²'),
        ('5', 'A stone weighs 500 N, contact area = 25 cm². Find pressure. (Class 8)',
         'F = 500 N; A = 25 cm² = 25 × 10⁻⁴ m² = 0.0025 m²',
         'P = F/A = 500 / 0.0025 = 2,00,000 Nm⁻²',
         '2 × 10⁵ Pa'),
        ('6', 'Geetha cycles at 2 m/s for 15 minutes. Find distance. (Class 7)',
         'Speed v = 2 m/s; Time t = 15 min = 900 s',
         'Distance = v × t = 2 × 900 = 1800 m',
         '1800 m = 1.8 km'),
    ]

    for i in range(0, len(probs), 2):
        row_items = [num_problem(*probs[i])]
        if i+1 < len(probs):
            row_items.append(num_problem(*probs[i+1]))
            t = Table([[row_items[0], row_items[1]]], colWidths=[COL_W, COL_W])
        else:
            t = Table([[row_items[0]]], colWidths=[USABLE_W])
        t.setStyle(TableStyle([
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
            ('TOPPADDING',(0,0),(-1,-1),0),
            ('BOTTOMPADDING',(0,0),(-1,-1),0),
            ('INNERGRID',(0,0),(-1,-1),0,WHITE),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
        ]))
        story += [t, sp(2)]

    story.append(sp(2))

    # ══════════════════════════════════════════════════════════════════════════
    # J. KEY FACTS — RAPID REVISION  (Numbers, Names, Years ONLY — no definitions)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('J  ·  KEY FACTS — Rapid Revision  (Numbers, Years & Names)'), sp(2)]

    story += [Paragraph('<b>Formulas, Values & Units — Memorise These</b>', BODYB), sp(1)]
    story += [
        rapid_numbers([
            ['Force (F)',               'F = m × a',                                   'Newton (N) | CGS: dyne'],
            ['1 Newton',                '= 10⁵ dyne',                                  'Unit conversion'],
            ['Weight (W)',              'W = m × g  (g = 9.8 m/s² ≈ 10)',             'Newton (N)'],
            ['Speed (s)',               's = d/t  (distance ÷ time)',                  'm/s | km/h'],
            ['1 km/h',                  '= 5/18 m/s  (multiply by 5/18 to convert)',   'Unit conversion'],
            ['1 m/s',                   '= 18/5 km/h = 3.6 km/h',                     'Unit conversion'],
            ['Velocity (v)',            'v = displacement ÷ time',                     'm/s (vector)'],
            ['Acceleration (a)',        'a = (v − u) / t',                             'm/s²'],
            ['Pressure (P)',            'P = F/A = Thrust / Area',                     'Pascal (Pa) = Nm⁻²'],
            ['1 atm',                   '= 76 cm Hg = 760 mmHg = 1.01 × 10⁵ Pa',     'Standard value'],
            ['Liquid pressure',         'P = ρ × g × h  (density × g × depth)',       'Pa (Nm⁻²)'],
            ['Surface tension',         'Force per unit length on liquid surface',     'Nm⁻¹'],
            ['Viscosity unit (CGS)',     'Poise',                                       'CGS unit'],
            ['Viscosity unit (SI)',      'kg m⁻¹ s⁻¹  =  N s m⁻²',                  'SI unit'],
            ['1 Nautical mile',         '= 1.852 km',                                  'Sea/air navigation'],
            ['Cheetah top speed',       '25–30 m/s (0 → 20 m/s in 2 s = 10 m/s² acc.)', 'Class 7 textbook data'],
            ['Speed of light',          '3 × 10⁸ m/s  (vacuum)',                       'Uniform velocity example'],
        ]),
        sp(3),
    ]

    story += [Paragraph('<b>Scientists, Discoverers & Years</b>', BODYB), sp(1)]
    story += [
        rapid_people([
            ['Isaac Newton',           'Laws of Motion; Law of Gravitation; Unit "newton" named after him', '1687 | Cl. 8'],
            ['Blaise Pascal',          'Pascal\'s Law (fluid pressure transmission); Unit "pascal" named after him', '1648 | Cl. 8'],
            ['Evangelista Torricelli', 'Invented mercury barometer — measures atmospheric pressure',            '1643 | Cl. 8'],
            ['Galileo Galilei',        'Law of falling bodies; studied free fall, velocity, acceleration',     '1638 | Cl. 7'],
            ['Archimedes',             'Archimedes\' Principle: buoyant force = weight of displaced fluid',    '287–212 BC | Cl. 8'],
            ['Aryabhata',              'Observed that rest and motion are RELATIVE (river bank appears moving)', '5th century CE | Cl. 6'],
        ]),
        sp(4),
    ]

    # ══════════════════════════════════════════════════════════════════════════
    # K. GLOSSARY  (Pure definitions only — no values, no applications)
    # ══════════════════════════════════════════════════════════════════════════
    story += [sec_head('K  ·  GLOSSARY — Definitions'), sp(2)]

    # Pure, concise definitions — no duplication with Key Facts section
    gloss = [
        ('Force',             'Push or pull by animate/inanimate agency; SI unit: Newton'),
        ('Thrust',            'Force acting perpendicularly on a given surface area'),
        ('Pressure',          'Thrust per unit area (P = F/A); SI unit: Pascal (Pa)'),
        ('Pascal (Pa)',       'SI unit of pressure; 1 Pa = 1 Nm⁻²; named after Blaise Pascal'),
        ('Newton (N)',        'SI unit of force; 1 N = force that accelerates 1 kg mass at 1 m/s²'),
        ('Motion',            'Change in position of an object with respect to time and a reference'),
        ('Rest',              'No change in position with respect to time and reference point'),
        ('Distance',          'Total length of path travelled — scalar quantity'),
        ('Displacement',      'Shortest straight-line path from start to end, with direction — vector'),
        ('Speed',             'Rate of change of distance — scalar quantity; unit: m/s'),
        ('Velocity',          'Rate of change of displacement — vector quantity; unit: m/s'),
        ('Acceleration',      'Rate of change of velocity; a = (v−u)/t; unit: m/s²'),
        ('Deceleration',      'Negative acceleration; velocity decreasing with time (retardation)'),
        ('Linear Motion',     'Motion along a straight-line path'),
        ('Circular Motion',   'Motion along a circular path around a fixed centre'),
        ('Rotatory Motion',   'Spinning of a body about its own axis'),
        ('Oscillatory Motion','To-and-fro motion of a body about a mean (rest) position'),
        ('Curvilinear Motion','Motion along a curved path where direction constantly changes'),
        ('Periodic Motion',   'Motion that repeats itself after a fixed time interval'),
        ('Uniform Motion',    'Equal distances covered in equal time intervals'),
        ('Atmospheric Pressure','Weight of atmospheric air per unit area of Earth\'s surface'),
        ('Barometer',         'Instrument to measure atmospheric pressure (mercury barometer)'),
        ('Buoyant Force',     'Upward force exerted by a fluid on a floating or submerged object'),
        ('Pascal\'s Law',     'Pressure applied to a confined liquid is transmitted equally in all directions'),
        ('Hydraulic Lift',    'Device using Pascal\'s Law; small force on small piston → large force on large piston'),
        ('Surface Tension',   'Property of liquid surface to contract; defined as force per unit length; unit: Nm⁻¹'),
        ('Viscosity',         'Property of a liquid to resist flow; internal friction between moving liquid layers'),
        ('Viscous Force',     'Frictional force between adjacent layers of a liquid in relative motion'),
        ('Friction',          'Force opposing relative motion between surfaces in contact; due to surface irregularities'),
        ('Static Friction',   'Friction acting on a body at rest before it starts moving; maximum value = limiting friction'),
        ('Kinetic Friction',  'Friction during motion; includes sliding and rolling friction'),
        ('Sliding Friction',  'Friction when one surface slides over another surface'),
        ('Rolling Friction',  'Friction when a body rolls over a surface; smallest type of friction'),
        ('Lubricant',         'Substance that reduces friction by filling gaps between rough surfaces (oil, grease, graphite)'),
        ('Centre of Gravity', 'Point through which the total weight of an object appears to act'),
        ('Stable Equilibrium','State where displaced object returns to original position; CG rises briefly'),
        ('Unstable Equilibrium','State where displaced object falls away and does NOT return; CG lowers'),
        ('Neutral Equilibrium','State where displaced object stays in new position; CG height unchanged'),
        ('Capillarity',       'Rise of liquid in a narrow tube due to surface tension and adhesion'),
        ('Knot (unit)',        'Unit of speed: 1 knot = 1 nautical mile per hour; used in aviation and shipping'),
    ]

    story += [glossary_2col(gloss), sp(3)]

    # Footer
    story += [
        HRFlowable(width=USABLE_W, thickness=1, color=TEAL),
        sp(1),
        Paragraph('ChalkPieceDiary.com | TET Paper II Science Handbook | P2: Force, Motion & Pressure | All sub-topics: Classes 6, 7 & 8',
                  S('ft', fontName=FNI, fontSize=7, textColor=TEAL, alignment=TA_CENTER)),
    ]

    return story


def build(out_path):
    def add_pg(canvas, doc):
        canvas.saveState()
        canvas.setFont(FN, 7)
        canvas.setFillColor(TEAL)
        canvas.drawRightString(PAGE_W - MARGIN, 11*mm,
                               f'P2 | Force, Motion & Pressure | Page {doc.page}')
        canvas.restoreState()

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=18*mm,
        title='TET Handbook P2: Force Motion Pressure',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=add_pg, onLaterPages=add_pg)
    print(f'PDF: {out_path}')

if __name__ == '__main__':
    out = 'output/P2_Force_Motion_Pressure.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
