# core/tts.py

import pyttsx3
from gtts import gTTS
import pygame
import tempfile
import time

# Initialize pyttsx3 for fast offline English TTS
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female
engine.setProperty('rate', 170)

def speak(text):
    print(f"MANAS (EN): {text}")
    engine.say(text)
    engine.runAndWait()

def speak_nepali(text):
    print(f"MANAS (NP): {text}")
    tts = gTTS(text=text, lang='hi')  # Hindi closest to Nepali
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        mp3_file = fp.name

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
