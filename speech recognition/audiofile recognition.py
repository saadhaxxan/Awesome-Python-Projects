import speech_recognition as sr

r = sr.Recognizer()

audio = "maybe-next-time-huh.wav"

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print("done")


try:
    text = r.recognize_google(audio)
    print(text)
except:
    print("not recognized")
