# 📌 Invoice OCR Extractor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/YOUR_USERNAME/YOUR_REPO)

A Python-based OCR invoice extractor that automatically reads invoices from a single input folder (PDFs or images), extracts key invoice fields and line items, and exports the results to a clean Excel report.



---

## 🚀 Features

- Supports PDF and image formats (JPG, PNG, TIFF, BMP)

- Automatic conversion of PDFs to images using Poppler

- OCR using EasyOCR

- Extracts invoice fields (supplier, date, total, etc.)

- Extracts line items (description, quantity, price, etc.)

- Exports results to Excel with formatted borders

- Works with multiple invoices at once

- Adds invoice file name for traceability



---



## 🗂️ Folder Structure

```bash
Invoice-ocr-extractor/
│
├── data/
│ ├── input/ # Drop all invoices here (PDF or images)
│ ├── output/ # Result Excel file saved here
│ └── samples/ # Sample invoices (optional)
│
├── src/
│ ├── load_document.py # Load PDF/Image files
│ ├── ocr_engine.py # OCR processing (EasyOCR)
│ ├── text_cleaning.py # Clean extracted text
│ ├── field_extraction.py # Extract invoice fields
│ ├── line_items_extraction.py# Extract line items
│ ├── export.py # Export to Excel with borders
│
├── main.py # Main program
└── README.md # Project documentation

```

<img width="1536" height="1024" alt="Invoice OCR extraction process overview" src="https://github.com/user-attachments/assets/0faeeca1-a820-4bf2-b331-efea3abb8ce3" />

---

## 🧰 Requirements

- Python 3.8+
- Windows OS (recommended)
- Poppler installed (for PDF conversion)

---

## ✅ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Invoice-ocr-extractor.git
cd Invoice-ocr-extractor
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install Poppler (Windows)

Download Poppler for Windows and extract it to:

```bash
C:\poppler
```

Make sure the folder contains:

```bash
C:\poppler\Library\bin\pdfinfo.exe
C:\poppler\Library\bin\pdftoppm.exe
```
---

### 🔧 Configuration

Update the path in main.py:

```bash
input_folder = r"C:\Users\khadi\Desktop\Git_share\Invoice-ocr-extractor\data\input"
output_file = r"C:\Users\khadi\Desktop\Git_share\Invoice-ocr-extractor\data\output\all_invoice_output.xlsx"
```

---

### ▶️ Usage

### 1. Put your PDF or image invoices into:

```bash
data/input/
```
---

### 2. Run the project:

```bash
python main.py
```

---
### 3. Output Excel file will be generated:

```bash
data/output/all_invoice_output.xlsx
```

---

### 📌 Output Example

The Excel file contains two sheets:

### 1. Invoices

| invoice_file | supplier | date | total |
| ------------ | -------- | ---- | ----- |
| inv1.pdf     | ...      | ...  | ...   |


### 2. Line_Items

| invoice_file | description | qty | price |
| ------------ | ----------- | --- | ----- |

All tables are formatted with borders for a professional look.

---

### ⚠️ Troubleshooting

PDF conversion error: poppler_path

If you get:

```bash
PDFInfoNotInstalledError
```

➡️ Make sure Poppler is installed and the path is correct.

---
### 🧩 Contribution

Contributions are welcome!
If you want to add features or improve extraction accuracy, feel free to open an issue or submit a pull request.

---

### 👩‍💻 Author

Eng. Khadija Bouadi


### 📧 Contact

For any queries, reach out to:

GitHub: @khadibd

Email:  khadibd00@gmail.com 


