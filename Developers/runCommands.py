import time
from win32com import client
from  win32gui import GetWindowText, GetForegroundWindow, SetForegroundWindow, EnumWindows
from win32process import GetWindowThreadProcessId

shell = client.Dispatch("WScript.Shell")

class CommandPrompt:
	
    def __init__(self):        
        #self.openCmd()										Only need if wanting to open a new command prompt window to send to
        #EnumWindows(self.setCmdToForeground, None)			^	
        shell.AppActivate(self.getPid())
		
	#Opens command window
    def openCmd(self):
        shell.run("cmd.exe")
        time.sleep(1)		
	
	#Brings the command prompt window to the foreground
    def setCmdToForeground(self, hwnd, extra):
        if "cmd.exe" in GetWindowText(hwnd):
            SetForegroundWindow(hwnd)
            return

	#Gets the process id for the command prompt window
    def getPid(self):
        window = GetForegroundWindow()
        return GetWindowThreadProcessId(window)[1]

	#Runs command that is passed into the method
    def runCommand(self, command):
        shell.SendKeys(command + " {ENTER}")