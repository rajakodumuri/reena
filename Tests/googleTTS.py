import argparse

def synthesize_text_with_audio_profile(text, output, effects_profile_id):
	from google.cloud import texttospeech as tts
	client = tts.TextToSpeechClient()
	input_text = tts.types.SynthesisInput(text=text)
	voice = tts.types.VoiceSelectionParams(language_code='en-US')
	audio_config = tts.types.AudioConfig(audio_encoding=tts.enums.AudioEncoding.MP3,effects_profile_id=[effects_profile_id])
	response = client.synthesize_speech(input_text, voice, audio_config)
	with open(output, 'wb') as out:
		out.write(response.audio_content)
		print('Audio content written to file "%s"' % output)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument('--output', help='The output mp3 file.')
	parser.add_argument('--text', help='The text from which to synthesize speech.')
	parser.add_argument('--effects_profile_id', help='The audio effects profile id to be applied.')
	args = parser.parse_args()
	synthesize_text_with_audio_profile(args.text, args.output, args.effects_profile_id)