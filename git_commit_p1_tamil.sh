#!/bin/bash
# ============================================================================
# Tamil Edition P1 — Git Commit Script
# Run from your local repo root after copying files in place.
# ============================================================================

set -e  # Exit on any error

echo "=== Step 1: Verify directory structure ==="
mkdir -p chapters_ta_html
mkdir -p shared/fonts
mkdir -p shared/css
mkdir -p shared/builders

echo "=== Step 2: Verify files exist ==="
files=(
  "chapters_ta_html/P1_measurement_ta.py"
  "shared/fonts/NotoSansTamil-Regular.ttf"
  "shared/fonts/NotoSansTamil-Bold.ttf"
  "shared/css/handbook_ta.css"
  "shared/builders/__init__.py"
  "shared/builders/html_builders.py"
  "output/P1_measurement_ta.pdf"
  "requirements.txt"
)
for f in "${files[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "❌ MISSING: $f"
    echo "   → Place it in correct location before running this script."
    exit 1
  else
    echo "✅ Found: $f"
  fi
done

echo ""
echo "=== Step 3: Show what will be committed ==="
git status

echo ""
read -p "Continue with commit? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

echo "=== Step 4: Stage Tamil-specific files ==="

# Tamil chapter source
git add chapters_ta_html/P1_measurement_ta.py

# Shared infrastructure (NEW for Tamil pipeline)
git add shared/fonts/NotoSansTamil-Regular.ttf
git add shared/fonts/NotoSansTamil-Bold.ttf
git add shared/css/handbook_ta.css
git add shared/builders/__init__.py
git add shared/builders/html_builders.py

# Final output PDF
git add output/P1_measurement_ta.pdf

# Updated project meta files
git add requirements.txt
git add README.md       # if you updated it with Tamil section
git add .gitignore      # if you appended Tamil-specific ignores

echo ""
echo "=== Step 5: Commit ==="
git commit -m "Add Tamil edition — P1 அளவீடு (Measurement) chapter

- New chapters_ta_html/ directory for Tamil chapter sources
- New shared/ infrastructure: WeasyPrint-based HTML/CSS pipeline
  - shared/fonts/NotoSansTamil-{Regular,Bold}.ttf
  - shared/css/handbook_ta.css (master stylesheet)
  - shared/builders/html_builders.py (builder library)
- P1 அளவீடு: 12 pages, 10 sections (A through J)
- Generic competitive exam scope (TNTET, TNPSC, TRB, NMMS, NTSE)
- TN textbook-aligned terminology

Engine: WeasyPrint (Pango+HarfBuzz) — required for proper Tamil shaping.
ReportLab cannot shape Tamil ligatures (வீ, ணை, கொ/கோ).

Co-authored-by: த. பெருமாள்ராஜ் <perumalraj@chalkpiecediary.com>"

echo ""
echo "=== Step 6: Push (manual — run when ready) ==="
echo "git push origin main"
echo ""
echo "✅ Done!"
