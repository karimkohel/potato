<<<<<<< HEAD
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

=======
from urllib.request import Request
from fastapi import FastAPI
import neuralintents
from tomatoServer.functions_tomato import mappings
import uvicorn

class request():
    mas: str
>>>>>>> 18c8d8f51c56ede9d3556369602d813c2efa7594
    

app = FastAPI()


bot = neuralintents.GenericAssistant("server/tomatoServer/intents_tomato.json", mappings, "model_tomato")
bot.train_model()
bot.save_model()
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


<<<<<<< HEAD
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5050)
=======
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5050)
>>>>>>> 18c8d8f51c56ede9d3556369602d813c2efa7594
