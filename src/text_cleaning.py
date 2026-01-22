import re
import unicodedata


class TextCleaner:

    @staticmethod
    def normalize_text(text: str) -> str:
        text = unicodedata.normalize("NFKC", text)

        # Remove extra spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Remove multiple empty lines
        text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()

    @staticmethod
    def normalize_numbers(text: str) -> str:
        """
        Converts:
        1.250,00 -> 1250.00
        1,250.00 -> 1250.00
        """
        # European format
        text = re.sub(r"(\d+)\.(\d{3}),(\d{2})", r"\1\2.\3", text)

        # US format
        text = re.sub(r"(\d+),(\d{3})\.(\d{2})", r"\1\2.\3", text)

        return text

    @staticmethod
    def normalize_currency(text: str) -> str:
        currency_map = {
            "€": "EUR",
            "$": "USD",
            "£": "GBP",
            "dh": "MAD",
            "dhs": "MAD",
            "درهم": "MAD"
        }

        for k, v in currency_map.items():
            text = re.sub(rf"\b{k}\b", v, text, flags=re.IGNORECASE)

        return text

    @staticmethod
    def normalize_dates(text: str) -> str:
        """
        Normalize dates to YYYY-MM-DD
        """
        # DD/MM/YYYY
        text = re.sub(
            r"\b(\d{2})[/-](\d{2})[/-](\d{4})\b",
            r"\3-\2-\1",
            text
        )

        return text

    @classmethod
    def clean(cls, text: str) -> str:
        text = cls.normalize_text(text)
        text = cls.normalize_numbers(text)
        text = cls.normalize_currency(text)
        text = cls.normalize_dates(text)
        return text
