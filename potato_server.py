import socket
import botsocks
import neuralintents
from functions import mappings

# serverSocket = botsocks.startConnection(socket.gethostname(), 5000)
bot = neuralintents.GenericAssistant("intents.json", mappings, "model")
bot.train_model()
# bot.save_model()
# bot.load_model()

while True:

    # msg = botsocks.getMessage(serverSocket)
    msg = input("enter msg: ")

    if msg == "exit":
        break
    else:
        bot.request(msg)
