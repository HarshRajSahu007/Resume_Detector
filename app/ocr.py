import pytesseract
from pdf2image import convert_from_path
import easyocr

def extract_text_with_tesseract(image_path):
    return pytesseract.image_to_string(image_path)


def extract_text_with_easyocr(image_path):
    reader=easyocr(['en'])
    result=reader.readtext(image_path)
    return " ".join([text[1] for text in result])


def extract_text_from_pdf(pdf_path):
    images=convert_from_path(pdf_path)
    text=""
    for image in images:
        text +=extract_text_with_tesseract(image)
    return text
