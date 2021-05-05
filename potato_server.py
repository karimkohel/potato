import socket
from botsocks import ServerSock
import neuralintents
from functions import mappings

serverObj =  ServerSock(socket.gethostbyname(socket.gethostname), 5000)

bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
# bot.save_model()
# bot.load_model()

while True:

    msg, clientSocket = serverObj.getMessage()

    if msg == "exit":
        break
    else:
        bot.request(msg, serverObj, clientSocket)