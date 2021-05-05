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
        
    def recvMsg(self):
        serverSocket, address = self.clientSocket.accept() # blocking code
        print(f"connection from : {address}")
        fullMsg = ''
        newMsg = True

        while True:

            msg = serverSocket.recv(self.HEADERSIZE+5)

            # if msg start then get it's len from the header
            if newMsg:
                decodedMsg = msg[:self.HEADERSIZE].decode("utf-8")
                msgLen = int(decodedMsg)
                newMsg = False

            fullMsg += msg.decode("utf-8")

            if len(fullMsg)-self.HEADERSIZE == msgLen:
                newMsg = True
                break
            
        return fullMsg[self.HEADERSIZE:]
