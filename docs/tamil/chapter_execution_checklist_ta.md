# Tamil Chapter Execution Checklist

Use this checklist before marking any Tamil chapter as done.

## 1) Scope & Source
- [ ] English source chapter in `chapters/` is read fully.
- [ ] Tamil target file is in `chapters_ta_html/`.
- [ ] English source file remains unmodified.

## 2) Structure
- [ ] Sections follow `A` to `J` only.
- [ ] Section `I` contains solved numericals (`prob_grid`), 4-8 problems.
- [ ] Section `J` uses memory-aid pattern (values/formulas + events + distinctions).
- [ ] No separate `K` glossary section.

## 3) Builder Selection
- [ ] `def_list` used for most definition/type blocks.
- [ ] `grid` used only for true multi-attribute comparison.
- [ ] `one_liners` used for bullet facts.
- [ ] `two_col` used only for genuine side-by-side contrasts.
- [ ] No deprecated use of bulky definition tables.

## 4) Terminology Quality
- [ ] TN textbook term is used wherever available.
- [ ] First-use format includes English in parentheses.
- [ ] No banned variants (`நியமம்`, `சிற்றலகு`, `குறை அளவீடு` etc.).
- [ ] Transliteration kept for accepted scientific terms where required.

## 5) Translation Integrity
- [ ] Every numerical statement preserves subject-object clarity.
- [ ] Units, symbols, formula values match source exactly.
- [ ] No mid-sentence awkward English fragments.
- [ ] Competitive-exam-neutral language used (no exam-specific labels like "TET Trap").

## 6) Layout Discipline
- [ ] WeasyPrint path only.
- [ ] All table colgroups are explicit.
- [ ] Each table width sum is exactly `174mm`.
- [ ] No emoji in section headers/titles.

## 7) Formatting Consistency
- [ ] Indian number grouping applied where relevant.
- [ ] Unicode scientific superscripts/subscripts are correct.
- [ ] Operator spacing is consistent (`=`, `×`, `÷`, `−`).

## 8) Build & Verification
- [ ] Chapter builds successfully via WeasyPrint.
- [ ] Overflow verification reports zero margin overflows.
- [ ] Visual QA done for wraps, table breaks, and page breaks.

## 9) Final Pre-Submit Grep
- [ ] Search for `TET` returns no unintended usage.
- [ ] Search for banned wrong terms returns no matches.
- [ ] Search for mixed-language formatting anomalies returns no matches.

## 10) Delivery
- [ ] Final chapter file ready in `chapters_ta_html/`.
- [ ] Output PDF generated.
- [ ] Notes captured for glossary updates and unresolved terminology decisions.
