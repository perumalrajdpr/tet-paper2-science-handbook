# WeasyPrint Setup (Windows)

Tamil HTML chapter builds require native GTK/Pango libraries in addition to the Python package.

## 1) Install Python package

```powershell
python -m pip install weasyprint
```

## 2) Install GTK runtime (required)

Install a GTK3 runtime that provides these DLLs:
- `libgobject-2.0-0.dll`
- `libpango-1.0-0.dll`
- `libcairo-2.dll`

Recommended options:
- MSYS2 + `mingw-w64-ucrt-x86_64-gtk3`
- or a standard Windows GTK runtime bundle

## 3) Ensure DLL path is available

Add the GTK `bin` directory to Windows `PATH`, then open a new terminal.

## 4) Verify build

```powershell
python build/build_tamil_chapter.py P1
```

Expected output file:
- `output_ta/P1_measurement_ta.pdf`

## 5) Tamil fonts

Place these in `shared/fonts/`:
- `NotoSansTamil-Regular.ttf`
- `NotoSansTamil-Bold.ttf`

