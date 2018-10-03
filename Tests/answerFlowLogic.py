	# Start of the troubleshooting code to integrate answerflow into Reena
	elif "power" in convertedAudioSplit:
		time.sleep(talkBack("That must be inconvenient, let's work on this together and fix the problem.", "power"))
		with microphone as source:
			time.sleep(talkBack("Have you checked on the knowledge base to see if this is a known issue for your laptop model? That will help us narrow the troubleshooting down.", "knownIssue"))
			try:
				troubleshootingAudio = recognizer.listen(source)
			except speech_recognition.UnknownValueError:
				print("Sorry, I couldn't understand what you said.\nError: {0}".format(e))

		a = recognizer.recognize_google(troubleshootingAudio)
		aSplit = a.split()

		if "Yes" in aSplit:
			time.sleep(talkBack("That's awesome, if you find that article, your issue should be resolved.", "powerKnownIssueYes"))
		elif "No" in aSplit:
			time.sleep(talkBack("Okay, let's go ahead and perform a hard reset on your laptop while making sure you use a known good power outlet for power supply", "powerKnownIssueNo"))
			with microphone as source:
				time.sleep(talkBack("Does the system power up after the hard reset on a known good outlet?", "powerKnownIssueNoHardReset"))
				try:
					troubleshootingAudio = recognizer.listen(source)
				except speech_recognition.UnknownValueError:
					print("Sorry, I couldn't understand what you said.\nError: {0}".format(e))

			b = recognizer.recognize_google(troubleshootingAudio)
			bSplit = b.split()

			if "Yes" in bSplit:
				with microphone as source:
					time.sleep(talkBack("When you go to BIOS, do you see AC Adapter listed on it?", "powerKnownIssueNoHardResetYesACAdapter"))
					try:
						troubleshootingAudio = recognizer.listen(source)
					except speech_recognition.UnknownValueError:
						print("Sorry, I couldn't understand what you said.\nError: {0}".format(e))

				c = recognizer.recognize_google(troubleshootingAudio)
				cSplit = c.split()

				if "Yes" in cSplit:
					time.sleep(talkBack("That's great! Looks like hard reset resolved the problem.", "powerKnownIssueNoHardResetYesACAdapterYes"))
				elif "No" in cSplit:
					time.sleep(talkBack("Do you notice any physical damage on the laptop?", "powerKnownIssueNoHardResetYesACAdapterNo"))
					with microphone as source:
						time.sleep(talkBack("When you go to BIOS, do you see AC Adapter listed on it?", "powerKnownIssueNoHardResetYesACAdapterNoDamage"))
						try:
							troubleshootingAudio = recognizer.listen(source)
						except speech_recognition.UnknownValueError:
							print("Sorry, I couldn't understand what you said.\nError: {0}".format(e))

					d = recognizer.recognize_google(troubleshootingAudio)
					dSplit = d.split()

					if "Yes" in dSplit:
						time.sleep(talkBack("Okay, refer the accidental damage global policy for more information.", "powerKnownIssueNoHardResetYesACAdapterNoDamageYes"))
