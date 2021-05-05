import socket
from botsocks import ServerSock
import neuralintents
from functions import mappings

serverObj =  ServerSock(socket.gethostbyname(socket.gethostname()), 5000)

bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
bot.save_model()
# bot.load_model()

clientSocket = serverObj.accept()
while True:

    msg = serverObj.getMessage(clientSocket)
    print("go msg : " + str(msg))

    if msg == "exit":
        break
    else:
        bot.request(msg, serverObj, clientSocket)