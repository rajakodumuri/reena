import os
import time
import random
import threading
import webbrowser
import tkinter as tk
from gtts import gTTS
from queue import Queue
from mutagen.mp3 import MP3
from PIL import ImageTk, Image
from playsound import playsound
import speech_recognition as sr
from weather import Weather, Unit

global mainQueue
global mainThread
mainQueue = Queue()
root = tk.Tk()

def startAssistant():
    keepRunning = 1
    while keepRunning is 1:
        startMainFunction = mainFunction()
        startMainFunction
        if startMainFunction is 0: break

mainThread = threading

def doNothing(): print("I don't do anything apart from printing this line of course!")

def mainFunction():

    f = open("assistant.txt", "a")

    # Printing what a user is saying for better user experience
    def say(text):
        print(text)
        f.write("\n" + text + "\n")
        return text

    # This function will take inputs to talk back
    def talkBack(text, recordingName):
        # Variable Declaration
        extension = ".mp3"

        # Synthesising the reponse as speech
        tts = gTTS(text=say(text), lang="en-us")

        # Saving the response files
        fileName = recordingName + extension
        audioPath = "audioFiles\\"
        responseFile = audioPath + fileName

        # Checking to see if the file is already created
        if not os.path.exists(responseFile):
            tts.save(responseFile)
        # Playing the audio
        playsound(responseFile)

    # Initialising things here
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Asking for input and saving that
    with microphone as source:
        print ("Speak:")
        audio = recognizer.listen(source)
        mainQueue.put(audio)

    # Converting audio into text
    convertedAudio = recognizer.recognize_google(audio)
    convertedAudioSplit = convertedAudio.split()

    # Printing what was picked up when the user Spoke and also logging it
    print("\n" + convertedAudio + "\n")
    f.write("\n" + convertedAudio + "\n")

    # Start of a conversation
    if "hello" in convertedAudioSplit:
        talkBack("Hi, how are you doing today?", "hello")

    # Wishing people based on the time of the day  
    elif "morning" in convertedAudioSplit:
        talkBack("Good morning! The sun's shining bright, let's head out for a run. We'll get back and make a healthy breakfast for ourselves", "morning")
    elif "afternoon" in convertedAudioSplit:
        talkBack("Good afternoon! You must be hungry right about now, why don't you break for lunch?", "afternoon")
    elif "night" in convertedAudioSplit:
        talkBack("Nighty night sleepy pot! Get a good night's sleep while I learn more to be more helpful to you tomorrow.", "night")

    # Getting her information
    elif "doing" in convertedAudioSplit:
        talkBack("I am doing very good, Thank you for asking!", "doing")

    # Making the assistant open web browser with a URL
    elif "Google" in convertedAudioSplit:
        talkBack("Okay, lets get you to Google.", "google")
        # Opening the browser with the required URL
        webbrowser.open("https://www.google.com/", new = 1)

    # Brings the weather report
    elif "weather" in convertedAudioSplit:
        weatherVariable = Weather(unit=Unit.CELSIUS)
        location = weatherVariable.lookup_by_location('bangalore')
        condition = location.condition.text
        talkBack("It is {0} right now in Bengaluru.".format(condition), "weather")

    # Exiting the program on user's consent
    elif "exit" in convertedAudioSplit:
        talkBack("Sure, if that's what you want! I will miss you, have a good day.", "exit")
        return 0

    # If there is an UnknownValueError, this will kick in
    elif sr.UnknownValueError:
        talkBack("I am sorry, I couldn't quite get what you said. Could you please say that again?", "UnknownValueError")

    # When things go out of the box
    else:
        # Out of scope reply
        talkBack("I am a demo version. When you meet the completed me, you will be surprised.", "somethingElse")
        return 0

def userInterface(thread, queue):
    thread.start()

    root.title("Voice Assistant")
    mainFrame = tk.Frame(root, width = 1024, height = 720, bg = "turquoise", borderwidth = 5)

    menu = tk.Menu(root)
    root.config(menu=menu)
    subMenu = tk.Menu(menu)

    startButton = tk.Button(mainFrame, text="Interact", command = startAssistant)
    startButton.place(relx = 0.5, rely = 1.0, anchor = tk.S)

    menu.add_cascade(label="File", menu=subMenu)

    subMenu.add_command(label="Do Nothing", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=root.quit)

    mainFrame.pack()

    while thread.is_alive():
        root.update()
        pass
    
    something = queue.get()
    return something

something = userInterface(mainThread, mainQueue)
root.mainloop()