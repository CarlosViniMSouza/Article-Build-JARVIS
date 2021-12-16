# pip install pyttsx3
# pip install decouple

import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Definir taxa:
engine.setProperty('rate', 190)

# Definir Volume:
engine.setProperty('volume', 1.0)

# Definir voz(feminina):
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Conversão de texto em fala:
def speak(text):
    # Usado para falar qualquer texto que seja passado a ele:
    engine.say(text)
    engine.runAndWait()


def greet_user():
    # Cumprimenta o usuário de acordo com o horário

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Bom Dia {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Boa Tarde {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Boa Noite {USERNAME}")
    speak(f"Eu sou {BOTNAME}. Como posso te ajudar?")


def take_user_input():
    # Takes user input, recognizes it using Speech Recognition module and converts it into text

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Escutando....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconhecendo...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Boa noite senhor, tome cuidado!")
            else:
                speak('Tenha um bom dia senhor!')
            exit()
    except Exception:
        speak('Desculpe, eu não consegui entender. Você poderia por favor dizer isso de novo?')
        query = 'Nada'
    return query