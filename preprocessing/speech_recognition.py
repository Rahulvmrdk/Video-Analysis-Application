# preprocessing/speech_recognition.py

import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Use "small" or "medium" for better accuracy
    result = model.transcribe(audio_path)
    return result["text"]
