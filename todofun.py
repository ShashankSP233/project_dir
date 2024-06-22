import speech_recognition as sr
from cboxfun import *
from subprocess import Popen


def todoSpeak():
    # tdata = open("tasks.txt", "r")
    tfile = open("tasks.txt", "r")
    tdata = tfile.read()
    tlist = tdata.split("\n")
    speak("your to do list consist of:")
    for t in tlist:
        speak(t)
    
def todorun():
   import todolis
todorun()