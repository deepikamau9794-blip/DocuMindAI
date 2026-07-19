from io import BytesIO

import fitz

from docx import Document

from utils.ocr_processor import (
    extract_text_from_image as ocr_extract_text_from_image,
    extract_text_from_scanned_pdf
)


def extract_text_from_pdf(file_bytes):

    pdf = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    text = ""

    for page in pdf:

        page_text = page.get_text()

        if page_text.strip():

            text += page_text + "\n"

    if text.strip():

        return text, len(pdf)

    ocr_text = extract_text_from_scanned_pdf(
        file_bytes
    )

    return ocr_text, len(pdf)


def extract_text_from_docx(file_bytes):

    document = Document(
        BytesIO(file_bytes)
    )

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():

            text += paragraph.text + "\n"

    return text, None


def extract_text_from_txt(file_bytes):

    text = file_bytes.decode(
        "utf-8",
        errors="ignore"
    )

    return text, None


def extract_text_from_image(file_bytes):

    text = ocr_extract_text_from_image(
        file_bytes
    )

    return text, None


def load_document(
    file_bytes,
    file_extension
):

    if file_extension == "pdf":

        return extract_text_from_pdf(
            file_bytes
        )

    elif file_extension == "docx":

        return extract_text_from_docx(
            file_bytes
        )

    elif file_extension == "txt":

        return extract_text_from_txt(
            file_bytes
        )

    elif file_extension in [
        "png",
        "jpg",
        "jpeg"
    ]:

        return extract_text_from_image(
            file_bytes
        )

    else:

        raise ValueError(
            "Unsupported file format"
        )