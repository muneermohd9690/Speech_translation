import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 1000
with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except:
    print("didn't work")

