from urllib.request import Request
from fastapi import FastAPI
import neuralintents
from tomatoServer.functions_tomato import mappings
import uvicorn

class request():
    mas: str
    

app = FastAPI()

request_file = "request.jason"
requests = []

bot = neuralintents.GenericAssistant("server/intents_tomato.json", mappings, "model_tomato")
bot.load_model()

   

@app.post("/potato")
async def handleClient(request: Request):
    #request to bot
    return bot.request(Request.msg)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)