import io
import pdfplumber


def extract_text_from_pdf(pdf_bytes):
    text = ""

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_tables_from_pdf(pdf_bytes):
    tables = []

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            extracted_tables = page.extract_tables()

            if extracted_tables:
                tables.extend(extracted_tables)

    return tables