# 1 Import statements

import pyttsx3

# 2 Initialing the engine

engine=pyttsx3.init()

# 3 Getting the list of voices in the system

for voice in engine.getProperty("voices"):
    print(voice)

# 4 Setting the voice of the engine

voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

# 5 Defining Speak function

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

# 6 Initialing Speak function
text=input("Enter your text now:")
Speak(text)