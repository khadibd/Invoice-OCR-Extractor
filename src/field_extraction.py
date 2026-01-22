import re


class InvoiceFieldExtractor:

    def __init__(self, text: str):
        self.text = text
        self.lines = [line.strip() for line in text.split("\n") if line.strip()]

    # -------------------------
    # VENDOR NAME
    # -------------------------
    def extract_vendor(self):
        """
        Heuristic:
        - Usually in first 5 lines
        - Not containing numbers
        """
        for line in self.lines[:5]:
            if not re.search(r"\d", line) and len(line) > 3:
                return line
        return None

    # -------------------------
    # INVOICE NUMBER
    # -------------------------
    def extract_invoice_number(self):
        patterns = [
            r"(invoice\s*(no|number)[:\s]*([A-Z0-9\-]+))",
            r"(facture\s*n[o°]?\s*[:\s]*([A-Z0-9\-]+))",
            r"(رقم\s*الفاتورة[:\s]*([A-Z0-9\-]+))",
        ]

        for p in patterns:
            match = re.search(p, self.text, re.IGNORECASE)
            if match:
                return match.group(match.lastindex)
        return None

    # -------------------------
    # DATE
    # -------------------------
    def extract_date(self):
        patterns = [
            r"\b(20\d{2}-\d{2}-\d{2})\b",
        ]

        for p in patterns:
            match = re.search(p, self.text)
            if match:
                return match.group(1)
        return None

    # -------------------------
    # VAT / TAX
    # -------------------------
    def extract_vat(self):
        patterns = [
            r"(vat|tva|taxe)\s*[:\s]*([\d\.]+%)",
            r"(vat|tva|taxe)\s*[:\s]*([\d\.]+)",
        ]

        for p in patterns:
            match = re.search(p, self.text, re.IGNORECASE)
            if match:
                return match.group(2)
        return None

    # -------------------------
    # TOTAL AMOUNT
    # -------------------------
    def extract_total(self):
        patterns = [
            r"(total\s*(amount|ttc)?[:\s]*([\d\.]+))",
            r"(montant\s*total[:\s]*([\d\.]+))",
            r"(المجموع[:\s]*([\d\.]+))",
        ]

        for p in patterns:
            match = re.search(p, self.text, re.IGNORECASE)
            if match:
                return match.group(match.lastindex)
        return None

    # -------------------------
    # CURRENCY
    # -------------------------
    def extract_currency(self):
        currencies = ["EUR", "USD", "GBP", "MAD"]
        for c in currencies:
            if c in self.text:
                return c
        return None

    # -------------------------
    # RUN ALL
    # -------------------------
    def extract_all(self):
        return {
            "vendor_name": self.extract_vendor(),
            "invoice_number": self.extract_invoice_number(),
            "invoice_date": self.extract_date(),
            "vat": self.extract_vat(),
            "total_amount": self.extract_total(),
            "currency": self.extract_currency(),
        }
