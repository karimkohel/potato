from tomatoServer.functions_tomato import mappings
from fastapi import FastAPI
import neuralintents
import uvicorn
from pydantic import BaseModel

class Request(BaseModel):
    msg : str
    

app = FastAPI()
bot = neuralintents.GenericAssistant("server/tomatoServer/intents_tomato.json", mappings, "server/tomatoServer/model_tomato")
# bot.train_model()
# bot.save_model()
bot.load_model()


@app.post("/potato")
def handleClient(request: Request):
    response = bot.request(request.msg)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5050)

# Protocooooool
# Request:
# {
#     "msg": user text: String
# }

# Response:
# {
#     "res": bot response + function response if any : String,
#     "clientFunctionCode": int
# }