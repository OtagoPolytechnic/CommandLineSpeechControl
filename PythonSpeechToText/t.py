import speech_recognition as sr
import re
#import cloudSpeech
#import runCommands
import csv

#-----------------------------------------
#Dictionary	
#-----------------------------------------

class WordReplacments:

	def __init__(self , command, replacement):
		self.command = command
		self.replacement = replacement
		
#-----------------------------------------
#Multi-threading function 
#start of speech recognition
#-----------------------------------------
def csvReading():
	with open('SpeechRecgonitionFile.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			 wordsList.append(WordReplacments(row[0], row[1]))
			
#used when the user want to do speech recognition through google
#mainly for testing
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

#used when the user want to do speech recognition through google cloud Speech api
def googleCloudSpeechRecog(recogniser, audio):
 
	try:
		audioText = cloudSpeech.Recognize(audio.get_raw_data())
		print(audioText)
		#findWords(audioText)
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
	command = "echo"
	arg = string
	for commands in wordsList:
		if re.match(commands.command, string, re.I) is not None:
			command = commands.replacement
			temparg = re.match(commands.command + r'\s(.*)$', string, re.I)
			arg = temparg.group(1)

	print(command)
	print(arg)	
	
	return(command, arg)	

def findWords(string):
	newString = findDashesAndSlashes(string)
	spoken_cmd, arguments = process(newString)
	

	print(command, arguments)
	runCommand(command, arguments)

def runCommand(command, args):
	prompt.runCommand(command + " " + args)

#-----------------------------------------
#Setting up Speech Recognition
#-----------------------------------------

#setting up the command prompt window to be able to send commands
#prompt = runCommands.CommandPrompt()

#adding command words to a list
wordsList = []

recogniser = sr.Recognizer()

csvReading()

string = "make directory test"
process(string)

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
#stopListening = recogniser.listen_in_background(mic, googleCloudSpeechRecog)


#keeps the program running
#while (True):
	#var = 1

#stops the background listening	
#SstopListening()