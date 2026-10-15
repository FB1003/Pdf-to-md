@echo off
rem Optional: installiert zusaetzlich Docling (gruendlicher, OCR fuer Scans, aber ca. 1-2 GB).
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Bitte zuerst install.bat ausfuehren.
  pause
  exit /b 1
)
.venv\Scripts\python -m pip install -r requirements-docling.txt
if errorlevel 1 (
  echo Installation fehlgeschlagen, siehe Meldungen oben.
  pause
  exit /b 1
)
echo.
echo Docling installiert. pdf2md.bat verwendet ab jetzt automatisch Docling.
pause
