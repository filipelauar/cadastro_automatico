import cv2
import os
from ocr.easyOCR import apply_ocr

img_path = "images"
img_names = os.listdir(img_path)
for img_name in img_names:
    image = cv2.imread(os.path.join(img_path, img_name))
    ocr_results = apply_ocr(image)