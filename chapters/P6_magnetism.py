"""
TET Paper II Science Handbook — P6: Magnetism
Style: P3 one-liner cheat-sheet | Font: 10.5pt body, 10pt cells
All sub-topics: Class 6 (Term III, Unit 1) & Class 8 (Unit 7)
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

CHAPTER_ID = "P6"
CHAPTER_TITLE = "Magnetism"
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

# ─── BUILDERS (same pattern as P5) ────────────────────────────────────────────

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
    t = Table([[P(title,S('sh',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=WHITE))]],
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
                P(_fix(val),S('ov',fontName=FN,fontSize=FS_CELL,leading=14,textColor=SLATE)),
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

def rapid_nums(rows):
    return grid(['Quantity / Concept','Value / Fact','Unit / Note'], rows,
                ws=[64*mm,72*mm,38*mm],hbg=TEAL_D)

def rapid_ppl(rows):
    return grid(['Scientist / Event','Contribution / Fact','Year'], rows,
                ws=[50*mm,90*mm,34*mm],hbg=PURPLE_D)

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
    s += [banner('P6','Magnetism','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  INTRODUCTION & CLASSIFICATION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  MAGNETS — Introduction & Classification'), sp(2)]

    s += [kv_list([
        ('Magnet',        'Object that attracts materials like iron, cobalt and nickel — property called MAGNETISM'),
        ('Magnetism',     'Branch of physics that deals with the properties of magnets — can be natural or induced'),
        ('Magnetite',     'Strongest natural magnet — iron oxide ore (Fe₃O₄) — also called Lodestone — found in sandy deposits'),
        ('Origin of name','Magnets discovered in Magnesia (region of Asia Minor) — named after the place; also named after shepherd Magnus whose iron-tipped staff stuck to rocks'),
        ('History',       'Chinese knew magnets before 200 BC — used magnetic compass for navigation from 1200 AD onward'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=44*mm), sp(2)]

    s += [sub_h('Natural vs Artificial Magnets — Comparison'), sp(1)]
    s += [grid(
        ['Feature','Natural Magnets','Artificial Magnets'],
        [
            ['Source',        'Found in nature (sandy deposits of earth)',   'Made in laboratory or factory by humans — also called man-made magnets'],
            ['Shape',         'Irregular shapes and dimensions',              'Made in various specific shapes and dimensions'],
            ['Strength',      'Well determined; difficult to change',         'Can be made with required and specific strength; usually STRONGER than natural'],
            ['Durability',    'Long lasting — permanent',                     'Time bound — may lose properties over time'],
            ['Usage',         'Limited practical use',                        'Vast usage in daily life'],
            ['Examples',      'Magnetite (Fe₃O₄), Pyrrhotite (FeS), Ferrite, Coulumbite', 'Bar magnet, Horseshoe, U-shaped, Ring, Disc, Cylindrical, Electromagnets'],
        ],
        ws=[32*mm,58*mm,84*mm]
    ), sp(2)]

    s += [sub_h('Natural Magnetic Ores (Iron Ores)'), sp(1)]
    s += [one_liners([
        ('Magnetite (Fe₃O₄)',    '72.4% iron — highest iron content — strongest magnetic property — used as natural magnet'),
        ('Hematite (Fe₂O₃)',     '69% iron — common iron ore — less magnetic than magnetite'),
        ('Siderite (FeCO₃)',     '48.2% iron — weakest of the three — least magnetic'),
    ]), sp(2)]

    s += [sub_h('Artificial Magnet Types — Shapes'), sp(1)]
    s += [one_liners([
        'Bar magnet — rectangular bar shape; most common type used in labs',
        'U-shaped / Horseshoe magnet — U-shaped; both poles face same direction; strong pull',
        'Ring magnet — circular ring; poles on flat faces; used in speakers',
        'Cylindrical / Disc magnets — used in electronic devices',
        'Needle magnet — thin, pointed; used in compass',
        'Electromagnet — coil of wire wound around iron core; magnetic only when current flows',
        'Made from: Iron, Nickel, Cobalt, Steel alloys; Neodymium alloy (strongest); Samarium alloy; ALNICO (Al+Ni+Co)',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  PROPERTIES OF MAGNETS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  PROPERTIES OF MAGNETS — Three Key Properties'), sp(2)]

    s += [pill('🔑', 'Three properties of magnets: (1) Attractive Property  (2) Repulsive Property  (3) Directive Property', TEAL_L, TEAL_D)]
    s += [sp(2)]

    s += [sub_h('1. Attractive Property'), sp(1)]
    s += [one_liners([
        'Magnets attract MAGNETIC MATERIALS — substances containing iron, cobalt, nickel',
        'Attractive force is MAXIMUM at the POLES (ends of magnet) — minimum at the centre',
        'Iron filings experiment: filings concentrate at poles, sparse in middle — proves poles have maximum attraction',
        'Magnetic substances (attracted): Iron, Cobalt, Nickel, Steel and their alloys',
        'Non-magnetic substances (not attracted): Paper, Plastic, Wood, Aluminium, Copper, Glass, Rubber',
        'Magnetic force acts through non-magnetic materials (paper, glass, wood) without them being affected',
    ]), sp(2)]

    s += [sub_h('2. Repulsive Property'), sp(1)]
    s += [one_liners([
        '<b>Like poles REPEL</b> — N-N repel; S-S repel',
        '<b>Unlike poles ATTRACT</b> — N-S attract; S-N attract',
        'Repulsion is the SUREST test to identify a magnet (attraction alone can be due to induction)',
        'Force of attraction/repulsion is GREATER when charged objects are CLOSER to each other',
        'Breaking a bar magnet into pieces: EACH piece becomes a complete magnet with its own N and S pole — magnetic poles ALWAYS exist in pairs',
        'Bar magnet broken into 2 pieces → 2 magnets | into 4 pieces → 4 magnets — each always has both poles',
        'Splitting magnet vertically → length changes | splitting horizontally → length unchanged — both reduce strength',
    ]), sp(2)]

    s += [sub_h('3. Directive Property'), sp(1)]
    s += [one_liners([
        'A freely suspended bar magnet ALWAYS aligns itself in geographic NORTH-SOUTH direction',
        'North pole of magnet points toward geographic NORTH; South pole toward geographic SOUTH',
        'Used in making magnetic compass — needle is a tiny pivoted magnet that rotates in horizontal plane',
        'This directive property is the basis of navigation using compass',
        'Magnetic Meridian: line passing through north and south magnetic poles at a given location',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  MAGNETIC FIELD & FIELD LINES
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  MAGNETIC FIELD & MAGNETIC FIELD LINES'), sp(2)]

    s += [kv_list([
        ('Magnetic Field',      'Space around a magnet where its magnetic effect or influence is observed — measured in tesla or gauss'),
        ('Unit',                '1 tesla (T) = 10,000 gauss — SI unit is tesla; gauss is CGS unit'),
        ('Magnetic Field Lines','Curved lines drawn around a magnet showing direction of magnetic force — traced using compass needle'),
        ('Plotting Compass',    'Tiny pivoted magnet in a case — also called compass needle — can rotate freely in horizontal plane'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=48*mm), sp(2)]

    s += [sub_h('Properties of Magnetic Field Lines'), sp(1)]
    s += [one_liners([
        'Field lines emerge from NORTH pole and enter SOUTH pole OUTSIDE the magnet',
        'Field lines travel from SOUTH pole to NORTH pole INSIDE the magnet',
        'Field lines are CLOSED CURVES — they form complete loops',
        'Field lines NEVER cross or intersect each other',
        'Field lines are CLOSER together where field is STRONGER (near poles)',
        'Field lines are FARTHER apart where field is WEAKER (away from poles, middle)',
        'Direction of field line at any point = direction a free North pole would move at that point',
        'At one point between two like poles facing each other, field lines cancel → NEUTRAL POINT (no magnetic force)',
    ]), sp(2)]

    s += [sub_h('Uniform vs Non-Uniform Magnetic Field'), sp(1)]
    s += [grid(
        ['','Uniform Magnetic Field','Non-Uniform Magnetic Field'],
        [
            ['Field lines',  'Parallel, equally spaced, same direction',    'Not parallel; varying distance between lines'],
            ['Strength',     'Same magnitude at all points in the region',   'Different magnitude at different points'],
            ['Example',      'Between poles of a very large horseshoe magnet at centre', 'Near the poles of a bar magnet'],
        ],
        ws=[30*mm,72*mm,72*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  MAGNETIC MATERIALS — Classification
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  MAGNETIC MATERIALS — Diamagnetic, Paramagnetic & Ferromagnetic'), sp(2)]

    s += [grid(
        ['Type','Alignment in Uniform Field','Movement in Non-Uniform Field','Magnetisation','Effect of Temperature','Examples'],
        [
            ['Diamagnetic',
             'PERPENDICULAR to field direction',
             'Moves from STRONGER to WEAKER region',
             'Opposite to the applied field',
             'NOT affected by temperature',
             'Bismuth, Copper, Mercury, Gold, Water, Alcohol, Air, Hydrogen'],
            ['Paramagnetic',
             'PARALLEL to field direction',
             'Moves from WEAKER to STRONGER region',
             'In the SAME direction as field',
             'Affected by temperature',
             'Aluminium, Platinum, Chromium, Oxygen, Manganese, Nickel/Iron salt solutions'],
            ['Ferromagnetic',
             'STRONGLY PARALLEL to field direction',
             'Moves QUICKLY from weaker to STRONGER region',
             'STRONGLY in the direction of field',
             'Affected by temperature — become paramagnetic on heating (Curie temperature)',
             'Iron, Cobalt, Nickel, Steel and their alloys'],
        ],
        ws=[28*mm,30*mm,30*mm,26*mm,28*mm,32*mm]
    ), sp(2)]

    s += [pill('📌', 'Curie Temperature: The temperature at which a ferromagnetic material becomes paramagnetic. Named after Pierre Curie.', AMBER_L, AMBER)]
    s += [sp(2)]

    s += [sub_h('Magnetically Hard vs Soft Materials'), sp(1)]
    s += [grid(
        ['Type','Magnetisation','Retains Magnetism?','Used For','Examples'],
        [
            ['Magnetically Hard',
             'Requires STRONG magnetic field to magnetise — difficult',
             'YES — retains magnetism (permanent magnets)',
             'Making permanent magnets',
             'Hardened steel, ALNICO alloy, Neodymium alloy'],
            ['Magnetically Soft',
             'Easily magnetised — requires weak field',
             'NO — loses magnetism when field removed (temporary magnets)',
             'Making electromagnets, transformer cores',
             'Soft iron, Mumetal'],
        ],
        ws=[28*mm,46*mm,28*mm,36*mm,36*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  PERMANENT & TEMPORARY MAGNETS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  PERMANENT & TEMPORARY MAGNETS — Methods & Storage'), sp(2)]

    s += [sub_h('Permanent Magnets'), sp(1)]
    s += [one_liners([
        ('Definition',       'Artificial magnets that RETAIN magnetic property even without external magnetic field'),
        ('Material',         'Made from hardened steel, ALNICO (Al+Ni+Co alloy), Neodymium alloy, Samarium alloy'),
        ('Strongest magnet', 'Neodymium magnets — strongest and most powerful artificial magnets on Earth'),
        ('ALNICO',           'Alloy of Aluminium, Nickel and Cobalt — most commonly used for permanent magnets'),
        ('Examples',         'Refrigerator door seal, speakers, fridge magnets, magnetic compass, credit/debit card strip'),
    ]), sp(2)]

    s += [sub_h('Temporary Magnets (Electromagnets)'), sp(1)]
    s += [one_liners([
        ('Definition',   'Magnets produced with help of EXTERNAL magnetic field — lose property when field removed'),
        ('Material',     'Made from SOFT IRON — easily magnetised and demagnetised'),
        ('How made',     'Coil of insulated wire wound around soft iron core — becomes magnet when current flows; loses magnetism when current stops'),
        ('Examples',     'Magnets in electric bells, cranes, MRI machines, electric motors'),
    ]), sp(2)]

    s += [sub_h('Methods of Magnetisation'), sp(1)]
    s += [one_liners([
        ('Single touch method',   'Stroke the magnetic material with ONE pole of a magnet in ONE direction only — repeat 20-30 times'),
        ('Double touch method',   'Stroke with both poles simultaneously from centre to ends'),
        ('Electrical method',     'Pass electric current through a coil wound around the material — most common industrial method'),
        ('Hammering method',      'Strike unmagnetised iron in N-S direction — weak magnetisation'),
    ]), sp(2)]

    s += [sub_h('Ways Magnets LOSE their Properties'), sp(1)]
    s += [one_liners([
        'HEATING a magnet to high temperature — thermal energy disrupts magnetic alignment',
        'Continuous HAMMERING of the magnetic substance',
        'DROPPING the magnet from a height — mechanical shock',
        'Placing magnet IDLE for a very long time',
        'Passing VARIABLE CURRENT in a coil that encloses the magnet (AC demagnetisation)',
        'IMPROPER STORAGE of the magnet',
        'Placing magnet near CELLPHONE, COMPUTER, DVDs — their magnetic/electric fields demagnetise',
    ]), sp(2)]

    s += [sub_h('Storage of Magnets'), sp(1)]
    s += [one_liners([
        'Bar magnets: stored in PAIRS with unlike poles on same side; separated by a piece of wood; soft iron pieces placed across ends as keepers',
        'Horseshoe magnets: single piece of soft iron (keeper) placed across the poles',
        'Keep away from electronic devices, cellphones, computers, DVDs',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  COMPASS — TYPES & WORKING
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  MAGNETIC COMPASS — Discovery, Types & Working'), sp(2)]

    s += [kv_list([
        ('Compass',          'Instrument to find directions — uses directive property of magnets — contains a magnetic needle'),
        ('Magnetic Needle',  'Tiny pivoted magnet (pointer) that can rotate freely in horizontal plane — points N-S'),
        ('Mariner\'s Compass','Compass used by sailors/seamen to find directions during sea voyages — oldest navigation tool'),
        ('Chinese discovery','Chinese discovered that suspended lode stone (magnetite) stops in N-S direction — ~800 years ago used in boats during storms'),
        ('Compass use',      'Used in ships, airplanes, military, mountaineers to find directions in unknown places'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=46*mm), sp(2)]

    s += [sub_h('Making a Homemade Compass'), sp(1)]
    s += [one_liners([
        'Magnetise a steel needle by stroking with a magnet (single touch method) 20-30 times',
        'Insert the magnetised needle into two styrofoam (thermocol) balls or a dry leaf/cork',
        'Float in a bowl of water — needle rotates and rests in N-S direction',
        'Marked end of compass needle = North Pole of the magnet inside',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  EARTH'S MAGNETISM
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  EARTH\'S MAGNETISM'), sp(2)]

    s += [kv_list([
        ('Earth as Magnet',        'Earth behaves as a huge magnetic dipole — imagined as a giant bar magnet inside'),
        ('Geographic North Pole',  'Earth\'s SOUTH magnetic pole is located near geographic North Pole (attracts magnet\'s North)'),
        ('Geographic South Pole',  'Earth\'s NORTH magnetic pole is located near geographic South Pole (attracts magnet\'s South)'),
        ('Magnetic Axis',          'Line joining Earth\'s magnetic poles — inclined at 10°–15° to geographical axis (rotation axis)'),
        ('Magnetic Declination',   'Angle between geographic north and magnetic north at any point on Earth\'s surface'),
        ('Earth\'s field strength', 'Ranges from 25 to 65 micro tesla at Earth\'s surface'),
        ('Earth\'s core',           'Liquid outer core (molten metallic fluid, radius ~3500 km) believed to cause Earth\'s magnetism — Earth\'s radius = 6400 km'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=52*mm), sp(2)]

    s += [sub_h('Why Earth Has Magnetic Field — Possible Causes'), sp(1)]
    s += [one_liners([
        'Masses of magnetic substances inside the Earth',
        'Radiation from the Sun',
        'Action of the Moon',
        'Most accepted: molten charged metallic fluid inside Earth\'s liquid outer core (3500 km radius) creates magnetic field',
        'Exact cause NOT yet fully known even today',
    ]), sp(2)]

    s += [note_box('Earth\'s Magnetism — TET Exam Trap', [
        'Geographic North Pole ≠ Magnetic North Pole — they are different points on Earth',
        'Earth\'s geographic NORTH has Earth\'s magnetic SOUTH pole (that\'s why compass North points there)',
        'Magnetic axis is inclined 10°–15° to geographic axis — hence compass does not point to exact geographic North',
        'A freely suspended magnet aligns with Earth\'s magnetic field (N-S direction) — used in navigation',
    ], icon='⚠')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  USES OF MAGNETS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  USES OF MAGNETS — Daily Life & Technology'), sp(2)]

    s += [grid(
        ['Application','How Magnet Is Used'],
        [
            ['Magnetic Compass',          'Directive property — finds geographic direction; used by seamen (as "direction stone"), pilots, mountaineers'],
            ['Dynamo / Generator',        'Moving magnet near coil → generates electricity (electromagnetic induction)'],
            ['Electric Bell',             'Electromagnet attracts hammer → strikes bell → spring pulls back → circuit breaks → cycle repeats'],
            ['Electric Motor',            'Current-carrying coil in magnetic field rotates → converts electrical to mechanical energy'],
            ['Loudspeaker / Microphone',  'Permanent magnet + electromagnet → converts electrical signals to sound / sound to signals'],
            ['Maglev Train',              'Extremely powerful electromagnets — train levitates (floats) above tracks — no friction — speed up to 600 km/h'],
            ['MRI (Magnetic Resonance Imaging)', 'Extremely powerful electromagnet scans internal organs; non-invasive medical imaging'],
            ['Magnetic Crane',            'Powerful electromagnet lifts heavy iron/steel scrap; releases by switching off current'],
            ['Hard Disk / Memory',        'Magnetic material stores data in computers; also used in debit/credit card magnetic strips'],
            ['MICR in Banking',           'Magnetic Ink Character Recognition — magnets in computers read MICR numbers on cheques'],
            ['Magnetic Conveyor Belt',    'Sorts magnetic substances from non-magnetic in industries'],
            ['Screwdrivers',              'Tip slightly magnetised so screws remain attached while working'],
            ['Alnico Cow Magnet',         'Swallowed by cattle — attracts sharp iron wires in digestive tract preventing internal damage'],
            ['Refrigerator / Door seals', 'Permanent magnets in door seal keep fridge door closed tightly'],
            ['Speakers / Earphones',      'Permanent ring magnet + voice coil electromagnet create vibration → sound'],
        ],
        ws=[54*mm,120*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  MAGLEV TRAIN (Class 6 Detailed Section)
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  MAGLEV TRAIN — Magnetic Levitation Technology'), sp(2)]

    s += [kv_list([
        ('Maglev',          'Magnetic Levitation — train floats above track using magnetic repulsion — no contact, no friction'),
        ('Principle',        'Like poles repel → electromagnets at bottom of train + track repel → train lifts ~10 cm above track'),
        ('Propulsion',       'Unlike poles attract → magnets on sides of track and train pull the train forward → directional control by changing current'),
        ('Speed',            'No friction → easily attains 300 km/h; capable of up to 600 km/h'),
        ('Features',         'No moving parts → no friction; no noise; less energy; eco-friendly'),
        ('Countries',        'China (Shanghai Maglev: 501 km/h record), Japan (SCMaglev: 603 km/h record), South Korea (KTX: 421 km/h record)'),
        ('India',            'Mumbai-Delhi, Mumbai-Nagpur, Chennai-Bengaluru-Mysuru routes under consideration/proposal'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=38*mm), sp(2)]

    s += [sub_h('Maglev Speed Records'), sp(1)]
    s += [grid(
        ['Country / Train','Max Operating Speed','Speed Record'],
        [
            ['Japan — SCMaglev',             '500 km/h',  '603 km/h (world record)'],
            ['China — Shanghai Maglev Train', '350 km/h',  '501 km/h'],
            ['South Korea — KTX',             '300 km/h',  '421 km/h'],
        ],
        ws=[60*mm,57*mm,57*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Values, Formulas & Key Numbers</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Magnetic field unit',          'Tesla (T) — SI unit  |  Gauss — CGS unit',            '1 T = 10,000 gauss'],
        ['Earth\'s field strength',      '25 to 65 micro tesla at Earth\'s surface',             'µT'],
        ['Magnetic axis inclination',    'Inclined 10°–15° to geographic (rotation) axis',       'Earth\'s magnet'],
        ['Earth\'s core radius',         '~3500 km (liquid outer core)',                          'Earth radius = 6400 km'],
        ['Magnetite iron content',       '72.4% iron — Fe₃O₄',                                   'Strongest natural magnet'],
        ['Hematite iron content',        '69% iron — Fe₂O₃',                                     'Common iron ore'],
        ['Siderite iron content',        '48.2% iron — FeCO₃',                                   'Weakest iron ore'],
        ['ALNICO composition',           'Aluminium + Nickel + Cobalt alloy',                     'Common permanent magnet'],
        ['Neodymium magnets',            'Strongest artificial magnets on Earth',                  'Nd alloy'],
        ['Maglev levitation height',     '~10 cm above track',                                    'Magnetic repulsion'],
        ['Japan SCMaglev record',        '603 km/h',                                              'Speed record'],
        ['China Shanghai Maglev',        '501 km/h (record) | 350 km/h (operating)',              'Speed'],
        ['Credit card strip',            'Tiny iron-based magnetic particles (20 millionth of an inch long) in thin plastic film', 'Magstripe'],
        ['Curie temperature',            'Temperature at which ferromagnetic → paramagnetic',     'Named after Pierre Curie'],
        ['Magnetar',                     'Most powerful magnet in universe — neutron star, 20 km diameter, 2-3 solar masses', 'Milky Way galaxy'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoveries & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['William Gilbert',      'Laid foundation of magnetism; suggested Earth has giant bar magnet; first systematic research on lodestone; published "De Magnete"', '1544–1603'],
        ['Chinese navigators',   'Used magnetite (lodestone) as compass for navigation in boats during storms',                     '~800 years ago | 1200 AD'],
        ['Pierre Curie',         'Curie temperature — ferromagnetic becomes paramagnetic on heating; named Curie temperature after him', '19th century'],
        ['Hans C. Oersted',      'Discovered magnetic effect of electric current — current produces magnetic field',                  '1819'],
        ['China (Maglev)',        'Shanghai Maglev operating — 350 km/h operating, 501 km/h record',                                '2003 onward'],
        ['Japan (Maglev)',        'SCMaglev — world speed record 603 km/h',                                                         '2015'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Magnet',                'Object that attracts iron, cobalt and nickel due to property called magnetism'),
        ('Magnetism',             'Branch of physics dealing with properties of magnets; also the attracting property itself'),
        ('Natural Magnet',        'Magnet found in nature — e.g., Lodestone/Magnetite (Fe₃O₄)'),
        ('Artificial Magnet',     'Man-made magnet — stronger than natural; made in specific shapes and sizes'),
        ('Lodestone / Magnetite', 'Strongest natural magnet — iron oxide ore Fe₃O₄; used historically as compass'),
        ('Pole',                  'Region near end of magnet where attractive force is maximum; always exist in pairs (N and S)'),
        ('Magnetic Meridian',     'Vertical plane passing through magnetic axis of Earth at a given location'),
        ('Attractive Property',   'Magnets attract magnetic materials (Fe, Co, Ni); strongest at poles'),
        ('Repulsive Property',    'Like poles repel each other; unlike poles attract'),
        ('Directive Property',    'Freely suspended magnet aligns along geographic N-S direction'),
        ('Magnetic Field',        'Space around magnet where magnetic effect is observed; unit: tesla or gauss'),
        ('Tesla (T)',             'SI unit of magnetic field; 1 T = 10,000 gauss'),
        ('Gauss',                 'CGS unit of magnetic field; 1 gauss = 10<super>-4</super> tesla'),
        ('Field Lines',           'Curved lines showing direction and pattern of magnetic field around a magnet'),
        ('Neutral Point',         'Point where magnetic fields of two magnets cancel; no net magnetic force'),
        ('Diamagnetic Material',  'Aligns perpendicular to field; moves to weaker region; magnetised opposite to field; not affected by temperature'),
        ('Paramagnetic Material', 'Aligns parallel to field; moves to stronger region; magnetised in field direction; affected by temperature'),
        ('Ferromagnetic Material','Strongly aligns parallel to field; quickly moves to stronger region; strongly magnetised; becomes paramagnetic at Curie temperature'),
        ('Curie Temperature',     'Temperature at which ferromagnetic material becomes paramagnetic'),
        ('Permanent Magnet',      'Retains magnetism even without external field; made from ALNICO, Neodymium alloy, hardened steel'),
        ('Temporary Magnet',      'Loses magnetism when external field removed; made from soft iron; used in electromagnets'),
        ('Magnetisation',         'Process of making a substance a permanent or temporary magnet using external magnetic field'),
        ('ALNICO',                'Alloy of Aluminium, Nickel and Cobalt — used for permanent magnets'),
        ('Neodymium Magnet',      'Strongest artificial magnet on Earth — made from neodymium alloy'),
        ('Compass',               'Instrument with magnetic needle to find geographic directions; uses directive property'),
        ('Plotting Compass',      'Small compass with freely rotating magnetic needle; used to trace magnetic field lines'),
        ('Earth\'s Magnetism',    'Earth behaves as giant magnetic dipole; magnetic axis inclined 10–15° to geographic axis'),
        ('Magnetic Declination',  'Angle between geographic north and magnetic north at a location'),
        ('Maglev Train',          'Magnetic levitation train — floats above track using like-pole repulsion — no friction'),
        ('Electromagnet',         'Magnet created by electric current through coil around iron core — temporary magnet'),
        ('MRI',                   'Magnetic Resonance Imaging — medical imaging using powerful electromagnets'),
        ('Magnetar',              'Most powerful magnet in universe — a type of neutron star; mass 2-3 times Sun'),
        ('Magneto-reception',     'Ability to sense Earth\'s magnetic field — seen in pigeons (magnetite in beaks)'),
        ('Magnetic Hard material','Material requiring strong field to magnetise; retains magnetism — used for permanent magnets'),
        ('Magnetic Soft material','Material easily magnetised but loses magnetism quickly — used for electromagnets'),
    ]

    s += [gloss_2col(g), sp(3)]

    s += [dyk([
        'A magnetar (magnetic neutron star) in the Milky Way has a field so powerful it could absorb iron atoms from blood even 1000 km away.',
        'Pigeons have magnetite crystals in their beaks — they can sense Earth\'s magnetic field for navigation (magnetoreception).',
        'Credit/debit card magnetic strip contains tiny iron-based magnetic particles just 20 millionths of an inch long.',
        'Earth\'s magnet is 20 times more powerful than a fridge magnet.',
        'Maglev trains have no wheels, no engine, no friction — they achieve 600+ km/h floating silently above tracks.',
    ])]
    s += [sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P6: Magnetism  |  Classes 6 • 7 • 8',
          S('ft',fontName=FNI,fontSize=8.5,textColor=TEAL,alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P6  |  Magnetism  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P6 Magnetism',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P6_magnetism.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
