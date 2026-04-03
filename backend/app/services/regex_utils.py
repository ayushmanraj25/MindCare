import re

# ✅ Clean text
def clean_text(text: str):
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.lower()

# ✅ Detect greeting
def check_greeting(text: str):
    if re.search(r"\b(hi|hello|hey)\b", text, re.I):
        return "Hello! How are you feeling today? 😊"
    return None

# 🚨 Detect critical words
def check_critical(text: str):
    if re.search(r"suicide|kill myself|die", text, re.I):
        return "⚠️ You are not alone. Please talk to someone you trust or contact a helpline."
    return None