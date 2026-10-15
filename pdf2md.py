"""PDF -> Markdown converter (wrapper around Docling or MarkItDown).

Usage:
    python pdf2md.py datei.pdf [weitere.pdf ...]
    python pdf2md.py ordner/                 # alle PDFs im Ordner (rekursiv)
    python pdf2md.py datei.pdf -o ausgabe/   # Zielordner festlegen
    python pdf2md.py datei.pdf --engine markitdown

Die .md-Datei wird standardmäßig neben der PDF abgelegt.
"""

import argparse
import sys
from pathlib import Path


def collect_pdfs(inputs):
    pdfs = []
    for item in inputs:
        path = Path(item)
        if path.is_dir():
            pdfs.extend(sorted(p for p in path.rglob("*") if p.suffix.lower() == ".pdf"))
        elif path.is_file() and path.suffix.lower() == ".pdf":
            pdfs.append(path)
        else:
            print(f"Übersprungen (keine PDF gefunden): {item}", file=sys.stderr)
    return pdfs


def make_docling_converter(ocr):
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    options = PdfPipelineOptions()
    options.do_ocr = ocr
    options.do_table_structure = True
    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=options)}
    )
    return lambda pdf: converter.convert(pdf).document.export_to_markdown()


def make_markitdown_converter():
    from markitdown import MarkItDown

    converter = MarkItDown()
    return lambda pdf: converter.convert(str(pdf)).text_content


def main():
    parser = argparse.ArgumentParser(description="Wandelt PDF-Dateien in Markdown um.")
    parser.add_argument("inputs", nargs="+", help="PDF-Dateien oder Ordner")
    parser.add_argument("-o", "--output", help="Zielordner (Standard: neben der PDF)")
    parser.add_argument(
        "--engine",
        choices=["docling", "markitdown"],
        default="docling",
        help="docling = gute Struktur/Tabellen (Standard), markitdown = schnell und einfach",
    )
    parser.add_argument(
        "--ocr",
        action="store_true",
        help="Texterkennung für eingescannte PDFs aktivieren (nur docling, langsamer)",
    )
    args = parser.parse_args()

    pdfs = collect_pdfs(args.inputs)
    if not pdfs:
        print("Keine PDF-Dateien gefunden.", file=sys.stderr)
        return 1

    if args.engine == "docling":
        convert = make_docling_converter(args.ocr)
    else:
        convert = make_markitdown_converter()

    out_dir = Path(args.output) if args.output else None
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)

    failed = 0
    for i, pdf in enumerate(pdfs, 1):
        target = (out_dir or pdf.parent) / (pdf.stem + ".md")
        print(f"[{i}/{len(pdfs)}] {pdf.name} -> {target}")
        try:
            target.write_text(convert(pdf), encoding="utf-8")
        except Exception as exc:  # eine defekte PDF soll den Stapel nicht abbrechen
            failed += 1
            print(f"    Fehler: {exc}", file=sys.stderr)

    print(f"Fertig: {len(pdfs) - failed} erfolgreich, {failed} fehlgeschlagen.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
