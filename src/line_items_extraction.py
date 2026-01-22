import re


class LineItemExtractor:

    def __init__(self, text: str):
        self.lines = [l.strip() for l in text.split("\n") if l.strip()]

    # -------------------------
    # Detect table zone
    # -------------------------
    def _find_table_zone(self):
        start_keywords = [
            "description", "désignation", "article", "libellé", "produit"
        ]

        end_keywords = [
            "total", "tva", "vat", "subtotal", "sous-total", "المجموع"
        ]

        start_idx, end_idx = None, None

        for i, line in enumerate(self.lines):
            if any(k in line.lower() for k in start_keywords):
                start_idx = i + 1
                break

        for i, line in enumerate(self.lines):
            if any(k in line.lower() for k in end_keywords):
                end_idx = i
                break

        if start_idx is not None:
            return self.lines[start_idx:end_idx]

        return []

    # -------------------------
    # Parse rows
    # -------------------------
    def extract_items(self):
        table_lines = self._find_table_zone()
        items = []

        for line in table_lines:
            # Match lines ending with numbers (prices)
            nums = re.findall(r"\d+\.\d{2}", line)

            if len(nums) >= 1:
                item = {
                    "description": re.sub(r"\d+\.\d{2}", "", line).strip(),
                    "quantity": 1,
                    "unit_price": nums[-1],
                    "line_total": nums[-1],
                }
                items.append(item)

        return items
