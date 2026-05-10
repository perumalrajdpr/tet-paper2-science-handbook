"""
Build an integrated Tamil print B/W handbook PDF (P1-P6 by default).

Includes:
- Cover page
- Inside/front matter pages
- Contents page
- Chapter body (selected chapters)
- Back cover page
"""

from __future__ import annotations

import importlib
import os
import re
import sys
from html import escape
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from shared.builders.html_builders import assemble_html

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters_ta_html"
PRINT_CSS_REL = "shared/css/handbook_ta_print_bw.css"
COLOR_CSS_REL = "shared/css/handbook_ta_color_book.css"
PRINT_SCALE = 170.0 / 174.0
ANONYMIZE_BOOK_OUTPUT = False

DEFAULT_CHAPTERS = [
    "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
]

COVER_PAGE = {
    "brand_name": "தமிழ்நண்பன் அகாடமி",
    "main_title_lines": ["போட்டித் தேர்வு", "அறிவியல்"],
    "main_title_accent": "களஞ்சியம்",
    "subtitle": "(6, 7, 8 வகுப்பு அறிவியல் பாடநூல்களின் அடிப்படையில்)",
    "exam_badges": [
        {"name": "TET", "sub": "Paper II Science"},
        {"name": "TNPSC", "sub": "Group 2, 2A, 4 & VAO"},
        {"name": "TRB", "sub": ""},
        {"name": "NMMS", "sub": ""},
    ],
}
FRONT_COVER_IMAGE_REL = "assets/cover_front.png"
BACK_COVER_IMAGE_REL = "assets/cover_back.png"

DEDICATION_PAGE = {
    "dedication": {
        "title": "சமர்ப்பணம்",
        "content": "அரசுப் பணியை இலக்காகக் கொண்டு, இரவு பகலாகத் தங்களைத் தயார்படுத்திக் கொண்டிருக்கும் லட்சக்கணக்கான போட்டித் தேர்வர்களுக்கு இக்கையேடு சமர்ப்பணம்.",
    },
    "acknowledgement": {
        "title": "நன்றியுரை",
        "content": "இந்தக் கையேட்டினை உருவாக்கத் துணைநின்ற ஆசிரியப் பெருமக்களுக்கும், தகவல்களைச் சேகரிக்க உதவிய தமிழ்நாடு அரசு சமச்சீர் கல்விப் பாடநூல்களுக்கும், மற்றும் எனக்கு ஊக்கமளித்த குடும்பத்தினருக்கும் எனது நெஞ்சார்ந்த நன்றிகள்.",
    },
    "copyright_note": "இந்த நூலின் எப்பகுதியையும் ஆசிரியரின் எழுத்துப்பூர்வமான முன் அனுமதியின்றி எவ்வகையிலும் மீண்டும் பதிப்பிக்கக் கூடாது.",
}

