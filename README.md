# PDF → Markdown (lokal, Open Source)

Kleines Werkzeug, das PDF-Dateien lokal auf dem eigenen Rechner in Markdown (`.md`) umwandelt. Es braucht keine Adminrechte und schickt keine Daten an externe Dienste. Im Hintergrund arbeitet eine von zwei Open-Source-Bibliotheken, beide unter **MIT-Lizenz**:

| Engine | Projekt | Stärken | Schwächen |
|---|---|---|---|
| `docling` (Standard) | [Docling](https://github.com/docling-project/docling) (IBM Research, LF AI & Data Foundation) | erkennt Überschriften, Listen, Tabellen und Lesereihenfolge, optional OCR für Scans | große Installation (ca. 1–2 GB unter Windows), lädt beim ersten Lauf einmalig Modelle von Hugging Face |
| `markitdown` | [MarkItDown](https://github.com/microsoft/markitdown) (Microsoft) | klein und schnell | liefert bei PDFs im Wesentlichen reinen Text ohne Überschriften- und Tabellenstruktur |

## Installation (Windows)

1. Diesen Ordner an einen beliebigen Ort kopieren, z. B. `C:\Users\<Name>\Tools\pdf-to-md`.
2. Doppelklick auf **`install.bat`**. Das Skript legt im Ordner eine eigene Python-Umgebung (`.venv`) an und installiert dort Docling und MarkItDown. Das dauert einige Minuten.

## Benutzung

**Am einfachsten:** eine oder mehrere PDFs (oder einen ganzen Ordner) mit der Maus auf **`pdf2md.bat`** ziehen. Die `.md`-Datei wird jeweils neben der PDF abgelegt.

**Über die Eingabeaufforderung** (im Programmordner):

```bat
.venv\Scripts\python pdf2md.py "C:\Pfad\zur\datei.pdf"
.venv\Scripts\python pdf2md.py "C:\Pfad\zum\Ordner" -o "C:\Pfad\Ausgabe"
.venv\Scripts\python pdf2md.py datei.pdf --ocr                 :: eingescannte PDFs
.venv\Scripts\python pdf2md.py datei.pdf --engine markitdown   :: schnelle Variante
```

## macOS / Linux

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python pdf2md.py datei.pdf
```

## Hinweise

- **Erster Lauf mit Docling:** Docling lädt einmalig seine Layout- und Tabellenmodelle von `huggingface.co` herunter. Blockiert ein Firmen-Proxy diese Adresse, entweder `--engine markitdown` verwenden oder die Modelle auf einem anderen Rechner mit `docling-tools models download` laden und in den Cache-Ordner kopieren.
- **Scans:** Bilder-PDFs ohne Textebene liefern nur mit `--ocr` brauchbaren Text.
- **Docling direkt:** Docling bringt auch ein eigenes Kommandozeilenprogramm mit, z. B. `.venv\Scripts\docling datei.pdf --to md --output Ausgabe`.
