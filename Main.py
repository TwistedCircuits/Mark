#functionality
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import pyaudio
import twint

#voice
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Tells me the time
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

#How command taking works
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Mark is getting ready, please wait one moment.")
speak("Mark is getting ready, please wait one moment.")
wishMe()
time.sleep(3)

if __name__=='__main__':


    while True:
        speak("Hello Sir, my name is Mark, your artificial intelligence assistant. How may I help you today?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Have a good day master")
            print("Have a good day master")
            break
        if "OSINT" in statement:
            speak("What tool do you need sir")
        elif "Twint" in statement:
            speak("mom")
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2000)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'Open reverse shell generator' in statement:
            webbrowser.open_new_tab("https://www.revshells.com/")
            speak("Reverse shell generator open")
        elif 'Open Shodan' in statement:
            webbrowser.open_new_tab("https://www.shodan.io/")
            speak("Shodan is now open")
            time.sleep(5)
        elif 'Open webcam' in statement:
            webbrowser.open_new_tab("http://www.insecam.org/")
            speak("Insecam open sir")
            time.sleep(5)
        elif 'Open threat map' in statement:
            webbrowser.open_new_tab("https://thr0.eatmap.checkpoint.com/")
            webbrowser.open_new_tab("https://livethreatmap.radware.com/")
            speak("Threat map open")
            time.sleep(5)
        elif 'Open aircraft tracker' in statement:
            webbrowser.open_new_tab("https://www.flightradar24.com/")
            speak("Aircraft tracker open")
            time.sleep(5)
        elif 'Open marine traffic tracker' in statement:
            webbrowser.open_new_tab("https://www.marinetraffic.com/")
            speak("Marine traffic tracker open")
            time.sleep(5)
        elif 'open you, open you.com' in statement:
            webbrowser.open_new_tab("https://www.you.com")
            speak("You.com is open now")
            time.sleep(5)    
        elif 'Open Breach news, Open CVE news, Open exploit news' in statement:
            webbrowser.open_new_tab("https://thehackernews.com/")
            webbrowser.open_new_tab("https://threatpost.com/")
            webbrowser.open_new_tab("https://www.exploit-db.com/")
            webbrowser.open_new_tab("https://portswigger.net/daily-swig/hacking-news")
            speak("You.com is open now")
            time.sleep(5)
        elif 'Open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com/")
            speak("Youtube.com is now open")
            time.sleep(5)
        elif 'Open github' in statement:
            webbrowser.open_new_tab("https://github.com")
            speak("Github.com is now open")
            time.sleep(5)
        elif 'Open email' in statement:
            webbrowser.open_new_tab("https://inbox.proton.me/")
            webbrowser.open_new_tab("https://mail.google.com/")
            speak("Email is now open")
            time.sleep(5)
        elif 'Open hacker one' in statement:
            webbrowser.open_new_tab("https://www.hackerone.com/")
            speak("Hacker one is now open")
            time.sleep(5)
# Tells me the time     
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
# AI Identity     
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Mark your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was open source code remade by my master Jack")
            print("I was open source code remade by my master Jack")
#Signs out of computer
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
