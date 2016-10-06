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
		
		startButton = tkinter.Button(self,text=u"Start Speech Recognition", command=self.onStartBtnClick, height=5, width=20)
		startButton.grid(column=0,row=1,pady=10)
		
		pauseButton = tkinter.Button(self,text=u"Pause Speech Recognition", command=self.onPauseBtnClick, height=5, width=20)
		pauseButton.grid(column=1,row=1,padx=8)
		
		stopButton = tkinter.Button(self,text=u"Stop Speech Recognition", command=self.onStopBtnClick, height=5, width=20)
		stopButton.grid(column=2,row=1,padx=8)
		
		self.grid_columnconfigure(0,weight=1)
		
		
	def onStartBtnClick(self):
		self.recognizeSpeech.startSpeechRecognition()
		
		
	def onStopBtnClick(self):
		self.recognizeSpeech.stopSpeechRecognition()
		
		
	def onPauseBtnClick(self):
		print("pause")
		
		
if __name__=="__main__":
	app = speechGui(None)
	app.title('Command Line Speech Control')
	app.mainloop()