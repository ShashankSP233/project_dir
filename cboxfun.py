import pyttsx4
import speech_recognition as sr

import time
import os
import subprocess

engine = pyttsx4.init()

def speak(text):
    print (text)
    engine.say(text)
    engine.runAndWait()

def greet_user():
    speak("Hello! I'm your startup assistant. How can I help you today?")

def start_desired_programs():
    # Replace these with the programs you want to start
    programs_to_start = [
        "notepad.exe",  
        "chrome.exe"    
    ]

    for program in programs_to_start:
        os.system(f"start {program}")
def start_set_programs():
    txtfl  = open('toopen.txt', 'r')

    programs_to_start = txtfl.readlines()

    for program in programs_to_start:
        os.system(f"start {program}")

def start_program_as_admin(program):
    try:
        subprocess.run(['runas', '/user:Administrator', program], check=True)
        print(f"Started {program} as administrator.")
    except subprocess.CalledProcessError:
        print(f"Failed to start {program} as administrator.")

def listen():
   

    r = sr.Recognizer()

    # print(sr.Microphone.list_microphone_names())

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say anything: ")

        start_time = time.time()
        while time.time() - start_time < 5:  # Adjust the timeout value (5 seconds in this example)
            try:
                audio = r.listen(source, timeout=1, phrase_time_limit=5)  # Adjust timeout and phrase_time_limit as needed
                text = r.recognize_google(audio)
                print(f"querry: {text}")
                return text.lower()
                break  # Break out of the loop once speech is recognized
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand what you said.")
                break
            except sr.RequestError:
                print("There was an error connecting to the Google API. Please check your internet connection.")
                break

# listen()

# todoSpeak()
        
        