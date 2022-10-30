from difflib import SequenceMatcher
import numpy as np

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_box_center_points(box):
    x_point = (box[2] - box[0])/2
    y_point = (box[3] - box[1])/2

    return np.array([x_point, y_point])

def bbox_distance(box1, box2):
    center_points_box1 = get_box_center_points(box1)
    center_points_box2 = get_box_center_points(box2)
    
    return sum(abs(center_points_box2 - center_points_box1))


def extract_closest_value_from_key(ocr_results, key: str):
    similarity = [similar(ocr_results[i]["text"], key) for i in range(len(ocr_results))]
    key_index = np.argmax(similarity)
    distance = [bbox_distance(ocr_results[i]["bbox"], ocr_results[key_index]["bbox"]) for i in range(len(ocr_results))]
    distance[key_index] = 100000
    return ocr_results[np.argmin(distance)]["text"]
