"""
TET Paper II Science Handbook — P5: Electricity
Style: P3 one-liner cheat-sheet | Font: 10.5pt body, 10pt cells
All sub-topics: Class 7 (Term II, Unit 2) & Class 8 (Unit 5)
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

CHAPTER_ID = "P5"
CHAPTER_TITLE = "Electricity"
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
    s += [banner('P5','Electricity','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  ELECTRIC CHARGE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  ELECTRIC CHARGE — Basics & Transfer'), sp(2)]

    s += [kv_list([
        ('Electric Charge',      'Basic property of matter that causes objects to attract or repel — carried by protons and electrons'),
        ('SI Unit of Charge',    'Coulomb (C) — denoted by letter q'),
        ('Elementary Charge (e)','Smallest charge that can exist freely = 1.602 × 10<super>-19</super> C — charge on one proton or one electron'),
        ('Positive Charge',      'Carried by PROTONS — less electrons than protons'),
        ('Negative Charge',      'Carried by ELECTRONS — more electrons than protons'),
        ('Neutral Atom',         'Equal number of protons and electrons — net charge = ZERO'),
        ('Like charges',         'REPEL each other (+ and + repel | − and − repel)'),
        ('Unlike charges',       'ATTRACT each other (+ and − attract)'),
        ('Law of Conservation',  'Charges can NEITHER be created NOR destroyed — total charge remains constant'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=50*mm), sp(2)]

    s += [sub_h('Transfer of Charges — Three Methods'), sp(1)]
    s += [grid(
        ['Method','How It Works','Example'],
        [
            ['Transfer by Friction',
             'When two materials are rubbed together, electrons transfer from one to other — both get charged',
             'Comb rubbed on dry hair → gains electrons → attracts paper bits; Glass rod + silk cloth; Ebonite rod + fur'],
            ['Transfer by Conduction',
             'Direct contact of charged body with uncharged body → charges flow from charged to uncharged',
             'Charged ebonite rod touches paper cylinder → cylinder gets charged and repels rod'],
            ['Transfer by Induction',
             'Charged body brought NEAR (NOT touching) uncharged body → opposite charge appears at near end',
             'Negatively charged rod near neutral rod → near end becomes positive, far end negative — no contact needed'],
        ],
        ws=[34*mm,72*mm,68*mm]
    ), sp(2)]

    s += [note_box('Critical Distinction — Friction Charging', [
        'A neutral object becomes positively charged by LOSING electrons — NOT by gaining positive charges',
        'Glass rod rubbed with silk: glass LOSES electrons → glass becomes +ve; silk GAINS electrons → silk becomes −ve',
        'Ebonite rod rubbed with fur: fur LOSES electrons → fur becomes +ve; ebonite GAINS electrons → ebonite becomes −ve',
        'Wet hair reduces friction → fewer electrons transfer → comb attracts less paper',
    ], icon='⚠')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  ELECTROSCOPE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  ELECTROSCOPE — Detection of Charge'), sp(2)]

    s += [kv_list([
        ('Electroscope',         'Scientific instrument to DETECT the presence and type of electric charge on a body'),
        ('Working Principle',    'Like charges repel — when charge is given, gold leaves move apart'),
        ('Inventor',             'William Gilbert (British physician) — invented first electroscope in 1600'),
        ('Gold-leaf type',       'Developed by Abraham Bennet (British scientist) in 1787 — gold/silver used (best conductors)'),
    ], bg_L=BLUE_D, bg_R=BLUE_L), sp(2)]

    s += [sub_h('Gold-Leaf Electroscope — Structure & Working'), sp(1)]
    s += [one_liners([
        'Structure: Glass jar + vertical brass rod through cork + brass disc at top + two gold leaves hanging from rod inside jar',
        'When charged body touches brass disc → charge transfers to gold leaves → leaves have same charge → REPEL → leaves DIVERGE (spread apart)',
        'More charge → greater divergence of gold leaves',
        'When charged body brought NEAR (not touching) → opposite charge appears at leaves → leaves still diverge',
        'Gold and silver used because they are the BEST conductors of electricity',
        'Pith-ball electroscope: simpler type — small light pith ball hung by silk thread; attracted/repelled by charges',
        'Electroscope detects PRESENCE of charge; cannot always determine the TYPE (positive or negative)',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  ELECTRIC CURRENT, POTENTIAL DIFFERENCE & RESISTANCE
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  CURRENT, POTENTIAL DIFFERENCE & RESISTANCE'), sp(2)]

    s += [kv_list([
        ('Electric Current (I)',  'Flow of electric charges through a conductor — measured in Ampere (A) — symbol: I'),
        ('Conventional Current',  'Flow of POSITIVE charges from + to − terminal (positive to negative) — direction: high to low potential'),
        ('Electron Flow',         'Flow of ELECTRONS from − to + terminal (negative to positive) — opposite to conventional current'),
        ('Potential Difference (V)','Energy needed to move 1 unit of charge between two points — SI unit: Volt (V)'),
        ('Resistance (R)',         'Opposition to flow of electric charges — SI unit: Ohm (Ω) — R = V/I'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=52*mm), sp(2)]

    s += [
        fstrip('Electric Current', 'I = q / t', 'q = charge (coulombs), t = time (seconds)', BLUE_D),
        sp(1),
        fstrip('Resistance', 'R = V / I', 'V = voltage (volts), I = current (amperes)', TEAL_D),
        sp(2),
    ]

    s += [sub_h('Units of Electric Current — Conversions'), sp(1)]
    s += [one_liners([
        ('1 Ampere (A)',      '= flow of 1 coulomb per second through a cross-section — 1 A = 1 C/s'),
        ('1 milliampere (mA)', '= 10<super>-3</super> A = 1/1000 A (for small currents)'),
        ('1 microampere (µA)','= 10<super>-6</super> A = 1/10,00,000 A (for very small currents)'),
        ('1 coulomb (C)',     '≈ charge of 6.242 × 10<super>18</super> protons or electrons — 1 C = 1 A × 1 s'),
    ]), sp(2)]

    s += [sub_h('Conventional Current vs Electron Flow'), sp(1)]
    s += [grid(
        ['','Conventional Current','Electron Flow'],
        [
            ['Direction',       'Positive terminal (+) to Negative terminal (−) of battery',
             'Negative terminal (−) to Positive terminal (+) of battery'],
            ['Charge carrier',  'Imaginary positive charges (historical assumption)',
             'Actual electrons (negatively charged particles)'],
            ['When established?','Before discovery of electrons (historical)',
             'After discovery of electrons by J.J. Thomson (1897)'],
            ['Usage today',     'Still used in circuit diagrams and calculations',
             'Actual physical reality of current in conductors'],
        ],
        ws=[32*mm,71*mm,71*mm]
    ), sp(2)]

    s += [sub_h('Electrical Conductivity & Resistivity'), sp(1)]
    s += [one_liners([
        ('Conductivity (σ)',    'Measure of material\'s ability to conduct electricity — SI unit: Siemens/metre (S/m) — symbol: σ (sigma)'),
        ('Resistivity (ρ)',     'Fundamental property opposing current flow — SI unit: ohm-metre (Ω·m) — symbol: ρ (rho)'),
        'Higher conductivity = lower resistivity → better conductor (metals have low resistivity)',
        'Silver has highest conductivity of all metals → best conductor',
        'Copper: resistivity 1.68 × 10<super>-8</super> Ω·m | Silver: 1.59 × 10<super>-8</super> Ω·m | Aluminium: 2.82 × 10<super>-8</super> Ω·m',
    ]), sp(2)]

    s += [sub_h('Measuring Instruments'), sp(1)]
    s += [grid(
        ['Quantity','Instrument','How Connected','Unit'],
        [
            ['Current (I)',            'Ammeter',  'IN SERIES with circuit component', 'Ampere (A)'],
            ['Potential Difference (V)','Voltmeter','IN PARALLEL across the component', 'Volt (V)'],
            ['Resistance (R)',          'Ohmmeter', 'When circuit is OFF (no current flowing)', 'Ohm (Ω)'],
        ],
        ws=[40*mm,34*mm,64*mm,36*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  ELECTRIC CIRCUITS — SERIES & PARALLEL
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  ELECTRIC CIRCUITS — Series & Parallel'), sp(2)]

    s += [kv_list([
        ('Electric Circuit',   'Complete closed path through which electric current flows — electrons travel from − to + terminal'),
        ('Open Circuit',        'Circuit with a gap/break — current DOES NOT flow'),
        ('Closed Circuit',      'Complete path with no breaks — current flows freely'),
        ('Short Circuit',       'Low-resistance connection between two conductors — causes excessive current, heat, sparks'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Circuit Components & Symbols'), sp(1)]
    s += [one_liners([
        ('Cell',         'Single unit of electrical energy — longer line = positive (+) terminal, shorter line = negative (−) terminal in symbol'),
        ('Battery',      'Two or more cells connected together — provides potential difference to drive current'),
        ('Switch',       'Device to open or close a circuit — controls current flow (ON = closed circuit; OFF = open circuit)'),
        ('Bulb (Lamp)',  'Electrical resistor that converts electrical energy to light and heat'),
        ('Fuse',         'Safety device — thin wire that MELTS when current exceeds safe limit → breaks circuit'),
        ('Ammeter',      'Measures current — connected in series (low resistance)'),
        ('Voltmeter',    'Measures voltage — connected in parallel (high resistance)'),
    ]), sp(2)]

    s += [sub_h('Series vs Parallel Circuits — Complete Comparison'), sp(1)]
    s += [grid(
        ['Feature','Series Circuit','Parallel Circuit'],
        [
            ['Connection',        'Components connected END to END in a single loop',
             'Components connected between SAME two points — multiple paths (branches)'],
            ['Current (I)',        'SAME current flows through ALL components\nI = I₁ = I₂ = I₃',
             'Current DIVIDES across components\nI = I₁ + I₂ + I₃'],
            ['Voltage (V)',        'Voltage DIVIDES across components\nV = V₁ + V₂ + V₃',
             'SAME voltage across all components\nV = V₁ = V₂ = V₃'],
            ['Total Resistance',  'Total R = R₁ + R₂ + R₃ (increases)',
             '1/R = 1/R₁ + 1/R₂ + 1/R₃ (decreases — less than smallest resistor)'],
            ['Brightness of bulbs','Dimmer — each bulb shares power from battery',
             'Brighter — each bulb gets full voltage'],
            ['If one bulb fails',  'ALL bulbs go OFF — circuit breaks',
             'OTHER bulbs stay ON — other paths still complete'],
            ['Everyday use',      'Rarely — series lights in older decoration strings',
             'HOME WIRING — all appliances/rooms; if one fails, others still work'],
        ],
        ws=[36*mm,69*mm,69*mm]
    ), sp(2)]

    s += [pill('📌', 'Homes use PARALLEL circuits — independent switches for each room, each appliance works independently at full voltage.', CYAN_L, CYAN)]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  CONDUCTORS & INSULATORS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  CONDUCTORS & INSULATORS'), sp(2)]

    s += [grid(
        ['Type','Definition','Why?','Examples'],
        [
            ['Conductor',
             'Material that ALLOWS electric current to pass easily — low resistance',
             'Has many FREE ELECTRONS in outermost orbit — loosely bound and can move freely through material',
             'Metals: Silver (best), Copper, Aluminium, Iron, Gold; also Salt water, human body'],
            ['Insulator\n(Bad Conductor)',
             'Material that DOES NOT allow current to pass easily — very high resistance',
             'Electrons in outermost orbit are tightly bound — cannot move freely — very few free electrons',
             'Rubber, Plastic, Wood, Glass, Ceramic, Dry air, Pure water, Silk, Cotton, Paper'],
            ['Semiconductor',
             'Partially conducts — between conductor and insulator in properties',
             'Moderate number of free electrons — conductivity changes with temperature and impurities',
             'Silicon (Si), Germanium (Ge) — used in transistors, diodes, solar cells, computer chips'],
        ],
        ws=[26*mm,42*mm,58*mm,48*mm]
    ), sp(2)]

    s += [one_liners([
        'Rubber gloves used by electricians — rubber is an insulator → protects against electric shock',
        'Electric wires coated with plastic/rubber insulation — prevents accidental shock',
        'Human body conducts electricity — touching live wire is dangerous (body acts as conductor to earth)',
        'Dry air = insulator; Moist/humid air = partial conductor (lightning possible)',
        'Distilled/pure water = insulator; Salt water (with dissolved ions) = conductor',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  LIGHTNING, EARTHING & LIGHTNING ARRESTER
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  LIGHTNING, EARTHING & LIGHTNING ARRESTER'), sp(2)]

    s += [kv_list([
        ('Lightning',             'Massive discharge of static electricity between charged clouds or between cloud and Earth — enormous heat and light'),
        ('Earthing (Grounding)',  'Safety measure connecting exposed metal parts of electrical devices to Earth via low-resistance wire — prevents shock'),
        ('Lightning Arrester',   'Device protecting buildings from lightning — metallic rod (spikes) at top of building connected to ground by copper cable'),
    ], bg_L=TEAL_D, bg_R=TEAL_L), sp(2)]

    s += [sub_h('Three-Wire System in Domestic Supply'), sp(1)]
    s += [one_liners([
        ('Live wire (L)',    'Carries current AT HIGH VOLTAGE from power station to appliance — colour: RED (old) or BROWN (new)'),
        ('Neutral wire (N)', 'Returns current back to power station — stays near zero voltage — colour: BLACK (old) or BLUE (new)'),
        ('Earth wire (E)',   'Connected to metallic body of appliance and to earth — safety wire — colour: GREEN or YELLOW-GREEN'),
        'Earth wire function: if live wire touches metal body (insulation failure) → current flows to earth safely → prevents shock',
        'Car during lightning storm: SAFE — car body acts as Faraday cage, protects occupants from electric field',
        'During lightning: DO NOT stand in open ground — squat down (make yourself small); avoid tall trees',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  EFFECTS OF ELECTRIC CURRENT
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  EFFECTS OF ELECTRIC CURRENT — Three Main Effects'), sp(2)]

    s += [pill('🔑', 'Three effects of electric current: (1) Heating Effect  (2) Magnetic Effect  (3) Chemical Effect', TEAL_L, TEAL_D)]
    s += [sp(2)]

    # G1 - Heating Effect
    s += [sub_h('1. Heating Effect of Electric Current'), sp(1)]
    s += [kv_list([
        ('Definition',          'When current passes through a conductor, electrical energy converts to HEAT energy — due to friction between electrons and conductor molecules'),
        ('Factors',             'Heat produced depends on: (1) Amount of current (2) Resistance of wire (3) Time for which current flows'),
        ('Nichrome',            'Alloy of Nickel + Iron + Chromium — used as heating element — HIGH melting point + HIGH resistance'),
        ('Tungsten',            'Used in bulb filament — HIGH melting point (3,422°C) + HIGH resistance → glows bright white when heated'),
        ('Fuse wire',           'Made of Lead + Tin alloy — LOW melting point → melts quickly when excess current flows → breaks circuit → protects appliances'),
        ('MCB',                 'Miniature Circuit Breaker — replaces fuse — breaks circuit automatically when excess current; can be switched back ON without replacing wire'),
    ], bg_L=ORANGE, bg_R=ORANGE_L, w_L=40*mm), sp(2)]

    s += [sub_h('Applications of Heating Effect'), sp(1)]
    s += [grid(
        ['Appliance','How Heating Effect Is Used'],
        [
            ['Electric Bulb',         'Tungsten filament heated to ~2500°C → emits visible white light'],
            ['Electric Iron',         'Nichrome heating element heats metal plate → heat conducted to clothes'],
            ['Geyser / Water Heater', 'Immersion heater coil heats water — convection distributes heat throughout water'],
            ['Electric Kettle',       'Heating element at bottom heats water — convection carries heat upward'],
            ['Electric Cooker',       'Coils turn red hot → heat conducted to cooking pot'],
            ['Arc Welding',           'Practical application of short circuit — enormous heat generated at arc point melts and fuses metals'],
        ],
        ws=[42*mm,132*mm]
    ), sp(3)]

    # G2 - Magnetic Effect
    s += [sub_h('2. Magnetic Effect of Electric Current'), sp(1)]
    s += [kv_list([
        ('Discovery',         'Hans Christian Oersted (Danish physicist) discovered in 1819 that electric current creates magnetic field around conductor'),
        ('Electromagnet',     'Coil of insulated wire wound around iron nail/core — becomes magnet ONLY when current flows — loses magnetism when current off'),
        ('Making electromagnet','Wind insulated wire tightly around iron nail in form of coil; connect to battery — nail becomes magnet'),
        ('Key property',      'Polarity of electromagnet CHANGES when direction of current changes'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=40*mm), sp(2)]

    s += [sub_h('Applications of Magnetic Effect'), sp(1)]
    s += [grid(
        ['Application','How Magnetic Effect Is Used'],
        [
            ['Electric Bell',         'Current through electromagnet → attracts hammer → hammer strikes bell → spring pulls hammer back → circuit breaks → repeats'],
            ['Electric Crane',        'Powerful electromagnet lifts heavy iron/steel loads; current switched off to drop the load'],
            ['Telephone',             'Changing magnetic field causes diaphragm (thin metal sheet) to vibrate → produces sound'],
            ['Electric Motor',        'Current-carrying coil in magnetic field → rotates → converts electrical to mechanical energy'],
            ['Hospital (eye surgery)', 'Electromagnets remove iron/steel splinters from eye without surgery'],
        ],
        ws=[42*mm,132*mm]
    ), sp(3)]

    # G3 - Chemical Effect
    s += [sub_h('3. Chemical Effect of Electric Current'), sp(1)]
    s += [kv_list([
        ('Definition',     'When current passes through a conducting liquid (electrolyte), chemical reactions occur — compounds decompose into ions'),
        ('Electrolysis',   'Decomposition of molecules of a solution into positive and negative ions by passing electric current through it'),
        ('Electrolyte',    'Conducting liquid/solution that allows current to pass and undergoes chemical change — e.g., copper sulphate solution, salt water, acids'),
        ('Anode (+)',      'Positive electrode — metal plate connected to positive terminal of battery'),
        ('Cathode (−)',    'Negative electrode — object to be plated — connected to negative terminal of battery'),
    ], bg_L=GREEN_D, bg_R=GREEN_L, w_L=40*mm), sp(2)]

    s += [sub_h('Electroplating — Most Common Application'), sp(1)]
    s += [kv_list([
        ('Electroplating',  'Depositing a thin layer of one metal over the surface of another metal by passing electric current'),
        ('Why?',            'Protect cheaper metals from corrosion, rust; give attractive appearance; reduce cost vs solid precious metal objects'),
        ('Anode',           'Pure metal plate (metal to be deposited) — e.g., copper plate; gradually dissolves'),
        ('Cathode',         'Object to be plated — e.g., iron spoon; metal deposits here'),
        ('Electrolyte',     'Salt solution of metal to be deposited — e.g., copper sulphate for copper plating'),
    ], bg_L=GREEN_D, bg_R=GREEN_L, w_L=42*mm), sp(2)]

    s += [sub_h('Electroplating Applications'), sp(1)]
    s += [grid(
        ['Object / Purpose','Metal Deposited','Why That Metal?'],
        [
            ['Iron bridges, automobiles (anti-rust)', 'Zinc (galvanisation)',
             'Zinc does not corrode; cheap; protects iron from rusting'],
            ['Car parts, bath taps, bicycle handles, kitchen gas burners',
             'Chromium', 'Shiny appearance; does not corrode; resists scratches; hard'],
            ['Jewellery (artificial gold/silver)',
             'Gold or Silver', 'Attractive appearance; tarnish-resistant; cheaper than solid gold/silver'],
            ['Food cans (tin cans)',
             'Tin', 'Non-toxic; does not corrode; safe for food contact'],
            ['Circuit boards (electronics)',
             'Copper or Gold', 'Excellent conductor; prevents oxidation; reliable contacts'],
        ],
        ws=[56*mm,28*mm,90*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  Solved Numerical Problems'), sp(2)]

    probs = [
        ('1', 'If 30 coulombs of electric charge flows through a wire in 2 minutes, find the current.',
         'q = 30 C; t = 2 min = 2 × 60 = 120 s',
         'I = q/t = 30/120 = 0.25 A',
         'Current = 0.25 A'),
        ('2', '0.002 A current flows through a circuit. Convert this to microamperes (µA).',
         'I = 0.002 A; 1 A = 10<super>6</super> µA',
         '0.002 A = 0.002 × 10<super>6</super> µA = 2 × 10<super>3</super> µA',
         '2000 µA (2 × 10<super>3</super> µA)'),
        ('3', 'The voltage across a resistor is 12 V and the current through it is 4 A. Find resistance.',
         'V = 12 V; I = 4 A',
         'R = V/I = 12/4 = 3 Ω',
         'Resistance = 3 Ω (3 ohms)'),
        ('4', 'Two resistors R₁ = 4 Ω and R₂ = 6 Ω connected in SERIES. Find total resistance.',
         'R₁ = 4 Ω; R₂ = 6 Ω; Series connection',
         'R_total = R₁ + R₂ = 4 + 6 = 10 Ω',
         'Total resistance = 10 Ω'),
        ('5', 'Two resistors R₁ = 4 Ω and R₂ = 6 Ω connected in PARALLEL. Find total resistance.',
         'R₁ = 4 Ω; R₂ = 6 Ω; Parallel connection',
         '1/R = 1/R₁ + 1/R₂ = 1/4 + 1/6 = 3/12 + 2/12 = 5/12 → R = 12/5 = 2.4 Ω',
         'Total resistance = 2.4 Ω (less than smallest resistor = 4 Ω)'),
        ('6', 'A charge of 240 C passes through a conductor in 4 minutes. Find current in mA.',
         'q = 240 C; t = 4 min = 240 s',
         'I = q/t = 240/240 = 1 A = 1 × 10<super>3</super> mA',
         'Current = 1 A = 1000 mA'),
    ]

    for p in probs:
        s += [prob(*p), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Formulas, Values & Units</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Electric Current (I)',       'I = q/t  (charge/time)',                           'Ampere (A)'],
        ['1 Ampere',                   '= 1 coulomb per second  (1 C/s)',                  'Definition'],
        ['1 milliampere',              '= 10<super>-3</super> A  (0.001 A)',               'Conversion'],
        ['1 microampere',              '= 10<super>-6</super> A  (0.000001 A)',            'Conversion'],
        ['Resistance (R)',             'R = V/I  (Voltage/Current)',                        'Ohm (Ω)'],
        ['Resistance — Series',        'R = R₁ + R₂ + R₃  (total increases)',             'Same current'],
        ['Resistance — Parallel',      '1/R = 1/R₁ + 1/R₂ + 1/R₃  (total decreases)',   'Same voltage'],
        ['Voltage — Series',           'V = V₁ + V₂ + V₃  (divides)',                    'Volt (V)'],
        ['Current — Parallel',         'I = I₁ + I₂ + I₃  (divides)',                    'Ampere (A)'],
        ['Elementary charge (e)',       '= 1.602 × 10<super>-19</super> C',               'Proton or electron charge'],
        ['1 coulomb (C)',               '≈ 6.242 × 10<super>18</super> elementary charges','1 A × 1 s'],
        ['Conductivity unit',           'Siemens/metre (S/m)',                              'σ (sigma)'],
        ['Resistivity unit',            'Ohm-metre (Ω·m)',                                 'ρ (rho)'],
        ['Silver resistivity',          '1.59 × 10<super>-8</super> Ω·m (lowest)',        'Best conductor'],
        ['Copper resistivity',          '1.68 × 10<super>-8</super> Ω·m',                'Common conductor'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoveries & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['William Gilbert',         'British physician — invented FIRST electroscope (first electrical instrument)', '1600'],
        ['Hans Christian Oersted',  'Danish physicist — discovered MAGNETIC EFFECT of electric current', '1819'],
        ['Abraham Bennet',          'British scientist — developed gold-leaf electroscope', '1787'],
        ['Thomas Alva Edison',      'American inventor — lit 14,000 bulbs in 9,000 New York houses (first power grid)', '1882'],
        ['Calcutta Electric Supply','First thermal power plant in India — Calcutta (Kolkata)', '1899 (Apr 17)'],
        ['J.J. Thomson',            'Discovered electron — proved electron flow in conductors', '1897'],
        ['Basin Bridge Madras',     'First power station in Madras city — powered government press, hospital, tramways', '~1900'],
        ['Nichrome discovery',      'Alloy of Ni+Fe+Cr — used in heating elements — high melting point', 'Early 1900s'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Electric Charge',       'Basic property of matter that causes attraction or repulsion; carried by protons and electrons; unit: Coulomb'),
        ('Elementary Charge (e)', 'Smallest freely existing charge = 1.602 × 10<super>-19</super> C; charge on one proton or one electron'),
        ('Coulomb (C)',           'SI unit of electric charge; 1 C = charge of ≈ 6.242 × 10<super>18</super> protons/electrons'),
        ('Electric Current (I)',  'Flow of electric charges through a conductor per unit time; I = q/t; SI unit: Ampere (A)'),
        ('Ampere (A)',            'SI unit of electric current; 1 A = 1 coulomb per second'),
        ('Conventional Current',  'Flow of positive charges from + to − terminal; historical concept; opposite to electron flow'),
        ('Electron Flow',         'Actual flow of electrons from − to + terminal; actual physical current'),
        ('Potential Difference (V)','Energy needed to move 1 unit of charge between two points; causes current to flow; SI unit: Volt (V)'),
        ('Resistance (R)',        'Opposition to flow of electric current; R = V/I; SI unit: Ohm (Ω)'),
        ('Conductivity (σ)',      'Measure of material\'s ability to conduct electricity; SI unit: Siemens per metre (S/m)'),
        ('Resistivity (ρ)',       'Property of material opposing current flow; SI unit: Ohm-metre (Ω·m)'),
        ('Conductor',             'Material with many free electrons that allows current to pass easily — metals, salt water'),
        ('Insulator',             'Material with tightly bound electrons that resists current flow — rubber, plastic, wood, glass'),
        ('Semiconductor',         'Material between conductor and insulator; conductivity changes with conditions — Silicon, Germanium'),
        ('Ammeter',               'Instrument to measure electric current; connected in SERIES; unit: Ampere'),
        ('Voltmeter',             'Instrument to measure potential difference; connected in PARALLEL; unit: Volt'),
        ('Ohmmeter',              'Instrument to measure resistance; used when circuit is OFF; unit: Ohm'),
        ('Electric Circuit',      'Complete closed path through which electric current flows'),
        ('Series Circuit',        'Components connected end to end in single loop; same current; voltage divides'),
        ('Parallel Circuit',      'Components connected between same two points; voltage same; current divides'),
        ('Fuse',                  'Safety device made of lead-tin alloy with low melting point; melts on excess current; breaks circuit'),
        ('MCB (Miniature Circuit Breaker)','Safety device replacing fuse; breaks circuit automatically; can be switched back on without replacing'),
        ('Short Circuit',         'Low-resistance connection between conductors; causes excess current, heat, sparks, damage'),
        ('Earthing',              'Connecting exposed metal parts of electrical appliances to Earth via low-resistance wire; prevents shock'),
        ('Lightning',             'Massive electrostatic discharge between charged clouds or cloud and Earth'),
        ('Lightning Arrester',    'Metallic rod on building connected to ground via copper cable; safely directs lightning to Earth'),
        ('Electroscope',          'Instrument to detect presence of electric charge; gold leaves repel when charged'),
        ('Induction',             'Charging an uncharged body by bringing a charged body near it without physical contact'),
        ('Heating Effect',        'Electric current through conductor converts electrical energy to heat; basis of electric bulb, heater, iron'),
        ('Magnetic Effect',       'Electric current creates magnetic field around conductor; discovered by Oersted (1819)'),
        ('Electromagnet',         'Coil of wire wound around iron core; becomes magnet only when current flows'),
        ('Chemical Effect',       'Electric current passing through electrolyte causes chemical changes; basis of electrolysis'),
        ('Electrolysis',          'Decomposition of liquid compound into ions by passing electric current through it'),
        ('Electroplating',        'Depositing a layer of one metal on another using electrolysis; protects and decorates metals'),
        ('Electrolyte',           'Conducting liquid that carries current and undergoes chemical change in electrolysis'),
        ('Nichrome',              'Alloy of Nickel, Iron and Chromium; high melting point and resistance; used in heating elements'),
        ('Tungsten',              'Metal with highest melting point (3422°C); used in bulb filaments; glows white when very hot'),
    ]

    s += [gloss_2col(g), sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P5: Electricity  |  Classes 6 • 7 • 8',
          S('ft',fontName=FNI,fontSize=8.5,textColor=TEAL,alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P5  |  Electricity  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P5 Electricity',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P5_electricity.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
