"""
Competitive Exams Handbook — Tamil HTML builders
Pattern: P3_heat_temperature.py reference standard, ported to HTML/CSS strings.
Engine: WeasyPrint (Pango + HarfBuzz for Tamil shaping)

Each builder takes the same logical inputs as the ReportLab P3 version,
but returns an HTML string fragment instead of a Flowable.
A chapter file collects fragments into a list and joins them into a final HTML doc.
"""

from html import escape as _esc

# ─── UNICODE FIXER (sup / sub) ────────────────────────────────────────────────
_SUP = {'\u2070':'0','\u00b9':'1','\u00b2':'2','\u00b3':'3','\u2074':'4',
        '\u2075':'5','\u2076':'6','\u2077':'7','\u2078':'8','\u2079':'9',
        '\u207b':'-','\u207a':'+'}
_SUB = {'\u2080':'0','\u2081':'1','\u2082':'2','\u2083':'3','\u2084':'4'}

def fix_supsub(text: str) -> str:
    """Convert Unicode superscript/subscript chars into <sup>/<sub> HTML."""
    import re
    sc = ''.join(_SUP.keys()); bc = ''.join(_SUB.keys())
    def rs(m): return '<sup>' + ''.join(_SUP.get(c, c) for c in m.group()) + '</sup>'
    def rb(m): return '<sub>' + ''.join(_SUB.get(c, c) for c in m.group()) + '</sub>'
    t = re.sub(f'[{re.escape(sc)}]+', rs, text)
    t = re.sub(f'[{re.escape(bc)}]+', rb, t)
    return t

def _safe(text: str) -> str:
    """
    Pass-through for content that should keep its inline HTML markup
    (<b>, <sup>, <sub>, <span class="...">, etc.).
    Only fixes superscript/subscript Unicode chars.
    Use only on author-controlled strings.
    """
    return fix_supsub(text)

# ─── BANNER ───────────────────────────────────────────────────────────────────

def banner(code: str, title: str, sub: str = '', foot: str = '') -> str:
    foot = foot or 'போட்டித் தேர்வுகளுக்கான அறிவியல் கையேடு'
    return f'''
<div class="banner">
  <div class="banner-code">{_esc(code)}</div>
  <div class="banner-body">
    <div class="banner-title">{_safe(title)}</div>
    <div class="banner-sub">{_safe(sub)}</div>
    <div class="banner-foot">{_safe(foot)}</div>
  </div>
</div>
'''

# ─── SECTION HEADERS ──────────────────────────────────────────────────────────

def sec(title: str) -> str:
    return f'<div class="sec">{_safe(title)}</div>\n'

def subh(title: str) -> str:
    return f'<div class="subh">{_safe(title)}</div>\n'

# ─── KV LIST ──────────────────────────────────────────────────────────────────

def kv_list(items, key_w_mm: int = 50) -> str:
    """
    items = [(key, value), ...]
    key_w_mm: width of key column (mm); value column gets (174 - key_w_mm)
    """
    val_w = 174 - key_w_mm
    colgroup = (
        '  <colgroup>\n'
        f'    <col style="width:{key_w_mm}mm;">\n'
        f'    <col style="width:{val_w}mm;">\n'
        '  </colgroup>\n'
    )
    rows = ''
    for key, val in items:
        rows += (
            f'  <tr>'
            f'<td class="k">{_safe(key)}</td>'
            f'<td class="v">{_safe(val)}</td>'
            f'</tr>\n'
        )
    return f'<table class="kv">\n{colgroup}{rows}</table>\n'


# ─── DEFINITION LIST (inline — saves vertical space vs kv table) ──────────────

def def_list(items) -> str:
    """
    Compact inline definition list — each entry: <b>term</b> — definition
    Use INSTEAD of kv_list for definitions where the term is short and
    the definition flows naturally as prose. Saves ~40% vertical space
    compared to a 2-column kv table.

    items = [(term, definition), ...]
    """
    body = ''
    for term, defn in items:
        body += (
            f'  <div class="dl-item">'
            f'<span class="dl-t">{_safe(term)}</span>'
            f'<span class="dl-sep"> — </span>'
            f'<span class="dl-d">{_safe(defn)}</span>'
            f'</div>\n'
        )
    return f'<div class="def-list">\n{body}</div>\n'

