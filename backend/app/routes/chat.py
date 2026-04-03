from fastapi import APIRouter
from pydantic import BaseModel

from app.services.regex_utils import clean_text, check_greeting, check_critical
from app.services.emotion import detect_emotion

router = APIRouter()

# ✅ Request body model (IMPORTANT FIX)
class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    message = req.message
    text = clean_text(message)

    # 🚨 Safety check
    critical = check_critical(text)
    if critical:
        return {"reply": critical}

    # 👋 Greeting
    greeting = check_greeting(text)
    if greeting:
        return {"reply": greeting}

    # 🧠 Emotion detection
    emotion = detect_emotion(text)

    return {
        "emotion": emotion,
        "reply": f"I understand you're feeling {emotion}. Tell me more 💙"
    }