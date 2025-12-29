import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("Hello, I am your voice assistant")

while True:
    command = listen()

    if command == "":
        continue

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        speak("Searching Wikipedia")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand")