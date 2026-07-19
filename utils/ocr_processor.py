import io                      

import pytesseract

from PIL import Image


def extract_text_from_image(image_bytes):

    image = Image.open(
        io.BytesIO(image_bytes)
    )

    text = pytesseract.image_to_string(
        image
    )

    return text


def extract_text_from_scanned_pdf(file_bytes):

    import fitz

    pdf = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    extracted_text = ""

    for page in pdf:

        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        image_bytes = pix.tobytes(
            "png"
        )

        page_text = extract_text_from_image(
            image_bytes
        )

        extracted_text += page_text + "\n"

    return extracted_text