# ─── ONE-LINERS (bullets + optional inline KV) ────────────────────────────────

def one_liners(items) -> str:
    """
    items: list of strings (bullet rows) OR (key, value) tuples (kv rows).
    Output: a single oneliners table.
    Fixed widths: 6mm bullet | 168mm content
    """
    colgroup = (
        '  <colgroup>\n'
        '    <col style="width:6mm;">\n'
        '    <col style="width:168mm;">\n'
        '  </colgroup>\n'
    )
    rows = ''
    for it in items:
        if isinstance(it, tuple):
            key, val = it
            rows += (
                f'  <tr>'
                f'<td class="bul" style="font-weight:bold;color:#0F766E;">▸</td>'
                f'<td><b>{_safe(key)}</b> &nbsp;—&nbsp; {_safe(val)}</td>'
                f'</tr>\n'
            )
        else:
            rows += (
                f'  <tr>'
                f'<td class="bul">▶</td>'
                f'<td>{_safe(it)}</td>'
                f'</tr>\n'
            )
    return f'<table class="oneliners">\n{colgroup}{rows}</table>\n'

# ─── PILL ─────────────────────────────────────────────────────────────────────

def pill(icon: str, text: str, color: str = 'green') -> str:
    """color: green | amber | red | blue | purple"""
    return (
        f'<div class="pill {color}">'
        f'<span class="icon">{_safe(icon)}</span>{_safe(text)}'
        f'</div>\n'
    )

# ─── FORMULA STRIP ────────────────────────────────────────────────────────────

def fstrip(label: str, formula: str, note: str = '') -> str:
    note_html = f' <span class="note">({_safe(note)})</span>' if note else ''
    return (
        f'<div class="fstrip">'
        f'<span class="label">{_safe(label)}</span>'
        f'<span class="formula">{_safe(formula)}</span>'
        f'{note_html}'
        f'</div>\n'
    )

# ─── DID YOU KNOW BOX ─────────────────────────────────────────────────────────

def dyk(items, title: str = 'உங்களுக்குத் தெரியுமா?') -> str:
    body = ''
    for it in items:
        body += f'  <div class="dyk-item">• {_safe(it)}</div>\n'
    return (
        f'<div class="dyk">\n'
        f'  <div class="dyk-title">{_safe(title)}</div>\n'
        f'{body}'
        f'</div>\n'
    )

# ─── NOTE BOX ─────────────────────────────────────────────────────────────────

def note_box(title: str, items) -> str:
    body = ''
    for it in items:
        body += f'  <div>• {_safe(it)}</div>\n'
    return (
        f'<div class="note-box">\n'
        f'  <div class="note-box-title">{_safe(title)}</div>\n'
        f'  <div class="note-box-body">\n{body}  </div>\n'
        f'</div>\n'
    )

# ─── FOOTER ───────────────────────────────────────────────────────────────────

def footer(text: str) -> str:
    return f'<div class="footer">{_safe(text)}</div>\n'

# ─── PAGE ASSEMBLER ───────────────────────────────────────────────────────────

# ─── GRID (multi-column comparison table) ─────────────────────────────────────

def grid(headers, rows, col_widths_mm=None) -> str:
    """
    headers: list of column header strings
    rows: list of row-lists (each row's cells)
    col_widths_mm: optional list of widths in mm; must sum to 174mm if provided
    """
    n = len(headers)
    if col_widths_mm and abs(sum(col_widths_mm) - 174) > 0.5:
        # Renormalise to 174mm usable width
        total = sum(col_widths_mm)
        col_widths_mm = [w * 174 / total for w in col_widths_mm]

    # Build colgroup
    colgroup = ''
    if col_widths_mm:
        colgroup = '  <colgroup>\n'
        for w in col_widths_mm:
            colgroup += f'    <col style="width:{w:.2f}mm;">\n'
        colgroup += '  </colgroup>\n'

    # Header row
    th = '  <tr>\n'
    for h in headers:
        th += f'    <th>{_safe(h)}</th>\n'
    th += '  </tr>\n'

    # Body rows
    body = ''
    for i, row in enumerate(rows):
        cls = ' class="alt"' if i % 2 == 0 else ''
        body += f'  <tr{cls}>\n'
        for cell in row:
            body += f'    <td>{_safe(str(cell))}</td>\n'
        body += '  </tr>\n'

    return f'<table class="grid">\n{colgroup}<thead>\n{th}</thead>\n<tbody>\n{body}</tbody>\n</table>\n'

