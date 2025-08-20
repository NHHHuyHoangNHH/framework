from ultralytics import YOLO
import numpy as np
import yaml
import os

def load_model(model_path: str) -> YOLO:
    return YOLO(model_path)

def run_inference(model: YOLO, img: np.ndarray, conf: float, iou: float) -> any:
    results = model(img, conf=conf, iou=iou)
    return results