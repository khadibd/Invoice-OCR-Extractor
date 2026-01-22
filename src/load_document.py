import os
from pdf2image import convert_from_path
from PIL import Image

SUPPORTED_IMAGES = (".png", ".jpg", ".jpeg", ".tiff", ".bmp")

def load_document(input_folder):
    if not os.path.isdir(input_folder):
        raise FileNotFoundError("Input folder not found")

    documents = []

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)

        # 📄 PDF → images
        if file.lower().endswith(".pdf"):
            images = convert_from_path(
                file_path,
                dpi=300,
                poppler_path=r"C:\Users\khadi\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"
            )
            documents.append((file, images))

        # 🖼 Image → load directly
        elif file.lower().endswith(SUPPORTED_IMAGES):
            image = Image.open(file_path).convert("RGB")
            documents.append((file, [image]))

        # ❌ Ignore unsupported files
        else:
            print(f"Skipped unsupported file: {file}")

    if not documents:
        raise ValueError("No supported files found in input folder")

    return documents
