"""
TET Paper II Science Handbook — P4: Light
Style: P3 one-liner cheat-sheet | Font: 10.5pt body, 10pt cells
All sub-topics: Class 7 (Term III, Unit 1) & Class 8 (Unit 3)
Also includes Class 6 basics (sources, transparent/opaque, shadow)
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

CHAPTER_ID = "P4"
CHAPTER_TITLE = "Light"
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

FS_BODY = 10.5
FS_CELL = 10.0
FS_SMALL= 9.5
FS_MINI = 9.0
FS_SEC  = 11.0
FS_FORM = 12.0

def S(nm, **kw): return ParagraphStyle(nm, **kw)

BD  = S('bd', fontName=FN,  fontSize=FS_BODY, leading=15,  textColor=GRAY_D, spaceAfter=2)
BDB = S('bb', fontName=FNB, fontSize=FS_BODY, leading=15,  textColor=SLATE)
CE  = S('ce', fontName=FN,  fontSize=FS_CELL, leading=14,  textColor=GRAY_D)
CEB = S('cb', fontName=FNB, fontSize=FS_CELL, leading=14,  textColor=SLATE)
HWC = S('hc', fontName=FNB, fontSize=FS_SMALL,leading=13,  textColor=WHITE, alignment=TA_CENTER)
SC  = S('sc', fontName=FNB, fontSize=FS_SEC,  leading=15,  textColor=WHITE)
MIN = S('mn', fontName=FN,  fontSize=FS_MINI, leading=13,  textColor=GRAY_D)

sp = lambda h: Spacer(1, h*mm)
P  = lambda t, st=BD: Paragraph(t, st)

_SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4',
        '\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9',
        '\u207b':'-','\u207a':'+'}
_SUB = {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4'}
def _fix(text):
    import re as _re
    sc=''.join(_SUP.keys()); bc=''.join(_SUB.keys())
    def rs(m): return '<super>'+''.join(_SUP.get(c,c) for c in m.group())+'</super>'
    def rb(m): return '<sub>'  +''.join(_SUB.get(c,c) for c in m.group())+'</sub>'
    t=_re.sub(f'[{_re.escape(sc)}]+',rs,text)
    t=_re.sub(f'[{_re.escape(bc)}]+',rb,t)
    return t

# ─── BUILDERS ─────────────────────────────────────────────────────────────────

def banner(code, title, sub=''):
    data = [[
        P(f'<font color="white"><b>{code}</b></font>',
          S('bu',fontName=FNB,fontSize=26,leading=30,textColor=WHITE,alignment=TA_CENTER)),
        [P(f'<font color="white"><b>{title}</b></font>',
           S('bt',fontName=FNB,fontSize=16,leading=21,textColor=WHITE)),
         P(f'<font color="#5EEAD4">{sub}</font>' if sub else '',
           S('bs',fontName=FNI,fontSize=9.5,leading=12,textColor=TEAL_M)),
         sp(1),
         P('<font color="#CCFBF1">Classes 6 • 7 • 8  |  TET Paper II Science</font>',
           S('bi',fontName=FN,fontSize=8.5,leading=11,textColor=TEAL_L))]
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
    t = Table([[P(title, S('sh',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=WHITE))]],
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
        total = sum(ws)
        if total and abs(total - UW) > 1e-6:
            ws = [w * (UW / total) for w in ws]
    data=[[P(h,HWC) for h in hdrs]]
    for row in rows:
        data.append([P(_fix(c),CE) if isinstance(c,str) else c for c in row])
    t=Table(data,colWidths=ws,repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),hbg),('GRID',(0,0),(-1,-1),0.4,GRAY_M),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),2.5*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[alt,WHITE]),
    ]))
    return t

def one_liners(items, bg_bullet=TEAL, key_w=55*mm):
    result_tables=[]
    cur_b=[]; cur_kv=[]; prev=None

    def flush_b():
        if not cur_b: return
        t=Table(cur_b,colWidths=[6*mm,UW-6*mm])
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),2*mm),('RIGHTPADDING',(0,0),(-1,-1),2.5*mm),
            ('TOPPADDING',(0,0),(-1,-1),1.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
            ('LINEBELOW',(0,0),(-1,-2),0.25,GRAY_M),
        ]))
        result_tables.append(t)

    def flush_kv():
        if not cur_kv: return
        t=Table(cur_kv,colWidths=[key_w,UW-key_w])
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
        if isinstance(item,tuple):
            if prev=='b': flush_b(); cur_b=[]
            key,val=item
            cur_kv.append([
                P(f'<b>{key}</b>',S('ok',fontName=FNB,fontSize=FS_CELL,leading=14,textColor=WHITE)),
                P(_fix(val),       S('ov',fontName=FN, fontSize=FS_CELL,leading=14,textColor=SLATE)),
            ])
            prev='kv'
        else:
            if prev=='kv': flush_kv(); cur_kv=[]
            cur_b.append([
                P('▶',S('ob',fontName=FNB,fontSize=FS_CELL,leading=14,textColor=bg_bullet,alignment=TA_CENTER)),
                P(_fix(item),S('oi',fontName=FN,fontSize=FS_CELL,leading=14,textColor=SLATE)),
            ])
            prev='b'

    flush_b(); flush_kv()
    if len(result_tables)==1: return result_tables[0]
    wrap=Table([[t] for t in result_tables],colWidths=[UW])
    wrap.setStyle(TableStyle([
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),1.5*mm),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return wrap

def kv_list(items, bg_L=TEAL, bg_R=TEAL_L, w_L=50*mm):
    rows=[]
    for key,val in items:
        rows.append([
            P(key,S('kl',fontName=FNB,fontSize=FS_CELL,leading=14,textColor=WHITE)),
            P(_fix(val),S('kr',fontName=FN,fontSize=FS_CELL,leading=14,textColor=SLATE)),
        ])
    t=Table(rows,colWidths=[w_L,UW-w_L])
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
    note_t=f'  <font size="8.5" color="#94A3B8">({_fix(note)})</font>' if note else ''
    t=Table([[
        P(label,S('fl',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=TEAL_M)),
        P(f'<b><font color="white">{_fix(formula)}</font></b>{note_t}',
          S('ff',fontName=FNB,fontSize=FS_FORM,leading=16,textColor=WHITE,alignment=TA_CENTER)),
    ]],colWidths=[48*mm,UW-48*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),3*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),3*mm),('BOTTOMPADDING',(0,0),(-1,-1),3*mm),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ]))
    return t

def pill(icon, text, bg=GREEN_L, fg=GREEN_D):
    t=Table([[P(f'{icon}  {_fix(text)}',
                S('pi',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=fg))]],
            colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
        ('BOX',(0,0),(-1,-1),0.6,fg),
    ]))
    return t

def note_box(title, items, bg_h=AMBER, bg_b=AMBER_L, icon='📌'):
    rows=[[P(f'{icon}  {title}',
             S('nt',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=WHITE))]]
    for item in items:
        rows.append([P(f'↳  {_fix(item)}',S('ni',fontName=FN,fontSize=FS_CELL,leading=14,textColor=SLATE))])
    t=Table(rows,colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),bg_h),('BACKGROUND',(0,1),(-1,-1),bg_b),
        ('BOX',(0,0),(-1,-1),1,bg_h),('LINEBELOW',(0,0),(0,0),1,bg_h),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t

def dyk(items, hbg=PURPLE_D, bg=PURPLE_L):
    rows=[[P('💡 Did You Know?',
             S('dk',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=WHITE))]]
    for item in items:
        rows.append([P(f'◆  {_fix(item)}',S('di',fontName=FN,fontSize=FS_CELL,leading=14,textColor=SLATE))])
    t=Table(rows,colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0),hbg),('BACKGROUND',(0,1),(-1,-1),bg),
        ('BOX',(0,0),(-1,-1),1,hbg),('LINEBELOW',(0,0),(0,0),1,hbg),
        ('LEFTPADDING',(0,0),(-1,-1),4*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2*mm),('BOTTOMPADDING',(0,0),(-1,-1),2*mm),
    ]))
    return t

def two_col(L, R):
    def mk(items): return [P(_fix(x)) if isinstance(x,str) else x for x in items]
    t=Table([[mk(L),mk(R)]],colWidths=[CW,CW])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),
        ('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0),
        ('INNERGRID',(0,0),(-1,-1),0,WHITE),('BOX',(0,0),(-1,-1),0,WHITE),
    ]))
    return t

def prob(num, q, given, soln, ans):
    rows=[
        [P(f'Problem {num}',S('pt',fontName=FNB,fontSize=FS_CELL,textColor=BLUE_D)),P(q,BD)],
        [P('Given',CEB),P(_fix(given),CE)],
        [P('Solution',CEB),P(_fix(soln),CE)],
        [P('Answer',S('pa',fontName=FNB,fontSize=FS_CELL,textColor=GREEN_D)),
         P(f'<b><font color="#14532D">{_fix(ans)}</font></b>',CE)],
    ]
    t=Table(rows,colWidths=[24*mm,UW-24*mm])
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
                ws=[60*mm,74*mm,40*mm],hbg=TEAL_D)

def rapid_ppl(rows):
    return grid(['Scientist / Event','Contribution / Fact','Year / Class'], rows,
                ws=[50*mm,86*mm,38*mm],hbg=PURPLE_D)

def gloss_2col(terms):
    rows=[]
    for i in range(0,len(terms),2):
        L=P(f'<b>{terms[i][0]}</b> — {terms[i][1]}',MIN)
        R=P(f'<b>{terms[i+1][0]}</b> — {terms[i+1][1]}',MIN) if i+1<len(terms) else P('',MIN)
        rows.append([L,R])
    t=Table(rows,colWidths=[CW,CW])
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

    s += [banner('P4','Light','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  SOURCES OF LIGHT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  SOURCES OF LIGHT — Natural & Artificial'), sp(2)]

    s += [kv_list([
        ('Light',            'Form of energy that enables us to see objects — stimulates the retina of our eye'),
        ('Luminous Object',  'Object that produces/emits its own light — e.g., Sun, stars, firefly, electric bulb, candle'),
        ('Non-luminous Object','Object that does NOT produce its own light — reflects light from another source — e.g., Moon, planets'),
        ('Moon',             'NOT luminous — reflects sunlight toward Earth; only the lit half visible from Earth'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Natural Sources of Light'), sp(1)]
    s += [one_liners([
        ('Sun',          'Primary and major source of natural light — essential for photosynthesis'),
        ('Stars',        'Produce light just like the Sun — appear dim because they are far away'),
        ('Firefly',      'Produces light by bioluminescence — chemical reaction inside the organism'),
        ('Bioluminescence','Ability of living organisms to produce light — fireflies, jellyfish, glow worms, deep sea creatures'),
    ]), sp(2)]

    s += [sub_h('Artificial Sources of Light'), sp(1)]
    s += [grid(
        ['Type of Artificial Source','Description','Examples'],
        [
            ['Incandescent Sources',
             'Objects heated to very high temperature begin to emit light — heat → light',
             'Candle, incandescent lamp (electric bulb), glowing hot iron rod'],
            ['Gas Discharge Sources',
             'Electricity passed through gas at very low pressure produces light — electrical discharge → light',
             'Neon lamp (Ne gas), Sodium lamp — used in street lights'],
            ['Fluorescent Sources',
             'UV light from mercury vapour excites phosphor coating on bulb → visible light',
             'Tube light (CFL) — gas discharge + fluorescence'],
        ],
        ws=[40*mm,72*mm,62*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  PROPERTIES OF LIGHT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  PROPERTIES OF LIGHT — Rectilinear Propagation & Speed'), sp(2)]

    s += [kv_list([
        ('Rectilinear Propagation','Light travels in a STRAIGHT LINE — cannot bend on its own path'),
        ('Speed of Light',         '3 × 10<super>8</super> m/s in air or vacuum — nothing can travel faster than light'),
        ('Light year',             'Distance light travels in one year — 9.46 × 10<super>15</super> m — used for astronomical distances'),
    ], bg_L=BLUE_D, bg_R=BLUE_L), sp(2)]

    s += [one_liners([
        'Evidence of rectilinear propagation: light through holes in matchboxes visible only when all holes align in a straight line',
        'Pinhole camera works because light travels in straight lines — image formed is inverted and real',
        'Al-Hasan al-Haytham (Arab scientist) — first to experiment with light; proved light enters eye from external source, not emitted by eye',
        'Solography: pinhole camera used to photograph Sun\'s movement over long periods',
        ('Parallel beam',    'Rays parallel to each other — e.g., sunlight, car headlights'),
        ('Convergent beam',  'Rays meeting at a point — e.g., rays focused by a lens'),
        ('Divergent beam',   'Rays spreading outward from a point — e.g., candle flame, torch'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  TRANSPARENT, TRANSLUCENT & OPAQUE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  INTERACTION OF LIGHT WITH MATTER — Transparent, Translucent, Opaque'), sp(2)]

    s += [grid(
        ['Type','Definition','Examples (Class 7 Textbook)'],
        [
            ['Transparent Material',
             'Allows light to pass through COMPLETELY — objects clearly visible through it',
             'Clear glass, eyeglasses, clear drinking glass, clear water, bus face glass, clear plastic ruler, clear water in jar'],
            ['Translucent Material',
             'Allows light to pass through PARTIALLY — objects not clearly visible through it',
             'Rough window glass, cellophane paper, tissue paper, oiled paper, frosted glass, coconut oil, diluted milk'],
            ['Opaque Material',
             'Does NOT allow light to pass through — objects not visible through it at all',
             'Wall, thick cardboard, stone, metal sheet, wood, aluminium foil, milk, thick coloured plastic'],
        ],
        ws=[32*mm,72*mm,70*mm]
    ), sp(2)]

    s += [note_box('Exam Trap — Transparent vs Translucent', [
        'Transparent: can see CLEAR image through it (eyeglasses, clear window)',
        'Translucent: light passes but image is BLURRED (frosted glass, tissue paper)',
        'Opaque: NO light passes through — forms SHADOW (wood, metal, thick cardboard)',
        'Same material can behave differently: thick glass = opaque; thin clear glass = transparent',
    ], icon='⚠')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  SHADOWS — Umbra & Penumbra
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  SHADOWS — Umbra, Penumbra & Eclipses'), sp(2)]

    s += [kv_list([
        ('Shadow',    'Dark region formed when an opaque object blocks light — shadow is on the OPPOSITE side of the light source'),
        ('Umbra',     'Completely dark inner region of shadow — NO light reaches here — formed when point source used'),
        ('Penumbra',  'Partially lit outer region around umbra — some light reaches here — formed with broad/extended source'),
    ], bg_L=TEAL_D, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Properties of Shadows'), sp(1)]
    s += [one_liners([
        'Only OPAQUE objects form shadows (transparent objects do not form shadows)',
        'Shadow is always on the OPPOSITE side of the light source from the object',
        'The colour of the light does NOT affect the colour of the shadow — shadow is always dark',
        'Light source + opaque object + shadow — all in the SAME straight line',
        'Size of shadow depends on: (1) distance between light source and object (2) distance between object and screen',
        'Smaller the light source → larger the umbra (point source → no penumbra, only umbra)',
        'Larger the light source → smaller the umbra + larger penumbra',
    ]), sp(2)]

    s += [sub_h('Solar & Lunar Eclipses'), sp(1)]
    s += [grid(
        ['Eclipse','When it Occurs','Shadow Type','Who Experiences'],
        [
            ['Solar Eclipse',
             'Moon comes BETWEEN the Sun and Earth — Moon\'s shadow falls on Earth',
             'Umbra = Total solar eclipse (complete darkness) | Penumbra = Partial solar eclipse',
             'People in umbra region (A) = total eclipse | People in penumbra (B,C) = partial eclipse'],
            ['Lunar Eclipse',
             'Earth comes BETWEEN the Sun and Moon — Earth\'s shadow falls on the Moon',
             'Earth blocks sunlight from reaching the Moon',
             'Visible from the night side of Earth — Moon appears red/dark during lunar eclipse'],
        ],
        ws=[26*mm,50*mm,50*mm,48*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  REFLECTION OF LIGHT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  REFLECTION OF LIGHT — Laws, Types & Terms'), sp(2)]

    s += [kv_list([
        ('Reflection',        'Bouncing back of light rays when they fall on a smooth, shiny, polished surface'),
        ('Incident Ray',      'Ray of light falling on the reflecting surface (PO in diagrams)'),
        ('Reflected Ray',     'Ray of light bouncing back from the reflecting surface after reflection (OQ)'),
        ('Normal',            'Imaginary perpendicular line drawn at the point of incidence to the reflecting surface (ON)'),
        ('Angle of Incidence (i)', 'Angle between incident ray and normal at point of incidence'),
        ('Angle of Reflection (r)','Angle between reflected ray and normal at point of incidence'),
        ('Point of Incidence','The exact point on the reflecting surface where the incident ray strikes (O)'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=52*mm), sp(2)]

    s += [sub_h('Laws of Reflection'), sp(1)]
    s += [one_liners([
        'LAW 1 — The angle of incidence (i) is ALWAYS EQUAL to the angle of reflection (r):  i = r',
        'LAW 2 — The incident ray, the reflected ray, and the normal at the point of incidence all lie in the SAME PLANE',
        'Laws of reflection hold for ALL surfaces — smooth or rough, flat or curved',
        'Silver metal is the BEST reflector of light — thin silver layer deposited on glass makes a mirror',
    ]), sp(2)]

    s += [sub_h('Types of Reflection'), sp(1)]
    s += [grid(
        ['Type of Reflection','Surface','What Happens','Example','Image Formed?'],
        [
            ['Regular (Specular) Reflection',
             'Smooth, polished, flat',
             'Parallel rays remain parallel after reflection — each ray obeys law of reflection equally',
             'Plane mirror, still water surface',
             'YES — clear, sharp image'],
            ['Irregular (Diffuse) Reflection',
             'Rough, uneven',
             'Parallel rays scatter in different directions after reflection — different normals at each point',
             'Wall, paper, road surface',
             'NO — no clear image; but allows us to SEE the object'],
        ],
        ws=[36*mm,26*mm,50*mm,32*mm,30*mm]
    ), sp(2)]

    s += [pill('💡', 'Diffuse reflection from walls illuminates the entire room — if walls were smooth mirrors, only parts directly lit by window would be visible.', PURPLE_L, PURPLE)]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  PLANE MIRROR — Images
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  PLANE MIRROR — Image Properties'), sp(2)]

    s += [sub_h('Properties of Image formed in a Plane Mirror — Memorise all 5'), sp(1)]
    s += [one_liners([
        ('Upright (Erect)',         'Image is right-side up — not inverted (unlike pinhole camera which gives inverted image)'),
        ('Virtual',                 'Image CANNOT be formed on a screen — appears to be behind the mirror'),
        ('Same size as object',     'Image size = Object size — magnification = 1 (neither enlarged nor diminished)'),
        ('Same distance behind mirror','Image distance from mirror = Object distance from mirror: a = b'),
        ('Laterally inverted',      'Left and right are swapped — left hand appears as right hand in mirror; "AMBULANCE" written reversed on vehicles so drivers see it correctly in rear-view mirror'),
    ]), sp(2)]

    s += [grid(
        ['','Pinhole Camera','Plane Mirror'],
        [
            ['Image type',     'Real (can be formed on screen)',  'Virtual (cannot be formed on screen)'],
            ['Orientation',    'Inverted (upside down)',          'Erect (upright)'],
            ['Size',           'May differ from object size',     'Same size as object'],
            ['How it works',   'Light passes through tiny hole',  'Light reflects off mirror surface'],
        ],
        ws=[30*mm,72*mm,72*mm]
    ), sp(2)]

    s += [dyk([
        '"AMBULANCE" written backwards on vehicle front — drivers see it correctly in their rear-view mirror due to LATERAL INVERSION.',
        'Multiple images in two mirrors: If angle between mirrors = θ, number of images = (360°/θ) - 1. For 90°: 3 images. For 60°: 5 images. For 45°: 7 images.',
        'When two mirrors are PARALLEL to each other, the number of images formed is INFINITE.',
    ])]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  MULTIPLE REFLECTION — Kaleidoscope & Periscope
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  MULTIPLE REFLECTION — Kaleidoscope & Periscope'), sp(2)]

    s += [fstrip('Images in 2 mirrors', 'n = (360° / θ) - 1', 'n = number of images; θ = angle between mirrors', BLUE_D)]
    s += [sp(2)]

    s += [grid(
        ['Device','Principle','Structure','Uses'],
        [
            ['Kaleidoscope',
             'Multiple reflection of light between mirrors inclined to each other — creates repeated patterns',
             '2 or 3 mirrors inclined at 60° angle, forming equilateral triangle; coloured objects (beads, bangles) inside',
             'Toy for children; design patterns; used by artists for symmetrical design inspiration'],
            ['Periscope',
             'Law of reflection — mirrors at each end of tube reflect light so observer can see over/around barriers',
             'Long tube with 2 plane mirrors at 45° at each end; light enters top, reflects down, reflects again to eye',
             'Submarines to see above water surface; military (bunker shooting); photographing restricted areas; doctors use fibre-optic endoscopes (similar principle)'],
        ],
        ws=[26*mm,52*mm,52*mm,44*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  SPHERICAL MIRRORS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  SPHERICAL MIRRORS — Concave & Convex'), sp(2)]

    s += [sub_h('Key Terms — Spherical Mirrors'), sp(1)]
    s += [kv_list([
        ('Pole (P)',              'Geometric centre of the spherical mirror — where principal axis meets the mirror surface'),
        ('Centre of Curvature (C)','Centre of the sphere from which the mirror is made — lies in front of concave, behind convex'),
        ('Radius of Curvature (R)','Distance between the centre of sphere and the pole (vertex) of the mirror'),
        ('Principal Axis',        'Imaginary line joining the Pole (P) and Centre of Curvature (C) of the mirror'),
        ('Focus / Focal Point (F)','Point where reflected rays converge (concave) or appear to diverge from (convex) on principal axis'),
        ('Focal Length (f)',      'Distance between the Pole (P) and the Focus (F): f = R/2'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=52*mm), sp(2)]

    s += [fstrip('Focal Length Formula', 'f = R / 2  →  R = 2f', 'Focal length = half of radius of curvature', TEAL_D)]
    s += [sp(2)]

    s += [sub_h('Concave vs Convex Mirror — Comparison'), sp(1)]
    s += [grid(
        ['Feature','Concave Mirror','Convex Mirror'],
        [
            ['Reflecting surface', 'Curved INWARD (like inside of bowl)', 'Curved OUTWARD (like outside of bowl)'],
            ['Image — general',    'Real and inverted (usually); virtual and erect only when object between F and P', 'Always VIRTUAL, ERECT and DIMINISHED'],
            ['Field of view',      'Narrow field of view',        'WIDER field of view — sees larger area'],
            ['Image size',         'Magnified (when object close) or diminished (when object far)', 'Always SMALLER than object'],
            ['Common uses',        'Make-up mirror; shaving mirror; torch/headlight; solar cooker; head mirror for ENT doctors; reflecting telescope', 'Rear-view mirror in vehicles; hallway safety mirrors; shop security mirrors; road curve mirrors'],
        ],
        ws=[36*mm,69*mm,69*mm]
    ), sp(2)]

    s += [sub_h('Image Formation by Concave Mirror — Position-wise'), sp(1)]
    s += [grid(
        ['Object Position','Image Position','Image Size','Nature'],
        [
            ['At Infinity',          'At F (focus)',         'Highly diminished (point-sized)', 'Real, Inverted'],
            ['Beyond C',             'Between C and F',      'Diminished',                     'Real, Inverted'],
            ['At C',                 'At C',                 'Same size as object',             'Real, Inverted'],
            ['Between C and F',      'Beyond C',             'Magnified (enlarged)',            'Real, Inverted'],
            ['At F (focus)',         'At Infinity',          'Highly magnified',               'Real, Inverted'],
            ['Between F and P (Pole)','Behind mirror',       'Magnified',                      'Virtual, Erect'],
        ],
        ws=[44*mm,34*mm,40*mm,56*mm]
    ), sp(2)]

    s += [pill('📌', 'Concave mirror ALWAYS forms real and inverted image EXCEPT when object is between F and P — then image is virtual and erect.', CYAN_L, CYAN)]
    s += [sp(2)]

    s += [sub_h('Image Formation by Convex Mirror'), sp(1)]
    s += [one_liners([
        'Object at Infinity → Image at F (behind mirror) → Highly diminished, point-sized → Virtual and Erect',
        'Object between Infinity and Pole → Image between P and F (behind mirror) → Diminished → Virtual and Erect',
        'Convex mirror image is ALWAYS virtual, erect and diminished — regardless of object position',
    ]), sp(2)]

    s += [sub_h('Applications of Curved Mirrors'), sp(1)]
    s += [two_col(
        ['<b>Concave Mirror Uses:</b>',
         '• Make-up / shaving mirror — magnifies face',
         '• Torch, search lights, headlights — focuses light to travel far',
         '• Solar cooker — collects and focuses sunlight',
         '• Head mirror (ENT doctors) — provides shadow-free illumination',
         '• Reflecting telescope — collects light from stars'],
        ['<b>Convex Mirror Uses:</b>',
         '• Rear-view mirror in vehicles — wider field of view; objects appear closer (safety warning)',
         '• Hallway mirrors in hospitals, hotels — safety at sharp turns',
         '• Road curve mirrors — see traffic around bends',
         '• Shop security mirrors — wider area surveillance',
         '• Parabolic mirrors — solar water heaters, radio telescopes, parabolic microphones']
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  REFRACTION OF LIGHT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  REFRACTION OF LIGHT — Snell\'s Law & Refractive Index'), sp(2)]

    s += [kv_list([
        ('Refraction',       'Bending of light at the normal when it passes from one transparent medium to another — due to change in speed'),
        ('Rarer Medium',     'Medium in which light travels FASTER — e.g., air (lower optical density)'),
        ('Denser Medium',    'Medium in which light travels SLOWER — e.g., water, glass (higher optical density)'),
        ('Rarer → Denser',   'Light BENDS TOWARDS the normal (angle of refraction < angle of incidence)'),
        ('Denser → Rarer',   'Light BENDS AWAY from the normal (angle of refraction > angle of incidence)'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=48*mm), sp(2)]

    s += [fstrip('Refractive Index (μ)', 'μ = Speed of light in air (c) / Speed of light in medium (v)', 'Absolute refractive index — always > 1; no unit', BLUE_D)]
    s += [sp(1)]
    s += [fstrip('Snell\'s Law', 'sin i / sin r = μ (constant)', 'i = angle of incidence; r = angle of refraction', TEAL_D)]
    s += [sp(2)]

    s += [sub_h('Snell\'s Laws of Refraction'), sp(1)]
    s += [one_liners([
        'LAW 1 — The incident ray, the refracted ray and the normal at the point of incidence all lie in the SAME PLANE',
        'LAW 2 — The ratio of sine of angle of incidence to sine of angle of refraction = refractive index (constant) for that medium',
        'Refractive index has NO UNIT — it is a ratio of two speeds (same quantity)',
        'Refractive index of any transparent medium is ALWAYS GREATER THAN 1 (light speed in medium < light speed in air)',
    ]), sp(2)]

    s += [sub_h('Refractive Index Values'), sp(1)]
    s += [grid(
        ['Substance','Refractive Index (μ)','Relative Speed of Light'],
        [
            ['Air',             '1.0  (reference)',  'Fastest — reference medium'],
            ['Water',           '1.33',              'Slower than air'],
            ['Ether',           '1.36',              'Slower than air'],
            ['Kerosene',        '1.41',              'Slower than air'],
            ['Ordinary Glass',  '1.5',               'Much slower than air'],
            ['Quartz',          '1.56',              'Much slower than air'],
            ['Diamond',         '2.41',              'Slowest — highest refractive index — that\'s why it sparkles!'],
        ],
        ws=[40*mm,36*mm,98*mm]
    ), sp(2)]

    s += [one_liners([
        'Why pencil in water appears bent: light travels from water (denser) to air (rarer) → bends away from normal → pencil looks bent',
        'Why pool appears shallower than actual depth: refraction at water-air boundary',
        'Why a coin invisible in empty bowl becomes visible when water added: refraction bends light toward your eye',
        ('Higher refractive index', 'More the bending of light; slower light travels in that medium'),
        ('Diamond (μ=2.41)',        'Light bends dramatically inside diamond → total internal reflection → sparkle effect'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  DISPERSION OF LIGHT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  DISPERSION OF LIGHT — Spectrum, VIBGYOR & Rainbow'), sp(2)]

    s += [kv_list([
        ('Dispersion',       'Splitting of white light into its seven constituent colours when passed through a transparent medium (prism)'),
        ('Spectrum',         'Band of seven colours produced by dispersion: VIBGYOR'),
        ('Prism',            'Transparent object with at least two flat surfaces forming an acute angle — refracts and disperses light'),
        ('VIBGYOR',          'Violet-Indigo-Blue-Green-Yellow-Orange-Red — order of colours in white light spectrum'),
        ('White light',      'Combination of ALL seven colours of visible spectrum — NOT a single colour'),
        ('Black',            'Absence of ALL wavelengths of visible light — opposite of white'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=36*mm), sp(2)]

    s += [sub_h('VIBGYOR — Wavelength & Deviation'), sp(1)]
    s += [grid(
        ['Colour','Wavelength','Deviation in Prism','Speed in Medium'],
        [
            ['Violet (V)', 'SHORTEST (~400 nm)', 'MOST deviated (bends most)',      'Slowest in medium'],
            ['Indigo (I)', 'Short',              'Highly deviated',                 'Very slow'],
            ['Blue (B)',   'Short',              'Highly deviated',                 'Slow'],
            ['Green (G)',  'Medium',             'Moderate deviation',              'Moderate'],
            ['Yellow (Y)', 'Medium-long',        'Moderate deviation',              'Moderate-fast'],
            ['Orange (O)', 'Long',               'Less deviated',                  'Fast'],
            ['Red (R)',    'LONGEST (~700 nm)',   'LEAST deviated (bends least)',   'Fastest in medium'],
        ],
        ws=[24*mm,36*mm,44*mm,70*mm]
    ), sp(2)]

    s += [one_liners([
        'Wavelength range of visible light: 400 nm (violet) to 700 nm (red) — 1 nm = 10<super>-9</super> metre',
        'Refraction is INVERSELY proportional to wavelength — shorter wavelength bends MORE',
        'Red light scattered LEAST by air → travels farthest through fog → used for danger signals in vehicles',
        'Why rainbow is seen opposite to Sun: white sunlight passing through water droplets undergoes dispersion → VIBGYOR formed',
        'Newton Disc: seven VIBGYOR colour sectors on rotating cardboard disc → appears white when spun fast (colour synthesis)',
        'Synthesis: mixing all VIBGYOR colours → white light; absence of all → black',
        'Second prism (inverted) after first prism recombines the seven colours back to white light',
        'Wavelength 400-700nm is VISIBLE LIGHT range; below 400nm = UV (invisible); above 700nm = IR (invisible)',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  OPTICAL FIBRE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  OPTICAL FIBRE — Total Internal Reflection'), sp(2)]

    s += [kv_list([
        ('Optical Fibre',       'Device based on TOTAL INTERNAL REFLECTION — transmits light signals with negligible energy loss'),
        ('Total Internal Reflection','When light in denser medium hits boundary at angle > critical angle, it is COMPLETELY reflected back — does not pass through'),
        ('Structure',           'Cable with thin flexible glass core; light travels through repeated internal reflections from one end to other'),
        ('Data transmission',   'Information sent as pulses of light through bundles of optical fibres'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [one_liners([
        'Optical fibres carry MORE data than traditional copper cable telephone lines',
        'Used in: cable TV, high-speed broadband internet, fibre optic communications',
        'Medical use: fibre-optic endoscopes used by doctors to see inside body organs (stomach, intestine)',
        'Periscopes sometimes use optical fibre instead of mirrors for higher resolution images',
        'Fibre can be twisted and bent — light still travels to the other end with negligible loss',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # L  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('L  ·  Solved Numerical Problems'), sp(2)]

    probs = [
        ('1','The radius of curvature of a spherical mirror is 20 cm. Find its focal length.',
         'R = 20 cm',
         'f = R / 2 = 20 / 2 = 10 cm',
         'Focal length = 10 cm'),
        ('2','Focal length of a spherical mirror is 7 cm. Find its radius of curvature.',
         'f = 7 cm',
         'R = 2 × f = 2 × 7 = 14 cm',
         'Radius of curvature = 14 cm'),
        ('3','A light ray strikes a plane surface at 43° with the plane surface. Find: (i) angle of incidence (ii) angle of reflection (iii) angle between incident and reflected ray.',
         'Angle with surface = 43°; Normal is perpendicular to surface',
         '(i) Angle of incidence i = 90° - 43° = 47°  |  (ii) By law of reflection: r = i = 47°  |  (iii) i + r = 47° + 47° = 94°',
         'i = 47°; r = 47°; angle between rays = 94°'),
        ('4','Two plane mirrors are inclined at 90° to each other. Find the number of images formed.',
         'Angle θ = 90°',
         'n = (360° / θ) - 1 = (360° / 90°) - 1 = 4 - 1 = 3',
         'Number of images = 3'),
        ('5','Speed of light in air = 3 × 10<super>8</super> m/s; speed in medium = 2 × 10<super>8</super> m/s. Find refractive index.',
         'c = 3 × 10<super>8</super> m/s; v = 2 × 10<super>8</super> m/s',
         'μ = c / v = (3 × 10<super>8</super>) / (2 × 10<super>8</super>) = 1.5',
         'Refractive index μ = 1.5 (same as ordinary glass)'),
        ('6','Refractive index of water = 4/3; refractive index of glass = 3/2. Find refractive index of glass w.r.t. water.',
         'μ(water) = 4/3; μ(glass) = 3/2',
         'w μ g = μ(glass) / μ(water) = (3/2) / (4/3) = (3/2) × (3/4) = 9/8 = 1.125',
         'Refractive index of glass w.r.t. water = 9/8 = 1.125'),
    ]

    for p in probs:
        s += [prob(*p), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # M  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('M  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Formulas, Values & Key Numbers</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Speed of light',             '3 × 10<super>8</super> m/s in air/vacuum (3 lakh km/s)',      'Fastest possible speed'],
        ['Light year',                  '9.46 × 10<super>15</super> m — distance light travels in 1 year', 'Astronomical unit'],
        ['Visible light wavelength',    '400 nm (violet) to 700 nm (red)',                             '1 nm = 10<super>-9</super> m'],
        ['Focal length formula',        'f = R/2  →  R = 2f',                                         'Spherical mirrors'],
        ['Refractive index',            'μ = c/v = speed in air / speed in medium',                  'No unit; always > 1'],
        ['Snell\'s Law',               'sin i / sin r = μ (constant)',                                'Refraction law'],
        ['μ of Air',                    '1.0 (reference)',                                             'Rarer medium'],
        ['μ of Water',                  '1.33',                                                         'Common in questions'],
        ['μ of Glass (ordinary)',        '1.5',                                                         'Most common in problems'],
        ['μ of Diamond',               '2.41 (highest common substance)',                              'Sparkle due to TIR'],
        ['Number of images (2 mirrors)','n = (360°/θ) - 1',                                           'θ = angle between mirrors'],
        ['90° mirrors',                 '(360/90) - 1 = 3 images',                                    'Common exam question'],
        ['60° mirrors',                 '(360/60) - 1 = 5 images',                                    'Kaleidoscope typical angle'],
        ['Parallel mirrors (θ=0°)',     'Infinite images',                                             'e.g., two walls of a corridor'],
        ['Concave mirror — at C',       'Image at C; same size; real and inverted',                    'Key position'],
        ['Concave mirror — at F',       'Image at infinity; highly magnified; real and inverted',      'Key position'],
        ['Concave — between F and P',   'Image virtual, erect, magnified (behind mirror)',             'Only virtual case'],
        ['Convex mirror — always',      'Virtual, erect, diminished — regardless of object position', 'Key fact'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoveries & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['Al-Hasan al-Haytham',   'First to experiment with light; proved rectilinear propagation; proved light enters eye from outside (not emitted by eye)', '10th–11th century'],
        ['Isaac Newton',          'Newton Disc experiment — showed VIBGYOR colours recombine to give white light; studied dispersion with prism', '1666'],
        ['Diocles (mathematician)','Wrote "On Burning Mirrors" — first mention of parabolic mirrors', 'Greco-Roman times'],
        ['Ibn Sahl (physicist)',   'Studied parabolic mirrors in 10th century',                       '10th century'],
        ['Heinrich Hertz',        'Constructed first parabolic mirrors as reflector antennae',        '1888'],
        ['SI Unit of angle (Radian)','Plane angle = radian | Solid angle = steradian',                '1995 reclassified'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # N  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('N  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Light',                   'Form of energy that enables us to see — stimulates the retina of the eye'),
        ('Luminous Object',         'Object that produces its own light — e.g., Sun, stars, electric bulb, firefly'),
        ('Non-luminous Object',     'Object that does not produce its own light — reflects light — e.g., Moon, planets'),
        ('Bioluminescence',         'Production of light by living organisms through chemical reactions — e.g., firefly, jellyfish'),
        ('Incandescent Source',     'Light produced by heating object to high temperature — e.g., candle, bulb'),
        ('Rectilinear Propagation', 'Property of light to travel in a straight line'),
        ('Pinhole Camera',          'Simple device demonstrating rectilinear propagation; forms real, inverted image through tiny hole'),
        ('Transparent Material',    'Allows light to pass through completely — clear image visible through it'),
        ('Translucent Material',    'Allows light to pass partially — objects visible but not clearly through it'),
        ('Opaque Material',         'Does not allow light to pass through — forms shadows'),
        ('Shadow',                  'Dark region formed when opaque object blocks light on the opposite side of light source'),
        ('Umbra',                   'Completely dark region of shadow — no light reaches — formed with point source'),
        ('Penumbra',                'Partially lit outer region of shadow — some light reaches — formed with extended source'),
        ('Reflection',              'Bouncing back of light rays when they fall on a smooth, polished surface'),
        ('Incident Ray',            'Light ray falling on the reflecting surface'),
        ('Reflected Ray',           'Light ray bouncing back after reflection'),
        ('Normal',                  'Imaginary perpendicular line at the point of incidence on the reflecting surface'),
        ('Angle of Incidence (i)',  'Angle between incident ray and normal at point of incidence'),
        ('Angle of Reflection (r)', 'Angle between reflected ray and normal — always equals angle of incidence'),
        ('Regular (Specular) Reflection','Reflection from smooth surface — reflected rays are parallel — forms clear image'),
        ('Diffuse (Irregular) Reflection','Reflection from rough surface — reflected rays scatter — no clear image formed'),
        ('Plane Mirror',            'Mirror with flat, polished reflective surface'),
        ('Lateral Inversion',       'Left-right reversal in plane mirror image'),
        ('Virtual Image',           'Image that cannot be formed on a screen — appears behind the mirror'),
        ('Real Image',              'Image that can be formed on a screen — formed by actual convergence of light rays'),
        ('Spherical Mirror',        'Mirror that is part of a hollow sphere — either concave or convex'),
        ('Concave Mirror',          'Spherical mirror reflecting at inner (concave) curved surface — converging mirror'),
        ('Convex Mirror',           'Spherical mirror reflecting at outer (convex) curved surface — diverging mirror'),
        ('Focal Length (f)',        'Distance from pole (P) to focus (F) of a spherical mirror: f = R/2'),
        ('Radius of Curvature (R)', 'Distance from centre of curvature to pole of mirror: R = 2f'),
        ('Kaleidoscope',            'Toy based on multiple reflection — 2 or 3 mirrors inclined at 60° create symmetrical patterns'),
        ('Periscope',               'Instrument using 2 mirrors at 45° to see over or around obstacles — used in submarines'),
        ('Refraction',              'Bending of light as it passes from one transparent medium to another due to change in speed'),
        ('Refractive Index (μ)',    'Ratio of speed of light in air to speed in medium — μ = c/v; no unit; always > 1'),
        ('Snell\'s Law',           'sin i / sin r = μ (constant) for a given medium — law governing refraction'),
        ('Dispersion',              'Splitting of white light into VIBGYOR when passed through a transparent medium like prism'),
        ('VIBGYOR',                 'Violet-Indigo-Blue-Green-Yellow-Orange-Red — order of colours in white light spectrum'),
        ('Spectrum',                'Band of colours produced when white light is dispersed — wavelength 400nm to 700nm'),
        ('Total Internal Reflection','Complete reflection of light inside denser medium when angle > critical angle — basis of optical fibre'),
        ('Optical Fibre',           'Thin glass fibre transmitting light signals by total internal reflection — used in communication and medicine'),
        ('Parabolic Mirror',        'Mirror with parabolic shape — focuses all parallel rays to a single focal point — used in solar cookers, telescopes'),
    ]

    s += [gloss_2col(g), sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P4: Light  |  Classes 6 • 7 • 8',
          S('ft',fontName=FNI,fontSize=8.5,textColor=TEAL,alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P4  |  Light  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P4 Light',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P4_light.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
