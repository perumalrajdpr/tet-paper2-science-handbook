"""
Chapter P1 — MEASUREMENT
Physics · Class 6 + 7 + 8
TET Paper II Science Handbook
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import mm

from shared.theme import (
    register_fonts, L_MARGIN, R_MARGIN, T_MARGIN, B_MARGIN,
    PRIMARY, SECONDARY, USABLE_W
)
from shared.components import (
    chapter_banner, section, subsec, p, pl, b, fact, defn, sp, two_col_body,
    dense_table, problems_table, two_col_glossary
)
from shared.page_chrome import make_page_chrome


# ─── CHAPTER METADATA ────────────────────────────────────────────────────────
CHAPTER_ID    = 'P1'
CHAPTER_TITLE = 'MEASUREMENT'
SUBTITLE      = 'Physics  ·  Class 6 + 7 + 8'


# ─── CONTENT ─────────────────────────────────────────────────────────────────

def content():
    """Return list of ReportLab flowables for this chapter."""
    s = []

    # ── BANNER ────────────────────────────────────────────────────────────────
    s += [chapter_banner(CHAPTER_ID, CHAPTER_TITLE, SUBTITLE), sp(1.5)]

    # ─────────────────────────────────────────────────────────────────────────
    # 1. BASICS
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('1', 'Measurement — Basics')]
    s += [two_col_body(
        '<b>Measurement</b>: comparing an unknown quantity with a known standard. '
        'Every measurement = <b>numerical value (magnitude) + unit</b>. '
        'Eg: pencil 15 cm → "15" = magnitude, "cm" = unit.',
        '<b>Three things needed:</b> (1) An instrument, (2) A standard quantity, '
        '(3) An acceptable unit.'
    )]

    # ─────────────────────────────────────────────────────────────────────────
    # 2. PHYSICAL QUANTITIES
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('2', 'Types of Physical Quantities')]

    s += [subsec('2.1', 'Fundamental (Base) Quantities — 7 in SI')]
    s += [p('Cannot be expressed in terms of any other quantity.')]
    s += [dense_table(
        header=['#', 'Quantity', 'SI Unit', 'Symbol', 'Instrument'],
        rows=[
            ['1', 'Length',             'metre',    'm',   'Metre scale, Measuring tape'],
            ['2', 'Mass',               'kilogram', 'kg',  'Beam balance, Electronic balance'],
            ['3', 'Time',               'second',   's',   'Clock, Stopwatch'],
            ['4', 'Temperature',        'kelvin',   'K',   'Thermometer'],
            ['5', 'Electric current',   'ampere',   'A',   'Ammeter'],
            ['6', 'Amount of substance','mole',     'mol', '—'],
            ['7', 'Luminous intensity', 'candela',  'cd',  'Photometer (Luminous intensity meter)'],
        ],
        col_widths=[5*mm, 28*mm, 18*mm, 14*mm, USABLE_W - 65*mm]
    )]
    s += [fact('Memory aid: <b>L M T T E A L</b> → '
               '"<b>L</b>ittle <b>M</b>en <b>T</b>each <b>T</b>he '
               '<b>E</b>arly <b>A</b>fternoon <b>L</b>esson"'), sp()]

    s += [subsec('2.2', 'Supplementary / Derived Angle Units (2)')]
    s += [p('Until <b>1995</b>: classified as supplementary. '
            '<b>From 1995</b>: shifted to derived quantities.')]
    s += [dense_table(
        header=['Quantity', 'Unit', 'Symbol', 'Definition'],
        rows=[
            ['Plane angle', 'radian',    'rad',
             'Angle at intersection of 2 lines/planes (2D). '
             'Arc-length = radius. π rad = 180°.'],
            ['Solid angle', 'steradian', 'sr',
             'Angle at vertex of cone / ≥3 planes (3D). '
             'Surface area = r². 4π sr = full sphere.'],
        ],
        col_widths=[USABLE_W*0.18, USABLE_W*0.16, USABLE_W*0.12, USABLE_W*0.54]
    )]
    s += [fact('<b>π rad = 180°</b>  |  <b>1 rad ≈ 57.3°</b>  |  '
               '<b>Full circle = 2π rad</b>  |  <b>Full sphere = 4π sr</b>'), sp()]

    s += [subsec('2.3', 'Derived Quantities')]
    s += [p('Obtained by multiplying / dividing fundamental quantities.')]
    s += [dense_table(
        header=['Derived Quantity', 'Formula', 'SI Unit', 'Symbol'],
        rows=[
            ['Area',           'Length × Breadth',     'square metre',     'm²'],
            ['Volume',         'L × B × H',            'cubic metre',      'm³'],
            ['Speed',          'Distance ÷ Time',      'metre/second',     'm/s'],
            ['Velocity',       'Displacement ÷ Time',  'metre/second',     'm/s (vector)'],
            ['Acceleration',   'Velocity ÷ Time',      'metre/sec²',       'm s⁻²'],
            ['Density',        'Mass ÷ Volume',        'kilogram/metre³',  'kg/m³'],
            ['Force',          'Mass × Acceleration',  'newton',           'N = kg·m/s²'],
            ['Pressure',       'Force ÷ Area',         'pascal',           'Pa = N/m²'],
            ['Work / Energy',  'Force × Distance',     'joule',            'J = N·m'],
            ['Power',          'Work ÷ Time',          'watt',             'W = J/s'],
            ['Electric charge','Current × Time',       'coulomb',          'C = A·s'],
            ['Frequency',      '1 ÷ Time period',      'hertz',            'Hz = 1/s'],
        ],
        col_widths=[USABLE_W*0.22, USABLE_W*0.28, USABLE_W*0.27, USABLE_W*0.23]
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 3. UNIT SYSTEMS
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('3', 'Unit Systems — Historical & Current')]
    s += [dense_table(
        header=['System', 'Length', 'Mass', 'Time', 'Notes'],
        rows=[
            ['FPS', 'Foot',       'Pound',    'Second', 'British system. Non-metric.'],
            ['CGS', 'Centimetre', 'Gram',     'Second', 'Metric. Used in physics.'],
            ['MKS', 'Metre',      'Kilogram', 'Second', 'Metric. Predecessor of SI.'],
            ['SI',  'Metre',      'Kilogram', 'Second', 'Standard since 1960. Modern metric.'],
        ],
        col_widths=[15*mm, 22*mm, 22*mm, 18*mm, USABLE_W - 77*mm]
    )]
    s += [fact('<b>SI = Système International d\'Unités</b> (French). Adopted at '
               '<b>11th General Conference on Weights and Measures, 1960, Paris, France</b>.')]
    s += [fact('<b>Metric system</b> created by the <b>French</b> in <b>1790</b>.')]
    s += [fact('<b>Standard metre rod</b>: kept at <b>Bureau of Weights and Measures, '
               'Sèvres, Paris</b> (alloy of <b>platinum and iridium</b>). Copy at '
               '<b>National Physical Laboratory, Delhi</b>.')]
    s += [fact('<b>Standard kilogram</b>: Pt-Ir alloy bar at International Bureau, '
               '<b>Sèvres, France since 1889</b>.')]
    s += [fact('<b>Ruler / Scale</b>: invented by <b>William Bedwell</b> in the '
               '<b>16th century</b>.')]
    s += [p('<b>NASA Mars Climate Orbiter crash:</b> launched Dec 1998; lost on '
            '<b>Sep 23, 1999</b>. One team used FPS, another MKS — unit mismatch '
            'caused loss of <b>$125 million</b>.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 4. SI PREFIXES
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('4', 'SI Prefixes (Multiples & Sub-multiples)')]
    s += [dense_table(
        header=['Prefix', 'Symbol', 'Multiplier', 'Prefix', 'Symbol', 'Multiplier'],
        rows=[
            ['Tera',  'T',  '10¹²', 'Deci',  'd', '10⁻¹'],
            ['Giga',  'G',  '10⁹',  'Centi', 'c', '10⁻²'],
            ['Mega',  'M',  '10⁶',  'Milli', 'm', '10⁻³'],
            ['Kilo',  'k',  '10³',  'Micro', 'µ', '10⁻⁶'],
            ['Hecto', 'h',  '10²',  'Nano',  'n', '10⁻⁹'],
            ['Deca',  'da', '10¹',  'Pico',  'p', '10⁻¹²'],
        ],
        col_widths=[USABLE_W/6]*6, font_size=7.8
    )]
    s += [subsec('4.1', 'Standard Conversions')]
    s += [dense_table(
        header=['Length', 'Mass', 'Volume / Capacity'],
        rows=[
            ['1 km = 1000 m',        '1 tonne = 1000 kg', '1 m³ = 1000 L'],
            ['1 m = 100 cm',         '1 kg = 1000 g',     '1 L = 1000 mL = 1000 cc'],
            ['1 cm = 10 mm',         '1 g = 1000 mg',     '1 cc = 1 cm³'],
            ['1 m = 1000 mm',        '1 quintal = 100 kg','1 gallon = 3785 mL'],
            ['1 light year = 9.46 × 10¹⁵ m', '1 carat = 200 mg', '1 ounce = 30 mL'],
        ],
        col_widths=[USABLE_W/3]*3
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 5. LENGTH
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('5', 'Length')]
    s += [p('<b>Length</b> = distance between two points. SI unit: <b>metre (m)</b>.')]
    s += [dense_table(
        header=['Instrument', 'Use / Range'],
        rows=[
            ['Metre scale / Ruler',          'Standard lengths in cm and mm'],
            ['Measuring tape',               'Longer lengths (height, room, field)'],
            ['String / Thread',              'Curved or irregular lines'],
            ['Divider',                      'Curved line — segment-by-segment method'],
            ['Vernier calipers',             'Precision measurement; least count 0.01 cm'],
            ['Screw gauge / Micrometer',     'Very small lengths; least count 0.001 cm'],
            ['Odometer',                     'Distance travelled by automobile'],
        ],
        col_widths=[USABLE_W*0.40, USABLE_W*0.60]
    )]
    s += [subsec('5.1', 'Common Errors')]
    s += [dense_table(
        header=['Error', 'Cause', 'Avoidance'],
        rows=[
            ['Zero error',     'Object\'s edge not at "0" mark.', 'Start from the 0 mark.'],
            ['Parallax error', 'Eye not vertically above the reading point.',
             'Place eye perpendicular to scale.'],
            ['Worn-edge error','Damaged scale ends.', 'Use un-damaged middle portion.'],
        ],
        col_widths=[USABLE_W*0.18, USABLE_W*0.42, USABLE_W*0.40]
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 6. MASS & WEIGHT
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('6', 'Mass and Weight')]
    s += [dense_table(
        header=['Property', 'Mass', 'Weight'],
        rows=[
            ['Definition',  'Quantity of matter',          'Gravitational force on mass'],
            ['Type',        'Scalar & fundamental',        'Vector & derived'],
            ['SI Unit',     'kilogram (kg)',                'newton (N)'],
            ['Variation',   '<b>Constant everywhere</b>',  'Changes with gravity'],
            ['On Moon',     'Same as Earth',               '<b>1/6 of Earth weight</b>'],
            ['In space',    'Same',                        '<b>Zero</b> (weightlessness)'],
            ['Formula',     '—',                           'W = m × g  (g = 9.8 m/s²)'],
            ['Instrument',  'Beam / electronic balance',   'Spring balance'],
        ],
        col_widths=[USABLE_W*0.20, USABLE_W*0.36, USABLE_W*0.44]
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 7. TIME
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('7', 'Time and Clocks')]
    s += [p('<b>Time</b> = duration between two events. SI unit: <b>second (s)</b>. '
            '1 hr = 3600 s. 1 day = 86,400 s. '
            '1 year (non-leap) = <b>3.153 × 10⁷ s</b>.')]
    s += [dense_table(
        header=['Ancient Device', 'Working Principle'],
        rows=[
            ['Sundial',               'Shadow of a vertical stick (gnomon) shows time.'],
            ['Sand clock (hourglass)','Sand falls through small hole at constant rate.'],
            ['Water clock (Clepsydra)','Steady water flow marks time intervals.'],
            ['Pulse counting',         '~72 beats/min in adults.'],
        ],
        col_widths=[USABLE_W*0.28, USABLE_W*0.72]
    )]
    s += [subsec('7.1', 'Clocks by Display Type')]
    s += [p('<b>(1) Analog clock</b> — 3 hands: hour (short thick), minute (long thin, '
            '1 rotation/60 min), second (thinnest, 1 rotation/60 s = 60 rotations/hr). '
            'Driven mechanically or electronically.  '
            '<b>(2) Digital clock</b> — time in numerals; often called "electronic clock". '
            'Shows date, day, month, year, temp.')]
    s += [subsec('7.2', 'Clocks by Working Mechanism')]
    s += [dense_table(
        header=['Type', 'Working Principle', 'Accuracy', 'Used In'],
        rows=[
            ['Pendulum', 'Oscillation of a pendulum',
             'Low', 'Old wall clocks'],
            ['Quartz', 'Vibration of <b>quartz crystal (SiO₂)</b>; freq ~32,768 Hz',
             '<b>1 s in 10⁹ s</b>', 'Watches, computers, GPS'],
            ['Atomic', 'Periodic vibrations of <b>caesium-133 atom</b>',
             '<b>1 s in 10¹³ s</b>', 'GPS, GLONASS, Intl. Time Distribution'],
        ],
        col_widths=[USABLE_W*0.16, USABLE_W*0.42, USABLE_W*0.16, USABLE_W*0.26]
    )]
    s += [fact('<b>GMT</b> = Greenwich Mean Time — Royal Observatory, Greenwich, London '
               '(longitude 0°). Earth: 24 time zones, each <b>15° wide</b>, '
               'adjacent zones differ by <b>1 hour</b>.')]
    s += [fact('<b>IST = GMT + 5:30 hours</b>. Based on <b>82.5°E longitude</b> passing '
               'through <b>Mirzapur, Uttar Pradesh</b>.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 8. TEMPERATURE
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('8', 'Temperature')]
    s += [p('<b>Temperature</b> = degree of hotness/coldness = measure of '
            '<b>average kinetic energy of particles</b>. SI unit: <b>kelvin (K)</b>. '
            'Instrument: <b>Thermometer</b>.')]
    s += [dense_table(
        header=['Scale', 'Symbol', 'Freezing of water', 'Boiling of water'],
        rows=[
            ['Celsius',    '°C', '0 °C',         '100 °C'],
            ['Fahrenheit', '°F', '32 °F',         '212 °F'],
            ['Kelvin',     'K',  '273 K (273.15)','373 K (373.15)'],
            ['Rankine',    '°R', '491.67 °R',     '671.67 °R'],
        ],
        col_widths=[USABLE_W*0.22, USABLE_W*0.16, USABLE_W*0.31, USABLE_W*0.31]
    )]
    s += [fact('<b>Conversions:</b> K = °C + 273  |  '
               '°C = (°F − 32) × 5/9  |  °F = (°C × 9/5) + 32')]
    s += [fact('<b>Absolute zero</b> = 0 K = −273.15°C. '
               '<b>Normal body temp</b> = 37°C = 98.6°F = 310 K.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 9. ELECTRIC CURRENT
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('9', 'Electric Current')]
    s += [p('<b>Electric current (I)</b> = flow of electric charges per unit time. '
            'SI unit: <b>ampere (A)</b>. Instrument: <b>Ammeter</b>.')]
    s += [fact('<b>I = Q / t</b>  (Current = Charge ÷ Time). Charge unit = <b>coulomb (C)</b>. '
               '<b>1 A = 1 coulomb per second</b>.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 10. AMOUNT OF SUBSTANCE
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('10', 'Amount of Substance')]
    s += [p('Number of entities (atoms, molecules, ions, electrons, protons). '
            'SI unit: <b>mole (mol)</b>.')]
    s += [fact('<b>1 mole = 6.023 × 10²³ entities</b> → called '
               '<b>Avogadro Number (N<sub>A</sub>)</b>.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 11. LUMINOUS INTENSITY
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('11', 'Luminous Intensity')]
    s += [p('Power of light emitted per unit solid angle in a given direction. '
            'SI unit: <b>candela (cd)</b>. Instrument: <b>Photometer</b>.')]
    s += [fact('1 common <b>wax candle ≈ 1 candela</b>. '
               '<b>Luminous flux unit = lumen (lm)</b>. '
               '<b>1 lm = 1 cd × 1 sr</b>.'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 12. AREA, VOLUME, DENSITY
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('12', 'Area, Volume and Density')]

    s += [subsec('12.1', 'Area Formulas (SI unit: m²)')]
    s += [dense_table(
        header=['Shape', 'Formula', 'Shape', 'Formula'],
        rows=[
            ['Square',       'A = a²',              'Triangle',    'A = ½ × b × h'],
            ['Rectangle',    'A = l × b',           'Circle',      'A = π r²  (π = 22/7)'],
            ['Parallelogram','A = b × h',            'Trapezium',   'A = ½(a+b) × h'],
        ],
        col_widths=[USABLE_W*0.20, USABLE_W*0.30, USABLE_W*0.20, USABLE_W*0.30]
    )]
    s += [fact('<b>Irregular shapes (graph sheet):</b> M = full, N = more-than-half, '
               'P = exactly half, Q = less-than-half → '
               '<b>Area ≈ M + ¾N + ½P + ¼Q</b> cm²')]

    s += [subsec('12.2', 'Volume Formulas (SI unit: m³)')]
    s += [dense_table(
        header=['Solid', 'Formula', 'Solid', 'Formula'],
        rows=[
            ['Cube',   'V = a³',           'Sphere',     'V = (4/3) π r³'],
            ['Cuboid', 'V = l × b × h',    'Cylinder',   'V = π r² h'],
            ['Cone',   'V = (1/3) π r² h', 'Hemisphere', 'V = (2/3) π r³'],
        ],
        col_widths=[USABLE_W*0.18, USABLE_W*0.32, USABLE_W*0.18, USABLE_W*0.32]
    )]
    s += [p('<b>Irregular solid (stone) — displacement method:</b> V₁ = water level '
            'before, V₂ = after immersion → <b>Volume = V₂ − V₁</b>. '
            '(Archimedes\' principle.)')]

    s += [subsec('12.3', 'Density')]
    s += [fact('<b>D = M / V</b>  |  <b>M = D × V</b>  |  <b>V = M / D</b>. '
               'SI unit: <b>kg/m³</b>. CGS: g/cm³.  <b>1 g/cm³ = 1000 kg/m³</b>.')]
    s += [fact('<b>Float / Sink:</b> D(object) &lt; D(fluid) → floats. '
               'D(object) &gt; D(fluid) → sinks. '
               'Iron sinks in water (7800 &gt; 1000) but floats in mercury (7800 &lt; 13600).')]
    s += [dense_table(
        header=['Material', 'Density', 'Material', 'Density', 'Material', 'Density'],
        rows=[
            ['Air',      '1.2',    'Wood',      '770',    'Iron',     '7,800'],
            ['Kerosene', '800',    'Water',     '1,000',  'Copper',   '8,900'],
            ['Castor oil','961',   'Aluminium', '2,700',  'Silver',   '10,500'],
            ['Petrol',   '720',    'Glass',     '2,500',  'Gold',     '19,300'],
            ['Ice',      '917',    'Brick',     '1,800',  'Mercury',  '13,600'],
            ['Milk',     '1,030',  'Diamond',   '3,510',  'Platinum', '21,400'],
        ],
        col_widths=[USABLE_W/6]*6, font_size=7.5
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 13. ASTRONOMICAL DISTANCES
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('13', 'Measuring Very Long Distances')]

    s += [subsec('13.1', 'Astronomical Unit (AU)')]
    s += [fact('<b>1 AU = average Earth–Sun distance = 149.6 million km '
               '= 1.496 × 10¹¹ m</b>. '
               'Perihelion: 147.1 Mkm. Aphelion: 152.1 Mkm. Neptune ≈ 30 AU.')]

    s += [subsec('13.2', 'Light Year')]
    s += [fact('<b>1 light year = distance light travels in vacuum in 1 year '
               '= 9.46 × 10¹⁵ m</b>. '
               'c = 3 × 10⁸ m/s. 1 year = 3.153 × 10⁷ s.')]
    s += [dense_table(
        header=['Stellar Object', 'Distance'],
        rows=[
            ['Proxima Centauri (nearest star)', '4.22 light years (= 2,68,770 AU)'],
            ['Sirius (brightest in night sky)', '8.6 light years'],
            ['Centre of Milky Way galaxy',      '≈ 25,000 light years'],
            ['Andromeda Galaxy (M31)',           '≈ 2.5 million light years'],
        ],
        col_widths=[USABLE_W*0.52, USABLE_W*0.48]
    )]
    s += [dense_table(
        header=['Unit', 'Equivalent', 'Used For'],
        rows=[
            ['Parsec (pc)',   '3.26 light years', 'Astronomy (star distances)'],
            ['Nautical mile', '1.852 km',         'Aviation, sea transport'],
            ['Knot',          '1 nautical mile/hr','Speed of ships, planes'],
            ['Angstrom (Å)',  '10⁻¹⁰ m',          'Atomic / molecular sizes'],
            ['Fermi (fm)',    '10⁻¹⁵ m',           'Nuclear sizes'],
        ],
        col_widths=[USABLE_W*0.22, USABLE_W*0.28, USABLE_W*0.50]
    ), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 14. ACCURACY, PRECISION, ERROR
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('14', 'Accuracy, Precision, Error & Approximation')]
    s += [dense_table(
        header=['Term', 'Definition'],
        rows=[
            ['<b>Accuracy</b>',     'Closeness of measured value to the <b>true (actual)</b> value.'],
            ['<b>Precision</b>',    'Closeness of <b>two or more</b> measurements to each other (consistency).'],
            ['<b>Error</b>',        'Difference between true value and measured value. Error = True − Measured.'],
            ['<b>Approximation</b>','Estimating a value to a nearby simpler number for easier calculation.'],
            ['<b>Rounding off</b>', 'Reducing digits while keeping the value close to the original.'],
            ['<b>Calibration</b>',  'Configuring an instrument to give correct readings within a specified range.'],
        ],
        col_widths=[USABLE_W*0.22, USABLE_W*0.78]
    )]
    s += [subsec('14.1', 'Rounding Off Rules')]
    s += [p('(1) Next digit &lt; 5 → drop it.  (Eg: 4.582 → 4.58)<br/>'
            '(2) Next digit &gt; 5 → round up. (Eg: 4.587 → 4.59)<br/>'
            '(3) Next digit = 5 → round to nearest <b>even</b> (banker\'s rule). '
            '(Eg: 4.585 → 4.58, 4.575 → 4.58)'), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 15. SOLVED PROBLEMS
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('15', 'Solved Numerical Problems')]
    s += [problems_table([
        ('Convert 7875 cm into metres.',
         '7875 ÷ 100 = <b>78.75 m</b> = 78 m 75 cm'),
        ('Convert 60° to radian.',
         '60° = (π × 60)/180 = <b>π/3 rad</b>'),
        ('Convert π/4 rad to degrees.',
         'π rad = 180°. So π/4 = <b>45°</b>'),
        ('Area of rectangle: l=12 m, b=4 m.',
         'A = l × b = 12 × 4 = <b>48 m²</b>'),
        ('Area of circle: r=7 m. (π=22/7)',
         'A = π r² = (22/7) × 49 = <b>154 m²</b>'),
        ('Volume of cube: side a=3 cm.',
         'V = a³ = 3³ = <b>27 cm³</b>'),
        ('Volume of cylinder: r=3 m, h=7 m.',
         'V = π r² h = (22/7) × 9 × 7 = <b>198 m³</b>'),
        ('Density: m=280 kg, V=4 m³.',
         'D = m/V = 280/4 = <b>70 kg/m³</b>'),
        ('Mass of iron block: V=125 cm³, D=7.8 g/cm³.',
         'm = D × V = 7.8 × 125 = <b>975 g</b>'),
        ('Volume of copper sphere: m=3000 kg, D=8900 kg/m³.',
         'V = m/D = 3000/8900 ≈ <b>0.34 m³</b>'),
        ('Current: Q=2 C, t=10 s.',
         'I = Q/t = 2/10 = <b>0.2 A</b>'),
        ('Convert 100°C to Kelvin.',
         'K = °C + 273 = <b>373 K</b>'),
        ('Convert 98.6°F to °C.',
         '°C = (98.6 − 32) × 5/9 = <b>37°C</b>'),
    ]), sp()]

    # ─────────────────────────────────────────────────────────────────────────
    # 16. GLOSSARY
    # ─────────────────────────────────────────────────────────────────────────
    s += [section('16', 'Glossary — Key Terms')]
    s += [two_col_glossary([
        ('Accuracy',           'Closeness of measured value to the true value.'),
        ('Ammeter',            'Measures electric current. Unit: ampere (A).'),
        ('Amount of substance','Number of entities in a substance. Unit: mole.'),
        ('Approximation',      'Estimating to a nearby simpler number.'),
        ('AU',                 'Avg. Earth–Sun distance ≈ 1.496 × 10¹¹ m.'),
        ('Avogadro number',    '6.023 × 10²³ — entities per mole.'),
        ('Beam balance',       'Compares unknown mass with standard mass.'),
        ('Calibration',        'Configuring instrument for correct readings.'),
        ('Candela (cd)',       'SI unit of luminous intensity (≈ 1 candle flame).'),
        ('Density',            'Mass per unit volume. Unit: kg/m³.'),
        ('Derived quantity',   'Obtained by combining fundamentals.'),
        ('Electric current',   'Flow of charges per unit time. Unit: ampere.'),
        ('Error',              'Difference between true and measured value.'),
        ('Fundamental qty',    'Cannot be expressed via others (7 in SI).'),
        ('GMT',                'Greenwich Mean Time — at 0° longitude, London.'),
        ('GPS',                'Global Positioning System — uses atomic clocks.'),
        ('IST',                'Indian Standard Time = GMT + 5:30 (at 82.5°E).'),
        ('Kelvin (K)',          'SI unit of temperature. 0 K = −273°C = absolute zero.'),
        ('Knot',               '1 nautical mile/hr. Used for ships & planes.'),
        ('Light year',         'Distance light travels in 1 year ≈ 9.46 × 10¹⁵ m.'),
        ('Luminous intensity', 'Light power emitted per unit solid angle.'),
        ('Magnitude',          'Numerical value (size) part of a measurement.'),
        ('Mass',               'Quantity of matter. Constant everywhere. Unit: kg.'),
        ('Measurement',        'Comparison of unknown qty with known standard.'),
        ('Mole (mol)',          'SI unit of substance = 6.023 × 10²³ entities.'),
        ('Nautical mile',      '1.852 km — used in aviation & sea transport.'),
        ('Parallax error',     'Wrong reading due to oblique eye position.'),
        ('Photometer',         'Measures luminous intensity.'),
        ('Plane angle',        'At intersection of 2 lines/planes. Unit: radian.'),
        ('Precision',          'Closeness of multiple measurements to each other.'),
        ('Quartz crystal',     'SiO₂ crystal used in modern clocks; ~32,768 Hz.'),
        ('Radian (rad)',        'SI unit of plane angle. 2π rad = 360°.'),
        ('Rounding off',       'Reducing digits while keeping value close.'),
        ('SI Units',           'Système Internat. d\'Unités — 1960, Paris.'),
        ('Solid angle',        'At vertex of cone / 3+ planes. Unit: steradian.'),
        ('Steradian (sr)',      'SI unit of solid angle. 4π sr = full sphere.'),
        ('Sundial',            'Ancient time device — shadow of stick.'),
        ('Temperature',        'Avg. kinetic energy of particles. Unit: kelvin.'),
        ('Time zone',          '15°-wide longitude zone; 24 on Earth; 1 hr apart.'),
        ('Vernier calipers',   'Precision length; least count 0.01 cm = 0.1 mm.'),
        ('Volume',             'Space occupied by 3D object. Unit: m³.'),
        ('Weight',             'Gravitational force on mass. Unit: newton (N).'),
        ('Zero error',         'Error from misaligned starting mark.'),
    ])]

    return s


# ─── BUILD FUNCTION ───────────────────────────────────────────────────────────

def build(out_path: str):
    """Entry point called by build/build_chapter.py."""
    from reportlab.platypus import SimpleDocTemplate
    from shared.theme import L_MARGIN, R_MARGIN, T_MARGIN, B_MARGIN, PAGE_SIZE

    doc = SimpleDocTemplate(
        out_path,
        pagesize=PAGE_SIZE,
        leftMargin=L_MARGIN,
        rightMargin=R_MARGIN,
        topMargin=T_MARGIN,
        bottomMargin=B_MARGIN,
        title=f"TET Handbook — {CHAPTER_ID}: {CHAPTER_TITLE}",
        author="ChalkPieceDiary",
    )

    chrome = make_page_chrome(CHAPTER_ID, CHAPTER_TITLE)
    doc.build(content(), onFirstPage=chrome, onLaterPages=chrome)


# ─── STANDALONE RUN ───────────────────────────────────────────────────────────
if __name__ == '__main__':
    register_fonts()
    out = 'output/P1_Measurement.pdf'
    os.makedirs('output', exist_ok=True)
    build(out)
    size = os.path.getsize(out) / 1024
    print(f"✅  {out}  ({size:.1f} KB)")
