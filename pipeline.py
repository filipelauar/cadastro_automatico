import cv2
import os
from ocr.easyOCR import apply_ocr
from information_extraction import extract_information

img_path = "images"
img_names = os.listdir(img_path)
for img_name in img_names:
    image = cv2.imread(os.path.join(img_path, img_name))
    ocr_results = apply_ocr(image)
    matricula = extract_information.extract_closest_value_from_key(ocr_results, "matricula")