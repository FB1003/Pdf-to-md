@echo off
rem PDFs oder Ordner per Drag-and-Drop auf diese Datei ziehen. Die .md-Datei landet neben der PDF.
if not exist "%~dp0.venv\Scripts\python.exe" (
  echo Bitte zuerst install.bat ausfuehren.
  pause
  exit /b 1
)
if "%~1"=="" (
  echo PDF-Dateien oder einen Ordner auf diese Datei ziehen.
  pause
  exit /b 1
)
"%~dp0.venv\Scripts\python.exe" "%~dp0pdf2md.py" %*
pause
