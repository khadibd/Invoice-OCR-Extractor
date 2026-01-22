import os
from src.load_document import load_document
from src.ocr_engine import OCREngine
from src.text_cleaning import TextCleaner
from src.field_extraction import InvoiceFieldExtractor
from src.line_items_extraction import LineItemExtractor
from src.export import Exporter


def main():
    # 📂 Paths
    pdf_folder = r"C:\Users\khadi\Desktop\Git_share\invoice_ocr_extractor\data\input"
    output_file = r"C:\Users\khadi\Desktop\Git_share\invoice_ocr_extractor\data\output\all_invoice_output.xlsx"

    # 📄 Load all PDFs (name + images)
    documents = load_document(pdf_folder)

    # 🔍 OCR engine
    ocr = OCREngine(languages=["en"])

    # 📊 Global storage (VERY IMPORTANT)
    all_fields = []
    all_items = []

    # 🔁 Process each PDF
    for pdf_name, images in documents:
        print(f"Processing: {pdf_name}")

        raw_text = ocr.extract_text_from_images(images)
        clean_text = TextCleaner.clean(raw_text)

        fields = InvoiceFieldExtractor(clean_text).extract_all()
        items = LineItemExtractor(clean_text).extract_items()

        # 🏷 Add PDF name for traceability
        fields["invoice_file"] = pdf_name
        for item in items:
            item["invoice_file"] = pdf_name

        all_fields.append(fields)
        all_items.extend(items)

    # 📤 Export ALL invoices to Excel
    Exporter.to_excel(all_fields, all_items, output_file)

    print("✅ All invoices exported successfully!")
    print("Output file:", output_file)


if __name__ == "__main__":
    main()
