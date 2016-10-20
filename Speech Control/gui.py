import tkinter
import speech

class SpeechGui(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		try:
			self.tk.call('wm', 'iconbitmap', self._w, '-default', 'icon.ico')
			self.initialize()
			self.recognizeSpeech = speech.SpeechToCommandLine()
		except Exception as e:
			print("Could not Load Application")
			print(str(e))			
			exit(0)				
		
		
	def initialize(self):
		self.geometry("400x235")
		self.grid()
		
		#buttons for start, stop, and pause
		startButton = tkinter.Button(self, text=u"Start Speech Recognition (F1)", command=self.onStartBtnClick, height=5, width=24)
		startButton.grid(column=0,row=1, sticky='W', padx=10, pady=10)
				
		stopButton = tkinter.Button(self, text=u"Stop Speech Recognition (F2)", command=self.onStopBtnClick, height=5, width=24)
		stopButton.grid(column=1,row=1, sticky='W', padx=10, pady=10)
		
		#label for whatradio buttons to select speech engine/api
		apiLabel = tkinter.Label(self, text=u"Please select a speech recognition engine:", anchor='w')
		apiLabel.grid(column=0,row=2, columnspan=2, sticky='W', pady=10, padx=10)
		
		#radio buttons for the different api's and the default one selected is the normal google speech api
		self.speechEngine = tkinter.StringVar()
		googleSpeechBtn = tkinter.Radiobutton(self, text=u"Google", variable=self.speechEngine, value='googleSpeechRecog')
		googleCloudSpeechBtn = tkinter.Radiobutton(self, text=u"Google Cloud", variable=self.speechEngine, value='googleCloudSpeechRecog')
		sphinxSpeechBtn = tkinter.Radiobutton(self, text=u"CMU Sphinx", variable=self.speechEngine, value='cmuSpeechRecog')
		googleSpeechBtn.grid(column=0, row=3, sticky='W', padx=10)
		googleCloudSpeechBtn.grid(column=0, row=4, sticky='W', padx=10)
		sphinxSpeechBtn.grid(column=0, row=5, sticky='W', padx=10)
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
		
	def startFuncKeyPressed(self, event):
		app.onStartBtnClick()
		
	def stopFuncKeyPressed(self, event):
		app.onStopBtnClick()
	
if __name__=="__main__":
	app = SpeechGui(None)
	app.title('Speech Transcriber')
	app.bind("<F1>", app.startFuncKeyPressed)
	app.bind("<F2>", app.stopFuncKeyPressed)
	app.mainloop()