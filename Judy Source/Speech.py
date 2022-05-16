import webbrowser
import string
import speech_recognition as sr
import os
import time
from datetime import datetime
from threading import Timer

# obtain audio 
def exitfunc():
    print("Exit Time", datetime.now())
    os._exit(0)

Timer(15, exitfunc).start()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please Speak Into Microphone")
    audio = r.listen(source)
    prnt = r.recognize_google(audio)
    try:
            print(prnt)
            text_file = open("Output1.txt", "w")
            text_file.write(prnt)
            text_file.close()
            os._exit(0)
            print(prnt)
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            os._exit(0)
    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            os._exit(0)