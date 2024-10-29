import cv2
import numpy as np
from PIL import Image
import pytesseract

# Specify Tesseract path if needed (Windows example)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Load the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    img = cv2.convertScaleAbs(img, alpha=1.5, beta=20)

    # Resize the image to enhance small text (optional)
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    # Apply Gaussian Blur to reduce noise
    img = cv2.GaussianBlur(img, (5, 5), 1)

    # Binarize the image (convert to pure black and white)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the preprocessed image (optional, for debugging)
    cv2.imwrite("preprocessed_image.png", img)

    return img

def extract_text_from_image(image_path):
    # Preprocess the image
    preprocessed_img = preprocess_image(image_path)

    # Convert OpenCV image back to PIL format for Tesseract
    pil_img = Image.fromarray(preprocessed_img)

    # Configure Tesseract with PSM 6 (block of text) and OEM 1 (LSTM)
    custom_config = r'--oem 1 --psm 6'

    # Extract text from the preprocessed image
    extracted_text = pytesseract.image_to_string(pil_img, config=custom_config)

    print("Extracted Text:\n", extracted_text)

# Specify the path to your image
image_path = "./img/02.webp"

extract_text_from_image(image_path)
