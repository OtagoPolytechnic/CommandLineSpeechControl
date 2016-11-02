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
	
4. Download [ActiveTcl](http://www.activestate.com/activetcl/downloads)
	* When installing make sure where you are installing it is in the virtual environment
5. Make sure Tkinter is installed in the virtual environment. There should be a "tkinter" folder in the "Lib" folder of your virtual environment.
	* If Tkinter is not in the virtual environment you will need to retrieve it from the original python install on you computer. To do this in the file explorer find your python install and in the "Lib" folder find the "tkinter" folder and copy it then paste it in the "Lib" folder of the vitual environment.

6. Install pyHook. 
	* Downlod [pyHook](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook) wheel file
	* Install using pip
	
	```
	pip install C:\path\to\pyHook\pyHook-1.5.1-cp35-none-win_amd64.whl
	```
	
7. To Run the program start the gui.
	
	```
	python gui.py
	```

*Google Cloud Service does not work with PyPiWin32 installed but this library is needed to send keystrokes to applications. Since the Google Cloud API is still in beta, this may be a import conflict that gets resolved in a later version of the Google Python API client.

*If you do wish to use the Google Cloud API though you will need to go to the [Google Cloud Platform](https://cloud.google.com/speech/) and activate to Speech Recognition service to receive JSON credentials to accesss the API.
	
##Modules Used

####SpeechRecognition
This module is the main module for speech recognition as it has the class that is used for listening to the microphone and getting an audio file. This module also contains the necessary code for the normal Google speech recognition to be used. The module also contains code to use the CMU Sphinx recognition service.

* This module is currently in the process of adding more recognition services(IBM Speech To Text, Microsoft Bing Voice Recognition).

####PocketSphinx
This module is for the CMU Sphinx recognition service. This modules is required as the CMU Sphinx service is an offline service. Since it does not need to be connected to the internet the module needs to downloaded as it contains all the necessary elements to do speech recognition.

####PyAudio
This is needed for the SpeechRecognition module to work. Without this module SpeechReconition is unable to find a microphone and understand any audio.

####Google Api Python Client
This modules contains all the code Google requires for their cloud speech recognition to work.

####PyPiWin32
PyPiWin is used to get the process of the application that is currently on the top and then sends keystrokes to that application. This module only works with Microsoft Windows computers.

####Pystray
This makes a sytem tray for the application. Though it is not currently integrated with the application.

####pyHook
This module checks when a key on the keyboard has been pressed no matter which application you are in.

####PyInstaller
This was used to make the python files into and executable for easy use.

##File Breakdown

####cloudSpeech
Calls cloudTranscribe which returns a JSON string then it parses the JSON string to get out the transcript. It then returns the transcript to where ever it was called from.

####cloudTranscribe
Takes in an audio file then sends it away to the google cloud service to be transcribed. Google returns a JSON string which this then returns. 

* This file should also set the variable "GOOGLE_APPLICATION_CREDENTIALS" for the oauth2client.client file. If you have done this and you are sure that you have made your Google Credentials correct and Enabled billing in the Google developers console, it may be necessary to set the path to the JSON file in the authorization file. To do this in your virtual environment got to "Lib\site-packages\oauth2client\" and open the "client.py" file. Then at this point set the "GOOGLE_APPLICATION_CREDENTIALS" to the json credentials file path. If it still is not working in the same file go to line 1224 and set "credentials_filename" to equal the json credentials file path.

####commandsFile
This file contains some commands that are used with the command prompt. Although it currently only contains words related to command prompt commands anything can be added so that if you say a particullar word or phrase it will be replaced with something else. To add to this file simply enter the word or phrase you wish to find in the first column then enter what you would like it to be replaced with in the second column and save the file. 

####gui
Has the code that creates the user interface and starts and stops the speech recognition when buttons are pressed. Also contains the pyHook code for checking key presses from the keyboard and when either 'F1' or 'F2' is pressed no matter which application you are in it will start and stop listening for speech.

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
