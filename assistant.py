import os
import time
import speech_recognition as sr
import google.generativeai as genai

# ================= CONFIG =================
MODEL_NAME = "gemini-2.5-flash"
MIC_INDEX = 1   # USB PnP Audio Device
LANG = "en-US"
# ==========================================

# Gemini API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(MODEL_NAME)

# Speech recognizer
r = sr.Recognizer()
r.energy_threshold = 200
r.dynamic_energy_threshold = True
r.pause_threshold = 0.8

mic = sr.Microphone(device_index=MIC_INDEX)

print("🤖 Gemini Assistant ready")

def listen():
    try:
        with mic as source:
            print("🎤 Speak...")
            r.adjust_for_ambient_noise(source, duration=0.4)
            audio = r.listen(source, phrase_time_limit=5)
        return r.recognize_google(audio, language=LANG)
    except sr.UnknownValueError:
        return None
    except Exception as e:
        print("❌ Mic error, backing off")
        time.sleep(1)
        return None

def ask_gemini(text):
    try:
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        print("❌ Gemini error:", e)
        return None

while True:
    user = listen()
    if not user:
        continue

    print("You:", user)
    reply = ask_gemini(user)

    if reply:
        print("Gemini:", reply)
