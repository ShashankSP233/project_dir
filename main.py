import pyttsx4
import speech_recognition as sr
import os
import subprocess
from  cboxfun import *
from  todofun import *
from  news import *
from  newsint import *
from  newscity import *
from  segn import *


if __name__ == "__main__":
    greet_user()
    
    while True:
        user_input = listen()
        
        if user_input:
            if "set startup" in user_input:
                txtfl = open('toopen.txt', 'w')
                speak('what do you wnat to start')
                lis = list(input('Enter'))
                for i in lis:
                    txtfl.write(i+'\n')
            
            elif "start set" in user_input:    
                start_set_programs()
                speak("I've started the desired programs.")
            
            elif "admin" in user_input:
                if "start" in user_input:
                   speak("can you specify what to start?")
                   user_input = listen()
                   start_program_as_admin(f'{user_input}.exe')
                else: 
                    start_desired_programs()
                speak("I've started the desired programs.")
        
            elif any(word in user_input for word in ["todo", "worklist", "Schedule","to do",'work list']):
                todoSpeak()
                speak("do you want to edit this")
                user_input = listen()
                if user_input == "yes":
                    todorun()

            elif any(word in user_input for word in ["news", "daily", "ongoing"]):
                if "indian" in user_input:
                    get_daily_news()
                    nes = open('dailynews.txt', 'r')
                    i= nes.readlines()
                    for article in i :
                        speak(article)
                if "international" in user_input:
                    get_daily_newsint()
                    nes = open('intdailynews.txt', 'r')
                    i= nes.readlines()
                    for article in i :
                        speak(article)
                if 'local' in user_input:
                    get_daily_newsloc()
                    nes = open('localnews.txt', 'r')
                    i= nes.readlines()
                    for article in i :
                        speak(article)
                    
            elif    "google search" in user_input.lower():
                words = user_input.split()
                try:
                    index = words.index("google search") + 1
                    term = words[index:]
                    get_site(term)

                except ValueError:
                     None
            
            elif "recommendations" in user_input:
                import recommendation
                speak("your recomendation are sent")

            elif any(word in user_input for word in ["close", "exit"]):
                speak("Goodbye!")
                break
            
            else:
                speak("I'm not sure how to help with that. Could you please try something else?")