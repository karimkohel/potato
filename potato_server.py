import socket
import botsocks

serverSocket = botsocks.startConnection(socket.gethostname(), 5000)

while True:

    msg = botsocks.getMessage(serverSocket)
    print(msg)
