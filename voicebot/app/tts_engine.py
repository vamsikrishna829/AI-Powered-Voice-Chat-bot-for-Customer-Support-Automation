from gtts import gTTS
import uuid

class TTSEngine:

    def synthesize(self, text: str, rate=1.0):
        filename = f"output_{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        return filename

