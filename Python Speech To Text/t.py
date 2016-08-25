import speech_recognition as sr
import re
import subprocess
	
#-----------------------------------------
#Dictionary	
#-----------------------------------------
commandDict = {'change directory': 'cd', 'list directories': 'ls', 'make directory': 'mkdir'}

class WordReplacments:

	def __init__(self , word, replacement):
		self.word = word
		self.replacement = replacement
		
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
def process(string):
	#hard coded reg expressions
	command = re.match(r'make directory', string, re.I)
	arg = re.match(r'make directory\s(.*)$', string, re.I)
	print(command.group())
	print(arg.group(1))	
	
	return(command.group(), arg.group(1))	

def findWords(string):
	newString = findDashesAndSlashes(string)
	spoken_cmd, arguments = process(newString)
	command = commandDict[spoken_cmd]

	print(command, arguments)
	runCommand(command, arguments)

def runCommand(command, args):
	mkdir = 'mkdir test'
	subprocess.Popen(mkdir.split(), shell=True)


#finds - and / etc
def findDashesAndSlashes(audioString):
  	
	alteredString = audioString
	
	for words in wordsList:
		alteredString = alteredString.replace(words.word, words.replacement)
	
	return alteredString
#-----------------------------------------
#Setting up Speech Recognition
#-----------------------------------------
#adding command words to a list
wordsList = []
wordsList.append(WordReplacments("dash","-"))
wordsList.append(WordReplacments("slash", "/"))
wordsList.append(WordReplacments("forward slash", "/"))
wordsList.append(WordReplacments("forwardslash", "/"))
wordsList.append(WordReplacments("back slash", "\\"))
wordsList.append(WordReplacments("backslash", "\\"))
wordsList.append(WordReplacments("dot", "."))
wordsList.append(WordReplacments("full stop", "."))
wordsList.append(WordReplacments("period", "."))
 
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