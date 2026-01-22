import easyocr
import numpy as np


class OCREngine:
    def __init__(self, languages=["en"]):
        self.reader = easyocr.Reader(languages, gpu=False)

    def extract_text_from_images(self, images):
        """
        Takes a list of PIL Images and returns raw extracted text
        """
        full_text = []

        for img in images:
            img_np = np.array(img)
            results = self.reader.readtext(img_np, detail=0)

            page_text = "\n".join(results)
            full_text.append(page_text)

        return "\n\n".join(full_text)
