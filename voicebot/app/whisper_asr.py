import whisper
import logging

class WhisperASR:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path: str):
        try:
            result = self.model.transcribe(audio_path)
            return result["text"]
        except Exception as e:
            logging.error(f"ASR Error: {str(e)}")
            raise

