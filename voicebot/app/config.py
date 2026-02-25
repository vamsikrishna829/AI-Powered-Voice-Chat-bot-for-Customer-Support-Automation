import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    # ===============================
    # APP SETTINGS
    # ===============================
    APP_NAME: str = "AI Voice Bot"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ===============================
    # ASR SETTINGS
    # ===============================
    ASR_MODEL_SIZE: str = "base"        # tiny, base, small, medium, large
    ASR_DEVICE: str = "cpu"             # cpu / cuda
    ASR_LANGUAGE: str = "en"

    # ===============================
    # NLP MODEL SETTINGS
    # ===============================
    INTENT_MODEL_PATH: str = "models/intent_model"
    MAX_SEQUENCE_LENGTH: int = 128
    CONFIDENCE_THRESHOLD: float = 0.60

    # ===============================
    # TTS SETTINGS
    # ===============================
    TTS_LANGUAGE: str = "en"
    TTS_SPEAKING_RATE: float = 1.0
    OUTPUT_AUDIO_DIR: str = "outputs"

    # ===============================
    # API SETTINGS
    # ===============================
    MAX_AUDIO_FILE_SIZE_MB: int = 10
    ALLOWED_AUDIO_FORMATS: list = ["wav", "mp3"]

    # ===============================
    # PERFORMANCE SETTINGS
    # ===============================
    USE_GPU: bool = False
    ENABLE_LOGGING: bool = True

    class Config:
        env_file = ".env"


# Create a global config instance
settings = Settings()

# Create output directory if not exists
os.makedirs(settings.OUTPUT_AUDIO_DIR, exist_ok=True)

