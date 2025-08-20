import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import logging
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_image(file_content: bytes) -> np.ndarray:
    img = Image.open(BytesIO(file_content))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def draw_results(img: np.ndarray, results, class_names: dict, task: str = "detect", backend: str = "yolo") -> np.ndarray:
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f"{class_names.get(cls, 'poles')} {conf:.2f}"
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return img

def image_to_bytes(img: np.ndarray) -> bytes:
    _, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes()