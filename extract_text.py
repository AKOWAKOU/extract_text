from PIL import Image
import pytesseract

path_to_tesseract = r"/usr/bin/tesseract"  
pytesseract.tesseract_cmd = path_to_tesseract

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
