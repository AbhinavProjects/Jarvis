import pyttsx3  
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print voice
engine.setProperty('voices', voices[0].id)

# text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query

# to wish


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello i am jarvis, please tell me how may i help you")


if __name__ == "__main__":
    wish()
    while True:
        # if 1:
        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("Start cmd")

        elif "play music" in query:
            music_dir = "G:\\Jarvis\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP addres is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("Youtube.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open google" in query:
            speak("What should i search on goolge")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "no thanks" in query:
            speak("Thanks for using me, have a good day")
            sys.exit()

        

        speak("sir, do you have any other work?")
