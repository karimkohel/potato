import socket

class ClientSock():

    HEADERSIZE = 20

    def __init__(self, IP, PORT):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((IP,PORT))


    def sendMsg(self, msg):
        data = f'{len(msg):<{HEADERSIZE}}'+ msg
        codedMsg = bytes(data, "utf-8")
        self.clientSocket.send(codedMsg)
        
