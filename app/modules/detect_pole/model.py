from core.inference import load_model
from core.config import settings
import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(CONFIG_PATH, 'r') as f:
    CONFIG = yaml.safe_load(f)

MODEL_PATH = os.path.join(settings.MODEL_DIR, CONFIG['model_file'])
model = load_model(MODEL_PATH)
class_name = CONFIG.get('class_names', {"0": "pole"})
conf_threshold = CONFIG.get('conf_threshold', settings.DEFAULT_CONF_THRESHOLD)
iou_threshold = CONFIG.get('iou_threshold', settings.DEFAULT_IOU_THRESHOLD)