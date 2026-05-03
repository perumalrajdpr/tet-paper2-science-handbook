"""
TET Paper II Science Handbook — P7: Sound
Style: P3 one-liner cheat-sheet | Font: 10.5pt body, 10pt cells
All sub-topics: Class 8 (Unit 6) — Production, Propagation, Waves,
Properties, Musical Instruments, Human Voice, Human Ear, Noise Pollution
+ Standard TN syllabus topics: Echo, Reverberation, SONAR
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

CHAPTER_ID = "P7"
CHAPTER_TITLE = "Sound"
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
    s += [banner('P7','Sound','Physics | Classes 6, 7 & 8 Combined'), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # A  PRODUCTION OF SOUND
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('A  ·  PRODUCTION OF SOUND'), sp(2)]

    s += [kv_list([
        ('Sound',            'A form of energy produced by vibrating objects — needs a MEDIUM to travel'),
        ('Vibration',        'Rapid to and fro motion of a particle about its mean position — also called oscillation'),
        ('Medium',           'Substance through which sound travels from the source to the listener'),
        ('Production',       'Sound is produced when an object is SET TO VIBRATE — stops when vibration stops'),
    ], bg_L=TEAL, bg_R=TEAL_L), sp(2)]

    s += [one_liners([
        'Plucked rubber band vibrates → humming sound | stops vibrating → sound stops',
        'Struck metal pan vibrates → sound produced; holding the pan stops vibration → sound stops',
        'Stringed instruments (guitar, sitar, veena): vibrating strings produce sound',
        'Percussion instruments (drum, tabla): striking membrane produces vibration and sound',
        'Sound waves travel outward from the vibrating source in ALL directions through the medium',
        'Thomas Alva Edison invented the phonograph in 1877 — first device to record and play back sound',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # B  PROPAGATION OF SOUND
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('B  ·  PROPAGATION OF SOUND — Medium, Speed & Wave Nature'), sp(2)]

    s += [kv_list([
        ('Sound needs medium',    'Sound CANNOT travel in vacuum — it needs a material medium (solid, liquid, gas)'),
        ('Speed in solids',       'Maximum — e.g., Aluminium = 6420 m/s, Steel = 5960 m/s, Iron = 5950 m/s'),
        ('Speed in liquids',      'Medium — Sea water = 1530 m/s, Distilled water = 1498 m/s'),
        ('Speed in gases',        'Minimum — Air ≈ 330–344 m/s (at 0°C: 331 m/s; at 22°C: 344 m/s)'),
        ('Speed order',           'Solid > Liquid > Gas (Sound travels fastest in solids)'),
        ('Effect of temperature', 'Speed of sound INCREASES with increase in temperature'),
        ('Effect of humidity',    'Speed of sound INCREASES with increase in humidity (density of air decreases)'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=48*mm), sp(2)]

    s += [sub_h('Speed of Sound in Various Media at 25°C'), sp(1)]
    s += [grid(
        ['State','Substance','Speed (m/s)'],
        [
            ['Solid', 'Aluminium', '6420'],
            ['Solid', 'Steel',     '5960'],
            ['Solid', 'Iron',      '5950'],
            ['Liquid','Sea Water', '1530'],
            ['Liquid','Distilled Water','1498'],
            ['Gas',   'Hydrogen',  '1284'],
            ['Gas',   'Air (at 25°C)','346'],
            ['Gas',   'Oxygen',    '316'],
        ],
        ws=[24*mm,60*mm,90*mm]
    ), sp(2)]

    s += [one_liners([
        'Sound CANNOT travel in vacuum — bell jar experiment proves: as air is pumped out, sound fades',
        'On the Moon there is no atmosphere — two astronauts cannot talk to each other directly (radio waves used)',
        'Light travels much faster than sound — that is why lightning is seen before thunder is heard',
        'Astronauts: helmet devices convert sound waves to radio waves for communication',
        'Compression (C): region of HIGH pressure when tuning fork moves forward',
        'Rarefaction (R): region of LOW pressure when tuning fork moves backward',
        'Sound propagates as a series of compressions and rarefactions through the medium',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # C  SOUND WAVES — Types
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('C  ·  SOUND WAVES — Wave Nature & Types of Mechanical Waves'), sp(2)]

    s += [kv_list([
        ('Mechanical Wave',  'Disturbance that propagates through a medium due to repeated periodic motion of particles'),
        ('Wave motion',      'Only ENERGY is transferred — NOT the particles of medium'),
        ('Wavelength (λ)',   'Distance between two consecutive particles in same phase of vibration — unit: metre (m)'),
        ('Frequency (n)',    'Number of vibrations of a particle in one second — unit: Hertz (Hz)'),
        ('Amplitude (A)',    'Maximum displacement of a vibrating particle from its mean position — unit: metre (m)'),
        ('Time Period (T)',  'Time taken by a vibrating particle to complete ONE vibration — unit: second (s)'),
        ('Speed formula',   'v = n × λ  (Speed = Frequency × Wavelength)'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=48*mm), sp(2)]

    s += [fstrip('Speed of Sound', 'v = n × λ', 'v = speed (m/s), n = frequency (Hz), λ = wavelength (m)', TEAL_D)]
    s += [sp(2)]

    s += [sub_h('Types of Mechanical Waves — Transverse vs Longitudinal'), sp(1)]
    s += [grid(
        ['Type','Particle Movement','Direction vs Wave','Medium','Examples'],
        [
            ['Transverse Wave',
             'Vibrates PERPENDICULAR to direction of wave propagation',
             'Perpendicular (90°)',
             'Solids and Liquids ONLY (not gases)',
             'Light waves, waves in strings, surface water waves'],
            ['Longitudinal Wave',
             'Vibrates PARALLEL to direction of wave propagation',
             'Parallel (same)',
             'Solids, Liquids AND Gases',
             'SOUND waves, waves in springs, seismic P-waves'],
        ],
        ws=[30*mm,48*mm,26*mm,32*mm,38*mm]
    ), sp(2)]

    s += [pill('📌', 'Sound waves are LONGITUDINAL waves — particles vibrate parallel to wave direction. Sound cannot be transverse.', CYAN_L, CYAN)]
    s += [sp(2)]

    s += [one_liners([
        'Seismic wave: formed during earthquake — longitudinal wave travelling through Earth\'s layers',
        'Seismology: branch of science that studies seismic waves using seismometer',
        'Hydrophone: instrument to detect sound/seismic waves underwater',
        'In wave motion, the velocity of wave is DIFFERENT from velocity of vibrating particle',
        'Medium must have: inertia, elasticity, uniform density and minimum friction — for mechanical wave propagation',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # D  PROPERTIES OF SOUND
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('D  ·  PROPERTIES OF SOUND — Loudness, Pitch, Quality, Audibility'), sp(2)]

    s += [grid(
        ['Property','Definition','Depends On','Examples'],
        [
            ['Loudness',
             'Characteristic that distinguishes a faint (weak) sound from a loud sound',
             'AMPLITUDE — Higher amplitude → Louder sound | Unit: decibel (dB)',
             'Softly beaten drum = weak sound | Strongly beaten drum = loud sound'],
            ['Pitch',
             'Characteristic that distinguishes a flat (low) sound from a shrill (high) sound',
             'FREQUENCY — Higher frequency → Higher pitch (shriller sound)',
             'Whistle, bell, flute, violin = high pitch | Lion\'s roar, drum beat = low pitch'],
            ['Quality\n(Timbre)',
             'Characteristic that distinguishes two sounds of same pitch and amplitude',
             'Waveform / overtones present in the sound',
             'Sounds of guitar vs violin at same pitch still sound different — due to timbre'],
        ],
        ws=[24*mm,52*mm,48*mm,50*mm]
    ), sp(2)]

    s += [one_liners([
        'Female voice has HIGHER PITCH than male voice — females have thinner, shorter vocal cords',
        'Male voice has LOWER PITCH — males have thicker, longer vocal cords → deeper sound',
        'Orchestra: different instruments produce sounds of same pitch but different timbre → identifiable',
        'Amplitude doubled → loudness does NOT double — relationship is logarithmic',
        'Amplitude quadrupled → loudness approximately doubles (in terms of decibels)',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # E  FREQUENCY RANGES — Audible, Infrasonic, Ultrasonic
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('E  ·  FREQUENCY RANGES — Audible, Infrasonic & Ultrasonic Sound'), sp(2)]

    s += [grid(
        ['Type','Frequency Range','Heard By','Uses / Applications'],
        [
            ['Infrasonic\n(Subsonic)',
             'Below 20 Hz',
             'NOT audible to humans | Dogs, dolphins, elephants, whales can sense',
             '• Earth monitoring / seismic study\n• Study of heart mechanism\n• Elephants communicate over long distances'],
            ['Sonic\n(Audible)',
             '20 Hz to 20,000 Hz (20 kHz)',
             'Human beings — the normal hearing range',
             '• All normal communication and music\n• Audible range called "sonic range"'],
            ['Ultrasonic\n(Supersonic)',
             'Above 20,000 Hz (20 kHz)',
             'NOT audible to humans | Bats, dogs, dolphins can hear',
             '• Medical: sonogram/ultrasound scan\n• SONAR (detect submarines, sea depth)\n• Galton\'s whistle (dog training)\n• Dish washers\n• ECHOLOCATION in bats'],
        ],
        ws=[24*mm,30*mm,40*mm,80*mm]
    ), sp(2)]

    s += [pill('🔑', 'Human Audible Range: 20 Hz to 20,000 Hz. Below 20 Hz = Infrasonic. Above 20,000 Hz = Ultrasonic.', TEAL_L, TEAL_D)]
    s += [sp(2)]

    s += [one_liners([
        'Bat echolocation: bats produce ultrasonic sound (>20,000 Hz) → reflects from objects → bat detects prey and navigates in dark',
        'Galton\'s whistle: produces ultrasonic sound — inaudible to humans but heard by dogs — used for dog training',
        'Sonogram: ultrasound imaging of internal organs (foetus, liver, kidney) — non-invasive medical diagnosis',
        'Infrasound: produced naturally by earthquakes, volcanoes, ocean waves, heavy winds, tornadoes',
        'Dolphins use echolocation (ultrasound) to navigate and communicate underwater',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # F  ECHO, REVERBERATION & SONAR
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('F  ·  ECHO, REVERBERATION & SONAR'), sp(2)]

    s += [kv_list([
        ('Reflection of Sound', 'Sound bounces back when it hits a hard, large surface — follows same laws as reflection of light'),
        ('Echo',                'Reflected sound heard SEPARATELY after original sound — minimum distance from wall = 17.2 m (approx. 17 m)'),
        ('Minimum Echo Distance','Speed of sound = 344 m/s | Ear needs 0.1 s to detect echo separately | Distance = 344 × 0.1 / 2 = 17.2 m'),
        ('Reverberation',       'Persistence of sound due to MULTIPLE reflections — sound continues after source stops; heard in closed halls'),
        ('Reverb vs Echo',      'Echo: single distinct reflection heard separately | Reverberation: multiple rapid reflections blending together'),
    ], bg_L=TEAL_D, bg_R=TEAL_L, w_L=52*mm), sp(2)]

    s += [sub_h('Applications of Reflection of Sound'), sp(1)]
    s += [one_liners([
        ('Megaphone / Loudspeaker','Funnel-shaped; reflects sound waves and channels them forward — prevents spreading in all directions'),
        ('Concert Halls / Auditoriums','Ceiling and walls curved to uniformly distribute reflected sound; absorbing materials reduce reverberation'),
        ('Stethoscope',         'Uses multiple reflections inside tube to carry heart/lung sound to doctor\'s ear'),
        ('Sound boards',        'Curved boards placed behind speakers in auditoria to reflect sound toward audience'),
    ]), sp(2)]

    s += [sub_h('SONAR — Sound Navigation And Ranging'), sp(1)]
    s += [kv_list([
        ('SONAR',               'Sound Navigation And Ranging — uses ULTRASOUND to detect and locate objects underwater'),
        ('Principle',           'Ultrasound pulses sent from ship → reflect from sea floor / submarine / fish → received back → time calculated'),
        ('Formula',             'd = v × t / 2  (d = depth, v = speed of sound in water, t = time for echo to return)'),
        ('Uses',                '(1) Measure depth of sea  (2) Detect submarines  (3) Detect icebergs  (4) Locate fish shoals  (5) Survey sea floor'),
        ('Speed in seawater',   '≈ 1530 m/s at 25°C'),
    ], bg_L=BLUE_D, bg_R=BLUE_L, w_L=44*mm), sp(2)]

    s += [fstrip('SONAR Depth Formula', 'd = (v × t) / 2', 'd = depth (m), v = speed in water (m/s), t = total time for echo (s)', BLUE_D)]
    s += [sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # G  MUSICAL INSTRUMENTS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('G  ·  MUSICAL INSTRUMENTS — Four Types'), sp(2)]

    s += [pill('🔑', 'Music = sound produced by REGULAR, PERIODIC vibrations | Noise = sound produced by IRREGULAR, NON-PERIODIC vibrations', TEAL_L, TEAL_D)]
    s += [sp(2)]

    s += [grid(
        ['Type','How Sound Produced','Frequency Control','Examples'],
        [
            ['Wind Instruments',
             'Vibration of air column in a hollow tube',
             'Changing the LENGTH of vibrating air column',
             'Trumpet, Flute, Shehnai, Saxophone, Nadaswaram'],
            ['Reed Instruments',
             'Reed vibrates when air is blown through — reed vibration produces specific sound',
             'Varying air pressure and reed position',
             'Harmonium, Mouth Organ (Harmonica)'],
            ['Stringed Instruments',
             'Vibration of stretched string/wire — hollow box amplifies the sound produced',
             'Varying length, tension and thickness of string',
             'Violin, Guitar, Sitar, Veena, Harp'],
            ['Percussion Instruments',
             'Struck, scraped or clashed together — oldest type of musical instrument',
             'Tension of stretched membrane / size of resonator',
             'Drum, Tabla, Mridangam, Cymbals, Xylophone'],
        ],
        ws=[28*mm,52*mm,42*mm,52*mm]
    ), sp(2)]

    s += [one_liners([
        'Guitar/Violin strings have natural frequencies called HARMONICS — depends on tension, linear density and length of string',
        'Percussion: drum/tabla has leather membrane stretched across hollow box called RESONATOR',
        'Harmonics: natural frequencies at which a string vibrates — multiple of fundamental frequency',
        'Keyboard (piano) = stringed instrument (hammers strike strings) — not percussion',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # H  HUMAN VOICE & HUMAN EAR
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('H  ·  HUMAN VOICE & HUMAN EAR — Structure & Function'), sp(2)]

    s += [sub_h('Human Voice — Production of Sound by Humans'), sp(1)]
    s += [kv_list([
        ('Voice Box (Larynx)',   'Organ of voice — located in throat at upper end of windpipe (trachea)'),
        ('Vocal Cords',         'Two ligaments stretched across the larynx — vibrate when air passes through them'),
        ('Narrow Slit',         'Gap between the vocal cords through which air from lungs is forced'),
        ('How voice is produced','Air from lungs → pushed through trachea → passes through slit between vocal cords → vocal cords vibrate → sound'),
        ('Pitch control',       'Varying THICKNESS of vocal cords changes the length of air column in slit → different pitches'),
        ('Male voice lower',    'Males have THICKER and LONGER vocal cords → lower, deeper pitch than females'),
        ('Female voice higher', 'Females have THINNER and SHORTER vocal cords → higher, shriller pitch'),
    ], bg_L=TEAL, bg_R=TEAL_L, w_L=46*mm), sp(2)]

    s += [sub_h('Human Ear — Structure & Function'), sp(1)]
    s += [grid(
        ['Part','Location','Function'],
        [
            ['Pinna',        'Outer ear — visible curved structure',
             'Collects sound waves from environment and directs them into the ear canal'],
            ['Ear Canal (Auditory Canal)',
             'Connects pinna to eardrum',
             'Conducts sound waves from pinna to the tympanic membrane'],
            ['Eardrum (Tympanic Membrane)',
             'Between outer and middle ear',
             'Vibrates when sound waves strike it — converts sound waves to mechanical vibrations'],
            ['Ossicles',
             'Three tiny bones in middle ear: Malleus, Incus, Stapes',
             'Amplify and transmit vibrations from eardrum to inner ear — move inward and outward'],
            ['Cochlea',
             'Inner ear — spiral/snail-shaped fluid-filled structure',
             'Contains special sensory cells that convert mechanical vibrations to nerve signals'],
            ['Eustachian Tube',
             'Connects middle ear to throat',
             'Equalises air pressure on both sides of eardrum'],
            ['Auditory Nerve',
             'Connects inner ear to brain',
             'Transmits nerve signals from cochlea to brain for interpretation as sound'],
            ['Semicircular Canals',
             'Inner ear',
             'Responsible for balance and equilibrium (not directly for hearing)'],
        ],
        ws=[32*mm,44*mm,98*mm]
    ), sp(2)]

    s += [one_liners([
        'Sound wave → Pinna → Ear Canal → Eardrum (vibrates) → Ossicles (amplify) → Cochlea (converts to signals) → Auditory Nerve → Brain',
        'Brain PERCEIVES these nerve signals as sound — hearing is a sensory process',
        'Aquatic animals\' ears designed to pick up high-frequency vibrations in WATER',
        'Ear ache, fullness/fluid in ear, ringing in ears = symptoms of hearing loss',
        'Causes of hearing loss: aging, ear infections (untreated), certain medicines, genetic disorders, severe blow to head, loud noise',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # I  NOISE POLLUTION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('I  ·  NOISE POLLUTION — Causes, Effects & Control'), sp(2)]

    s += [kv_list([
        ('Noise',          'Any UNPLEASANT, unwanted, irritating and loud sound — produced by IRREGULAR and NON-PERIODIC vibrations'),
        ('Noise Pollution', 'Disturbance in the environment due to loud and harsh sounds from various sources'),
        ('Major source',   'INDUSTRIES — noise pollution is a by-product of industrialisation, urbanisation and modern civilisation'),
    ], bg_L=RED, bg_R=RED_L, w_L=44*mm), sp(2)]

    s += [sub_h('Causes of Noise Pollution'), sp(1)]
    s += [one_liners([
        'Busy roads and vehicle horns — excessive honking is a major urban noise source',
        'Airplanes and airports — jet engine noise',
        'Electrical appliances at home — mixer grinder, washing machine, un-tuned radio',
        'Loudspeakers during festivals, religious and political events',
        'Crackers/fireworks during festivals',
        'Industrial machines — factories, construction sites',
    ]), sp(2)]

    s += [sub_h('Health Hazards of Noise Pollution'), sp(1)]
    s += [one_liners([
        'Irritation, stress, nervousness and headache',
        'Changes sleeping pattern — long term exposure disturbs sleep',
        'Sustained exposure → affects hearing ability → may lead to permanent hearing loss',
        'Sudden loud noise → heart attack and unconsciousness',
        'Lack of concentration in work — horns, loudspeakers cause disturbances',
        'Peace of mind disturbed → high blood pressure, short-tempered nature',
    ]), sp(2)]

    s += [sub_h('Measures to Control Noise Pollution'), sp(1)]
    s += [one_liners([
        'Strict guidelines for use of loudspeakers on social, religious and political occasions',
        'All automobiles should have effective silencers',
        'People should refrain from excessive honking while driving',
        'Industrial machines and home appliances should be properly maintained',
        'All communication systems operated in low volumes',
        'Residential areas should be free from heavy vehicles',
        'Green corridor belt set up around industries (as per Pollution Control Board regulations)',
        'People working in noisy factories should wear ear plugs',
        'Planting trees and using absorbing materials like curtains and cushions at home',
    ]), sp(3)]

    # ══════════════════════════════════════════════════════════════════════════
    # J  SOLVED PROBLEMS
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('J  ·  Solved Numerical Problems'), sp(2)]

    probs = [
        ('1', 'A sound has a frequency of 50 Hz and a wavelength of 10 m. What is the speed of sound?',
         'n = 50 Hz; λ = 10 m',
         'v = n × λ = 50 × 10 = 500 m/s',
         '500 m/s'),
        ('2', 'A sound has a frequency of 5 Hz and a speed of 25 m/s. Find the wavelength.',
         'n = 5 Hz; v = 25 m/s',
         'v = n × λ  →  λ = v/n = 25/5 = 5 m',
         'Wavelength = 5 m'),
        ('3', 'A wave with a frequency of 500 Hz is traveling at 200 m/s. Find the wavelength.',
         'n = 500 Hz; v = 200 m/s',
         'λ = v/n = 200/500 = 0.4 m',
         'Wavelength = 0.4 m'),
        ('4', 'A sound wave travels 2000 m in 8 seconds. What is its velocity?',
         'd = 2000 m; t = 8 s',
         'v = d/t = 2000/8 = 250 m/s',
         'Velocity = 250 m/s'),
        ('5', 'Ruthvik and Ruha hear a gunshot 2 seconds after it is fired. How far are they from the gun? (Speed of sound in air = 330 m/s)',
         't = 2 s; v = 330 m/s',
         'd = v × t = 330 × 2 = 660 m',
         'Distance = 660 m'),
        ('6', 'A SONAR sends ultrasound and receives the echo in 6 seconds. What is the depth of the sea? (Speed of sound in seawater = 1530 m/s)',
         'v = 1530 m/s; t = 6 s (total time for echo)',
         'd = v × t / 2 = 1530 × 6 / 2 = 9180 / 2 = 4590 m',
         'Depth of sea = 4590 m = 4.59 km'),
    ]

    for p in probs:
        s += [prob(*p), sp(2)]

    s += [sp(2)]

    # ══════════════════════════════════════════════════════════════════════════
    # K  KEY FACTS — RAPID REVISION
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('K  ·  Key Facts — Rapid Revision  (Numbers, Years & Names only)'), sp(2)]

    s += [P('<b>Formulas, Values & Key Numbers</b>', BDB), sp(1)]
    s += [rapid_nums([
        ['Speed of sound formula',    'v = n × λ  (frequency × wavelength)',           'm/s'],
        ['SONAR depth formula',       'd = v × t / 2',                                 'metres'],
        ['Speed in air at 0°C',       '331 m/s',                                       'Temperature dependent'],
        ['Speed in air at 22°C',      '344 m/s',                                       'Increases with temp'],
        ['Speed in aluminium',        '6420 m/s (fastest common medium)',               'Solid'],
        ['Speed in steel',            '5960 m/s',                                       'Solid'],
        ['Speed in sea water',        '1530 m/s',                                       'Liquid'],
        ['Speed in distilled water',  '1498 m/s',                                       'Liquid'],
        ['Speed in oxygen (gas)',     '316 m/s',                                        'Gas'],
        ['Audible range (humans)',    '20 Hz to 20,000 Hz (20 kHz)',                   'Sonic sound'],
        ['Infrasonic',                'Below 20 Hz',                                    'Subsonic'],
        ['Ultrasonic',                'Above 20,000 Hz',                               'Supersonic'],
        ['Minimum echo distance',     '≈ 17.2 m (from reflecting surface)',             'At 344 m/s, 0.1 s separation'],
        ['Loudness unit',             'Decibel (dB)',                                   'Amplitude dependent'],
        ['Wavelength unit',           'Metre (m)',                                      'λ (lambda)'],
        ['Frequency unit',            'Hertz (Hz) = vibrations per second',            'n'],
        ['Amplitude unit',            'Metre (m)',                                      'A'],
        ['Time period unit',          'Second (s)',                                     'T'],
    ]), sp(3)]

    s += [P('<b>Scientists, Discoveries & Years</b>', BDB), sp(1)]
    s += [rapid_ppl([
        ['Thomas Alva Edison',      'Invented phonograph (first device to record and play back sound)',              '1877'],
        ['Daniel Bernoulli',        'Studied harmonics of vibrating strings — natural frequencies',                  '18th century'],
        ['Francis Galton',          'Invented Galton\'s whistle — ultrasonic whistle for dog training',             '1876'],
        ['SONAR invention',         'Used during World War I to detect submarines underwater',                       '~1915-1918'],
        ['Speed of sound (air)',    'First accurate measurement by Pierre Gassendi and Marin Mersenne',              '1635-1636'],
        ['Eustachius',              'Eustachian tube named after Italian anatomist Bartolomeo Eustachi',             '16th century'],
    ]), sp(4)]

    # ══════════════════════════════════════════════════════════════════════════
    # L  GLOSSARY
    # ══════════════════════════════════════════════════════════════════════════
    s += [sec('L  ·  Glossary — Definitions'), sp(2)]

    g = [
        ('Sound',               'A form of energy produced by vibrating objects; needs a material medium to travel'),
        ('Vibration',           'Rapid to-and-fro (oscillatory) motion of a particle about its mean position'),
        ('Medium',              'Substance through which sound energy is transmitted from source to listener'),
        ('Compression (C)',     'Region of HIGH pressure in a sound wave — when vibrating body moves forward'),
        ('Rarefaction (R)',     'Region of LOW pressure in a sound wave — when vibrating body moves backward'),
        ('Mechanical Wave',     'Disturbance propagating through a medium due to periodic motion of particles'),
        ('Transverse Wave',     'Wave in which particles vibrate perpendicular to direction of wave propagation; in solids and liquids only'),
        ('Longitudinal Wave',   'Wave in which particles vibrate parallel to direction of propagation; sound is a longitudinal wave'),
        ('Wavelength (λ)',      'Distance between two consecutive particles in same phase of vibration; unit: metre'),
        ('Frequency (n)',       'Number of vibrations per second; unit: Hertz (Hz)'),
        ('Amplitude (A)',       'Maximum displacement of vibrating particle from mean position; unit: metre'),
        ('Time Period (T)',     'Time for one complete vibration; T = 1/n; unit: second'),
        ('Loudness',            'Property distinguishing weak from loud sound; depends on amplitude; unit: decibel (dB)'),
        ('Pitch',               'Property distinguishing flat from shrill sound; depends on frequency; higher freq = higher pitch'),
        ('Quality/Timbre',      'Property that distinguishes two sounds of same pitch and amplitude from different sources'),
        ('Audible Range',       '20 Hz to 20,000 Hz — frequency range audible to normal human ears'),
        ('Infrasonic Sound',    'Sound with frequency below 20 Hz — not audible to humans; detected by dogs, dolphins, elephants'),
        ('Ultrasonic Sound',    'Sound with frequency above 20,000 Hz — not audible to humans; used in SONAR, medical imaging'),
        ('Echo',                'Reflected sound heard distinctly after original sound; reflecting surface must be at least ~17 m away'),
        ('Reverberation',       'Persistence of sound due to multiple reflections in closed spaces; sound continues after source stops'),
        ('SONAR',               'Sound Navigation And Ranging — uses ultrasound to detect and measure distances underwater'),
        ('Echolocation',        'Navigation by sending ultrasound pulses and detecting echoes — used by bats and dolphins'),
        ('Wind Instrument',     'Musical instrument producing sound by vibrating air column in hollow tube — e.g., flute, trumpet'),
        ('Reed Instrument',     'Musical instrument with reed that vibrates when air is blown — e.g., harmonium, mouth organ'),
        ('Stringed Instrument', 'Musical instrument producing sound by vibrating string/wire — e.g., guitar, violin, sitar'),
        ('Percussion Instrument','Musical instrument producing sound when struck, scraped or clashed — e.g., drum, tabla'),
        ('Larynx',              'Voice box — organ in throat at upper end of windpipe; contains vocal cords'),
        ('Vocal Cords',         'Two ligaments in larynx that vibrate when air passes through them to produce voice'),
        ('Pinna',               'Outer visible curved part of ear that collects sound waves from environment'),
        ('Eardrum (Tympanic Membrane)','Thin membrane that vibrates when sound waves strike it; between outer and middle ear'),
        ('Ossicles',            'Three tiny bones in middle ear (Malleus, Incus, Stapes) that amplify and transmit vibrations'),
        ('Cochlea',             'Spiral fluid-filled structure in inner ear that converts vibrations to nerve signals'),
        ('Eustachian Tube',     'Tube connecting middle ear to throat — equalises air pressure on both sides of eardrum'),
        ('Noise',               'Unwanted, irritating, unpleasant sound produced by irregular and non-periodic vibrations'),
        ('Noise Pollution',     'Disturbance in environment due to loud, harsh sounds; bi-product of industrialisation'),
        ('Phonograph',          'First device to record and play back sound — invented by Thomas Alva Edison in 1877'),
        ('Seismology',          'Branch of science studying seismic waves (produced during earthquakes, explosions)'),
        ('Galton\'s Whistle',   'Ultrasonic whistle inaudible to humans but heard by dogs — used in dog training'),
        ('Sonogram',            'Medical imaging using ultrasound waves to visualise internal organs; non-invasive'),
    ]

    s += [gloss_2col(g), sp(3)]

    s += [dyk([
        'Bats use echolocation to navigate in total darkness — they produce ultrasonic cries (>20,000 Hz) and detect echoes to locate prey.',
        'Lightning travels at speed of light (3 × 10<super>8</super> m/s) while thunder travels at ~330 m/s in air — that is why lightning is seen before thunder is heard.',
        'On the Moon, two astronauts cannot talk directly because there is no atmosphere — sound needs a medium. They use radio waves.',
        'The speed of sound is about 880,000 times slower than the speed of light — that is why distant explosions are heard after they are seen.',
        'Whales communicate using infrasound — frequencies as low as 10–39 Hz — detectable over thousands of kilometres in ocean.',
    ])]
    s += [sp(3)]

    # FOOTER
    s += [
        HRFlowable(width=UW, thickness=1, color=TEAL), sp(1),
        P('ChalkPieceDiary.com  |  TET Paper II Science Handbook  |  P7: Sound  |  Classes 6 • 7 • 8',
          S('ft',fontName=FNI,fontSize=8.5,textColor=TEAL,alignment=TA_CENTER)),
    ]
    return s


def build_pdf(path):
    def pg(cv, doc):
        cv.saveState()
        cv.setFont(FN, 8.5)
        cv.setFillColor(TEAL)
        cv.drawRightString(PW-MAR, 11*mm, f'P7  |  Sound  |  Page {doc.page}')
        cv.restoreState()
    doc = SimpleDocTemplate(
        path,
        pagesize=(PW, PH),
        leftMargin=MAR, rightMargin=MAR,
        topMargin=MAR, bottomMargin=19*mm,
        title='TET Handbook P7 Sound',
        author='ChalkPieceDiary'
    )
    doc.build(content(), onFirstPage=pg, onLaterPages=pg)
    print(f'✅ PDF: {path}')


def build(out_path):
    build_pdf(out_path)


if __name__ == '__main__':
    out = 'output/P7_sound.pdf'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(out)
