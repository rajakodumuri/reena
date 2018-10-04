import os
import time
import random
import threading
import webbrowser
import tkinter as tk
from gtts import gTTS
from queue import Queue
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
import speech_recognition as sr
from weather import Weather, Unit
from playsound import playsound as ps

global mainQueue
global mainThread

mainQueue = Queue()
root = tk.Tk()

def getAudio():

    # Initialize speech recognition and microphone utiliser
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Use the microphone utilizer to get audio input
    with microphone as source:
        print ("Speak: ")
        audio = recognizer.listen(source)
        mainQueue.put(audio)

    # Convert the received audio into text after processing speech recognition
    convertedAudio = recognizer.recognize_google(audio)
    convertedAudioSplit = convertedAudio.split()

    output = print(convertedAudioSplit)

    # Get the function to return the array of words recognized
    return output

mainThread = threading.Thread(target = getAudio, args=())

def userInterface(thread, queue):
    thread.start()

    mainFrame = tk.Frame(root, width = 1024, height = 720, bg = "purple", borderwidth = 5)

    startButton = tk.Button(mainFrame, text = "Interact", command = getAudio)
    startButton.place(relx = 0.5, rely = 1.0, anchor = tk.S)

    mainFrame.pack()

    while thread.is_alive():
        root.update()
    
    userInterfaceOutput = queue.get()
    return userInterfaceOutput

testingOutput = userInterface(mainThread, mainQueue)
root.mainloop()