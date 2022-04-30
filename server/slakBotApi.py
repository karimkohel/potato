from http import client
from fastapi import FastAPI
import neuralintents
from functions_tomato import mappings
from fastapi.encoders import jsonable_encoder
from requests import request


app = FastAPI()

request_file = "request.jason"
requests = []

bot = neuralintents.GenericAssistant("server/intents_tomato.json", mappings, "model_tomato")
bot.load_model()

   

@app.post("/potato")
async def handleClient(Jason):
    #request to bot
    return bot.request(Jason.msg)


    
    
    


    


    









bot = neuralintents.GenericAssistant("server/intents.json", mappings, "model")
bot.load_model()