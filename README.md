# PDF → Markdown (lokal, Open Source)

Kleines Werkzeug, das PDF-Dateien lokal auf dem eigenen Rechner in Markdown (`.md`) umwandelt. Es braucht keine Adminrechte und schickt keine Daten an externe Dienste. Im Hintergrund arbeitet eine von zwei kostenlosen Open-Source-Bibliotheken, beide unter **MIT-Lizenz**:

| Engine | Projekt | Größe | Stärken | Schwächen |
|---|---|---|---|---|
| `markitdown` (Standard) | [MarkItDown](https://github.com/microsoft/markitdown) (Microsoft) | ca. 250 MB | klein, schnell, kein Download beim ersten Lauf | liefert bei PDFs im Wesentlichen reinen Text ohne Überschriften- und Tabellenstruktur, keine Texterkennung für Scans |
| `docling` (optional) | [Docling](https://github.com/docling-project/docling) (IBM Research, LF AI & Data Foundation) | ca. 1–2 GB | erkennt Überschriften, Listen, Tabellen und Lesereihenfolge, OCR für Scans | große Installation, lädt beim ersten Lauf einmalig Modelle von Hugging Face |

## Installation (Windows)

1. Diesen Ordner an einen beliebigen Ort kopieren, z. B. `C:\Users\<Name>\Tools\pdf-to-md`.
2. Doppelklick auf **`install.bat`**. Das Skript legt im Ordner eine eigene Python-Umgebung (`.venv`) an und installiert dort MarkItDown.
3. Optional: Doppelklick auf **`install-docling.bat`**, um zusätzlich Docling zu installieren. Danach wird automatisch Docling verwendet.

## Benutzung

**Am einfachsten:** eine oder mehrere PDFs (oder einen ganzen Ordner) mit der Maus auf **`pdf2md.bat`** ziehen. Die `.md`-Datei wird jeweils neben der PDF abgelegt.

**Über die Eingabeaufforderung** (im Programmordner):

```bat
.venv\Scripts\python pdf2md.py "C:\Pfad\zur\datei.pdf"
.venv\Scripts\python pdf2md.py "C:\Pfad\zum\Ordner" -o "C:\Pfad\Ausgabe"
.venv\Scripts\python pdf2md.py datei.pdf --engine markitdown   :: MarkItDown erzwingen
.venv\Scripts\python pdf2md.py datei.pdf --ocr                 :: eingescannte PDFs (nur Docling)
```

## macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -r requirements-docling.txt   # optional
.venv/bin/python pdf2md.py datei.pdf
```

## Hinweise

- **Struktur:** MarkItDown übernimmt bei PDFs Überschriften und Tabellen nicht als Markdown-Formatierung. Wer gegliederte Ausgaben mit Tabellen braucht, sollte Docling nachinstallieren.
- **Scans:** Bilder-PDFs ohne Textebene liefern nur mit Docling und `--ocr` brauchbaren Text.
- **Erster Lauf mit Docling:** Docling lädt einmalig seine Modelle von `huggingface.co`. Blockiert ein Firmen-Proxy diese Adresse, die Modelle auf einem anderen Rechner mit `docling-tools models download` laden und in den Cache-Ordner kopieren.
