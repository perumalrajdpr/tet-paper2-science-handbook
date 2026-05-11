# பதிப்பு திருத்த குறிப்புகள் (Edit Notes)

> நீங்கள் PDF-ஐ வாசிக்கும் போது குறிப்புகளை இங்கே எழுதுங்கள்.
> Claude அவற்றை chapter source-ல apply செய்வார்.

## Format / எழுதும் முறை

ஒவ்வொரு குறிப்புக்கும்:
```
- [chapter] page X — what to change
   e.g.
- [P3] page 41 — Section H title "தீர்க்கப்பட்ட கணக்குகள்" → "முக்கிய கணக்குகள்"
- [B5] page 240 — "muscles" section-ல "தசை வகை" row நீக்க
- [C2] page 130 — atom structure table-ல "ஐசோடோப்" column சேர்க்க
```

## Quick build commands

```bash
# Build single chapter (fast)
python build/build_tamil_color_book.py P3

# Build full book
python build/build_tamil_color_book.py

# B/W print version
python build/build_tamil_print_bw_book.py
```

## Open files

- Chapter source: `chapters_ta_html/<CID>_*.py`
- Output PDF: `output_ta_color/Tamil_Science_*.pdf`
- Output HTML (fast preview): `output_ta_color/Tamil_Science_*.html`
- Final release: `release/color/Tamil_Science_*.pdf`

---

## P1 · அளவீடு

(notes here…)

## P2 · விசை, இயக்கம் & அழுத்தம்

(notes here…)

## P3 · வெப்பம் & வெப்பநிலை

(notes here…)

## P4 · ஒளியியல்

(notes here…)

## P5 · மின்னியல்

(notes here…)

## P6 · காந்தவியல்

(notes here…)

## P7 · ஒலியியல்

(notes here…)

## P8 · அண்டம் & விண்வெளி

(notes here…)

## C1 · நம்மைச் சுற்றியுள்ள பருப்பொருள்கள்

(notes here…)

## C2 · அணு அமைப்பு

(notes here…)

## C3 · நம்மைச் சுற்றி நிகழும் மாற்றங்கள்

(notes here…)

## C4 · காற்று

(notes here…)

## C5 · நீர்

(notes here…)

## C6 · அமிலம், காரம் & உப்புகள்

(notes here…)

## C7 · அன்றாட வாழ்வில் வேதியியல்

(notes here…)

## B1 · உயிரின அடிப்படை அலகு — செல்

(notes here…)

## B2 · வகைப்பாட்டியல்

(notes here…)

## B3 · தாவர உலகம்

(notes here…)

## B4 · விலங்கு உலகம் & உயிரியல் ஒருங்கமைவு

(notes here…)

## B5 · மனித உறுப்பு மண்டலங்கள்

(notes here…)

## B6 · சுகாதாரம் & தொற்று நோய்கள்

(notes here…)

## B7 · பயிர் உற்பத்தி & மேலாண்மை

(notes here…)

## B8 · சுற்றுச்சூழல் & உயிரின பாதுகாப்பு

(notes here…)
