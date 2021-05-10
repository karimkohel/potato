import socket
from botsocks import ServerSock
import neuralintents
import threading
from functions import mappings


bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
bot.save_model()
# bot.load_model()

serverObj =  ServerSock(socket.gethostbyname(socket.gethostname()), 5000, bot)


while True:
    clientSocket = serverObj.accept()

    t = threading.Thread(target=serverObj.handelClient, args=(clientSocket, ))
    t.start()
