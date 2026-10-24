from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.voice_biometrics import VoiceBiometricsEngine

app = FastAPI(title="Voice Biometrics Speaker Authentication API", version="1.0")
engine = VoiceBiometricsEngine()

class VerificationInput(BaseModel):
    speaker_id: str
    embedding_vector: List[float]

@app.get("/")
def home():
    return {"message": "Voice Biometrics Identification & Verification API is online!"}

@app.post("/verify")
def verify_voice(data: VerificationInput):
    result = engine.verify_speaker(data.speaker_id, data.embedding_vector)
    return result
