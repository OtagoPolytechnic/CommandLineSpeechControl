#Import Files
import tempfile
import json
from cloudTranscribe import main as getJsonFromGoogle

#Parses the JSON that was returned from google and gets the best match for what was said 
def ParseJson(jsonString):
	parsedJson = json.loads(jsonString)
	results = parsedJson['results']
	results = results[0]
	alternatives = results['alternatives']
	alternatives = alternatives[0]
	transcript = alternatives['transcript']
	return transcript

#Calls cloud transcribe to send the speech file away to google
def Recognize(audioFile):
	returnJson = getJsonFromGoogle(audioFile)
	#Calls the parse json method to get the speech string
	speechString = ParseJson(returnJson)
	return speechString