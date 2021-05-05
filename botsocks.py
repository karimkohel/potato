import socket

class ServerSock():
    HEADERSIZE = 20

    def __init__(self, IP, PORT):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((IP, PORT))
        self.serverSocket.listen(10)
        

    def getMessage(self):
        clientSocket, address = self.serverSocket.accept() # blocking code
        print(f"connection from : {address}")
        fullMsg = ''
        newMsg = True

        while True:

            msg = clientSocket.recv(self.HEADERSIZE+5)

            # if msg start then get it's len from the header
            if newMsg:
                decodedMsg = msg[:self.HEADERSIZE].decode("utf-8")
                msgLen = int(decodedMsg)
                newMsg = False

            fullMsg += msg.decode("utf-8")

            if len(fullMsg)-self.HEADERSIZE == msgLen:
                newMsg = True
                break
            
        return fullMsg[self.HEADERSIZE:], clientSocket

    def sendMessage(self, clientSocket, msg):

        data = f'{len(msg):<{self.HEADERSIZE}}'+ msg
        codedMsg = bytes(data, "utf-8")
        clientSocket.send(codedMsg)
        if lastMsg:
            # clientSocket.close()