FOREWORD_PAGE = {
    "title": "வெற்றியை நோக்கி உங்களுடன்",
    "greeting": "அன்பார்ந்த மாணவர்களுக்கும், போட்டித் தேர்வர்களுக்கும் வணக்கம்!",
    "paragraphs": [
        "உங்கள் கல்வி மற்றும் லட்சியப் பயணத்தில் வெற்றிபெற எங்களின் மனமார்ந்த வாழ்த்துகள். இந்தப் பயணத்தில் உங்களுக்கு வழிகாட்டும் ஒரு துணையாக இந்தக் கையேட்டை மிகுந்த அக்கறையுடன் உருவாக்கியுள்ளோம்.",
        "அறிவியலில் ஆண்டுகள், அறிவியலாளர்கள் பெயர்கள், விதிகள், மற்றும் அளவீடுகளை (Fact-dense data) துல்லியமாக நினைவில் வைத்துக்கொள்வது அவசியம். பள்ளிப் பாடப்புத்தகங்களை முழுமையாக வாசிக்க நேரமில்லாதவர்களுக்கும், இறுதி நேர மீள்பார்வைக்கும் (Revision) இது ஒரு சிறந்த அடிப்படை ஆதாரமாக விளங்கும்.",
    ],
    "features": {
        "title": "இக்கையேட்டின் சிறப்பம்சங்கள்:",
        "points": [
            "6 முதல் 8 ஆம் வகுப்பு வரையிலான அறிவியல் பாடங்கள் 22 முக்கிய அத்தியாயங்களாகப் பிரிக்கப்பட்டுள்ளன.",
            "தேவையற்ற விரிவான விளக்கங்கள் தவிர்க்கப்பட்டு, தேர்வு நோக்கில் குறிப்புகள் (Point-wise) தரப்பட்டுள்ளன.",
            "நினைவில் நிறுத்த எளிதான வகையில் ஒப்பீட்டு அட்டவணைகள் (Comparison tables), மற்றும் நட்சத்திரக் குறியிடப்பட்ட முக்கியத் தகவல்கள் (★ Highlighted facts) கொடுக்கப்பட்டுள்ளன.",
            "எளிதில் படிப்பதற்காக அனைத்துக் கலைச்சொற்களும் அகரவரிசையில் (Glossary) தொகுக்கப்பட்டுள்ளன.",
        ],
    },
    "closing": "நம்பிக்கையோடு படியுங்கள், வெற்றி நிச்சயம் உங்கள் வசமாகும்!",
    "sign_off": "வாழ்த்துகளுடன்,\nChalkPieceDiary\nExclusively for தமிழ் நண்பன் அகாடமி",
}

EXAM_INTRO_PAGE = {
    "title": "போட்டித் தேர்வுகள் - ஓர் அறிமுகம்",
    "subtitle": "இந்தக் கையேடு உங்களுக்கு எப்படி உதவும்?",
    "exams": [
        {
            "name": "1. TET (ஆசிரியர் தகுதித் தேர்வு - தாள் II):",
            "description": "தாள் 2 (அறிவியல்) தேர்வர்களுக்கு இந்தப் புத்தகத்தின் ஒவ்வொரு வரியும் மிக முக்கியம். நேரடி வினாக்கள் பெருமளவு இங்கிருந்துதான் எடுக்கப்படுகின்றன. தேர்வு நோக்கத்திற்காகவே பிரத்யேகமாக வடிவமைக்கப்பட்டுள்ளது.",
        },
        {
            "name": "2. TNPSC (தமிழ்நாடு அரசுப் பணியாளர் தேர்வாணையம்):",
            "description": "குரூப் 4 மற்றும் குரூப் 2 தேர்வுகளில் பொது அறிவுப் பகுதியில் அறிவியல் பாடத்திலிருந்து கணிசமான கேள்விகள் கேட்கப்படுகின்றன. 6-8ஆம் வகுப்பு அடிப்படைகள் வலுவாக இருந்தால் மட்டுமே 9-10ஆம் வகுப்புப் பாடங்களை எளிதில் புரிந்துகொள்ள முடியும்.",
        },
        {
            "name": "3. NMMS தேர்வு:",
            "description": "எட்டாம் வகுப்பு படிக்கும் அரசுப் பள்ளி மாணவர்களுக்கான இத்தேர்வில், SAT (படிப்பறிவுத் திறன் தேர்வு) பகுதியில் அறிவியல் முக்கியப் பங்கு வகிக்கிறது. 7 மற்றும் 8 ஆம் வகுப்பு அறிவியலை முழுமையாகப் படித்தால் உதவித்தொகையை எளிதில் பெறலாம்.",
        },
    ],
}

