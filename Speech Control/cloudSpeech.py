import tempfile
import json
from cloudTranscribe import main as getJsonFromGoogle

def ParseJson(jsonString):
	parsedJson = json.loads(jsonString)
	results = parsedJson['results']
	results = results[0]
	alternatives = results['alternatives']
	alternatives = alternatives[0]
	transcript = alternatives['transcript']
	return transcript


def Recognize(audioFile):
	returnJson = getJsonFromGoogle(audioFile)
	speechString = ParseJson(returnJson)
	return speechString