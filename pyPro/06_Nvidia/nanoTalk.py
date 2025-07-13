import os
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('voice','english+f2')
text='Get ready Player 1 Are you ready'
engine.say(text)
engine.runAndWait()