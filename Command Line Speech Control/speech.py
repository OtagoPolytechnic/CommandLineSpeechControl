import speech_recognition as sr
import re
import cloudSpeech
import runCommands
import csv


class WordReplacments:

	def __init__(self, command, replacement):
		self.command = command
		self.replacement = replacement


class SpeechToCommandLine:

	def __init__(self):

		#creates a word list from the command words csv file
		self.wordsList = []
		self.csvReading()
		
		#setting up the command prompt window to be able to send commands
		self.prompt = runCommands.CommandPrompt()
				
		self.recogniser = sr.Recognizer()

		
	#starts the speech recognition
	def startSpeechRecognition(self):

		#set default microphone as the source for audio
		with sr.Microphone() as mic:

			#adjust the threshold for ambient noise in the room
			#so that it doesnt try and recognize random noise into words
			print("Adjusting for ambient room noise")
			self.recogniser.adjust_for_ambient_noise(mic)
			self.recogniser.energy_threshold = 400
			self.recogniser.dynamic_energy_threshold = False

		print("Speak when ready")

		#starts the method to make a background thread and continually search for sound
		self.stopListening = self.recogniser.listen_in_background(mic, self.googleSpeechRecog)

		
	#stops the speech recognition
	def stopSpeechRecognition(self):
		self.stopListening()
		
		
	#Reads the csv file containing the list of commands and adds them
	#to a list so that they can be searched through
	def csvReading(self):
		with open('commandsFile.csv', 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:
				 self.wordsList.append(WordReplacments(row[0], row[1]))
	


	#-----------------------------------------
	#Processes the words and returns the
	#commands and arguments
	#-----------------------------------------	
	#finds the words
	def findWords(self, string):
		spoken_cmd, arguments = self.process(newString)

		print(command, arguments)
		self.runCommand(command, arguments)
	
	
	#run all words through the reg expressions to try find any command words
	def process(self, string):
		#hard coded reg expressions
		command = "echo"
		arg = string
		for commands in self.wordsList:
			if re.match(commands.command, string, re.I) is not None:
				command = commands.replacement
				temparg = re.match(commands.command + r'\s(.*)$', string, re.I)
				arg = temparg.group(1)

		print(command)
		print(arg)	

		return(command, arg)

	
	#-----------------------------------------
	#Runs Commands
	#-----------------------------------------
	#Runs a command in the command prompt
	def runCommand(self, command, args):
		self.prompt.runCommand(command + " " + args)
			
		
	#-----------------------------------------
	#Speech Recognition APIs
	#-----------------------------------------
	#used when the user want to do speech recognition through google
	#mainly for testing
	def googleSpeechRecog(recogniser, audio):
	 
		try:
			audioText = recogniser.recognize_google(audio)
			self.findWords(audioText)
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
			#self.findWords(audioText)
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
			self.findWords(audioText)
		except LookupError:            
			print("Could not understand audio")
			
