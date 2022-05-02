# from http import client
# from urllib.request import Request
from fastapi import FastAPI
import neuralintents
from functions_tomato import mappings
# from fastapi.encoders import jsonable_encoder
# from requests import request
# import uvicorn
from pydantic import BaseModel
class Request(BaseModel):
    msg : str

    

app = FastAPI()


bot = neuralintents.GenericAssistant("server/intents_tomato.json", mappings, "model_tomato")
bot.load_model()

# @app.get("/")
# def hello():
#     return{"data":"hello"}

@app.post("/potato")
def handleClient(request: Request):
    print(request.msg)
    response = bot.request(request.msg)
    return{"data":response}




    #request to bot
    # return bot.request(Request.msg)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5050)