from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

predictionKey = os.getenv('predictionKey', None)
predictionEndpoint = os.getenv('predictionEndpoint', None)
app_id = os.getenv('app_id', None)

runtimeCredentials = CognitiveServicesCredentials(predictionKey)
clientRuntime = LUISRuntimeClient(endpoint=predictionEndpoint, credentials=runtimeCredentials)

def getIntent(request):
    predictionRequest = { "query" : request }
    predictionResponse = clientRuntime.prediction.get_slot_prediction(app_id, "Production", predictionRequest)
    if (predictionResponse.prediction.intents[predictionResponse.prediction.top_intent].score < 0.3):
        return 'None'
    else:
        return predictionResponse.prediction.top_intent