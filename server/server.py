from tomatoServer.functions_tomato import mappings
from fastapi import FastAPI
import neuralintents
import uvicorn
from pydantic import BaseModel

class Request(BaseModel):
    msg : str
    

app = FastAPI()
tomatoBot = neuralintents.GenericAssistant("server/tomatoServer/intents_tomato.json", mappings, "server/tomatoServer/model_tomato")
# tomatoBot.train_model()
# tomatoBot.save_model()
tomatoBot.load_model()


@app.post("/potato")
def handleClient(request: Request):
    response = tomatoBot.request(request.msg)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.2.10", port=5050)

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