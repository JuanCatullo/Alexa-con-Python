from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import urllib.request
import json

name = 'alexa'
key = 'AIzaSyB5qTLBfjlFZxBw-ijwvHW-ZZuunP26JBE'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', "")
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    if 'Cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tienereproduce', "").strip()
        data = urllib.request.urlopen('')
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk (name_subs + " tiene {:,d} ".filter(int()))


run()

    