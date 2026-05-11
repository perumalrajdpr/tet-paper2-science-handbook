# Authoring Roadmap

## Current state — TET Paper II Science Handbook (this book)

- Authoring format: **Python files** (`chapters_ta_html/*_ta.py`)
- Each chapter calls builder functions from `shared/builders/html_builders.py`:
  `sec()`, `subh()`, `def_list()`, `kv_list()`, `one_liners()`, `grid()`,
  `rapid_3col()`, `pill()`, `dyk()`, `note_box()`, `prob()`, `gloss_2col()`,
  `term_pairs()`, `para()`, `footer()`.
- Build pipeline: chapters → `assemble_html()` → WeasyPrint → PDF
- 23 chapters · 3 output formats (color PDF, B/W print PDF, web HTML)

This book stays in `.py` format. **No migration.** It's working, tested, and
shipping. Touching it risks breakage.

---

## Next book onwards — Markdown authoring

**Decision: switch to `.md` for the next book and all future books.**

### Why
- Subject experts (non-coders) can write chapters directly
- 90% Tamil content, 10% structure (vs 30/70 with Python)
- Clean git diffs, easy review on GitHub / WhatsApp
- Copy-paste sections between books
- Lower typo risk (no commas/quotes/brackets breaking builds)

### What needs to be built (when next book starts)

1. **`build/md_to_html.py`** — parser:
   - YAML frontmatter (chapter id, title, subject, classes, etc.)
   - Standard markdown for headings → `sec()` / `subh()`
   - Custom fenced directives → builder calls:
     ```markdown
     :::defs           → def_list()
     :::kv             → kv_list()
     :::grid widths=…  → grid()
     :::rapid          → rapid_3col()
     :::pill icon=★    → pill()
     :::dyk title=…    → dyk()
     :::note title=…   → note_box()
     :::prob num=1     → prob() / probc()
     :::gloss          → gloss_2col()
     :::twocol         → two_col()
     ```
   - Plain markdown for paragraphs, bold (`**`), italics (`*`),
     inline code (`` ` ``), tables (raw markdown)

2. **`build/build_book_md.py`** — orchestrator:
   - Walks `chapters_md/*.md` (or per-book dir)
   - Parses each MD → fragments
   - Runs through same `assemble_html()` + WeasyPrint pipeline
   - Outputs to same `release/<color|print|web>/` structure

3. **`templates/`**:
   - `chapter_template.md` — starter file with all directive examples
   - `book_config.yaml` — series/book-level config (title, authors, ISBN, …)

4. **`docs/MARKDOWN_AUTHORING.md`** — Tamil authoring guide for contributors

### Effort estimate
- Parser + orchestrator: ~6-8 hours
- Tune output to match current visual quality: ~2-3 hours
- Authoring guide + templates: ~1 hour
- **Total: ~1 day of focused work**

This is a **one-time investment** that pays off for every future book.

### Migration of this book? — NO
- Current book in `.py` stays as-is
- New books use `.md` from chapter 1

---

## Books planned (rough wishlist — update as decisions firm up)

- [x] TET Paper II Science — current, `.py`
- [ ] **TNPSC General Studies** — next? `.md`
- [ ] TRB Mathematics handbook — `.md`
- [ ] 10th/12th Public exam Science guides — `.md`
- [ ] General Science classes 6-8 — `.md`
- [ ] Tamil literature exam guide — `.md`

Each book = new repo OR new folder in this monorepo. Decision later.

---

## Trigger point — when to start markdown engine

When **any of these** happens, start building MD engine:
1. Current TET book is locked (no more content edits) AND
2. Next book scope/title decided OR
3. New author (non-coder) joins and needs to write a chapter
