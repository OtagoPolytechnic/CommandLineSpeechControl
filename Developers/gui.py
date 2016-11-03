#Import Files
import tkinter
from tkinter import messagebox
import speech
import systray
from threading import Thread
import pyHook

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
			self.recognitionRunning = False
			self.setStartKeyFlag = False
			self.setStopKeyFlag = False
			self.startKey = 'F1'
			self.stopKey = 'F2'
		except Exception as e:
			print("Could not Load Application")
			print(str(e))
			messagebox.showinfo("Could Not Load Application!",str(e))			
			exit(0)				
		
	#sets the dimensions for the UI and adds all the objetcs to it
	def initialize(self):
		self.geometry("400x300")
		self.grid()
		
		#buttons for start and stop
		startButton = tkinter.Button(self, text=u"Start Speech Recognition", command=self.onStartBtnClick, height=5, width=24)
		startButton.grid(column=0,row=1, sticky='W', padx=10, pady=10)
				
		stopButton = tkinter.Button(self, text=u"Stop Speech Recognition", command=self.onStopBtnClick, height=5, width=24)
		stopButton.grid(column=1,row=1, sticky='W', padx=10, pady=10)
		
		#buttons for setting the starting and stopping keys for the speech recognition
		startKeySetButton = tkinter.Button(self, text=u"Set Start Key", command=self.onSetStartBtnClick, height=2, width=24)
		startKeySetButton.grid(column=0,row=6, sticky='W', padx=10, pady=10)
		
		stopKeySetButton = tkinter.Button(self, text=u"Set Stop Key", command=self.onSetStopBtnClick, height=2, width=24)
		stopKeySetButton.grid(column=1,row=6, sticky='W', padx=10, pady=10)
		
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
	
	#When the on set start key is clicked it sets the set start key flag to true
	def onSetStartBtnClick(self):
		self.setStartKeyFlag = True
		print("Press key to set as start key")
	
	#When the on set stop key is clicked it sets the set stp key flag to true
	def onSetStopBtnClick(self):
		self.setStopKeyFlag = True
		print("Press key to set as stop key")
	
	#Sets the clicked key to the key for starting the recognition
	def setStartKey(self, event):
		self.startKey = event.Key
		self.setStartKeyFlag = False
		print("Key Set")
	
	#Sets the clicked key to the key for stopping the recognition
	def setStopKey(self, event):
		self.stopKey = event.Key
		self.setStopKeyFlag = False
		print("Key Set")
		
	#Function for when a key is pressed on the keyboard to see if it is a command key
	def keyBoardPress(self, event):
		#For if the setting either of the keys flag is true it calls the events to set the keys
		if (self.setStartKeyFlag == True) or (self.setStopKeyFlag == True):
			if self.setStartKeyFlag == True:
				self.setStartKey(event)
			if self.setStopKeyFlag == True:
				self.setStopKey(event)
				
		#else it will just check the key against the starting and stopping keys
		else:
			if event.Key == self.startKey:
				self.onStartBtnClick()
			if event.Key == self.stopKey:
				self.onStopBtnClick()
						
		return True

		
# create a hook manager for key board presses
hm = pyHook.HookManager()

#Starts the GUI	
if __name__=="__main__":
	app = SpeechGui(None)
	app.title('Speech Transcriber')
	# watch for all key events
	hm.KeyDown = app.keyBoardPress
	# set the hook for key presses
	hm.HookKeyboard()
	app.mainloop()

	