# ─── TWO-COLUMN BLOCK (parallel content) ──────────────────────────────────────

def two_col(left_lines, right_lines) -> str:
    """Each side: list of HTML strings (one per row)."""
    left  = ''.join(f'<div>{_safe(line) if line else "&nbsp;"}</div>' for line in left_lines)
    right = ''.join(f'<div>{_safe(line) if line else "&nbsp;"}</div>' for line in right_lines)
    return (
        f'<table class="twocol">\n'
        f'  <tr>\n'
        f'    <td class="lcol">{left}</td>\n'
        f'    <td class="rcol">{right}</td>\n'
        f'  </tr>\n'
        f'</table>\n'
    )

# ─── SOLVED PROBLEM ───────────────────────────────────────────────────────────

def prob(num, question, given, solution, answer) -> str:
    """Single-column full-width solved problem (compact internal spacing)."""
    return (
        f'<table class="prob">\n'
        f'  <colgroup><col style="width:24mm;"><col style="width:150mm;"></colgroup>\n'
        f'  <tr><td class="pnum">{_safe(num)}</td>'
        f'<td class="pq"><b>{_safe(question)}</b></td></tr>\n'
        f'  <tr><td class="plbl">தரப்பட்டது</td><td>{_safe(given)}</td></tr>\n'
        f'  <tr><td class="plbl">தீர்வு</td><td>{_safe(solution)}</td></tr>\n'
        f'  <tr><td class="plbl pans-lbl">விடை</td><td class="pans">{_safe(answer)}</td></tr>\n'
        f'</table>\n'
    )


def _prob_compact(num, question, given, solution, answer) -> str:
    """Compact problem cell (no outer table.prob — used inside prob_grid)."""
    return (
        f'<div class="probc">\n'
        f'  <div class="probc-head">'
        f'<span class="probc-num">{_safe(num)}</span>'
        f'<span class="probc-q">{_safe(question)}</span>'
        f'</div>\n'
        f'  <div class="probc-row"><span class="probc-lbl">தரப்பட்டது</span>'
        f'<span class="probc-val">{_safe(given)}</span></div>\n'
        f'  <div class="probc-row"><span class="probc-lbl">தீர்வு</span>'
        f'<span class="probc-val">{_safe(solution)}</span></div>\n'
        f'  <div class="probc-row probc-ans"><span class="probc-lbl probc-ans-lbl">விடை</span>'
        f'<span class="probc-val">{_safe(answer)}</span></div>\n'
        f'</div>\n'
    )


def prob_grid(problems) -> str:
    """
    Render problems in newspaper-style vertical column flow:
      Column 1: problems 1, 2, 3 (top to bottom)
      Column 2: problems 4, 5, 6 (top to bottom)
    Reader scans down column 1 first, then column 2.
    Uses CSS column-count for natural flow.
    """
    cells = ''.join(_prob_compact(*p) for p in problems)
    return f'<div class="prob-cols">\n{cells}</div>\n'

# ─── RAPID-REVISION TABLES (3 columns) ────────────────────────────────────────

