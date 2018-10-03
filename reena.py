import os
import sys
import time
import random
import webbrowser
from gtts import gTTS
from mutagen.mp3 import MP3
from playsound import playsound
import speech_recognition as sr
import PySimpleGUI as psg
from weather import Weather, Unit

def mainFunction():

	f = open("reena.txt", "a")

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

	# Converting audio into text
	convertedAudio = recognizer.recognize_google(audio)
	convertedAudioSplit = convertedAudio.split()

	# Printing what was picked up when the user Spoke and also logging it
	print("\n" + convertedAudio + "\n")
	f.write("\n" + convertedAudio + "\n")

	# Start of a conversation
	if "hello" in convertedAudioSplit:
		talkBack("Hi, how are you doing today?", "hello")

	# Understanding who user is	interacting with
	elif "who" in convertedAudioSplit:
		talkBack("I am an Interactive Voice Assistant made by Dell.", "who")

	# Wishing people based on the time of the day	
	elif "morning" in convertedAudioSplit:
		talkBack("Good morning! The sun's shining bright, let's head out for a run. We'll get back and make a healthy breakfast for ourselves", "morning")
	elif "afternoon" in convertedAudioSplit:
		talkBack("Good afternoon! You must be hungry right about now, why don't you break for lunch?", "afternoon")
	elif "night" in convertedAudioSplit:
		talkBack("Nighty night sleepy pot! Get a good night's sleep while I learn more to be more helpful to you tomorrow.", "night")

	# Reena dancing to entertain users
	elif "dance" in convertedAudioSplit:
		talkBack("Ooooh! I like this one! I am a trendy dancer, let me entertain your neural functions while I shake a leg!", "dance")
		webbrowser.open("https://www.youtube.com/watch?v=mYtsF7ngCxU", new = 1)

	# Getting her information
	elif "doing" in convertedAudioSplit:
		talkBack("I am doing very good, Thank you for asking!", "doing")

	# Understanding who Reena is
	elif "name" in convertedAudioSplit:
		 talkBack("My name is Reena! I am a Resolution and Enablement specialist made by my friends at Dell.", "name")

	# Making Reena open web browser with a URL
	elif "Google" in convertedAudioSplit:
		talkBack("Okay, lets get you to Google.", "google")
		# Opening the browser with the required URL
		webbrowser.open("https://www.google.com/", new = 1)

	# Getting call recordings based on the user requests
	elif "call" in convertedAudioSplit:
		# Randomizing the audio file that is being picked up
		randomNumber = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
		
		if "accountability" in convertedAudioSplit:
			talkBack("Sure, bringing up a random recording of a call with accountability.", "accountability")
			# Playing the call recording
			os.system('explorer "C:\\Users\\test\\Desktop\\Reena\\Calls"')
			os.system("start Calls\\Accountability\\call" + str(randomNumber) + ".mp3")
		elif "empathy" in convertedAudioSplit:
			talkBack("Sure, bringing up a random recording of a call with empathy.", "empathy")
			# Playing the call recording
			os.system('explorer "C:\\Users\\test\\Desktop\\Reena\\Calls"')
			os.system("start Calls\\Empathy\\call" + str(randomNumber) + ".mp3")
		elif "expectation" in convertedAudioSplit:
			talkBack("Sure, bringing up a random recording of a call with expectation setting.", "expectation")
			# Playing the call recording
			os.system('explorer "C:\\Users\\test\\Desktop\\Reena\\Calls"')
			os.system("start Calls\\Expectations\\call" + str(randomNumber) + ".mp3")
		elif "good" in convertedAudioSplit:
			talkBack("Sure, bringing up a random recording of a good call.", "good")
			# Playing the call recording
			os.system('explorer "C:\\Users\\test\\Desktop\\Reena\\Calls"')
			os.system("start Calls\\Good\\call" + str(randomNumber) + ".mp3")
		else:
			talkBack("Could you please say that again with recording's type clearly?", "recordingElse")

	# Getting the statistics based on user input
	elif "scores" in convertedAudioSplit:
		talkBack("You are in the top 10 for this month, here take a look", "scores")
		os.system("start scores.png")

	# Booking cabs for end of shift drop requests
	elif "drop" in convertedAudioSplit:
		talkBack("Why don't you leave it to me, consider it done", "drop")
		webbrowser.open("file:///C:/Users/test/Desktop/Reena/Transport%20Management%20Tool%20(TMT).htm", new = 1)

	# Marking an agent's attendance irrespective of user giving the timing
	elif "attendance" in convertedAudioSplit:
		talkBack("I have marked you present for 20 30 to 5 30 today. Have a good day at work", "attendance")
		os.system("start Kronos.png")

	# Helping users get the dinner menu of the day
	elif "breakfast" in convertedAudioSplit:
		talkBack("Bringing up the breakfast menu, bon appetit", "breakfast")
		webbrowser.open("https://goodboxapp.com/dell4cafeteria-sodexo-app", new = 1)
	elif "dinner" in convertedAudioSplit:
		talkBack("Bringing up the dinner menu, bon appetit", "dinner")
		webbrowser.open("https://goodboxapp.com/dell4cafeteria-sodexo-app", new = 1)

	# Brings the weather report
	elif "weather" in convertedAudioSplit:
		weatherVariable = Weather(unit=Unit.CELSIUS)
		location = weatherVariable.lookup_by_location('bangalore')
		condition = location.condition.text
		talkBack("It is {0} right now in Bengaluru.".format(condition), "weather")

	# Reena trying to run SupportAssist

	# Performance issues
	elif "performing" in convertedAudioSplit:
		talkBack("Sure, I will optimize your computer for better performance right away.", "performanceSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Performance  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "stuck" in convertedAudioSplit:
		talkBack("Sure, I will optimize your computer for better performance right away.", "performanceSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Performance  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "freezing" in convertedAudioSplit:
		talkBack("Sure, I will optimize your computer for better performance right away.", "performanceSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Performance  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "performance" in convertedAudioSplit:
		talkBack("Sure, I will optimize your computer for better performance right away.", "performanceSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Performance  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "slow" in convertedAudioSplit:
		talkBack("Sure, I will optimize your computer for better performance right away.", "performanceSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Performance  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")

	# Noise issues
	elif "loud" in convertedAudioSplit:
		talkBack("Using SupportAssist, I will scan your computer to see what is going on, don't you worry, I got this covered.", "noiseSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Noise  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "noise" in convertedAudioSplit:
		talkBack("Using SupportAssist, I will scan your computer to see what is going on, don't you worry, I got this covered.", "noiseSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Noise  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")

	# Display issues
	elif "display" in convertedAudioSplit:
		talkBack("I will optimize the display of this computer for optimal viewing experience.", "touchSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Display_Touch  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "spots" in convertedAudioSplit:
		talkBack("I will optimize the display of this computer for optimal viewing experience.", "touchSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Display_Touch  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")

	# Sound issues
	elif "sound" in convertedAudioSplit:
		talkBack("Okay, I wonder if you can hear me? It's a problem if you can't. I will do my magic while you take a sip of some hot coffee", "soundSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Sound_Issue  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
	elif "muted" in convertedAudioSplit:
		talkBack("Okay, I wonder if you can hear me? It's a problem if you can't. I will do my magic while you take a sip of some hot coffee", "soundSA")
		os.system("SupportAssist.exe RunDiags silent=false script=Sound_Issue  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")

	# Start of the troubleshooting code to integrate answerflow into Reena
	elif "power" in convertedAudioSplit:
		talkBack("That must be inconvenient, let's work on this together and fix the problem.", "power")
		talkBack("Have you checked on the knowledge base to see if this is a known issue for your laptop model? That will help us narrow the troubleshooting down.", "knownIssue")
	elif "Yes" in convertedAudioSplit:
		talkBack("That's awesome, if you find that article, your issue should be resolved.", "powerKnownIssueYes")
	elif "No" in convertedAudioSplit:
		talkBack("Okay, let's go ahead and perform a hard reset on your laptop while making sure you use a known good power outlet for power supply", "powerKnownIssueNo")
		talkBack("Does the system power up after the hard reset on a known good outlet?", "powerKnownIssueNoHardReset")
	elif "yes" in convertedAudioSplit:
		talkBack("That's awesome, if you find that article, your issue should be resolved.", "powerKnownIssueYes")
	elif "no" in convertedAudioSplit:
		talkBack("Okay, let's go ahead and perform a hard reset on your laptop while making sure you use a known good power outlet for power supply", "powerKnownIssueNo")
		talkBack("Does the system power up after the hard reset on a known good outlet?", "powerKnownIssueNoHardReset")
	elif "powered" in convertedAudioSplit:
		talkBack("When you go to BIOS, do you see AC Adapter listed on it?", "powerKnownIssueNoHardResetYesACAdapter")
	elif "doesn't" in convertedAudioSplit:
		talkBack("Are there any signs of power on your laptop?", "powerKnownIssueNoHardResetNoACAdapter")
	elif "lights" in convertedAudioSplit:
		talkBack("Okay, this doesn't look like a no power issue on your laptop. Based on the symptoms of the laptop, you may have to follow appropriate article", "powerKnownIssueNoHardResetNoACAdapterYes")
	elif "indication" in convertedAudioSplit:
		talkBack("Did the system experience any physical damage before this issue occured?", "powerKnownIssueNoHardResetNoACAdapterNoDamage")
	elif "listed" in convertedAudioSplit:
		talkBack("That's great! Looks like hard reset resolved the problem.", "powerKnownIssueNoHardResetYesACAdapterYes")
	elif "powering" in convertedAudioSplit:
		talkBack("Do you notice any physical damage on the laptop?", "powerKnownIssueNoHardResetYesACAdapterNo")
	elif "notice" in convertedAudioSplit:
		talkBack("Okay, refer the accidental damage global policy for more information.", "powerKnownIssueNoHardResetYesACAdapterNoDamageYes")
	elif "don't" in convertedAudioSplit:
		talkBack("Alright, we need to check if there are any damages on the Dell's AC Adapter or the DC Port", "powerKnownIssueNoHardResetYesACAdapterNoDamageNo")
	elif "damaged" in convertedAudioSplit:
		talkBack("Let's check if the system powers on with a known good adapter, you may have access to?", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapter")
	elif "do" in convertedAudioSplit:
		talkBack("Alright, is the AC Adapter working with a known good power cord?", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYes")
	elif "working" in convertedAudioSplit:
		talkBack("Okay, it looks like the power cord is causing this problem and what I am going to do is, send a new power cord to the registered address on your Dell account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCord")
	elif "didn't" in convertedAudioSplit:
		talkBack("Okay, it looks like the adapter you have is causing this problem and what I am going to do is, send a new adapter to the registered address on your Dell account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCordNo")
	elif "nothing" in convertedAudioSplit:
		talkBack("Okay, it looks like the adapter and the power cord are faulty and what I am going to do is send a new set of adapter and power cord to the registered address on your Dell Account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCordNoFit")

	# Triggering the touch troubleshooting function
	elif "touch" in convertedAudioSplit:
		keepRunning = 2
		talkBack("I understand that this is an inconvenience, let me help you.", "troubleshootTrigger")
		talkBack("Is there any physical damage on the display?", "physicalDamageOnDisplay")
		while keepRunning is 2:
			troubleshoot()
			if troubleshoot is 0:
				break
	elif "touchscreen" in convertedAudioSplit:
		keepRunning = 2
		talkBack("I understand that this is an inconvenience, let me help you.", "troubleshootTrigger")
		talkBack("Is there any physical damage on the display?", "physicalDamageOnDisplay")
		while keepRunning is 2:
			troubleshoot()
			if troubleshoot is 0:
				break

	# Exiting the program on user's consent
	elif "exit" in convertedAudioSplit:
		talkBack("Sure, if that's what you want! I will miss you, have a good day.", "exit")
		return 0

	# If there is an UnknownValueError, this will kick in
	elif sr.UnknownValueError:
		talkBack("I am sorry, I couldn't quite get what you said. Could you please say that again?", "UnknownValueError")

	# When things go out of the box
	else:
		# Out of scope reply by Reena
		talkBack("I am a demo version. When you meet the completed me, you will be surprised.", "somethingElse")
		return 0

def troubleshoot():

	f = open("reena.txt", "a")

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
	recognizerTroubleshoot = sr.Recognizer()
	microphoneTroulbeshoot = sr.Microphone()

	# Asking for input and saving that
	with microphoneTroulbeshoot as source:
		print ("Speak:")
		audio = recognizerTroubleshoot.listen(source)

	# Converting audio into text
	convertedAudioTroubleshoot = recognizerTroubleshoot.recognize_google(audio)
	convertedAudioTroubleshootSplit = convertedAudioTroubleshoot.split()

	# Printing what was picked up when the user Spoke and also logging it
	print("\n" + convertedAudioTroubleshoot + "\n")
	f.write("\n" + convertedAudioTroubleshoot + "\n")

	# Start of troubleshooting conversation between the agent and Reena
	if "yes" in convertedAudioTroubleshootSplit:
		talkBack("I’m sorry to hear that, let me connect you to a Dell Technical Representative through chat, who will help you further", "physicalDamageOnDisplayYes")
		webbrowser.open("https://www.dell.com/learn/us/en/uscorp1/campaigns/chat-splitter", new = 1)
	elif "no" in convertedAudioTroubleshootSplit:
		aRecognizer = sr.Recognizer()
		aMicrophone = sr.Microphone()
		talkBack("Why don't we clean the display with a clean and soft cloth to see if that helps.", "physicalDamageOnDisplayNo")
		with aMicrophone as source:
			print("Speak:")
			aAudio = aRecognizer.listen(source)

		convertedaAudio = aRecognizer.recognize_google(aAudio)
		convertedaAudioSplit = convertedaAudio.split()

		# Printing what was picked up when the user Spoke and also logging it
		print("\n" + convertedaAudio + "\n")
		f.write("\n" + convertedaAudio + "\n")

		if "yes" in convertedaAudioSplit:
			talkBack("I am glad that the issue is resolved.", "physicalDamageOnDisplayNoCleanYes")
		elif "no" in convertedaAudioSplit:
			bRecognizer = sr.Recognizer()
			bMicrophone = sr.Microphone()
			talkBack("Do you have any screen protector on the display glass?", "physicalDamageOnDisplayNoCleanNo")
			with bMicrophone as source:
				print("Speak:")
				bAudio = bRecognizer.listen(source)

			convertedbAudio = bRecognizer.recognize_google(bAudio)
			convertedbAudioSplit = convertedbAudio.split()

			# Printing what was picked up when the user Spoke and also logging it
			print("\n" + convertedbAudio + "\n")
			f.write("\n" + convertedbAudio + "\n")

			if "yes" in convertedbAudioSplit:
				cRecognizer = sr.Recognizer()
				cMicrophone = sr.Microphone()
				talkBack("Let's remove the screen protector and clean the display again", "physicalDamageOnDisplayNoCleanNoProtectorYes")
				with cMicrophone as source:
					print("Speak:")
					cAudio = cRecognizer.listen(source)

				convertedcAudio = cRecognizer.recognize_google(cAudio)
				convertedcAudioSplit = convertedcAudio.split()

				# Printing what was picked up when the user Spoke and also logging it
				print("\n" + convertedcAudio + "\n")
				f.write("\n" + convertedcAudio + "\n")

				if "yes" in convertedcAudioSplit:
					talkBack("I am glad that the issue is resolved. Thank you for working with me, it was a pleasure.", "physicalDamageOnDisplayNoCleanNoProtectorYesResolvedYes")
				elif "no" in convertedcAudioSplit:
					talkBack("Let me go ahead and caliberate the touchscreen, I might need your help in completing the test", "physicalDamageOnDisplayNoCleanNoProtectorNoResolvedNo")
					os.system("SupportAssist.exe RunDiags silent=false script=Display_Touch  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")
			elif "no" in convertedbAudioSplit:
				talkBack("Let me go ahead and caliberate the touchscreen, I might need your help in completing the test", "physicalDamageOnDisplayNoCleanNoProtectorNoResolvedNo")
				os.system("SupportAssist.exe RunDiags silent=false script=Display_Touch  key=98546726a7d1c084de4977ebfb90fa74b5f1efd1")

	elif "exit" in convertedAudioTroubleshootSplit:
		talkBack("Sure, if that's what you want! I will exit the troubleshooting mode.", "exitTroubleshooting")
		return 0

	elif sr.UnknownValueError:
		talkBack("I am sorry, I couldn't quite get what you said. Could you please say that again?", "UnknownValueError")

	else:
		talkBack("Sorry, I am a demo version and I am still learning, you will be thrilled to meet the real me", "everythingElseYouFailToDo")

mainFunction()
