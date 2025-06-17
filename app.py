from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from gtts import gTTS
import uuid
import os

app = FastAPI()

OUTPUT_DIR = "output_mp3"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/tts")
async def tts(text: str = Form(...)):
    # Generate unique filename
    filename = f"{uuid.uuid4().hex}.mp3"
    output_path = os.path.join(OUTPUT_DIR, filename)
    # Generate TTS (wanita Indonesia)
    tts = gTTS(text, lang='id', tld='com', slow=False)
    tts.save(output_path)
    return FileResponse(output_path, media_type="audio/mpeg", filename=filename) 