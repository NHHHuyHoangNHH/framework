from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from modules.detect_pole.model import model, class_name, conf_threshold, iou_threshold
from core.utils import load_image, draw_results, image_to_bytes
from core.inference import run_inference
from io import BytesIO

router = APIRouter(prefix="/detect/pole", tags=["Detect Pole"])

@router.post("/")
async def detect_pole(file: UploadFile = File(...)):
    img = load_image(await file.read())
    results = run_inference(model, img, conf=conf_threshold, iou=iou_threshold)
    output_img = draw_results(img, results, class_name)
    return StreamingResponse(BytesIO(image_to_bytes(output_img)), media_type="image/jpeg")