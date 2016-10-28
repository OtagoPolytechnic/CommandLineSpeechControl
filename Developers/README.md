#Developer

##Installation and Use
1. Create a python virtual environment on your machine and activate it.

	```
	C:\path\to\virtual\env virtualenv nameofenvironment
	C:\path\to\virtual\env nameofenvironment\Scripts\activate
	```

2. Navigate your way to the Developers folder in the repository you downloaded.
3. Install the dependencies needed to run the program.

	```
	pip install -r requirements.txt
	```
	
4. Download ActiveTcl from http://www.activestate.com/activetcl/downloads
	* When installing make sure where you are installing it is in the virtual environment
5. Make sure Tkinter is installed in the virtual environment.
	* If Tkinter is not in the virtual environment you will need to retrieve it from the original python install on you computer. To do this in the file explorer find your python install and in the "Lib" folder find the "tkinter" folder and copy it then paste it in the "Lib" folder of the vitual environment.
6. To Run the program start the gui.
	
	```
	python gui.py
	```

##Modules Used

####SpeechRecognition
This module is the main module for speech recognition as it has the class that is used for listening to the microphone and getting an audio file. This module also contains the necessary code for the normal Google speech recognition to be used. The module also contains code to use the CMU Sphinx recognition service.

####PocketSphinx
This module is for the CMU Sphinx recognition service. This modules is required as the CMU Sphinx service is an offline service. Since it does not need to be connected to the internet the module needs to downloaded as it contains all the necessary elements to do speech recognition.

####PyAudio
This is needed for the SpeechRecognition module to work. Without this module SpeechReconition is unable to find a microphone and understand any audio.

####Google Api Python Client
This modules contains all the code google requires for their cloud speech recognition to work.

####PyPiWin32
PyPiWin is used to get the process of the application that is currently on the top and then sends keystrokes to that application. This module only works with Microsoft Windows computers.

####Pystray
This makes a sytem tray for the application. Though it is not currently integrated with the application.

##File Breakdown

####cloudSpeech
Calls cloudTranscribe which returns a JSON string then it parses the JSON string to get out the transcript. It then returns the transcript to where ever it was called from.

####cloudTranscribe
Takes in an audio file then sends it away to the google cloud service to be transcribed. Google returns a JSON string which this then returns.

####commandsFile
This file contains some commands that are used with the command prompt. Although it currently only contains words related to command prompt commands anything can be added so that if you say a particullar word or phrase it will be replaced with something else. To add to this file simply enter the word or phrase you wish to find in the first column then enter what you would like it to be replaced with in the second column and save the file. 

####gui
Has the code that creates the user interface and starts and stops the speech recognition when buttons are pressed.

####icon
This is just the application icon

####requirements
This txt file contains the names of all the modules, that need to be downloaded for this application to work, so that they can be easily installed. 

#####runCommands
Conatins the code that identifies the correct process of the window on the top (hopefully the one that is wanted to be used) and then sends the string that was returned to that application that was identified.

####speech
This is a bit of a worker class. It is where the functions to start listening and stop listening are called and where it calls the speech recognition.It contains the words that are in the command file and checks them against what was transcribed and calls the function in the run commands file that sends the string to the correct application.

####systray(not currently implemented)
This has the code to create a system tray for the application.