HOW_TO_USE_PAGE = {
    "title": "இந்தக் கையேட்டைப் பயன்படுத்துவது எப்படி?",
    "intro": "வெற்றியை உறுதி செய்ய, இந்தக் கையேட்டைக் கீழ்க்கண்டவாறு பயன்படுத்துங்கள்:",
    "instructions": [
        {
            "step": "முக்கியக் குறிப்புகளை அடிக்கோடிடுக",
            "detail": "படிக்கும்போது உங்களுக்குப் புதிதாகத் தோன்றும் தகவல்களை அல்லது எண்களை 'Highlighter' கொண்டு குறித்துக் கொள்ளுங்கள்.",
        },
        {
            "step": "அட்டவணைகளுக்கு முன்னுரிமை",
            "detail": "பாடங்களுக்கு இடையே கொடுக்கப்பட்டுள்ள 'உங்களுக்குத் தெரியுமா?', ஒப்பீட்டு அட்டவணைகள் (Comparison tables) ஆகியவற்றை ஒருபோதும் தவறவிடாதீர்கள்.",
        },
        {
            "step": "சுய பரிசோதனை",
            "detail": "ஒவ்வொரு பாடத்தின் இறுதியிலும் உள்ள கலைச்சொற்களையும் (Glossary), தீர்க்கப்பட்ட கணக்குகளையும் (Solved problems) திரும்பத் திரும்பப் பயிற்சி செய்யுங்கள்.",
        },
        {
            "step": "தொடர் திருப்புதல் (Revision)",
            "detail": "தேர்விற்கு ஒரு மாதம் முன்பு புதிய தலைப்புகளைப் படிப்பதைத் தவிர்த்து, இந்தக் கையேட்டில் உள்ள குறிப்புகளைத் திரும்பத் திரும்பப் படியுங்கள்.",
        },
    ],
}

TABLE_OF_CONTENTS = [
    {
        "section": "பகுதி அ - இயற்பியல் (Physics)",
        "chapters": [
            {"id": "P1", "title": "அளவீடுகள் (Measurement)"},
            {"id": "P2", "title": "விசை, இயக்கம் மற்றும் அழுத்தம் (Force, Motion & Pressure)"},
            {"id": "P3", "title": "வெப்பம் மற்றும் வெப்பநிலை (Heat & Temperature)"},
            {"id": "P4", "title": "ஒளியியல் (Light)"},
            {"id": "P5", "title": "மின்னியல் (Electricity)"},
            {"id": "P6", "title": "காந்தவியல் (Magnetism)"},
            {"id": "P7", "title": "ஒலியியல் (Sound)"},
            {"id": "P8", "title": "அண்டம் மற்றும் விண்வெளி அறிவியல் (Universe & Space Science)"},
        ],
    },
    {
        "section": "பகுதி ஆ - வேதியியல் (Chemistry)",
        "chapters": [
            {"id": "C1", "title": "பருப்பொருள் மற்றும் அதன் பண்புகள் (Matter & Its Properties)"},
            {"id": "C2", "title": "அணு அமைப்பு (Atomic Structure)"},
            {"id": "C3", "title": "நம்மைச் சுற்றி நிகழும் மாற்றங்கள் (Changes Around Us)"},
            {"id": "C4", "title": "காற்று (Air)"},
            {"id": "C5", "title": "நீர் (Water)"},
            {"id": "C6", "title": "அமிலங்கள், காரங்கள் மற்றும் உப்புகள் (Acids, Bases & Salts)"},
            {"id": "C7", "title": "அன்றாட வாழ்வில் வேதியியல் (Chemistry in Daily Life)"},
        ],
    },
    {
        "section": "பகுதி இ - உயிரியல் (Biology)",
        "chapters": [
            {"id": "B1", "title": "தாவர உலகம் (Plant Kingdom)"},
            {"id": "B2", "title": "விலங்கு உலகம் மற்றும் இயக்கங்கள் (Animal Kingdom & Movements)"},
            {"id": "B3", "title": "செல் மற்றும் உயிரினங்களின் ஒருங்கமைவு (Cell & Organisation of Life)"},
            {"id": "B4", "title": "நுண்ணுயிரிகள் (Microorganisms)"},
            {"id": "B5", "title": "உடல்நலம், சுகாதாரம் மற்றும் வளரிளம் பருவமடைதல் (Health, Hygiene & Adolescence)"},
            {"id": "B6", "title": "பயிர்ப்பெருக்கம் மற்றும் மேலாண்மை (Crop Production & Management)"},
            {"id": "B7", "title": "சுற்றுச்சூழல் மற்றும் சூழலியல் (Environment & Ecology)"},
        ],
    },
]


