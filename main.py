
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import cohere
import os
import uuid

# 🔑 مفتاح API من https://dashboard.cohere.com/api-keys
co = cohere.Client("Your id Key")

# 🎤 تسجيل الصوت
def record_audio(filename="input.wav", duration=5):
    fs = 44100
    print("🎤 تكلم الآن...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    sf.write(filename, recording, fs)
    print("✅ تم التسجيل.")

# 🧠 تحويل الصوت إلى نص
def transcribe_audio(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="ar-SA")
    except sr.UnknownValueError:
        return "❌ ما قدرت أفهم الكلام"
    except sr.RequestError:
        return "❌ مشكلة في الاتصال بالإنترنت"

# 🤖 طلب الرد من Cohere
def get_reply(text):
    try:
        response = co.chat(message=text)
        return response.text
    except Exception as e:
        return f"❌ خطأ من Cohere: {e}"

# 🔊 تحويل النص إلى صوت باستخدام gTTS
def speak(text):
    tts = gTTS(text=text, lang='ar')
    filename = f"temp_{uuid.uuid4()}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# 🔁 حلقة التفاعل
while True:
    record_audio()
    user_input = transcribe_audio()
    print("👤 قلت:", user_input)

    if "خلاص" in user_input or "مع السلامة" in user_input:
        speak("مع السلامة! سعدت بخدمتك.")
        break

    bot_reply = get_reply(user_input)
    print("🤖 رد البوت:", bot_reply)
    speak(bot_reply)
