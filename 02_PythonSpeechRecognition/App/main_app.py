import speech_recognition as sr

recognizer = sr.Recognizer()

print(recognizer)

with sr.Microphone() as source:
    print("Say Something")
    audio = recognizer.listen(source,timeout=10)
    print("Time up")

try:
    print(recognizer.recognize_google(audio))
except:
    print("Error in converting speech to text")