def _load_weasyprint_html():
    """Import WeasyPrint HTML with Windows GTK DLL bootstrap."""
    if os.name == "nt":
        dll_candidates = [
            Path(r"C:\msys64\mingw64\bin"),
            Path(r"C:\msys64\ucrt64\bin"),
        ]
        for dll_dir in dll_candidates:
            if not dll_dir.exists():
                continue
            os.environ["PATH"] = f"{dll_dir};{os.environ.get('PATH', '')}"
            if hasattr(os, "add_dll_directory"):
                try:
                    os.add_dll_directory(str(dll_dir))
                except OSError:
                    continue
    from weasyprint import HTML  # pylint: disable=import-outside-toplevel

    return HTML


def _scale_inline_mm_widths(html: str, scale: float) -> str:
    pattern = re.compile(r"(?P<k>max-width|width)\s*:\s*(?P<v>\d+(?:\.\d+)?)mm")

    def repl(match: re.Match[str]) -> str:
        key = match.group("k")
        value = float(match.group("v"))
        scaled = value * scale
        text = f"{scaled:.2f}".rstrip("0").rstrip(".")
        return f"{key}:{text}mm"

    return pattern.sub(repl, html)


def _sanitize_for_anonymous_book(html: str) -> str:
    """
    Optionally anonymize personal/brand mentions from generated output.
    """
    if not ANONYMIZE_BOOK_OUTPUT:
        return html

    for token in ("த. பெருமாள்ராஜ்", "ChalkPieceDiary.com", "ChalkPieceDiary"):
        html = html.replace(token, "")

    # Cleanup leftover separators in footers after token removal.
    html = re.sub(r"\s*\|\s*\|\s*", " | ", html)
    html = re.sub(r"\s+\|\s+</div>", "</div>", html)
    html = re.sub(r">\s*\|\s+", ">", html)
    html = re.sub(r"\s{2,}", " ", html)
    return html


def _chapter_span_label(chapter_ids: list[str]) -> str:
    if not chapter_ids:
        return "BOOK"
    if len(chapter_ids) == 1:
        return chapter_ids[0]
    return f"{chapter_ids[0]}_{chapter_ids[-1]}"


def _subject_label(chapter_id: str) -> str:
    prefix = chapter_id[:1].upper()
    if prefix == "P":
        return "இயற்பியல்"
    if prefix == "C":
        return "வேதியியல்"
    if prefix == "B":
        return "உயிரியியல்"
    return "அறிவியல்"


def _subject_class(chapter_id: str) -> str:
    prefix = chapter_id[:1].upper()
    if prefix == "P":
        return "subject-p"
    if prefix == "C":
        return "subject-c"
    if prefix == "B":
        return "subject-b"
    return "subject-generic"


_SUBJECT_DIVIDER_META = {
    "P": {
        "part": "முதல் பகுதி",
        "mark": "P",
        "title": "இயற்பியல்",
        "en": "PHYSICS",
        "tagline": "அளவீடு, விசை, இயக்கம், ஒளி, ஒலி, மின்சாரம் — இயற்கையின் அடிப்படை விதிகளைப் புரிந்துகொள்ள.",
    },
    "C": {
        "part": "இரண்டாம் பகுதி",
        "mark": "C",
        "title": "வேதியியல்",
        "en": "CHEMISTRY",
        "tagline": "பொருளின் கட்டமைப்பு, அணுக்கள், மாற்றங்கள், அமிலம்-காரம் — பொருட்களின் இயல்பை ஆராய.",
    },
    "B": {
        "part": "மூன்றாம் பகுதி",
        "mark": "B",
        "title": "உயிரியியல்",
        "en": "BIOLOGY",
        "tagline": "உயிரணு, தாவரங்கள், விலங்குகள், மனிதர், சுற்றுச்சூழல் — உயிரின உலகின் கட்டமைப்பு மற்றும் இயக்கம்.",
    },
}


