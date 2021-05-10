import socket

class ServerSock():
    HEADERSIZE = 20

    def __init__(self, IP, PORT, bot):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((IP, PORT))
        self.serverSocket.listen(10)
        self.bot = bot
        print("Listening on " + str(IP) + ":" + str(PORT))
        
    def accept(self):
        clientSocket, address = self.serverSocket.accept() # blocking code
        print(f"connection from : {address}")
        return clientSocket

    def getMessage(self, clientSocket):
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
            
        return fullMsg[self.HEADERSIZE:]

    def sendMessage(self, clientSocket, msg):

        data = f'{len(msg):<{self.HEADERSIZE}}'+ msg
        codedMsg = bytes(data, "utf-8")
        clientSocket.send(codedMsg)

    def handelClient(self, clientSocket):
        try:
            msg = self.getMessage(clientSocket)
            self.bot.request(msg, self, clientSocket)
        except ConnectionResetError:
            pass
        except Exception as e:
            print(e)
        print("closing connection")
        clientSocket.close()
