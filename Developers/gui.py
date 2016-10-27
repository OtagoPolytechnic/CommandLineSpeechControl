import tkinter
from tkinter import messagebox
import speech
import systray
from threading import Thread

class SpeechGui(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent = parent
		try:
			#sets the gui icon as the correct icon for the application
			self.tk.call('wm', 'iconbitmap', self._w, '-default', 'icon.ico')
			#calls the initialize method to set up the objects on the gui
			self.initialize()
			#makes an instance of the speech recognition class 
			self.recognizeSpeech = speech.SpeechToCommandLine()
			#boolean so only 1 speech recognition thread can be activated at once
			self.recognitionRunning = False;
		except Exception as e:
			print("Could not Load Application")
			print(str(e))
			messagebox.showinfo("Could Not Load Application!",str(e))			
			exit(0)				
		
	#sets the dimensions for the UI and adds all the objetcs to it
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
		sphinxSpeechBtn = tkinter.Radiobutton(self, text=u"CMU Sphinx", variable=self.speechEngine, value='cmuSpeechRecog')
		googleCloudSpeechBtn = tkinter.Radiobutton(self, text=u"Google Cloud (Under Development)", variable=self.speechEngine, value='googleCloudSpeechRecog')
		googleSpeechBtn.grid(column=0, row=3, sticky='W', padx=10)
		sphinxSpeechBtn.grid(column=0, row=4, sticky='W', padx=10)
		googleCloudSpeechBtn.grid(column=0, row=5, sticky='W', padx=10, columnspan=2)
		#Sets the google recognition to the default
		googleSpeechBtn.select()
			
		self.grid_columnconfigure(0,weight=1)
		
	#Function for when start button is selected	
	def onStartBtnClick(self):
		#If statement so you can not open multiple threads of speech recognition
		if self.recognitionRunning == False:
			#gets the radio button that was selected
			rbtnValue = self.speechEngine.get()	
			#starts the speech recognition
			self.recognizeSpeech.startSpeechRecognition(rbtnValue)
			self.recognitionRunning = True
		else:
			print("Already Running")
			messagebox.showinfo("Running!","Speech Recognition is already Running")
		
	#Function for when stop button is selected	
	def onStopBtnClick(self):
		#If statement so it doesn't try to stop a thread that doesn't exist
		if self.recognitionRunning:
			#stops the speech recognition
			self.recognizeSpeech.stopSpeechRecognition()
			self.recognitionRunning = False
		else:
			messagebox.showinfo("Not Running!","Speech Recognition is not currently running")
			print("Not Running")
		
	def startFuncKeyPressed(self, event):
		self.onStartBtnClick()
		
	def stopFuncKeyPressed(self, event):
		self.onStopBtnClick()
		
if __name__=="__main__":
	app = SpeechGui(None)
	app.title('Speech Transcriber')
	app.bind("<F1>", app.startFuncKeyPressed)
	app.bind("<F2>", app.stopFuncKeyPressed)
	app.mainloop()

	