def _subject_divider(
    prefix: str, chapter_ids: list[str], chapter_titles: list[str]
) -> str:
    meta = _SUBJECT_DIVIDER_META.get(prefix)
    if not meta:
        return ""
    cls = {"P": "subject-p", "C": "subject-c", "B": "subject-b"}[prefix]
    items = "".join(
        f'<li><span class="sd-cid">{cid}</span><span>{title}</span></li>'
        for cid, title in zip(chapter_ids, chapter_titles)
    )
    return (
        f'<section class="subject-divider {cls}">'
        f'  <div class="sd-eyebrow">{meta["part"]}</div>'
        f'  <div class="sd-mark">{meta["mark"]}</div>'
        f'  <div class="sd-title">{meta["title"]}</div>'
        f'  <div class="sd-en">{meta["en"]}</div>'
        f'  <hr class="sd-rule">'
        f'  <div class="sd-tagline">{meta["tagline"]}</div>'
        f'  <div class="sd-toc">'
        f'    <div class="sd-toc-title">இந்தப் பகுதி அத்தியாயங்கள்</div>'
        f'    <ol>{items}</ol>'
        f'  </div>'
        f'</section>'
    )


def _profile_css(profile: str) -> str:
    if profile == "color":
        return COLOR_CSS_REL
    return PRINT_CSS_REL


def _profile_suffix(profile: str) -> str:
    if profile == "color":
        return "color_book"
    return "print_bw_book"


def _short_running_title(chapter_title: str, max_len: int = 24) -> str:
    """
    Keep running header compact to avoid wrapping in the top margin.
    Drops English parenthetical and trims long Tamil titles.
    """
    base = chapter_title.split("(", 1)[0].strip()
    if len(base) <= max_len:
        return base
    cut = base[:max_len].rstrip()
    last_space = cut.rfind(" ")
    if last_space > 0:
        cut = cut[:last_space].rstrip()
    if not cut:
        cut = base[:max_len].rstrip()
    return f"{cut}…"


def discover_tamil_chapters() -> dict[str, tuple[str, str]]:
    """
    Return chapter map:
      chapter_id -> (python_module_name, base_filename_without_extension)
    """
    chapter_map: dict[str, tuple[str, str]] = {}
    for path in sorted(CHAPTERS_DIR.glob("*_ta.py")):
        if path.name == "__init__.py":
            continue
        stem = path.stem
        chapter_id = stem.split("_", 1)[0].upper()
        module_name = f"chapters_ta_html.{stem}"
        chapter_map[chapter_id] = (module_name, stem)
    return chapter_map


def _load_chapter(chapter_id: str, chapters: dict[str, tuple[str, str]]):
    if chapter_id not in chapters:
        valid = ", ".join(sorted(chapters.keys()))
        raise ValueError(
            f"Unsupported chapter ID for book build: {chapter_id}. Valid IDs: {valid}"
        )
    module_name, _ = chapters[chapter_id]
    mod = importlib.import_module(module_name)
    return mod


def _with_break(section_html: str, first_page: bool = False) -> str:
    if first_page:
        return section_html
    return section_html.replace('class="frontmatter-page"', 'class="frontmatter-page chapter-break"', 1)


def _render_multiline(text: str) -> str:
    return "<br>".join(escape(line) for line in text.split("\n"))


def _render_cover_art_page(page_class: str, image_rel_path: str) -> str:
    return (
        f'<section class="{page_class}">'
        f'<img class="cover-art-image" src="{escape(image_rel_path)}" alt="Cover Art">'
        "</section>"
    )


def _render_cover_page() -> str:
    return _render_cover_art_page("cover-page cover-art-page", FRONT_COVER_IMAGE_REL)


