from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from app.asr.whisper_asr import WhisperASR
from app.nlp.intent_model import IntentClassifier
from app.nlp.response_generator import ResponseGenerator
from app.tts.tts_engine import TTSEngine
import shutil

app = FastAPI()

asr = WhisperASR()
intent_model = IntentClassifier()
response_gen = ResponseGenerator()
tts_engine = TTSEngine()


@app.post("/voicebot")
async def voicebot(file: UploadFile = File(...)):

    audio_path = f"temp_{file.filename}"
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = asr.transcribe(audio_path)
    prediction = intent_model.predict(text)
    response_text = response_gen.generate(prediction["intent"])
    audio_output = tts_engine.synthesize(response_text)

    return FileResponse(audio_output, media_type="audio/mpeg")

