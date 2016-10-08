import tkinter
import speech

class speechGui(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		self.recognizeSpeech = speech.SpeechToCommandLine()
		
		
	def initialize(self):
		self.geometry("500x500")
		self.grid()
		
		#buttons for start, stop, and pause
		startButton = tkinter.Button(self, text=u"Start Speech Recognition", command=self.onStartBtnClick, height=5, width=20)
		startButton.grid(column=0,row=1,pady=10)
		
		pauseButton = tkinter.Button(self, text=u"Pause Speech Recognition", command=self.onPauseBtnClick, height=5, width=20)
		pauseButton.grid(column=1,row=1,padx=8)
		
		stopButton = tkinter.Button(self, text=u"Stop Speech Recognition", command=self.onStopBtnClick, height=5, width=20)
		stopButton.grid(column=2,row=1,padx=8)
		
		#label for whatradio buttons to select speech engine/api
		apiLabel = tkinter.Label(self, text=u"Please select a speech recognition engine:", anchor='w')
		apiLabel.grid(column=0,row=2, columnspan=2, sticky='W', pady=10, padx=8)
		
		#radio buttons for the different api's and the default one selected is the normal google speech api
		self.speechEngine = tkinter.StringVar()
		googleSpeechBtn = tkinter.Radiobutton(self, text=u"Google", variable=self.speechEngine, value='googleSpeechRecog')
		googleCloudSpeechBtn = tkinter.Radiobutton(self, text=u"Google Cloud", variable=self.speechEngine, value='googleCloudSpeechRecog')
		sphinxSpeechBtn = tkinter.Radiobutton(self, text=u"CMU Sphinx", variable=self.speechEngine, value='cmuSpeechRecog')
		googleSpeechBtn.grid(column=0, row=3, sticky='W', padx=8)
		googleCloudSpeechBtn.grid(column=0, row=4, sticky='W', padx=8)
		sphinxSpeechBtn.grid(column=0, row=5, sticky='W', padx=8)
		googleSpeechBtn.select()
		
		
		self.grid_columnconfigure(0,weight=1)
		
	#Function for when start button is selected	
	def onStartBtnClick(self):
		#gets the radio button that was selected
		rbtnValue = self.speechEngine.get()	
		#starts the speech recognition
		self.recognizeSpeech.startSpeechRecognition(rbtnValue)
		
	#Function for when stop button is selected	
	def onStopBtnClick(self):
		#stops the speech recognition
		self.recognizeSpeech.stopSpeechRecognition()
		
	#Function for when pause button is selected		
	def onPauseBtnClick(self):
		print("pause")
		
		
if __name__=="__main__":
	app = speechGui(None)
	app.title('Command Line Speech Control')
	app.mainloop()