def _render_after_cover_pages(profile: str) -> list[str]:
    tone_class = "insert-color" if profile == "color" else "insert-bw"
    page1 = f"""
<section class="cover-page chapter-break insert-page {tone_class}">
  <div class="insert-page-body insert-page-one">
    <div class="insert-main-title">போட்டித் தேர்வு களஞ்சியம்</div>
    <div class="insert-main-sub">அறிவியல்</div>
    <div class="insert-main-note">(6,7,8 அறிவியல் பாடநூல்களின் அடிப்படையில்)</div>

    <div class="insert-main-exams">TET, TRB, NMMS, TNPSC</div>
    <div class="insert-main-exam-note">அனைத்துப் போட்டித் தேர்வுகளுக்குமான கையேடு</div>

    <div class="insert-main-author">தொகுப்பு</div>
    <div class="insert-main-author-name">சாக்பீஸ் டைரி</div>

    <div class="insert-main-brand">தமிழ் நண்பன் அகாடமி</div>
  </div>
</section>
"""
    page2 = f"""
<section class="cover-page chapter-break insert-page {tone_class}">
  <div class="insert-page-body insert-page-two">
    <div class="insert-pub-title">போட்டித்தேர்வு களஞ்சியம்</div>
    <div class="insert-pub-sub">அறிவியல்</div>

    <div class="insert-pub-block">
      <div>தொகுப்பு: சாக்பீஸ்டைரி</div>
      <div>பக்கங்கள்: 240</div>
      <div>முதற் பதிப்பு: 2026</div>
    </div>

    <div class="insert-pub-block">
      <div>© சாக்பீஸ் டைரி</div>
      <div>இந்த நூலின் எப்பகுதியையும் எழுத்துப்பூர்வமான முன் அனுமதியின்றி</div>
      <div>எவ்வகையிலும் மீண்டும் பதிப்பிக்கக் கூடாது.</div>
    </div>

    <div class="insert-pub-block">
      <div>வெளியீடு:</div>
      <div>தமிழ் நண்பன் அகாடமி,</div>
      <div>விளாத்திகுளம், தூத்துக்குடி மாவட்டம்.</div>
      <div>63693 71452, 88076 56338</div>
      <div>chalkpiecefoundation@gmail.com</div>
    </div>

    <div class="insert-pub-block">
      <div>விலை: ₹ 480</div>
    </div>

    <div class="insert-pub-block">
      <div>வடிவமைப்பு:</div>
      <div>பிரியம் மீடியா, பட்டீஸ்வரம்.</div>
      <div>82204 71077.</div>
    </div>
  </div>
</section>
"""
    return [page1, page2]


def _render_dedication_page() -> str:
    dedication = DEDICATION_PAGE["dedication"]
    acknowledgement = DEDICATION_PAGE["acknowledgement"]
    return f"""
<section class="frontmatter-page">
  <div class="inside-title">{escape(dedication["title"])}</div>
  <p class="inside-text">{escape(dedication["content"])}</p>
  <div class="inside-title">{escape(acknowledgement["title"])}</div>
  <p class="inside-text">{escape(acknowledgement["content"])}</p>
  <div class="copyright-note">{escape(DEDICATION_PAGE["copyright_note"])}</div>
</section>
"""


def _render_foreword_page() -> str:
    paragraphs = "".join(
        f'<p class="inside-text">{escape(paragraph)}</p>'
        for paragraph in FOREWORD_PAGE["paragraphs"]
    )
    feature_points = "".join(
        f"<li>{escape(point)}</li>" for point in FOREWORD_PAGE["features"]["points"]
    )
    instruction_rows = "".join(
        (
            '<div class="instruction-item">'
            f'<div class="instruction-num">{idx}</div>'
            f'<div class="instruction-step">{escape(item["step"])}</div>'
            f'<div class="instruction-detail">{escape(item["detail"])}</div>'
            "</div>"
        )
        for idx, item in enumerate(HOW_TO_USE_PAGE["instructions"], start=1)
    )
    return f"""
<section class="frontmatter-page foreword-page">
  <div class="foreword-top">
    <div class="inside-title">{escape(FOREWORD_PAGE["title"])}</div>
    <p class="inside-text foreword-greeting">{escape(FOREWORD_PAGE["greeting"])}</p>
  </div>
  <div class="foreword-body">
    {paragraphs}
  </div>
  <div class="feature-box">
    <div class="feature-title">{escape(FOREWORD_PAGE["features"]["title"])}</div>
    <ul class="feature-list">{feature_points}</ul>
  </div>
  <div class="howto-inline">
    <div class="inside-title howto-inline-title">{escape(HOW_TO_USE_PAGE["title"])}</div>
    <p class="inside-text howto-intro">{escape(HOW_TO_USE_PAGE["intro"])}</p>
    <div class="instruction-list">{instruction_rows}</div>
  </div>
  <div class="foreword-bottom">
    <p class="inside-text foreword-closing">{escape(FOREWORD_PAGE["closing"])}</p>
    <p class="inside-text foreword-signoff">{_render_multiline(FOREWORD_PAGE["sign_off"])}</p>
  </div>
</section>
"""


