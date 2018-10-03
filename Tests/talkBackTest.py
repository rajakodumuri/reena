import os
import time
import webbrowser
from gtts import gTTS
from pygame import mixer
from mutagen.mp3 import MP3

# Talking what is necessary to the person passing commands
tts = gTTS(text="Okay, let's take you to google.com", lang='en-us')
extension = ".mp3"
fileName = "takingToGoogle" + extension

if not os.path.exists(fileName):
	tts.save(fileName)

# os.system('start ' + fileName)
mixer.init()
music = mixer.music
music.load(fileName)
music.play()

timeTaken = (MP3(fileName).info.length)

# Performing the task we need
url = "https://www.google.com"

time.sleep(timeTaken)
webbrowser.open(url, new=1)