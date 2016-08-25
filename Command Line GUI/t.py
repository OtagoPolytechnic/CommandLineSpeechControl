import speech_recognition as sr
import sys
print(sys.argv[1])

#-----------------------------------------
#Multi-threading function 
#start of speech recognition
#-----------------------------------------

def speechRecog(recogniser, audio):
 
	try:
		audioText = recogniser.recognize_google(audio)
		findCommandWords(audioText)
	except LookupError:                            # speech is unintelligible
		print("Could not understand audio")
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand the audio")
	except sr.RequestError:
		print("Could not request results from Google Speech Recognition")

			
#-----------------------------------------
#run all words through the reg expressions 
#to try find any command words
#-----------------------------------------

def findCommandWords(audioString):
	
	#audioString.find('dash')
	#if 'dash' in audioString:
	#	print("-")
		
	print(audioString)


#-----------------------------------------
#start of speech recognition
#-----------------------------------------

recogniser = sr.Recognizer()
#os.system("start /wait cmd")

#set default microphone as the source for audio
with sr.Microphone() as mic:

	#adjust the threshold for ambient noise in the room
	#so that it doesnt try and recognize random noise into words
	print("Adjusting for ambient room noise")
	recogniser.adjust_for_ambient_noise(mic)

print("Speak when ready")

stopListening = recogniser.listen_in_background(mic, speechRecog)

while (True):
	var = 1
	
stopListening()
