import webbrowser
import string
import speech_recognition as sr
import os
import time
from datetime import datetime
from threading import Timer

def listen():
	try:
		r = sr.Recognizer()
		print("hello")
		with sr.Microphone() as source:
		    audio = r.listen(source)
		    prnt = r.recognize_google(audio)
		    try:
		            print(prnt)
		            text_file = open("Output1.txt", "w")
		            text_file.write(prnt)
		            text_file.close()
		            listen()
		            print(prnt)
		    except sr.UnknownValueError:
		            listen()
		    except sr.RequestError as e:
		            listen()
	except sr.UnknownValueError:
		listen()


listen()