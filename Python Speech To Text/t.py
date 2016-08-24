import speech_recognition as sr
	
#-----------------------------------------
#Dictionary	
#-----------------------------------------
commandDict = {'change directory': 'cd', 'list directories': 'ls'}


#-----------------------------------------
#Multi-threading function 
#start of speech recognition
#-----------------------------------------

#used when the user want to do speech recognition through google
def googleSpeechRecog(recogniser, audio):
 
	try:
		audioText = recogniser.recognize_google(audio)
		findWords(audioText)
	except LookupError:            
		print("Could not understand audio")
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand the audio")
	except sr.RequestError:
		print("Could not request results from Google Speech Recognition")

#used when the user want to do speech recognition offline through CMU Sphinx	
def cmuSpeechRecog(recogniser, audio):
 
	try:
		audioText = recogniser.recognize_sphinx(audio)
	except LookupError:            
		print("Could not understand audio")
		
#-----------------------------------------
#run all words through the reg expressions 
#to try find any command words
#-----------------------------------------
def process(s):
        return(s, "")

def findWords(string):
	spoken_cmd, arguments = process(string)
	command = commandDict[spoken_cmd]

	print(command, arguments)


#-----------------------------------------
#Setting up Speech Recognition
#-----------------------------------------

recogniser = sr.Recognizer()

#set default microphone as the source for audio
with sr.Microphone() as mic:

	#adjust the threshold for ambient noise in the room
	#so that it doesnt try and recognize random noise into words
	print("Adjusting for ambient room noise")
	recogniser.adjust_for_ambient_noise(mic)
	recogniser.energy_threshold = 400
	recogniser.dynamic_energy_threshold = False

print("Speak when ready")

#starts the method to make a background thread and continually search for sound
stopListening = recogniser.listen_in_background(mic, googleSpeechRecog)


#keeps the program running
while (True):
	var = 1

#stops the background listening	
stopListening()