@echo off
rem Einmalige Installation: legt eine eigene Python-Umgebung im Ordner .venv an und installiert MarkItDown (keine Adminrechte noetig).
cd /d "%~dp0"
set PY=python
where py >nul 2>nul && set PY=py
%PY% -m venv .venv
if errorlevel 1 (
  echo Python wurde nicht gefunden. Bitte pruefen, ob "python --version" in der Eingabeaufforderung funktioniert.
  pause
  exit /b 1
)
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt
if errorlevel 1 (
  echo Installation fehlgeschlagen, siehe Meldungen oben.
  pause
  exit /b 1
)
echo.
echo Installation abgeschlossen. PDFs jetzt einfach auf pdf2md.bat ziehen.
pause
