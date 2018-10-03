import speech_recognition as sr

# Code to take commands is below
#--------------------------------
# Obtaining audio from the microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

for mic in microphone.list_microphone_names():
	print("\n" + mic + "\n")

with microphone as source:
	print("Hello, how can I help you today?")
	audio = recognizer.listen(source)

# Acting based on the input received
try:
	print("\nReena thinks you said " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
	print("\nSorry, I couldn't understand what you said")
except sr.RequestError as e:
	print("\nReena ran into an error; {0}".format(e))