# Voice Biometrics: Speaker Identification and Verification

A secure voice authentication pipeline that extracts speaker embeddings (x-vectors / d-vectors) and performs text-dependent and text-independent verification using cosine similarity and metric learning.

## Features
- **Speaker Enrollment Database:** Manages enrolled voiceprint profiles.
- **Verification & Similarity Scoring:** Evaluates incoming speech embeddings against registered profiles.
- **FastAPI REST Endpoint:** Ready for banking security, forensic audio, and smart device authentication.

## Project Structure
```text
voice_biometrics_project/
├── data/
│   └── enrolled_speakers.csv
├── src/
│   ├── voice_biometrics.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run verification script: `python src/voice_biometrics.py`
3. Start API server: `uvicorn src.app:app --reload`
