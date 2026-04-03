import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")


API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-emotion"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def detect_emotion(text: str):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text}
    )

    data = response.json()

    try:
        # pick highest score emotion
        emotions = data[0]
        top_emotion = max(emotions, key=lambda x: x['score'])
        return top_emotion['label']
    except:
        return "neutral"