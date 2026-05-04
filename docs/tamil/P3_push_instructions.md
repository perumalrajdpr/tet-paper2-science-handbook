# 📤 P3 Chapter — Git Push Instructions

## 📁 Files to push (3 files)

| File | Path in repo | Size |
|------|--------------|------|
| `P3_heat_temperature_ta.py` | `chapters_ta_html/` | 67 KB |
| `NotoSansTamil-Regular.ttf` | `shared/fonts/` | 72 KB |
| `NotoSansTamil-Bold.ttf` | `shared/fonts/` | 76 KB |

---

## 🚀 Quick Push (5 steps)

Open terminal, navigate to your local repo, and run:

```bash
# 1. Navigate to your local repo
cd /path/to/tet-paper2-science-handbook

# 2. Pull latest from remote (safety)
git pull origin main

# 3. Copy downloaded files to correct locations
#    (Replace ~/Downloads with your actual download path)
cp ~/Downloads/P3_heat_temperature_ta.py chapters_ta_html/
cp ~/Downloads/NotoSansTamil-Regular.ttf shared/fonts/
cp ~/Downloads/NotoSansTamil-Bold.ttf shared/fonts/

# 4. Stage and commit
git add chapters_ta_html/P3_heat_temperature_ta.py
git add shared/fonts/NotoSansTamil-Regular.ttf
git add shared/fonts/NotoSansTamil-Bold.ttf

git commit -m "P3: Heat & Temperature chapter (Tamil) — Manual-aligned

- Translated using TN textbook + NMMS Manual (Mohan & Ramesh) as authoritative source
- 16 sections: A (Heat) → J (Memory aid with 9 distinctions)
- Modern Noto Sans Tamil fonts (v2.001) embedded for proper glyph rendering
- 73+ terminology corrections applied (வெப்பநிலைமானி, நிலக்காற்று, குளிர்தல், etc.)
- Chapter-local CSS override for cleaner J-section pagination
- 13 pages, 0 margin overflows"

# 5. Push to GitHub
git push origin main
```

---

## ✅ Verification (after push)

Visit: https://github.com/perumalrajdpr/tet-paper2-science-handbook

Check:
- [ ] `chapters_ta_html/P3_heat_temperature_ta.py` appears
- [ ] `shared/fonts/NotoSansTamil-{Regular,Bold}.ttf` updated
- [ ] Commit message shows correctly

---

## 🔧 If you hit auth issues

GitHub may ask for credentials. Use **Personal Access Token (PAT)**:

1. Generate at: https://github.com/settings/tokens
2. Scope: `repo`
3. Use as password when git prompts

---

## 📝 What changed

### P3_heat_temperature_ta.py (NEW)
- 13-page Tamil chapter on Heat & Temperature
- Sections A-J with full TN textbook + NMMS Manual alignment
- Authoritative terminology (verified against NMMS Manual by Mohan & Ramesh)

### Noto Sans Tamil fonts (UPDATED)
- Previous: 304 KB (broken — were actually HTML files due to GitHub raw-content block)
- Current: 72/76 KB (genuine v2.001 from `apt fonts-noto`)
- Fixes: Modern glyph shapes for `லை`, `ணா`, `ஞா`, etc.

---

## 🐛 Troubleshooting

**Q: Build fails after push — fonts not found?**  
A: Run `pip install -r requirements.txt` in repo, ensure WeasyPrint installed

**Q: Tamil characters render wrong?**  
A: System needs font cache refresh: `fc-cache -fv`

**Q: Want to test locally first before push?**  
A: Run `python chapters_ta_html/P3_heat_temperature_ta.py` — should produce PDF in `/mnt/user-data/outputs/` or wherever your build script targets

---

✅ **All set.** நீங்களே push செய்துவிடுங்கள் ஐயா!
