# [START import_libraries]
import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
# [END import_libraries]


# [START authenticating]
DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


# Application default credentials provided by env variable

def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])

    http = httplib2.Http()
    credentials.authorize(http)


    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)
# [END authenticating]


def main(speech_file):
    """Transcribe the given audio file.
    Args:
        speech_file: the name of the audio file.
    """
    
    # [START construct_request]
    speech_content = base64.b64encode(speech_file)

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'LINEAR16',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                # See https://goo.gl/A9KJ1A for a list of supported languages.
                #'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()
    return(json.dumps(response))
    # [END send_request]

# [START run_application]
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)
    # [END run_application]