def rapid_3col(rows, headers=None, col_widths_mm=None) -> str:
    """
    Generic 3-column rapid-revision table.
    rows = [[col1, col2, col3], ...]
    Defaults to fixed column widths optimised for: term | description | tag.
    Pass col_widths_mm to override widths for compatibility with denser tables.
    """
    # 174mm total default: 50mm | 96mm | 28mm
    if col_widths_mm:
        total = float(sum(col_widths_mm)) or 174.0
        widths = [w * 174.0 / total for w in col_widths_mm]
    else:
        widths = [50.0, 96.0, 28.0]

    colgroup = '  <colgroup>\n'
    for w in widths:
        colgroup += f'    <col style="width:{w:.2f}mm;">\n'
    colgroup += '  </colgroup>\n'
    th = ''
    if headers:
        th = '  <tr>'
        for h in headers:
            th += f'<th>{_safe(h)}</th>'
        th += '</tr>\n'
    body = ''
    for i, row in enumerate(rows):
        cls = ' class="alt"' if i % 2 == 0 else ''
        body += f'  <tr{cls}>'
        for cell in row:
            body += f'<td>{_safe(str(cell))}</td>'
        body += '</tr>\n'
    return f'<table class="rapid">\n{colgroup}{th}{body}</table>\n'

# ─── GLOSSARY (2-column) ──────────────────────────────────────────────────────

def gloss_2col(terms) -> str:
    """
    terms: list of (term, definition) tuples.
    Splits into two columns side-by-side.
    """
    n = len(terms)
    half = (n + 1) // 2
    left = terms[:half]
    right = terms[half:]

    def col_html(items):
        h = '<table class="glcol">\n'
        for term, defn in items:
            h += (f'  <tr>'
                  f'<td class="gt"><b>{_safe(term)}</b></td>'
                  f'<td class="gd">{_safe(defn)}</td>'
                  f'</tr>\n')
        h += '</table>\n'
        return h

    return (
        f'<table class="gloss-wrap">\n'
        f'  <tr>\n'
        f'    <td class="gl-left">{col_html(left)}</td>\n'
        f'    <td class="gl-right">{col_html(right)}</td>\n'
        f'  </tr>\n'
        f'</table>\n'
    )


def gloss_1col(terms) -> str:
    """
    Compact single-column glossary — much denser than 2-col for Tamil
    because Tamil definitions wrap less and gain readability.

    Format: <b>term</b> — definition (each entry on its own line, tight spacing)
    terms: list of (term, definition) tuples.
    """
    body = ''
    for term, defn in terms:
        body += (
            f'  <div class="g1-item">'
            f'<span class="g1-t">{_safe(term)}</span>'
            f'<span class="g1-sep"> — </span>'
            f'<span class="g1-d">{_safe(defn)}</span>'
            f'</div>\n'
        )
    return f'<div class="gloss-1col">\n{body}</div>\n'


def term_pairs(pairs, n_cols: int = 3) -> str:
    """
    Dense English ↔ Tamil term-pair lookup table.
    Use INSTEAD of full glossary when concepts are already explained
    in the chapter body — purely a quick lookup for synonyms/translations.

    pairs: list of (english, tamil) tuples
    n_cols: number of columns (default 3 — fits ~30 pairs in compact space)

    Output: multi-column flow with each pair as `English = Tamil`.
    """
    items = ''.join(
        f'<div class="tp-item"><span class="tp-en">{_safe(en)}</span>'
        f'<span class="tp-eq"> = </span>'
        f'<span class="tp-ta">{_safe(ta)}</span></div>\n'
        for en, ta in pairs
    )
    return f'<div class="term-pairs" style="column-count:{n_cols};">\n{items}</div>\n'

# ─── PARAGRAPH (general body text) ────────────────────────────────────────────

def para(text: str, bold: bool = False) -> str:
    cls = 'pbold' if bold else 'pbody'
    return f'<p class="{cls}">{_safe(text)}</p>\n'

def assemble_html(title: str, css_path: str, body_fragments) -> str:
    """
    Build a complete HTML document from a title, CSS path (relative to the
    output HTML file), and a list of body fragments.
    """
    body = ''.join(body_fragments)
    return f'''<!DOCTYPE html>
<html lang="ta">
<head>
  <meta charset="utf-8">
  <title>{_esc(title)}</title>
  <link rel="stylesheet" href="{_esc(css_path)}">
</head>
<body>
{body}
</body>
</html>
'''
