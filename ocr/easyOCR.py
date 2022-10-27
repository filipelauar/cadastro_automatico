from easyOCR import Reader


def apply_ocr(image):
    model = Reader(["pt"])
    ocr_results = model.read_text(image)
    return ocr_results