def _render_exam_intro_page() -> str:
    exam_cards = "".join(
        (
            '<div class="exam-card">'
            f'<div class="exam-name">{escape(exam["name"])}</div>'
            f'<div class="exam-desc">{escape(exam["description"])}</div>'
            "</div>"
        )
        for exam in EXAM_INTRO_PAGE["exams"]
    )
    return f"""
<section class="frontmatter-page">
  <div class="inside-title">{escape(EXAM_INTRO_PAGE["title"])}</div>
  <div class="inside-text exam-subtitle">{escape(EXAM_INTRO_PAGE["subtitle"])}</div>
  <div class="exam-list">{exam_cards}</div>
</section>
"""


def _render_how_to_use_page() -> str:
    instruction_rows = "".join(
        (
            '<div class="instruction-item">'
            f'<div class="instruction-num">{idx}</div>'
            f'<div class="instruction-step">{escape(item["step"])}</div>'
            f'<div class="instruction-detail">{escape(item["detail"])}</div>'
            "</div>"
        )
        for idx, item in enumerate(HOW_TO_USE_PAGE["instructions"], start=1)
    )
    return f"""
<section class="frontmatter-page howto-page">
  <div class="inside-title">{escape(HOW_TO_USE_PAGE["title"])}</div>
  <p class="inside-text howto-intro">{escape(HOW_TO_USE_PAGE["intro"])}</p>
  <div class="instruction-list">{instruction_rows}</div>
</section>
"""


def _render_toc_page(chapter_ids: list[str]) -> str:
    selected = set(chapter_ids)
    toc_rows = ""
    for section in TABLE_OF_CONTENTS:
        section_rows = ""
        for chapter in section["chapters"]:
            cid = chapter["id"]
            if cid not in selected:
                continue
            chapter_anchor = f"#chapter-{cid.lower()}"
            section_rows += (
                f'<tr><td class="toc-id">{escape(cid)}</td>'
                f'<td><a class="toc-link" href="{chapter_anchor}">{escape(chapter["title"])}</a></td>'
                f'<td class="toc-page"><a class="toc-page-ref" href="{chapter_anchor}"></a></td></tr>'
            )
        if section_rows:
            toc_rows += (
                f'<tr class="toc-section"><td colspan="3">{escape(section["section"])}</td></tr>'
                f"{section_rows}"
            )
    return f"""
<section class="frontmatter-page">
  <div class="toc-title">பொருளடக்கம் (Table of Contents)</div>
  <table class="toc-table">
    <thead>
      <tr><th>அத்தியாயம்</th><th>தலைப்பு</th><th>பக்கம்</th></tr>
    </thead>
    <tbody>{toc_rows}</tbody>
  </table>
</section>
"""


def _front_matter(chapter_ids: list[str], chapter_titles: list[str], profile: str) -> list[str]:
    del chapter_titles
    pages = [
        _render_cover_page(),
    ]
    pages.extend(_render_after_cover_pages(profile))
    pages.extend([
        _with_break(_render_foreword_page()),
        _with_break(_render_toc_page(chapter_ids)),
    ])
    return pages


def _back_cover() -> str:
    return (
        _render_cover_art_page(
            "back-cover-page chapter-break cover-art-page",
            BACK_COVER_IMAGE_REL,
        )
    )


