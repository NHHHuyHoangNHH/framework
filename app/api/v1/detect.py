from fastapi import APIRouter
from modules.detect_pole.router import router as detect_pole_router

router = APIRouter(tags=["Detect"])

router.include_router(detect_pole_router)