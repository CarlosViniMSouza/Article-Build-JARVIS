# pip install pyttsx3
# pip install decouple

import pyttsx3
from decouple import config

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

