from fastapi import FastAPI
from api.v1.detect import router as detect_router

app = FastAPI(title="CT UAV Detection API", version="1.0.0")

app.include_router(detect_router, prefix="/v1")