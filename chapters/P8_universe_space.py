"""
TET Paper II Science Handbook — P8: Universe and Space
Style: P3 one-liner cheat-sheet | Font: 10.5pt body, 10pt cells
All sub-topics: Class 7 (Term III, Unit 2) & Class 8 (Unit 8)
Covers: Geocentric/Heliocentric, Big Bang, Galaxies, Stars, Constellations,
Satellites, ISRO, Rockets, Chandrayaan 1/2/3, Mangalyaan, NASA
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

CHAPTER_ID = "P8"
CHAPTER_TITLE = "Universe and Space"
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
FS_BODY=10.5; FS_CELL=10.0; FS_SMALL=9.5; FS_MINI=9.0; FS_SEC=11.0; FS_FORM=12.0

def S(nm, **kw): return ParagraphStyle(nm, **kw)

BD  = S('bd', fontName=FN,  fontSize=FS_BODY, leading=15, textColor=GRAY_D, spaceAfter=2)
BDB = S('bb', fontName=FNB, fontSize=FS_BODY, leading=15, textColor=SLATE)
CE  = S('ce', fontName=FN,  fontSize=FS_CELL, leading=14, textColor=GRAY_D)
CEB = S('cb', fontName=FNB, fontSize=FS_CELL, leading=14, textColor=SLATE)
HWC = S('hc', fontName=FNB, fontSize=FS_SMALL,leading=13, textColor=WHITE, alignment=TA_CENTER)
SC  = S('sc', fontName=FNB, fontSize=FS_SEC,  leading=15, textColor=WHITE)
MIN = S('mn', fontName=FN,  fontSize=FS_MINI, leading=13, textColor=GRAY_D)

sp = lambda h: Spacer(1, h*mm)
P  = lambda t, st=BD: Paragraph(t, st)

def _fix(text):
    import re as _re
    sup={'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4',
         '\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9','\u207b':'-'}
    sub={'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4'}
    sc=''.join(sup.keys()); bc=''.join(sub.keys())
    def rs(m): return '<super>'+''.join(sup.get(c,c) for c in m.group())+'</super>'
    def rb(m): return '<sub>'  +''.join(sub.get(c,c) for c in m.group())+'</sub>'
    t=_re.sub(f'[{_re.escape(sc)}]+',rs,text)
    t=_re.sub(f'[{_re.escape(bc)}]+',rb,t)
    return t

# ─── BUILDERS ─────────────────────────────────────────────────────────────────
def banner(code, title, sub=''):
    data=[[
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
    t=Table(data,colWidths=[28*mm,UW-28*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),TEAL_D),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(0,0),6*mm),('LEFTPADDING',(1,0),(1,0),4*mm),
        ('RIGHTPADDING',(0,0),(-1,-1),4*mm),
        ('TOPPADDING',(0,0),(-1,-1),5*mm),('BOTTOMPADDING',(0,0),(-1,-1),5*mm),
    ]))
    return t

def sec(title, bg=TEAL):
    t=Table([[P(title,SC)]],colWidths=[UW])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg),
        ('LEFTPADDING',(0,0),(-1,-1),5*mm),('RIGHTPADDING',(0,0),(-1,-1),3*mm),
        ('TOPPADDING',(0,0),(-1,-1),2.5*mm),('BOTTOMPADDING',(0,0),(-1,-1),2.5*mm),
    ]))
    return t

def sub_h(title, bg=colors.HexColor('#0D9488')):
    t=Table([[P(title,S('sh',fontName=FNB,fontSize=FS_SMALL,leading=13,textColor=WHITE))]],
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
    result_tables=[]; cur_b=[]; cur_kv=[]; prev=None
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
            ('BACKGROUND',(0,0),(0,-1),TEAL),('BACKGROUND',(1,0),(1,-1),TEAL_L),
            ('BOX',(0,0),(-1,-1),0.6,TEAL),('LINEAFTER',(0,0),(0,-1),0.6,TEAL),
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

def rapid_ppl(rows):
    return grid(['Person / Event','Key Fact / Contribution','Date / Year'],
                rows, ws=[52*mm,88*mm,34*mm], hbg=PURPLE_D)

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
    s += [banner('P8','Universe & Space','Physics | Classes 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  ASTRONOMY & UNIVERSE — BASICS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  ASTRONOMY & UNIVERSE — Definitions & Units'), sp(2)]

    s += [kv_list([
        ('Astronomy',       'Science that deals with the study of stars, planets, their motions, positions and compositions'),
        ('Universe',        'Totality of everything that exists — consists of galaxies, planets, stars, meteorites, satellites and all matter/energy'),
        ('Celestial Objects','Stars, planets, Moon and other objects like asteroids and comets in the sky'),
        ('Solar System',    'The Sun and all celestial bodies revolving around it'),
        ('Galaxy',          'Large collection of stars or cluster of stars and celestial bodies held together by gravitational attraction'),
        ('Milky Way',       'Galaxy in which our Solar System is located — barred spiral galaxy'),
        ('Exoplanets',      'Planets orbiting around stars other than our Sun — proves planetary systems exist throughout universe'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=44*mm), sp(2)]

    s += [sub_h('Distance Units Used in Astronomy'), sp(1)]
    s += [one_liners([
        ('Astronomical Unit (AU)','Average distance between Earth and Sun = 1 AU = 1.496 × 10<super>8</super> km'),
        ('Light Year (ly)',       'Distance light travels in one year = 1 ly = 9.4607 × 10<super>12</super> km'),
        ('Parsec (pc)',            '1 pc = 3.2615 ly = 3.09 × 10<super>13</super> km — used for large cosmic distances'),
        ('Neptune distance from Sun','30 AU — thirty times farther than Earth from Sun'),
        ('Nearest star (Proxima Centauri)','4.22 light years from Earth and our Solar System'),
        ('Earth from galactic centre', '~27,000 light years away from the center of Milky Way'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  GEOCENTRIC & HELIOCENTRIC THEORIES
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  GEOCENTRIC & HELIOCENTRIC THEORIES'), sp(2)]

    s += [grid(
        ['Theory','Core Claim','Proposed By','Evidence / Notes'],
        [
            ['Geocentric Theory\n(Geocentrism)',
             'Earth is at the CENTRE of the Universe; Sun, Moon, stars and planets all orbit the Earth',
             'Plato & Aristotle (6th century BC, Greece); standardized by Ptolemy (2nd century AD)',
             'Based on: Sun appears to revolve around Earth daily; Earth feels stationary'],
            ['Heliocentric Theory\n(Heliocentrism)',
             'SUN is at the CENTRE; all planets including Earth revolve around the Sun',
             'Nicolaus Copernicus proposed; Galileo Galilei confirmed with telescope observations (1610–11)',
             'Galileo\'s Venus phase observations proved Venus orbits the Sun, not Earth'],
        ],
        ws=[34*mm,56*mm,44*mm,40*mm]
    ), sp(2)]

    s += [one_liners([
        'Retrograde motion: apparent reversal of direction of planets — could NOT be explained by simple geocentric model',
        'Epicycle model: modification of geocentric model to explain retrograde — used by Ptolemy, Aryabhata, Tycho Brahe, Neelakanta Somayaji',
        'Telescope invented by Hans Lippershey; Galileo used it first to study the sky',
        'Galileo discovered: mountains on Moon, sunspots on Sun, dim stars invisible to naked eye, Milky Way is thousands of stars',
        'Venus phases (crescent to gibbous) → could only happen if Venus orbits the SUN → proved heliocentric model',
        'Aryabhata (Indian astronomer): said Earth spins on its axis — explains apparent E→W daily motion of celestial objects',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  ORIGIN OF UNIVERSE — BIG BANG THEORY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  ORIGIN OF UNIVERSE — Big Bang Theory'), sp(2)]

    s += [kv_list([
        ('Big Bang Theory',   'Prevailing model of universe evolution — space and time emerged together ~14 billion years ago'),
        ('Starting point',    'All matter was inside a bubble thousands of times smaller than a pinhead — hotter and denser than anything imaginable'),
        ('Expansion',         'Suddenly expanded — grew from smaller than atom to bigger than galaxy in fraction of a second — still expanding today'),
        ('First 3 minutes',   'Temperature dropped below 1 billion degrees Celsius'),
        ('After 300,000 yrs', 'Universe cooled to ~3000°C — atomic nuclei captured electrons to form atoms — clouds of hydrogen and helium'),
        ('After 100 M years', 'Gas became hot and dense enough for first stars to form — 10x higher star formation rate than today'),
        ('Galaxy formation',  'Small galaxies formed ~1 billion years after Big Bang — closer together then — collisions created larger galaxies'),
        ('Evidence',          'All galaxies are moving AWAY from us (redshift) — farther they are, faster they move — implies single origin point'),
        ('Cosmic Microwave Background (CMB)','Faint glow in space — only direct evidence of the Big Bang itself'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=50*mm), sp(2)]

    s += [pill('📌', 'Big Bang: Space, Time and Matter all began together ~14 billion years ago. Universe is still expanding today.', TEAL_L, TEAL_D)]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  GALAXIES — Types & Milky Way
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  GALAXIES — Types & Milky Way'), sp(2)]

    s += [kv_list([
        ('Galaxy',           'Large collection of stars/celestial bodies held by gravity — billions of galaxies in universe'),
        ('Size range',       'Most galaxies: thousands to ten thousand parsecs in diameter'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=36*mm), sp(2)]

    s += [sub_h('Four Types of Galaxies'), sp(1)]
    s += [grid(
        ['Type','Shape & Structure','Key Features','Example'],
        [
            ['Spiral Galaxy',
             'Flat rotating disk with stars, gas and dust; central bulge (concentration of stars)',
             'Spiral arms are sites of ongoing star formation — brighter due to young, hot stars',
             'Many known spiral galaxies'],
            ['Elliptical Galaxy',
             'Three-dimensional ellipsoidal shape; smooth image; no spiral structure',
             'Stars in random orbits; stars much OLDER than in spiral galaxies; surrounded by globular clusters',
             'Common in galaxy clusters'],
            ['Irregular Galaxy',
             'No distinct regular shape — chaotic, no nuclear bulge, no spiral arms',
             'About ONE-FOURTH of all galaxies; may have been spiral/elliptical deformed by external gravity; abundant gas and dust',
             '~1/4 of known galaxies'],
            ['Barred Spiral Galaxy',
             'Spiral galaxy with central BAR-SHAPED structure composed of stars at center',
             'Bars found in approximately 1/3 to 2/3 of all spiral galaxies',
             'MILKY WAY is a barred spiral galaxy'],
        ],
        ws=[28*mm,52*mm,54*mm,40*mm]
    ), sp(2)]

    s += [sub_h('Milky Way — Our Galaxy'), sp(1)]
    s += [one_liners([
        ('Type',            'BARRED SPIRAL galaxy — our Solar System is located within it'),
        ('Diameter',        'Over 100,000 light years'),
        ('Number of stars', 'At least 100 billion (10<super>11</super>) stars'),
        ('Distance to centre','Our Solar System is ~27,000 light years from the galactic centre'),
        ('Rotation speed',  'Solar system travels at ~828,000 km/h around Milky Way centre'),
        ('Galactic year',   'Solar system takes ~230 million years to complete one orbit around Milky Way'),
        ('Black hole',      'Monstrous black hole at centre — billions of times more massive than Sun'),
        ('Nearest galaxy',  'Andromeda Galaxy (M31) — closest major galaxy to Milky Way'),
        ('Indian name',     '"Akasha Ganga" — band of light in night sky'),
        ('Resolved by',     'Galileo Galilei first resolved the Milky Way band into individual stars using telescope — 1610'),
        ('Galaxies count',  'Edwin Hubble showed Milky Way is just ONE of many galaxies — early 1920s'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  STARS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  STARS — Definition, Types & Key Facts'), sp(2)]

    s += [kv_list([
        ('Star',            'Luminous heavenly body that radiates energy produced by nuclear fusion in its core'),
        ('Why stars twinkle','Atmospheric disturbances bend light on its way to us — causes twinkling (stars are stationary)'),
        ('Why planets don\'t twinkle','Planets are closer, appear as small discs — light from them is more stable'),
        ('Visible to naked eye','~3,000 stars in night sky visible without telescope; ~2,000 commonly cited'),
        ('Sun',             'The NEAREST star to Earth — average distance from Earth = 1 AU = 1.496 × 10<super>8</super> km'),
        ('Nearest star system','Alpha Centauri — nearest star system to our Solar System; Proxima Centauri is 4.22 ly away'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=52*mm), sp(2)]

    s += [sub_h('Moon Phases — Key Facts'), sp(1)]
    s += [one_liners([
        'New Moon: Moon between Earth and Sun → illuminated side faces away from Earth → dark side toward Earth → Moon invisible',
        'Full Moon: Earth between Sun and Moon → illuminated side fully faces Earth → Moon appears round',
        'First Quarter (waxing half): Sun-Earth-Moon at 90° → half illuminated half visible',
        'Third Quarter (waning half): Moon at 90° on other side → half illuminated half visible',
        'Crescent: phases where Moon is LESS than half illuminated | Gibbous: MORE than half illuminated',
        'Waxing = growing/expanding illumination | Waning = shrinking/decreasing illumination',
        'Sangam literature (Purananuru 65) by Kalathalaiyar describes full moon observation — evidence of ancient Indian astronomy',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  CONSTELLATIONS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  CONSTELLATIONS — Definition, Key Constellations & Names'), sp(2)]

    s += [kv_list([
        ('Constellation',   'Recognizable PATTERN of stars in the night sky when viewed from Earth — optical appearance, NOT a real physical system'),
        ('Total number',    'International Astronomical Union (IAU) has classified 88 constellations to cover the entire celestial sphere'),
        ('Names origin',    'Many have Greek or Latin names — often named after mythological characters'),
        ('vs Galaxy',       'In galaxy: stars bound by gravity; in constellation: stars may be very far apart but appear close due to same direction'),
        ('Why visible at different times','Different constellations visible at different times of year — due to Earth\'s revolution around the Sun'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=44*mm), sp(2)]

    s += [sub_h('Key Constellations'), sp(1)]
    s += [grid(
        ['Constellation','Indian Name','Key Feature / Stars'],
        [
            ['Ursa Major',  'Saptha Rishi Mandalam (சப்த ரிஷி மண்டலம்)',
             'Large constellation covering large sky area; 7 bright stars = Big Dipper (Sapta Maharishi in Indian astronomy)'],
            ['Ursa Minor',  'Dhruva Mandalam',
             '"Little bear" in Latin; lies in northern sky; contains POLE STAR — Polaris (Dhruva); 7 stars = Little Dipper'],
            ['Orion',       'Vyadha / Kalpurusha',
             'Named after hunter in Greek mythology; ~81 stars, only ~10 visible to naked eye; contains Betelgeuse, Rigel'],
        ],
        ws=[28*mm,52*mm,94*mm]
    ), sp(2)]

    s += [sub_h('Indian & English Constellation Names (Zodiac Signs)'), sp(1)]
    s += [grid(
        ['Indian Name','English Name','Indian Name','English Name','Indian Name','English Name'],
        [
            ['Mesham','Aries','Rishabham','Taurus','Midhunam','Gemini'],
            ['Kadakam','Cancer','Simmam','Leo','Kanni','Virgo'],
            ['Thulam','Libra','Vrischikam','Scorpio','Dhanusu','Sagittarius'],
            ['Makaram','Capricorn','Kumbam','Aquarius','Meenam','Pisces'],
        ],
        ws=[28*mm,28*mm,28*mm,28*mm,28*mm,34*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  SATELLITES — Natural & Artificial
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  SATELLITES — Natural & Artificial'), sp(2)]

    s += [kv_list([
        ('Satellite',         'Object that revolves around a planet in a stable, consistent orbit'),
        ('Natural Satellite',  'Natural objects revolving around a planet — also called MOONS — mostly spherical'),
        ('Artificial Satellite','Man-made objects placed in orbit to rotate around a planet — usually Earth'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=44*mm), sp(2)]

    s += [sub_h('Natural Satellites — Key Facts'), sp(1)]
    s += [one_liners([
        'All planets EXCEPT Mercury and Venus have natural moons',
        'Earth has only ONE moon (The Moon) — average distance from Earth = 3,84,400 km | Diameter = 3,474 km',
        'Moon has NO atmosphere — does not produce its own light — reflects sunlight',
        'Jupiter and Saturn have more than 60 moons each',
        'Moon\'s rotation period = Revolution period around Earth → we always see the SAME side of Moon from Earth',
        'Some non-spherical moons = asteroids/meteors captured by strong planetary gravity',
    ]), sp(2)]

    s += [sub_h('Artificial Satellites — World & India Firsts'), sp(1)]
    s += [one_liners([
        ('World\'s first satellite', 'Sputnik-1 — launched by RUSSIA (USSR) — first artificial satellite in space'),
        ('India\'s first satellite',  'ARYABHATA — built by ISRO, launched by Soviet Union on 19 April 1975 — named after Indian astronomer Aryabhata'),
        ('First Indian satellite in Indian orbit', 'Rohini — launched in 1980 by Indian SLV-3 rocket — first satellite placed in orbit by Indian-made launch vehicle'),
        ('Satellite uses', 'Television/radio transmission, weather forecasting, agriculture yield study, mineral resource location, GPS/navigation, Earth mapping'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  ISRO — Indian Space Research Organisation
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  ISRO — Indian Space Research Organisation'), sp(2)]

    s += [kv_list([
        ('Full form',         'Indian Space Research Organisation'),
        ('Headquarters',      'Bangalore (Bengaluru), Karnataka'),
        ('Formed',            '1969 — superseded INCOSPAR (Indian National Committee for Space Research) which was established in 1962'),
        ('Founded by',        'Scientist Vikram Sarabhai — father of Indian space programme'),
        ('Vision',            '"Harness space technology for national development while pursuing space science research and planetary exploration"'),
        ('Managed by',        'Department of Space — reports to the Prime Minister of India'),
        ('Popular rockets',   'PSLV (Polar Satellite Launch Vehicle) and GSLV (Geosynchronous Satellite Launch Vehicle)'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=46*mm), sp(2)]

    s += [sub_h('ISRO Key Milestones'), sp(1)]
    s += [one_liners([
        ('Aryabhata (1975)',           '19 April 1975 — India\'s first satellite — launched by Soviet Union'),
        ('Rohini / SLV-3 (1980)',       'First satellite placed in orbit by an INDIAN-MADE launch vehicle — SLV-3 rocket'),
        ('PSLV',                       'Polar Satellite Launch Vehicle — for polar orbits'),
        ('GSLV',                       'Geosynchronous Satellite Launch Vehicle — for geostationary orbits'),
        ('Cryogenic engine (2014)',    'January 2014 — GSLV-D5 used indigenous cryogenic engine to launch GSAT-14'),
        ('20 satellites (2016)',       '18 June 2016 — ISRO launched 20 satellites in a single payload — set record then'),
        ('104 satellites (2017)',      '15 February 2017 — PSLV-C37 launched 104 satellites in a SINGLE rocket — world record'),
        ('GSLV-Mk III (2017)',         '5 June 2017 — India\'s heaviest rocket; placed GSAT-19 in orbit; capable of launching 4-ton satellites'),
        ('GAGAN',                      'GPS Aided Geo Augmented Navigation — satellite navigation system'),
        ('IRNSS',                      'Indian Regional Navigation Satellite System — India\'s own navigation system'),
        ('Rakesh Sharma (1984)',       '2 April 1984 — First Indian to enter space — in joint India-USSR space programme; called "Cosmonaut"'),
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  ROCKETS — Parts, Propellants & Launch Principle
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  ROCKETS — Parts, Propellants & Launch Principle'), sp(2)]

    s += [kv_list([
        ('Rocket',          'Space vehicle with very powerful engine — carries people or equipment beyond Earth into space'),
        ('First rockets',   'China invented rockets 800+ years ago — cardboard tube packed with gunpowder called "fire arrows" — used in 1232 AD'),
        ('Rocket principle','Newton\'s Third Law — gas released DOWNWARD → rocket moves UPWARD — equal and opposite reaction'),
        ('Multistage rocket','Single rocket cannot develop high velocities needed → multistage rockets used; upper stages ignite after lower stages exhaust'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=44*mm), sp(2)]

    s += [sub_h('Four Parts of a Rocket'), sp(1)]
    s += [grid(
        ['System','What It Does','Materials / Details'],
        [
            ['Structural System (Frame)',
             'Frame that covers the rocket — provides shape and strength',
             'Made of lightweight, strong materials like titanium or aluminium; fins at bottom for stability during flight'],
            ['Payload System',
             'Carries the satellite or cargo into orbit',
             'Depends on mission — satellites for communication, weather, spying, planetary exploration, or manned missions'],
            ['Guidance System',
             'Guides and navigates the rocket in its correct path',
             'Sensors, on-board computers, radars, communication equipment; tilts rocket to correct trajectory'],
            ['Propulsion System',
             'Provides thrust to move rocket — takes up most space in rocket',
             'Fuel tanks, pumps, combustion chamber; two types: liquid and solid propulsion'],
        ],
        ws=[30*mm,56*mm,88*mm]
    ), sp(2)]

    s += [sub_h('Three Types of Propellants'), sp(1)]
    s += [grid(
        ['Type','Description','Fuel Examples','Oxidizer Examples'],
        [
            ['Liquid Propellants',
             'Fuel and oxidiser combined in combustion chamber; burn and exit from base with great force',
             'Liquid hydrogen, Hydrazine, Ethyl alcohol',
             'Oxygen, Ozone, Hydrogen peroxide, Fuming nitric acid'],
            ['Solid Propellants',
             'Fuel and oxidiser already combined — when ignited burn and produce heat; CANNOT be stopped once ignited',
             'Polyurethanes, Poly butadienes',
             'Nitrate salts, Chlorate salts'],
            ['Cryogenic Propellants',
             'Fuel/oxidiser or both are LIQUEFIED GASES stored at very LOW temperature; react on mixing — start own flame (no ignition system needed)',
             'Liquid hydrogen (stored at -253°C)',
             'Liquid oxygen (stored at -183°C)'],
        ],
        ws=[28*mm,56*mm,48*mm,42*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  CHANDRAYAAN MISSIONS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  CHANDRAYAAN MISSIONS — 1, 2 & 3'), sp(2)]

    s += [sub_h('Chandrayaan-1 — Moon Vehicle'), sp(1)]
    s += [grid(
        ['Detail','Information'],
        [
            ['Launch date', '22 October 2008'],
            ['Launch vehicle', 'PSLV (Polar Satellite Launch Vehicle)'],
            ['Launch site', 'Satish Dhawan Space Centre, Sriharikota, Andhra Pradesh'],
            ['Lunar orbit insertion', '8 November 2008'],
            ['Orbit height', '100 km from lunar surface'],
            ['Duration', 'Operated for 312 days; achieved 95% of objectives'],
            ['Communication lost', '28 August 2009'],
            ['Objectives', 'Find water on Moon; find elements of matter; search Helium-3; make 3D atlas of Moon; study solar system evolution'],
            ['Key achievement', 'Discovered presence of WATER MOLECULES in lunar soil — major discovery'],
            ['Other achievements', 'Confirmed Moon was completely molten once; 40,000+ images in 75 days; found caves on lunar surface; imaged Apollo-11 and Apollo-15 landing sites'],
        ],
        ws=[40*mm,134*mm]
    ), sp(2)]

    s += [sub_h('Chandrayaan-2'), sp(1)]
    s += [one_liners([
        'Launch date: 22 July 2019 by GSLV-Mk III rocket',
        'Consisted of: Orbiter + Lander (Vikram) + Rover (Pragyan — Sanskrit for "wisdom", 6-wheeled robotic vehicle)',
        'Vikram lander named after Dr. Vikram A. Sarabhai — father of Indian space programme',
        'Lunar orbit insertion: 20 August 2019',
        'Final stage: 7 September 2019 — Lander Vikram lost communication with ground station just 2.1 km above lunar surface — crashed',
        'Orbiter continues working successfully — still operational',
        'Project Director: Vanitha Muthayya — first woman project director at ISRO; born 2 August 1964 in Chennai',
    ]), sp(2)]

    s += [sub_h('Chandrayaan-3 — Follow-up to Chandrayaan-2'), sp(1)]
    s += [one_liners([
        'Launch date: 14 July 2023 from Satish Dhawan Space Centre, Sriharikota',
        'Lunar orbit insertion: 5 August 2023',
        'SUCCESSFUL landing: 23 August 2023 on lunar SOUTH POLE region',
        'India became FOURTH country to land on Moon (after Russia, USA, China) AND FIRST to land on lunar South Pole',
        'Consists of: Lander (Vikram) + Rover (Pragyan)',
        'Achievements: measured lunar soil temperature at various depths; detected moonquakes; Rover found Aluminium, Iron, Calcium, Sulphur, Oxygen on lunar surface',
        'Project Director: Dr. P. Veeramuthuvel — born 22 October 1976 in Villupuram district; PhD from IIT Madras; joined ISRO in 2014',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  MANGALYAAN — MARS ORBITER MISSION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  MANGALYAAN — Mars Orbiter Mission (MOM)'), sp(2)]

    s += [grid(
        ['Detail','Information'],
        [
            ['Mission name', 'Mars Orbiter Mission (MOM) — Mangalyaan means "Mars vehicle"'],
            ['Launch date', '5 November 2013'],
            ['Launch vehicle', 'PSLV rocket from Sriharikota, Andhra Pradesh'],
            ['Mars orbit insertion', '24 September 2014'],
            ['Significance', 'India\'s FIRST interplanetary mission — ISRO became 4th space agency to reach Mars (after Soviet Space Program, NASA, European Space Agency)'],
            ['Historic first', 'India was FIRST NATION to succeed on its FIRST ATTEMPT to Mars | FIRST ASIAN country to reach Mars'],
            ['Mission duration', 'Successfully completed 3+ years in Martian orbit; continued working as expected'],
            ['Objectives', 'Develop interplanetary mission technology; explore Mars surface; study Mars atmosphere; investigate past/future life possibility'],
        ],
        ws=[40*mm,134*mm]
    ), sp(2)]

    s += [note_box('Mars — Key Facts', [
        'Fourth planet from Sun; second smallest planet in solar system',
        'Called "Red Planet" — iron oxide (rust) on its surface and dusty atmosphere gives reddish colour',
        'Mars rotation: once in 24 hours 37 minutes (similar to Earth\'s 24 hours)',
        'Mars revolution: once in 687 days around Sun',
        'Project Director of Chandrayaan-1: Dr. Mylsamy Annadurai — born 2 July 1958 in Kodhavadi near Pollachi, Coimbatore',
    ], icon='🔴')]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # L  NASA & INDIANS IN NASA
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('L  ·  NASA & INDIANS IN NASA'), sp(2)]

    s += [kv_list([
        ('NASA',                'National Aeronautics and Space Administration'),
        ('Headquarters',        'Washington, USA'),
        ('Established',         '1st October 1958'),
        ('Field centers',       '10 field centers — support NASA\'s work globally'),
        ('International Space Station','NASA supports ISS — international collaborative space research project'),
        ('Achievements',        'Landed rovers on Mars; analysed Jupiter atmosphere; explored Saturn and Mercury; satellites for weather, environment'),
        ('NASA-ISRO partnership','NISAR Satellite — NASA-ISRO Synthetic Aperture Radar — joint programme'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=50*mm), sp(2)]

    s += [sub_h('Apollo Missions — NASA\'s Most Famous Programme'), sp(1)]
    s += [one_liners([
        'Apollo programme: total 17 missions — made American astronauts land on Moon',
        ('Apollo-8',  'First MANNED mission to go to the Moon — orbited Moon and returned to Earth'),
        ('Apollo-11', 'First "Man Landing Mission" — landed on Moon on 20 July 1969'),
        ('Neil Armstrong','First man to WALK on the surface of the Moon — Apollo-11'),
        ('Crew of Apollo-11', 'Neil Armstrong, Buzz Aldrin (both landed on Moon), Michael Collins (stayed in orbit)'),
    ]), sp(2)]

    s += [sub_h('Indians in NASA'), sp(1)]
    s += [grid(
        ['Person','Birth / Background','Key Achievement'],
        [
            ['Kalpana Chawla',
             'Born 17 March 1962, Karnal, Punjab; joined NASA in 1988',
             'First Indian woman astronaut in space (1997 Columbia Shuttle Mission); died in second mission (Columbia Shuttle) on re-entry; 10.4 million miles in 252 orbits, 372+ hours in space'],
            ['Sunitha Williams',
             'Born 19 September 1965 in USA; astronaut career started August 1998',
             'Two trips to International Space Station; SET WORLD RECORD for longest spacewalk time by female astronaut — 50 hours 40 minutes total (7 spacewalks) in 2012; crew of NASA\'s Manned Mars Mission'],
        ],
        ws=[28*mm,50*mm,96*mm]
    ), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # M  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('M  ·  Key Facts — Rapid Revision  (Names, Dates, Records)'), sp(2)]

    s += [P('<b>Scientists, Missions & Key Dates</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['Plato & Aristotle',          'Proposed Geocentric model — Earth at center',                            '6th century BC'],
        ['Ptolemy',                    'Standardized geocentric model (epicycle)',                                '2nd century AD'],
        ['Aryabhata',                  'Said Earth spins on its axis — Indian astronomer',                       '5th–6th century AD'],
        ['Nicolas Copernicus',         'Proposed Heliocentric model — Sun at center',                           '16th century'],
        ['Hans Lippershey',            'Invented the telescope',                                                 '1608'],
        ['Galileo Galilei',            'First used telescope to study sky; confirmed heliocentric using Venus phases', '1610–11'],
        ['Edwin Hubble',               'Showed Milky Way is just one of many galaxies',                         'Early 1920s'],
        ['Vikram Sarabhai',            'Founded INCOSPAR (1962); father of Indian space programme',             '1919–1971'],
        ['ISRO founded',               'Indian Space Research Organisation — Bangalore',                        '1969'],
        ['Aryabhata satellite',        'India\'s first satellite — launched by Soviet Union',                   '19 Apr 1975'],
        ['Rohini / SLV-3',             'First Indian satellite by Indian launch vehicle',                       '1980'],
        ['Rakesh Sharma',              'First Indian in space — joint India-USSR programme',                    '2 Apr 1984'],
        ['Kalpana Chawla',             'First Indian woman in space (Columbia Shuttle)',                        '1997'],
        ['Chandrayaan-1 launch',       'PSLV from Sriharikota — to study Moon',                               '22 Oct 2008'],
        ['Chandrayaan-1 lunar orbit',  'Put into lunar orbit at 100 km height',                                '8 Nov 2008'],
        ['Chandrayaan-1 ended',        'Communication lost after 312 days; 95% objectives achieved',           '28 Aug 2009'],
        ['Mangalyaan launch',          'PSLV from Sriharikota — India\'s first Mars mission',                  '5 Nov 2013'],
        ['Mangalyaan Mars orbit',      'India = 4th space agency, 1st Asian nation, 1st first-attempt success to Mars', '24 Sep 2014'],
        ['104 satellites record',      'PSLV-C37 — world record for satellites in single launch',              '15 Feb 2017'],
        ['GSLV-Mk III first launch',   'India\'s heaviest rocket; placed GSAT-19; capable of 4-ton satellites', '5 Jun 2017'],
        ['Chandrayaan-2 launch',       'GSLV-Mk III; Orbiter+Vikram Lander+Pragyan Rover',                   '22 Jul 2019'],
        ['Chandrayaan-2 lunar orbit',  'Successfully inserted into lunar orbit',                               '20 Aug 2019'],
        ['Chandrayaan-2 crash',        'Vikram Lander lost contact 2.1 km above surface',                     '7 Sep 2019'],
        ['Chandrayaan-3 launch',       'Follow-up mission to successfully land on Moon',                       '14 Jul 2023'],
        ['Chandrayaan-3 landing',      'Successfully landed on lunar SOUTH POLE — India 4th country to land on Moon', '23 Aug 2023'],
        ['NASA established',           'National Aeronautics and Space Administration — Washington, USA',       '1 Oct 1958'],
        ['Apollo-8',                   'First manned mission to go to Moon (orbit, no landing)',                '1968'],
        ['Neil Armstrong',             'First human to walk on Moon — Apollo-11',                              '20 Jul 1969'],
        ['KalamSat',                   'World\'s smallest satellite (64g) — built by high school students led by Rifath Sharook, 18, from Pallapatti, Karur district, TN', '22 Jun 2017'],
        ['Sunitha Williams',           'Longest spacewalk time by female astronaut — 50 hrs 40 min (7 walks)',  '2012'],
        ['Dr. Annadurai (Chandrayaan-1)','Project Director — born in Kodhavadi near Pollachi, Coimbatore',    '1958–present'],
        ['Vanitha Muthayya (CY-2)',    'Project Director Chandrayaan-2 — first woman PD at ISRO; born Chennai', '1964–present'],
        ['Dr. P. Veeramuthuvel (CY-3)','Project Director Chandrayaan-3 — born Villupuram; PhD from IIT Madras', '1976–present'],
        ['Dr. K.V. Sivan',             'ISRO Chairperson during Chandrayaan-2; born Sarakkalvilai, Kanyakumari; "Rocket Man"', 'in office 2018–2022'],
        ['S. Chandrasekhar',           'Indian-American astrophysicist; Nobel Prize for Physics 1983; Chandrasekhar limit (white dwarf mass limit)', '1910–1995'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # N  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('N  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Astronomy',       'Science studying stars, planets, their motions, positions and compositions'),
        ('Universe',        'Totality of everything that exists — all matter, energy, space and time'),
        ('Celestial Object','Any natural object in space — stars, planets, Moon, asteroids, comets'),
        ('Solar System',    'The Sun and all celestial bodies (planets, moons, asteroids) revolving around it'),
        ('Galaxy',          'Large collection of stars/celestial bodies held together by gravitational attraction'),
        ('Milky Way',       'Barred spiral galaxy containing our Solar System; 100+ billion stars; >100,000 ly diameter'),
        ('Astronomy Unit (AU)','Average distance from Earth to Sun = 1.496 × 10<super>8</super> km'),
        ('Light Year (ly)', 'Distance light travels in one year = 9.46 × 10<super>12</super> km'),
        ('Parsec (pc)',     '1 pc = 3.2615 ly — unit for large cosmic distances'),
        ('Geocentric Theory','Earth at center; all celestial bodies orbit Earth — Plato, Aristotle, Ptolemy'),
        ('Heliocentric Theory','Sun at center; all planets including Earth orbit the Sun — Copernicus, confirmed by Galileo'),
        ('Retrograde Motion','Apparent reversal of planet\'s direction of motion — key problem for geocentric model'),
        ('Epicycle Model',  'Modified geocentric model to explain retrograde motion — used by Ptolemy and Aryabhata'),
        ('Big Bang Theory', 'Prevailing model — universe began ~14 billion years ago from a single point; still expanding'),
        ('Cosmic Microwave Background','Faint microwave glow — only direct evidence of the Big Bang'),
        ('Spiral Galaxy',   'Flat rotating disk with spiral arms — sites of ongoing star formation'),
        ('Elliptical Galaxy','3D ellipsoidal shape; no structure; older stars; surrounded by globular clusters'),
        ('Irregular Galaxy', 'No distinct shape; ~1/4 of all galaxies; may be deformed former spiral/elliptical'),
        ('Barred Spiral Galaxy','Spiral with central bar-shaped structure — Milky Way is this type'),
        ('Star',            'Luminous heavenly body that radiates energy from nuclear fusion in its core'),
        ('Constellation',   'Recognizable pattern of stars in night sky; 88 total (IAU); optical appearance, not physical system'),
        ('Satellite',       'Object revolving around a planet in stable orbit'),
        ('Natural Satellite','Natural moon revolving around a planet — e.g., Earth\'s Moon'),
        ('Artificial Satellite','Man-made object placed in orbit — e.g., Aryabhata, Chandrayaan'),
        ('ISRO',            'Indian Space Research Organisation — Bangalore; formed 1969 — India\'s space agency'),
        ('Rocket',          'Vehicle propelling itself by ejecting part of its mass — works on Newton\'s Third Law'),
        ('Propellant',      'Chemical substance that undergoes combustion to produce thrust in rockets'),
        ('Liquid Propellant','Fuel and oxidiser stored separately; combined in combustion chamber'),
        ('Solid Propellant', 'Fuel and oxidiser pre-mixed; burns when ignited; cannot be stopped'),
        ('Cryogenic Propellant','Liquefied gases stored at very low temperature; react on mixing; used in GSLV'),
        ('PSLV',            'Polar Satellite Launch Vehicle — India\'s reliable rocket for polar orbits'),
        ('GSLV',            'Geosynchronous Satellite Launch Vehicle — for geostationary orbits; uses cryogenic engine'),
        ('Chandrayaan',     'Indian Moon missions — 1 (2008), 2 (2019), 3 (2023 — first landing on south pole)'),
        ('Mangalyaan',      'Mars Orbiter Mission — India\'s first interplanetary mission; ISRO 4th space agency to reach Mars'),
        ('NASA',            'National Aeronautics and Space Administration — USA\'s space agency; established 1 Oct 1958'),
        ('Apollo Mission',  'NASA programme — 17 missions; Apollo-8 first to orbit Moon; Apollo-11 first Moon landing (1969)'),
        ('Payload',         'Object/satellite carried into orbit by rocket; depends on mission'),
        ('Space Probe',     'Unmanned vehicle sent into space to study planets — e.g., Mangalyaan'),
        ('Exoplanet',       'Planet orbiting a star other than our Sun — proves planetary systems exist throughout universe'),
    ]

    s += [gloss_2col(g), sp(3)]

    s += [dyk([
        'KalamSat — world\'s smallest satellite weighing just 64 grams — built by high school students led by Rifath Sharook (18 years old) from Pallapatti near Karur, Tamil Nadu — launched by NASA on 22 June 2017.',
        'When Milky Way was last in the same position as today (~230 million years ago), there were no humans — not even Himalayan mountains — dinosaurs were roaming Earth.',
        'Subrahmanyan Chandrasekhar — Indian-American astrophysicist — won Nobel Prize for Physics in 1983 for his work on stellar evolution and black holes. Chandrasekhar limit: maximum mass (~1.4 solar masses) of a stable white dwarf star.',
        'India is the FIRST nation to successfully land on the lunar SOUTH POLE — with Chandrayaan-3 on 23 August 2023.',
        'Mars Orbiter Mission (Mangalyaan) cost only ₹450 crore (~$74 million) — cheaper than making the Hollywood movie "Gravity" ($100 million) — making it the most cost-effective Mars mission in history.',
    ])]
    s += [sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P8: Universe & Space  |  Classes 7 & 8',
          S('ft',fontName=FNI,fontSize=8.5,textColor=TEAL,alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P8  |  Universe & Space  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P8 Universe and Space',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P8_universe_space.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
