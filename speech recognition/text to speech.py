from gtts import gTTS
import pyglet
import os
import time
import speech_recognition as sr
import pyglet

r = sr.Recognizer()


with sr.Microphone() as source:
    print("speak anything")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
    lang = "en"
    file = gTTS(text=text, lang=lang,slow=False)
    file.save("info.mp3")
    os.system("start info.mp3")
    
    
except Exception as e:
    print(e)
