from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

predictionKey = config.get('luis', 'predictionKey')
predictionEndpoint = config.get('luis', 'predictionEndpoint')
app_id = config.get('luis', 'app_id')

runtimeCredentials = CognitiveServicesCredentials(predictionKey)
clientRuntime = LUISRuntimeClient(endpoint=predictionEndpoint, credentials=runtimeCredentials)

def getIntent(request):
    predictionRequest = { "query" : request }
    predictionResponse = clientRuntime.prediction.get_slot_prediction(app_id, "Production", predictionRequest)
    if (predictionResponse.prediction.intents[predictionResponse.prediction.top_intent].score < 0.3):
        return 'None'
    else:
        return predictionResponse.prediction.top_intent