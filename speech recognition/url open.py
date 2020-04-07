import speech_recognition as sr
import webbrowser as wb
from gtts import gTTS
import pyglet
import os
import time

path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

r = sr.Recognizer()
#def tts(text,lang):
    #file = gTTS(text=text, lang=lang)
    

    #music = pyglet.resource.media("temp.wav", streaming= False)
    #music.play()
    #pyglet.app.run()

    #time.sleep(music.duration)
    #os.remove(filename)

with sr.Microphone() as source:
    print("speak anything")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
    #lang = "en"
    #tts(text,lang)
    #search_text = "https://www.google.com/search?q=" + text
    wb.get(path).open(text)
        
        
except Exception as e:
    print(e)


