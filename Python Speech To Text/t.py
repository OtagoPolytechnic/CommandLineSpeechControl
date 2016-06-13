import speech_recognition as sr

#---------------------------------------------
#Word class to hold all the command words and 
#what they need to be replaced with
#---------------------------------------------

class Word:

	def __init__(self , word, replacement):
		self.word = word
		self.replacement = replacement
	
	
#-----------------------------------------
#Multi-threading function 
#start of speech recognition
#-----------------------------------------

def speechRecog(recogniser, audio):
 
	try:
		audioText = recogniser.recognize_google(audio)
		findCommandWords(audioText)
	except LookupError:            
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
	
	#searching the list of words
	alteredString = audioString
	
	for words in wordsList:
		alteredString = alteredString.replace(words.word, words.replacement)
		
	print(alteredString)


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

print("Speak when ready")

#starts the method to make a background thread and continually search for sound
stopListening = recogniser.listen_in_background(mic, speechRecog)

#adding command words to a list
wordsList = []
wordsList.append(Word("dash","-"))
wordsList.append(Word("change directory", "cd"))

#keeps the program running
while (True):
	var = 1

#stops the background listening	
stopListening()