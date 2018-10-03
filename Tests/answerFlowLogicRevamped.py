elif "power" in convertedAudioSplit:
	time.sleep(talkBack("That must be inconvenient, let's work on this together and fix the problem.", "power"))
	time.sleep(talkBack("Have you checked on the knowledge base to see if this is a known issue for your laptop model? That will help us narrow the troubleshooting down.", "knownIssue"))
elif "Yes" in convertedAudioSplit:
	time.sleep(talkBack("That's awesome, if you find that article, your issue should be resolved.", "powerKnownIssueYes"))
elif "No" in convertedAudioSplit:
	time.sleep(talkBack("Okay, let's go ahead and perform a hard reset on your laptop while making sure you use a known good power outlet for power supply", "powerKnownIssueNo"))
	time.sleep(talkBack("Does the system power up after the hard reset on a known good outlet?", "powerKnownIssueNoHardReset"))
elif "yes" in convertedAudioSplit:
	time.sleep(talkBack("That's awesome, if you find that article, your issue should be resolved.", "powerKnownIssueYes"))
elif "no" in convertedAudioSplit:
	time.sleep(talkBack("Okay, let's go ahead and perform a hard reset on your laptop while making sure you use a known good power outlet for power supply", "powerKnownIssueNo"))
	time.sleep(talkBack("Does the system power up after the hard reset on a known good outlet?", "powerKnownIssueNoHardReset"))
elif "powers" in convertedAudioSplit:
	time.sleep(talkBack("When you go to BIOS, do you see AC Adapter listed on it?", "powerKnownIssueNoHardResetYesACAdapter"))
elif "doesn't" in convertedAudioSplit:
	time.sleep(talkBack("Are there any signs of power on your laptop?", "powerKnownIssueNoHardResetNoACAdapter"))
elif "light" in convertedAudioSplit:
	time.sleep(talkBack("Okay, this doesn't look like a no power issue on your laptop. Based on the symptoms of the laptop, you may have to follow appropriate article", "powerKnownIssueNoHardResetNoACAdapterYes"))
elif "indication" in convertedAudioSplit:
	time.sleep(talkBack("Did the system experience any physical damage before this issue occured?", "powerKnownIssueNoHardResetNoACAdapterNoDamage"))
elif "listed" in convertedAudioSplit:
	time.sleep(talkBack("That's great! Looks like hard reset resolved the problem.", "powerKnownIssueNoHardResetYesACAdapterYes"))
elif "not" in convertedAudioSplit:
	time.sleep(talkBack("Do you notice any physical damage on the laptop?", "powerKnownIssueNoHardResetYesACAdapterNo"))
elif "notice" in convertedAudioSplit:
	time.sleep(talkBack("Okay, refer the accidental damage global policy for more information.", "powerKnownIssueNoHardResetYesACAdapterNoDamageYes"))
elif "don't" in convertedAudioSplit:
	time.sleep(talkBack("Alright, we need to check if there are any damages on the Dell's AC Adapter or the DC Port", "powerKnownIssueNoHardResetYesACAdapterNoDamageNo"))
elif "damaged" in convertedAudioSplit:
	time.sleep(talkBack("Let's check if the system powers on with a known good adapter, you may have access to?", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapter"))
elif "have" in convertedAudioSplit:
	time.sleep(talkBack("Alright, is the AC Adapter working with a known good power cord?", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYes"))
elif "working" in convertedAudioSplit:
	time.sleep(talkBack("Okay, it looks like the power cord is causing this problem and what I am going to do is, send a new power cord to the registered address on your Dell account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCord"))
elif "didn't" in convertedAudioSplit:
	time.sleep(talkBack("Okay, it looks like the adapter you have is causing this problem and what I am going to do is, send a new adapter to the registered address on your Dell account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCordNo"))
elif "nothing" in convertedAudioSplit:
	time.sleep(talkBack("Okay, it looks like the adapter and the power cord are faulty and what I am going to do is send a new set of adapter and power cord to the registered address on your Dell Account.", "powerKnownIssueNoHardResetNoACAdapterNoDamageYesAdapterYesCordNoFit"))
