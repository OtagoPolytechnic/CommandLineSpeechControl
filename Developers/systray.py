from pystray import Icon, Menu, MenuItem
from PIL import Image

class SystemTray:
	def __init__(self):
		image = Image.open('icon.ico')
		image.load()
		menu = Menu(
			MenuItem('Start Recognition', self.onStartRecognition),
			MenuItem('Stop Recognition', self.onStopRecognition),
			MenuItem('Exit', self.exitProgram))
		self.icon = Icon(name='Speech Transcriber', title='Speech Transcriber', icon=image, menu=menu)
		self.icon.visible = True
	
	def startSysTray(self):		
		self.icon.run()

	def onStartRecognition(self, icon):
		self.startspeech
		print("start")

	def onStopRecognition(self, icon):
		print("stop")

	def exitProgram(self, icon):
		self.icon.stop()
		
if __name__=="__main__":
	tray = SystemTray()
	tray.startSysTray()