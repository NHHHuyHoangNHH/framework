from pydantic import BaseSettings

class Settings(BaseSettings):
    MODEL_DIR: str = "models/"
    DEFAULT_CONF_THRESHOLD: float = 0.5
    DEFAULT_IOU_THRESHOLD: float = 0.45
    
settings = Settings()