def build_book(
    chapter_ids: list[str] | None = None,
    out_dir: str = "output_ta_print_bw",
    profile: str = "bw",
) -> tuple[Path, Path]:
    chapter_ids = chapter_ids or DEFAULT_CHAPTERS
    chapter_ids = [c.upper() for c in chapter_ids]
    profile = profile.lower()
    if profile not in {"bw", "color"}:
        raise ValueError("profile must be either 'bw' or 'color'")

    chapter_map = discover_tamil_chapters()
    chapters = [_load_chapter(cid, chapter_map) for cid in chapter_ids]
    chapter_titles = [
        getattr(ch, "CHAPTER_TITLE", cid) for ch, cid in zip(chapters, chapter_ids)
    ]

    fragments: list[str] = []
    fragments.extend(_front_matter(chapter_ids, chapter_titles, profile))

    insert_dividers = profile == "color"
    if insert_dividers:
        subject_groups: dict[str, list[int]] = {}
        for idx, cid in enumerate(chapter_ids):
            subject_groups.setdefault(cid[:1].upper(), []).append(idx)

    last_prefix: str | None = None
    for idx, ch in enumerate(chapters):
        prefix = chapter_ids[idx][:1].upper()
        if insert_dividers and prefix != last_prefix and prefix in _SUBJECT_DIVIDER_META:
            indices = subject_groups[prefix]
            fragments.append(
                _subject_divider(
                    prefix,
                    [chapter_ids[i] for i in indices],
                    [chapter_titles[i] for i in indices],
                )
            )
        last_prefix = prefix

        marker = f"{chapter_ids[idx]} · {_short_running_title(chapter_titles[idx])}"
        chapter_anchor_id = f'chapter-{chapter_ids[idx].lower()}'
        fragments.append(
            f'<h1 id="{chapter_anchor_id}" class="chapter-marker{" chapter-break" if idx == 0 else " chapter-break"}">{marker}</h1>'
        )
        fragments.append(f'<section class="subject-chapter {_subject_class(chapter_ids[idx])}">')
        fragments.extend(ch.content())
        fragments.append("</section>")

    fragments.append(_back_cover())

    html = assemble_html(
        title=f"Tamil Science Handbook ({profile.upper()}) ({_chapter_span_label(chapter_ids).replace('_', '-')})",
        css_path=_profile_css(profile),
        body_fragments=fragments,
    )
    html = _scale_inline_mm_widths(html, PRINT_SCALE)
    html = _sanitize_for_anonymous_book(html)

    out_path = ROOT / out_dir
    out_path.mkdir(parents=True, exist_ok=True)

    span = _chapter_span_label(chapter_ids)
    suffix = _profile_suffix(profile)
    out_html = out_path / f"Tamil_Science_{span}_{suffix}.html"
    out_pdf = out_path / f"Tamil_Science_{span}_{suffix}.pdf"
    out_html.write_text(html, encoding="utf-8")

    HTML = _load_weasyprint_html()
    HTML(string=html, base_url=str(ROOT)).write_pdf(str(out_pdf), optimize_size=())
    return out_pdf, out_html


def main() -> int:
    args = sys.argv[1:]
    requested: list[str] = []
    profile = "bw"
    out_dir = "output_ta_print_bw"

    idx = 0
    while idx < len(args):
        arg = args[idx]
        if arg == "--profile":
            if idx + 1 >= len(args):
                print("ERROR: --profile expects bw|color")
                return 1
            profile = args[idx + 1].lower()
            idx += 2
            continue
        if arg == "--out-dir":
            if idx + 1 >= len(args):
                print("ERROR: --out-dir expects a directory path")
                return 1
            out_dir = args[idx + 1]
            idx += 2
            continue
        requested.append(arg.upper())
        idx += 1

    if not requested:
        requested = DEFAULT_CHAPTERS

    try:
        out_pdf, out_html = build_book(requested, out_dir=out_dir, profile=profile)
        size_kb = out_pdf.stat().st_size / 1024
        print(f"Built integrated book: {out_pdf} ({size_kb:.1f} KB)")
        print(f"HTML source: {out_html}")

        import shutil
        release_subdir = "color" if profile == "color" else "print"
        release_dir = ROOT / "release" / release_subdir
        release_dir.mkdir(parents=True, exist_ok=True)
        release_pdf = release_dir / out_pdf.name
        shutil.copy2(out_pdf, release_pdf)
        print(f"\n>>> FINAL RELEASE PDF: {release_pdf}")
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
