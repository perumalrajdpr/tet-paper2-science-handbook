"""
P1: MEASUREMENT — A4 Two-Column with proper full-width spanning
Strategy: Single wide frame for full-width elements, twin frames for body text
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    NextPageTemplate, PageTemplate, Frame, FrameBreak, BaseDocTemplate
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ── FONTS
dv = '/usr/share/fonts/truetype/dejavu'
for name, fname in [('DV','DejaVuSans'),('DV-B','DejaVuSans-Bold'),
                    ('DV-I','DejaVuSans-Oblique'),('DV-BI','DejaVuSans-BoldOblique')]:
    pdfmetrics.registerFont(TTFont(name, f'{dv}/{fname}.ttf'))
registerFontFamily('DV', normal='DV', bold='DV-B', italic='DV-I', boldItalic='DV-BI')

# ── THEME
PRIMARY   = HexColor('#0F766E')
ACCENT    = HexColor('#F59E0B')
LIGHT_BG  = HexColor('#F0FDFA')
HIGHLIGHT = HexColor('#FEF3C7')
BORDER    = HexColor('#CBD5E1')
TEXT      = HexColor('#0F172A')
MUTED     = HexColor('#64748B')

# ── GEOMETRY
PW, PH   = A4
ML = MR  = 20*mm
MT       = 22*mm
MB       = 16*mm
CGAP     = 6*mm
CW       = (PW - ML - MR - CGAP) / 2   # one column
FW       = PW - ML - MR                 # full usable width
CH       = PH - MT - MB                 # column height

# ── STYLES
def sty(nm, **kw):
    d = dict(fontName='DV', fontSize=8.5, leading=11.5, textColor=TEXT, spaceAfter=2)
    d.update(kw)
    return ParagraphStyle(nm, **d)

ST = {
    'sec' : sty('sec', fontName='DV-B', fontSize=10, leading=13,
                textColor=white, backColor=PRIMARY, borderPadding=(3,4,3,4),
                spaceBefore=5, spaceAfter=3),
    'sub' : sty('sub', fontName='DV-B', fontSize=9, textColor=PRIMARY,
                spaceBefore=4, spaceAfter=2),
    'body': sty('body', alignment=TA_JUSTIFY),
    'fact': sty('fact', backColor=HIGHLIGHT, borderPadding=3,
                leftIndent=4, spaceBefore=2, spaceAfter=3),
    'defn': sty('defn', fontName='DV-I', backColor=LIGHT_BG,
                borderPadding=3, leftIndent=4, spaceAfter=3),
    'th'  : sty('th', fontName='DV-B', fontSize=8, textColor=white,
                alignment=TA_CENTER, leading=9.5),
    'td'  : sty('td', fontSize=8, textColor=TEXT, alignment=TA_LEFT, leading=9.5),
    'gc'  : sty('gc', fontSize=7.8, leading=10),
    'ph'  : sty('ph', fontName='DV-B', fontSize=8, textColor=white,
                alignment=TA_CENTER, leading=9),
    'pb'  : sty('pb', fontSize=8, textColor=TEXT, alignment=TA_LEFT, leading=9.5),
    'bid' : sty('bid', fontName='DV-B', fontSize=22, textColor=white,
                leading=24, alignment=TA_CENTER),
    'btit': sty('btit', fontName='DV-B', fontSize=16, textColor=white,
                leading=18, alignment=TA_LEFT),
    'bsub': sty('bsub', fontName='DV-I', fontSize=9, textColor=white,
                leading=11, alignment=TA_LEFT),
}

# ── PAGE CHROME
def chrome(canv, doc):
    canv.saveState()
    canv.setFillColor(PRIMARY)
    canv.rect(0, PH-7*mm, PW, 7*mm, fill=1, stroke=0)
    canv.setFillColor(white)
    canv.setFont('DV-B', 7.5)
    canv.drawString(ML, PH-4.8*mm, 'TET PAPER II SCIENCE  ·  P1 MEASUREMENT')
    canv.setFont('DV', 7.5)
    canv.drawRightString(PW-MR, PH-4.8*mm, 'ChalkPieceDiary')
    canv.setStrokeColor(BORDER); canv.setLineWidth(0.4)
    canv.line(ML, MB-4*mm, PW-MR, MB-4*mm)
    canv.setFillColor(MUTED); canv.setFont('DV', 7)
    canv.drawString(ML, MB-7*mm, 'TET Paper II Science Handbook')
    canv.drawCentredString(PW/2, MB-7*mm, f'P1.{doc.page}')
    canv.drawRightString(PW-MR, MB-7*mm, 'chalkpiecediary.com')
    canv.restoreState()

# ── HELPERS
def p(txt): return Paragraph(txt, ST['body'])
def sp(h=1.5): return Spacer(1, h*mm)

def section(num, title):
    return Paragraph(f'<b>{num}.  {title}</b>', ST['sec'])

def subsec(num, title):
    return Paragraph(f'<b>{num}</b>  {title}', ST['sub'])

def fact(txt):
    return Paragraph(f'<b>★</b>  {txt}', ST['fact'])

def tbl(header, rows, cw=None, fs=8, hcol=PRIMARY):
    if cw is None: cw = [FW/len(header)]*len(header)
    hs = ParagraphStyle('_h', fontName='DV-B', fontSize=fs, textColor=white,
                        alignment=TA_CENTER, leading=fs+2)
    bs = ParagraphStyle('_b', fontSize=fs, textColor=TEXT,
                        alignment=TA_LEFT, leading=fs+2)
    data = [[Paragraph(str(c), hs) for c in header]]
    for row in rows:
        data.append([Paragraph(str(c), bs) for c in row])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), hcol),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[white, LIGHT_BG]),
        ('GRID',          (0,0),(-1,-1),0.3, BORDER),
        ('VALIGN',        (0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',   (0,0),(-1,-1),3),
        ('RIGHTPADDING',  (0,0),(-1,-1),3),
        ('TOPPADDING',    (0,0),(-1,-1),2),
        ('BOTTOMPADDING', (0,0),(-1,-1),2),
    ]))
    return t

def prob_tbl(probs):
    cw = [8*mm, FW*0.52, FW*0.48-8*mm]
    data = [[Paragraph(c, ST['ph']) for c in ['#','Problem','Solution']]]
    for i,(q,a) in enumerate(probs,1):
        data.append([Paragraph(str(i),ST['pb']),
                     Paragraph(q,ST['pb']),
                     Paragraph(a,ST['pb'])])
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), PRIMARY),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[white, LIGHT_BG]),
        ('GRID',          (0,0),(-1,-1),0.3, BORDER),
        ('VALIGN',        (0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',   (0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
        ('TOPPADDING',    (0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
    ]))
    return t

def gloss(items):
    def cell(t,d): return Paragraph(
        f'<font name="DV-B" color="#0F766E">{t}:</font> {d}', ST['gc'])
    cells = [cell(t,d) for t,d in items]
    rows = []
    for i in range(0, len(cells), 2):
        r = cells[i+1] if i+1<len(cells) else Paragraph('',ST['gc'])
        rows.append([cells[i], r])
    t = Table(rows, colWidths=[FW/2, FW/2])
    t.setStyle(TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3),
        ('TOPPADDING',(0,0),(-1,-1),1),('BOTTOMPADDING',(0,0),(-1,-1),1),
        ('LINEBELOW',(0,0),(-1,-2),0.2,BORDER),
    ]))
    return t

def banner():
    data = [[
        Paragraph('<b>P1</b>', ST['bid']),
        [Paragraph('<b>MEASUREMENT</b>', ST['btit']),
         Spacer(1,1*mm),
         Paragraph('Physics  ·  Class 6 + 7 + 8', ST['bsub'])],
    ]]
    t = Table(data, colWidths=[22*mm, FW-22*mm], rowHeights=[14*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),PRIMARY),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
        ('LINEAFTER',(0,0),(0,0),0.5,HexColor('#FFFFFF80')),
    ]))
    return t

# ── CONTENT: each element is (zone, flowable)
# zone 'F' = full-width (1 col page), zone 'C' = 2-col body
def content():
    F = 'F'  # full-width
    C = 'C'  # 2-column body

    items = []
    def f(x): items.append((F, x))  # full-width item
    def c(x): items.append((C, x))  # body column item

    f(banner()); f(sp(2))

    # 1
    f(section('1','Measurement — Basics'))
    c(p('<b>Measurement</b>: comparing an unknown quantity with a known standard. '
        'Every measurement = <b>numerical value (magnitude) + unit</b>. '
        'Eg: pencil 15 cm → "15" = magnitude, "cm" = unit.'))
    c(p('<b>Three things needed:</b> (1) Instrument  '
        '(2) Standard quantity  (3) Acceptable unit.'))

    # 2
    f(section('2','Types of Physical Quantities'))
    f(subsec('2.1','Fundamental (Base) Quantities — 7 in SI'))
    c(p('Cannot be expressed in terms of any other quantity.'))
    f(tbl(['#','Quantity','SI Unit','Symbol','Instrument'],[
        ['1','Length','metre','m','Metre scale, Measuring tape'],
        ['2','Mass','kilogram','kg','Beam balance, Electronic balance'],
        ['3','Time','second','s','Clock, Stopwatch'],
        ['4','Temperature','kelvin','K','Thermometer'],
        ['5','Electric current','ampere','A','Ammeter'],
        ['6','Amount of substance','mole','mol','—'],
        ['7','Luminous intensity','candela','cd','Photometer'],
    ], cw=[7*mm,32*mm,22*mm,16*mm,FW-77*mm]))
    f(fact('Memory aid: <b>L M T T E A L</b> → '
           '"<b>L</b>ittle <b>M</b>en <b>T</b>each <b>T</b>he '
           '<b>E</b>arly <b>A</b>fternoon <b>L</b>esson"'))

    f(subsec('2.2','Supplementary / Derived Angle Units (2)'))
    c(p('Until <b>1995</b>: supplementary. <b>From 1995</b>: reclassified as derived quantities.'))
    f(tbl(['Quantity','Unit','Symbol','Definition'],[
        ['Plane angle','radian','rad',
         '2D angle at intersection of 2 lines/planes. Arc-length = radius. π rad = 180°.'],
        ['Solid angle','steradian','sr',
         '3D angle at vertex of cone / ≥3 planes. Surface area = r². 4π sr = full sphere.'],
    ], cw=[28*mm,22*mm,14*mm,FW-64*mm]))
    f(fact('<b>π rad = 180°</b>  |  <b>1 rad ≈ 57.3°</b>  |  '
           '<b>Full circle = 2π rad = 360°</b>  |  <b>Full sphere = 4π sr</b>'))

    f(subsec('2.3','Derived Quantities'))
    c(p('Obtained by multiplying / dividing fundamental quantities.'))
    f(tbl(['Derived Quantity','Formula','SI Unit','Symbol'],[
        ['Area','Length × Breadth','square metre','m²'],
        ['Volume','L × B × H','cubic metre','m³'],
        ['Speed','Distance ÷ Time','metre/second','m/s'],
        ['Velocity','Displacement ÷ Time','metre/second','m/s (vector)'],
        ['Acceleration','Velocity ÷ Time','metre/sec²','m s<super>-2</super>'],
        ['Density','Mass ÷ Volume','kg/metre³','kg/m³'],
        ['Force','Mass × Acceleration','newton','N = kg·m/s²'],
        ['Pressure','Force ÷ Area','pascal','Pa = N/m²'],
        ['Work / Energy','Force × Distance','joule','J = N·m'],
        ['Power','Work ÷ Time','watt','W = J/s'],
        ['Electric charge','Current × Time','coulomb','C = A·s'],
        ['Frequency','1 ÷ Time period','hertz','Hz = 1/s'],
    ], cw=[FW*0.24,FW*0.28,FW*0.26,FW*0.22]))

    # 3
    f(section('3','Unit Systems — Historical & Current'))
    f(tbl(['System','Length','Mass','Time','Type'],[
        ['FPS','Foot','Pound','Second','British — non-metric'],
        ['CGS','Centimetre','Gram','Second','Metric'],
        ['MKS','Metre','Kilogram','Second','Metric — predecessor of SI'],
        ['SI','Metre','Kilogram','Second','Standard since 1960'],
    ], cw=[16*mm,28*mm,26*mm,20*mm,FW-90*mm]))
    f(fact('<b>SI = Système International d\'Unités</b> (French). '
           'Adopted at the <b>11th General Conference on Weights and Measures, '
           '1960, Paris, France</b>.'))
    f(fact('<b>Metric system</b> created by the <b>French, 1790</b>. '
           'Standard metre rod (Pt-Ir): <b>Bureau of Weights & Measures, Sèvres, Paris</b>. '
           'India copy: <b>National Physical Laboratory, Delhi</b>. '
           'Standard kg at Sèvres since <b>1889</b>.'))
    f(fact('<b>Ruler / Scale</b> invented by <b>William Bedwell, 16th century</b>. '
           'NASA Mars Orbiter: launched Dec 1998; lost <b>Sep 23, 1999</b>. '
           'FPS vs MKS mismatch → <b>$125 million</b> loss.'))

    # 4
    f(section('4','SI Prefixes — Multiples & Sub-multiples'))
    f(tbl(['Prefix','Sym','Multiplier','Prefix','Sym','Multiplier'],[
        ['Tera','T','10<super>12</super>','Deci','d','10<super>-1</super>'],
        ['Giga','G','10<super>9</super>','Centi','c','10<super>-2</super>'],
        ['Mega','M','10<super>6</super>','Milli','m','10<super>-3</super>'],
        ['Kilo','k','10<super>3</super>','Micro','µ','10<super>-6</super>'],
        ['Hecto','h','10<super>2</super>','Nano','n','10<super>-9</super>'],
        ['Deca','da','10<super>1</super>','Pico','p','10<super>-12</super>'],
    ], cw=[FW/6]*6, fs=8))
    f(subsec('4.1','Standard Conversions'))
    f(tbl(['Length','Mass','Volume / Capacity'],[
        ['1 km = 1000 m','1 tonne = 1000 kg','1 m³ = 1000 L'],
        ['1 m = 100 cm','1 kg = 1000 g','1 L = 1000 mL = 1000 cc'],
        ['1 cm = 10 mm','1 g = 1000 mg','1 cc = 1 cm³'],
        ['1 m = 1000 mm','1 quintal = 100 kg','1 gallon = 3785 mL'],
        ['1 light year = 9.46 × 10<super>1</super>⁵ m','1 carat = 200 mg','1 ounce = 30 mL'],
    ], cw=[FW/3]*3))

    # 5
    f(section('5','Length'))
    c(p('<b>Length</b> = distance between two points. SI unit: <b>metre (m)</b>.'))
    f(tbl(['Instrument','Use / Range'],[
        ['Metre scale / Ruler','Standard lengths in cm and mm'],
        ['Measuring tape','Longer lengths — height, room, field'],
        ['String / Thread','Curved or irregular lines'],
        ['Divider','Curved line — segment method'],
        ['Vernier calipers','Precision; least count 0.01 cm (0.1 mm)'],
        ['Screw gauge / Micrometer','Very small; least count 0.001 cm (10 µm)'],
        ['Odometer','Distance travelled by automobile'],
    ], cw=[FW*0.38,FW*0.62]))
    f(subsec('5.1','Common Errors While Measuring'))
    f(tbl(['Error','Cause','Avoidance'],[
        ['Zero error','Object edge not at "0" mark.','Start from 0 mark.'],
        ['Parallax error','Eye not perpendicular to scale.','Eye vertically above reading point.'],
        ['Worn-edge error','Damaged scale ends.','Use middle (undamaged) portion.'],
    ], cw=[FW*0.18,FW*0.42,FW*0.40]))

    # 6
    f(section('6','Mass and Weight'))
    f(tbl(['Property','Mass','Weight'],[
        ['Definition','Quantity of matter','Gravitational force on mass'],
        ['Type','Scalar — fundamental','Vector — derived'],
        ['SI Unit','kilogram (kg)','newton (N)'],
        ['Variation','<b>Constant everywhere</b>','Changes with gravity g'],
        ['On Moon','Same as Earth','<b>1/6 of Earth weight</b>'],
        ['In space','Same','<b>Zero (weightlessness)</b>'],
        ['Formula','—','W = m × g  (g = 9.8 m/s²)'],
        ['Instrument','Beam / electronic balance','Spring balance'],
    ], cw=[FW*0.20,FW*0.36,FW*0.44]))

    # 7
    f(section('7','Time and Clocks'))
    c(p('<b>Time</b> = duration between two events. SI unit: <b>second (s)</b>. '
        '1 hr = 3600 s. 1 day = 86,400 s. 1 year (non-leap) = <b>3.153 × 10<super>7</super> s</b>.'))
    f(tbl(['Ancient Device','Working Principle'],[
        ['Sundial','Shadow of vertical stick (gnomon) shows time.'],
        ['Sand clock (hourglass)','Sand falls through small hole at constant rate.'],
        ['Water clock (Clepsydra)','Steady water flow marks time intervals.'],
    ], cw=[FW*0.30,FW*0.70]))
    c(p('<b>(1) Analog clock</b> — 3 hands: hour (short thick), minute (long thin, '
        '1 rotation/60 min), second (thinnest, 60 rotations/hr).  '
        '<b>(2) Digital clock</b> — time in numerals; "electronic clock".'))
    f(tbl(['Type','Working Principle','Accuracy','Used In'],[
        ['Pendulum','Oscillation of a pendulum','Low','Old wall clocks'],
        ['Quartz','Vibration of <b>quartz crystal (SiO<sub>2</sub>)</b>; ~32,768 Hz',
         '<b>1 s in 10<super>9</super> s</b>','Watches, GPS, computers'],
        ['Atomic','Periodic vibrations of <b>caesium-133 atom</b>',
         '<b>1 s in 10<super>1</super>³ s</b>','GPS, GLONASS, Intl. Time Distribution'],
    ], cw=[FW*0.14,FW*0.44,FW*0.16,FW*0.26]))
    f(fact('<b>GMT</b> = Greenwich Mean Time — Royal Observatory, Greenwich, London (0° lon). '
           'Earth: <b>24 time zones</b>, each <b>15° wide</b>, adjacent zones differ by <b>1 hr</b>.'))
    f(fact('<b>IST = GMT + 5:30 hours</b>. Based on <b>82.5°E</b> through '
           '<b>Mirzapur, Uttar Pradesh</b>.'))

    # 8
    f(section('8','Temperature'))
    c(p('<b>Temperature</b> = degree of hotness/coldness = measure of '
        '<b>average kinetic energy of particles</b>. '
        'SI unit: <b>kelvin (K)</b>. Instrument: <b>Thermometer</b>.'))
    f(tbl(['Scale','Symbol','Freezing of water','Boiling of water'],[
        ['Celsius','°C','0 °C','100 °C'],
        ['Fahrenheit','°F','32 °F','212 °F'],
        ['Kelvin','K','273 K (273.15)','373 K (373.15)'],
        ['Rankine','°R','491.67 °R','671.67 °R'],
    ], cw=[FW*0.20,FW*0.14,FW*0.33,FW*0.33]))
    f(fact('<b>Conversions:</b> K = °C + 273  |  '
           '°C = (°F − 32) × 5/9  |  °F = (°C × 9/5) + 32'))
    f(fact('<b>Absolute zero</b> = 0 K = −273.15 °C. '
           '<b>Normal body temp</b> = 37 °C = 98.6 °F = 310 K.'))

    # 9-11
    f(section('9','Electric Current'))
    c(p('<b>Electric current (I)</b> = flow of charges per unit time. '
        'SI unit: <b>ampere (A)</b>. Instrument: <b>Ammeter</b>.'))
    f(fact('<b>I = Q / t</b>. Charge unit = <b>coulomb (C)</b>. '
           '<b>1 A = 1 coulomb per second</b>.'))

    f(section('10','Amount of Substance'))
    c(p('Number of entities (atoms, molecules, ions, electrons, protons). '
        'SI unit: <b>mole (mol)</b>.'))
    f(fact('<b>1 mole = 6.023 × 10<super>2</super>³ entities</b> = <b>Avogadro Number (N<sub>A</sub>)</b>.'))

    f(section('11','Luminous Intensity'))
    c(p('Power of light per unit solid angle in a direction. '
        'SI unit: <b>candela (cd)</b>. Instrument: <b>Photometer</b>.'))
    f(fact('1 common <b>wax candle ≈ 1 candela</b>. '
           'Luminous flux unit = <b>lumen (lm)</b>. '
           '<b>1 lm = 1 cd × 1 sr</b>.'))

    # 12
    f(section('12','Area, Volume and Density'))
    f(subsec('12.1','Area Formulas (SI unit: m²)'))
    f(tbl(['Shape','Formula','Shape','Formula'],[
        ['Square','A = a²','Triangle','A = ½ × b × h'],
        ['Rectangle','A = l × b','Circle','A = π r²  (π=22/7)'],
        ['Parallelogram','A = b × h','Trapezium','A = ½(a+b) × h'],
    ], cw=[FW*0.20,FW*0.30,FW*0.20,FW*0.30]))
    f(fact('<b>Irregular shapes (graph sheet):</b> M=full squares, N=more-than-half, '
           'P=exactly half, Q=less-than-half → <b>Area ≈ M + ¾N + ½P + ¼Q</b> cm²'))

    f(subsec('12.2','Volume Formulas (SI unit: m³)'))
    f(tbl(['Solid','Formula','Solid','Formula'],[
        ['Cube','V = a³','Sphere','V = (4/3) π r³'],
        ['Cuboid','V = l × b × h','Cylinder','V = π r² h'],
        ['Cone','V = (1/3) π r²h','Hemisphere','V = (2/3) π r³'],
    ], cw=[FW*0.18,FW*0.32,FW*0.18,FW*0.32]))
    c(p('<b>Irregular solid (stone) — displacement method:</b> V₁ = water level before, '
        'V₂ = after immersion → <b>Volume = V₂ − V₁</b>. (Archimedes\' principle.)'))

    f(subsec('12.3','Density'))
    f(fact('<b>D = M/V  |  M = D×V  |  V = M/D</b>. '
           'SI unit: <b>kg/m³</b>. CGS: g/cm³. <b>1 g/cm³ = 1000 kg/m³</b>.'))
    f(fact('<b>Float/Sink:</b> D(obj) &lt; D(fluid) → floats. '
           'Iron (7800) sinks in water (1000) but floats in mercury (13600)!'))
    f(tbl(['Material','Density','Material','Density','Material','Density'],[
        ['Air','1.2','Wood','770','Iron','7,800'],
        ['Kerosene','800','Water','1,000','Copper','8,900'],
        ['Castor oil','961','Aluminium','2,700','Silver','10,500'],
        ['Petrol','720','Glass','2,500','Gold','19,300'],
        ['Ice','917','Brick','1,800','Mercury','13,600'],
        ['Milk','1,030','Diamond','3,510','Platinum','21,400'],
    ], cw=[FW/6]*6, fs=8))

    # 13
    f(section('13','Measuring Very Long Distances'))
    f(fact('<b>1 AU = avg Earth–Sun distance = 149.6 million km = 1.496 × 10<super>1</super>¹ m</b>. '
           'Perihelion: 147.1 Mkm. Aphelion: 152.1 Mkm. Neptune ≈ 30 AU.'))
    f(fact('<b>1 light year = 9.46 × 10<super>1</super>⁵ m</b>. '
           'c = 3×10<super>8</super> m/s. 1 year = 3.153×10<super>7</super> s.'))
    f(tbl(['Stellar Object','Distance'],[
        ['Proxima Centauri (nearest star)','4.22 light years (= 2,68,770 AU)'],
        ['Sirius (brightest in night sky)','8.6 light years'],
        ['Centre of Milky Way galaxy','≈ 25,000 light years'],
        ['Andromeda Galaxy (M31)','≈ 2.5 million light years'],
    ], cw=[FW*0.54,FW*0.46]))
    f(tbl(['Unit','Equivalent','Used For'],[
        ['Parsec (pc)','3.26 light years','Astronomy (star distances)'],
        ['Nautical mile','1.852 km','Aviation, sea transport'],
        ['Knot','1 nautical mile/hr','Speed of ships, planes'],
        ['Angstrom (Å)','10<super>-1</super>⁰ m','Atomic / molecular sizes'],
        ['Fermi (fm)','10<super>-1</super>⁵ m','Nuclear sizes'],
    ], cw=[FW*0.22,FW*0.28,FW*0.50]))

    # 14
    f(section('14','Accuracy, Precision, Error & Approximation'))
    f(tbl(['Term','Definition'],[
        ['<b>Accuracy</b>','Closeness of measured value to the <b>true (actual)</b> value.'],
        ['<b>Precision</b>','Closeness of <b>two or more</b> measurements to each other.'],
        ['<b>Error</b>','Difference between true and measured value.'],
        ['<b>Approximation</b>','Estimating to a nearby simpler number for calculation.'],
        ['<b>Rounding off</b>','Reducing digits while keeping the value close to original.'],
        ['<b>Calibration</b>','Configuring instrument for correct readings within a range.'],
    ], cw=[FW*0.22,FW*0.78]))
    c(p('<b>Rounding rules:</b> (1) Next digit &lt;5 → drop. '
        '(2) Next digit &gt;5 → round up. '
        '(3) Next digit =5 → round to nearest <b>even</b> (banker\'s rule).'))

    # 15
    f(section('15','Solved Numerical Problems'))
    f(prob_tbl([
        ('Convert 7875 cm to metres.','7875 ÷ 100 = <b>78.75 m</b>'),
        ('Convert 60° to radian.','(π×60)/180 = <b>π/3 rad</b>'),
        ('Convert π/4 rad to degrees.','180/4 = <b>45°</b>'),
        ('Area of rectangle: l=12m, b=4m.','A = 12×4 = <b>48 m²</b>'),
        ('Area of circle: r=7m. (π=22/7)','A = (22/7)×49 = <b>154 m²</b>'),
        ('Volume of cube: a=3cm.','V = 3³ = <b>27 cm³</b>'),
        ('Volume of cylinder: r=3m, h=7m.','V = (22/7)×9×7 = <b>198 m³</b>'),
        ('Density: m=280 kg, V=4 m³.','D = 280/4 = <b>70 kg/m³</b>'),
        ('Mass: V=125 cm³, D=7.8 g/cm³.','m = 7.8×125 = <b>975 g</b>'),
        ('Volume of copper sphere: m=3000 kg, D=8900 kg/m³.','V = 3000/8900 ≈ <b>0.34 m³</b>'),
        ('Current: Q=2 C, t=10 s.','I = 2/10 = <b>0.2 A</b>'),
        ('Convert 100°C to Kelvin.','K = 100+273 = <b>373 K</b>'),
        ('Convert 98.6°F to °C.','°C = (98.6−32)×5/9 = <b>37°C</b>'),
    ]))

    # 16
    f(section('16','Key Facts — Rapid Revision'))
    f(tbl(['Value','Quantity'],[
        ['6.023 × 10<super>2</super>³','Avogadro number (entities in 1 mole)'],
        ['1.496 × 10<super>1</super>¹ m','1 Astronomical Unit (AU) — Earth–Sun distance'],
        ['9.46 × 10<super>1</super>⁵ m','1 Light year'],
        ['3 × 10<super>8</super> m/s','Speed of light in vacuum'],
        ['3.153 × 10<super>7</super> s','Seconds in 1 year'],
        ['9.8 m/s²','Acceleration due to gravity (g) on Earth'],
        ['1.852 km','1 nautical mile'],
        ['32,768 Hz','Quartz crystal vibration frequency'],
        ['76 cm of Hg','Standard atmospheric pressure (sea level)'],
        ['1.01 × 10<super>⁵</super> N/m²','1 atmosphere (atm)'],
        ['10<super>9</super> s','Quartz clock accuracy (1 sec error per...)'],
        ['10<super>1</super>³ s','Atomic clock accuracy (1 sec error per...)'],
        ['82.5° E','Indian Standard Meridian longitude'],
        ['IST = GMT + 5:30','Indian Standard Time offset'],
        ['15°','Width of one time zone'],
        ['24','Number of time zones on Earth'],
        ['4.22 ly','Distance to Proxima Centauri (nearest star)'],
        ['25,000 ly','Distance to centre of Milky Way galaxy'],
    ], cw=[FW*0.30,FW*0.70]))
    f(tbl(['Year / Period','Event'],[
        ['16th century','<b>William Bedwell</b> invented the ruler / scale'],
        ['1790','<b>Metric system</b> created by the French'],
        ['1889','Standard kg (Pt-Ir alloy) placed at Sèvres, France'],
        ['1960','<b>SI System</b> adopted — 11th GCWM, Paris, France'],
        ['1995','Plane & solid angle reclassified: supplementary → derived'],
        ['Dec 1998','NASA Mars Climate Orbiter launched'],
        ['Sep 23, 1999','Mars Orbiter lost — FPS vs MKS unit error — $125M loss'],
    ], cw=[FW*0.22,FW*0.78]))
    f(tbl(['Name / Place','Significance'],[
        ['<b>William Bedwell</b>','Invented ruler / scale (16th century)'],
        ['<b>Avogadro</b>','6.023 × 10<super>2</super>³ named after him'],
        ['<b>Sèvres, France</b>','Bureau of Weights & Measures (Std. kg, Std. m)'],
        ['<b>Paris, France</b>','11th GCWM 1960 — SI system adopted'],
        ['<b>Greenwich, London</b>','Royal Observatory — GMT origin (0° longitude)'],
        ['<b>Mirzapur, Uttar Pradesh</b>','On 82.5°E — defines Indian Standard Time'],
        ['<b>NPL, Delhi</b>','National Physical Laboratory — India copy of Std. metre'],
        ['<b>Caesium-133</b>','Atom whose vibrations define atomic clocks'],
        ['<b>Pt-Ir alloy</b>','Material of standard metre rod & kilogram'],
        ['<b>SiO<sub>2</sub> (Quartz)</b>','Crystal in modern clocks; vibrates at ~32,768 Hz'],
    ], cw=[FW*0.30,FW*0.70]))

    # 17
    f(section('17','Glossary — Key Terms'))
    f(gloss([
        ('Accuracy','Closeness of measured value to the true value.'),
        ('Ammeter','Measures electric current. Unit: ampere (A).'),
        ('Amount of substance','Number of entities in substance. Unit: mole.'),
        ('Approximation','Estimating to a nearby simpler number.'),
        ('AU','Avg. Earth–Sun distance ≈ 1.496 × 10<super>1</super>¹ m.'),
        ('Avogadro number','6.023 × 10<super>2</super>³ entities per mole.'),
        ('Beam balance','Compares unknown mass with standard mass.'),
        ('Calibration','Configuring instrument for correct readings.'),
        ('Candela (cd)','SI unit of luminous intensity.'),
        ('Density','Mass per unit volume. SI: kg/m³.'),
        ('Derived quantity','Obtained by combining fundamentals.'),
        ('Electric current','Flow of charges per unit time. Unit: A.'),
        ('Error','True value minus measured value.'),
        ('Fundamental qty','Cannot be expressed via others. 7 in SI.'),
        ('GMT','Greenwich Mean Time — 0° longitude, London.'),
        ('GPS','Global Positioning System — uses atomic clocks.'),
        ('IST','Indian Standard Time = GMT + 5:30 (82.5°E).'),
        ('Kelvin (K)','SI temp unit. 0 K = −273°C = absolute zero.'),
        ('Knot','1 nautical mile/hr. Ships & planes speed.'),
        ('Light year','Distance light travels in 1 yr ≈ 9.46×10<super>1</super>⁵m.'),
        ('Luminous intensity','Light power per unit solid angle. Unit: cd.'),
        ('Magnitude','Numerical value part of a measurement.'),
        ('Mass','Quantity of matter. Constant. Unit: kg.'),
        ('Measurement','Comparison of unknown with known standard.'),
        ('Mole (mol)','SI unit = 6.023 × 10<super>2</super>³ entities.'),
        ('Nautical mile','1.852 km — aviation & sea transport.'),
        ('Parallax error','Wrong reading from oblique eye position.'),
        ('Photometer','Measures luminous intensity.'),
        ('Plane angle','At 2 line/plane intersection. Unit: radian.'),
        ('Precision','Closeness of multiple readings to each other.'),
        ('Quartz crystal','SiO<sub>2</sub> — used in modern clocks at ~32,768 Hz.'),
        ('Radian (rad)','SI plane angle. 2π rad = 360°.'),
        ('Rounding off','Reducing digits while keeping value close.'),
        ('SI Units','Système Internat. d\'Unités — 1960, Paris.'),
        ('Solid angle','At cone vertex / 3+ planes. Unit: steradian.'),
        ('Steradian (sr)','SI solid angle. 4π sr = full sphere.'),
        ('Sundial','Ancient device — shadow of stick shows time.'),
        ('Temperature','Avg. KE of particles. SI unit: kelvin.'),
        ('Time zone','15°-wide zone; 24 on Earth; 1 hr apart.'),
        ('Vernier calipers','Precision length; least count 0.1 mm.'),
        ('Volume','Space occupied by 3D object. SI: m³.'),
        ('Weight','Gravitational force on mass. Unit: newton.'),
        ('Zero error','Error from misaligned starting mark.'),
    ]))

    return items

# ── BUILD ─────────────────────────────────────────────────────────────────────
def build(out='output/P1_Measurement_A4.pdf'):
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)

    # 3 frame layout per page:
    # frame_full  = full-width (for tables, headings, fact boxes)
    # frame_left  = left column (for body text)
    # frame_right = right column (for body text)
    # Strategy: We alternate between a single-frame and two-frame page template
    # But simpler: use ONE wide frame with a 2-column Table for body text pairs,
    # and keep tables/headings as normal full-width elements.

    # SIMPLEST correct approach for ReportLab:
    # Use a SINGLE full-width frame, but lay out body paragraphs in 2-col table
    # when we have pairs. For now: single-frame, everything works cleanly.
    # Two-col body text via paired Table.

    story = []
    body_buf = []  # collect body 'C' items to pair into 2-col

    def flush_body():
        if not body_buf:
            return
        # Pair paragraphs into a 2-column table
        rows = []
        i = 0
        while i < len(body_buf):
            left = body_buf[i]
            right = body_buf[i+1] if i+1 < len(body_buf) else Paragraph('', ST['body'])
            rows.append([left, right])
            i += 2
        t = Table(rows, colWidths=[CW, CW], spaceBefore=0, spaceAfter=2)
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),0),
            ('RIGHTPADDING',(0,0),(-1,-1),0),
            ('TOPPADDING',(0,0),(-1,-1),0),
            ('BOTTOMPADDING',(0,0),(-1,-1),0),
            ('LEFTPADDING',(0,0),(0,-1),0),
            ('RIGHTPADDING',(0,0),(0,-1),3),  # gap between cols
        ]))
        story.append(t)
        body_buf.clear()

    for zone, item in content():
        if zone == 'C':
            body_buf.append(item)
        else:  # 'F' = full-width
            flush_body()
            story.append(item)

    flush_body()

    # Single-frame page template (full width)
    frame = Frame(ML, MB, FW, PH-MT-MB,
                  leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0, id='main')
    pt = PageTemplate(id='main', frames=[frame], onPage=chrome)

    doc = BaseDocTemplate(
        out,
        pagesize=A4,
        leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
        title='TET Handbook — P1: Measurement',
        author='ChalkPieceDiary',
    )
    doc.addPageTemplates([pt])
    doc.build(story)
    print(f'✅  {out}  ({os.path.getsize(out)/1024:.1f} KB)')

if __name__ == '__main__':
    build()
