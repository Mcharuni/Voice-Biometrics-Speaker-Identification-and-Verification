import pandas as pd
import numpy as np

class VoiceBiometricsEngine:
    def __init__(self, data_path="data/enrolled_speakers.csv"):
        self.df = pd.read_csv(data_path)

    def parse_vector(self, vec_str):
        return np.array([float(x) for x in vec_str.split(";")])

    def verify_speaker(self, target_speaker_id, incoming_embedding_mock):
        speaker_row = self.df[self.df["speaker_id"] == target_speaker_id]
        if speaker_row.empty:
            return {"verified": False, "reason": "Speaker ID not found in enrollment database."}
        
        enrolled_vec = self.parse_vector(speaker_row.iloc[0]["embedding_vector_mock"])
        incoming_vec = np.array(incoming_embedding_mock)
        
        # Cosine similarity calculation
        cosine_sim = np.dot(enrolled_vec, incoming_vec) / (np.linalg.norm(enrolled_vec) * np.linalg.norm(incoming_vec))
        threshold = 0.75
        
        is_verified = bool(cosine_sim >= threshold)
        return {
            "speaker_id": target_speaker_id,
            "speaker_name": speaker_row.iloc[0]["speaker_name"],
            "verified": is_verified,
            "confidence_score": round(float(cosine_sim), 4),
            "threshold": threshold
        }

if __name__ == "__main__":
    engine = VoiceBiometricsEngine()
    # Test verification against Alice (SPK001) with a similar mock embedding vector
    print(engine.verify_speaker("SPK001", [0.10, -0.42, 0.85, 0.30, -0.12]))
