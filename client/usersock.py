import socket

class ClientSock():

    HEADERSIZE = 20

    def __init__(self, ip, port, functions):
        self.PORT = port
        self.IP = ip
        self.functions = functions

    def connect(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.IP, self.PORT))

    def sendMsg(self, msg):
        data = f'{len(msg):<{self.HEADERSIZE}}'+ msg
        codedMsg = bytes(data, "utf-8")
        self.clientSocket.send(codedMsg)
        
    def recvMsg(self):

        fullMsg = ''
        newMsg = True

        while True:

            msg = self.clientSocket.recv(self.HEADERSIZE+5)

            # if msg start then get it's len from the header
            if newMsg:
                decodedMsg = msg[:self.HEADERSIZE].decode("utf-8")
                msgLen = int(decodedMsg)
                newMsg = False

            fullMsg += msg.decode("utf-8")

            if len(fullMsg)-self.HEADERSIZE == msgLen:
                newMsg = True
                break
            
        fullMsg = fullMsg[self.HEADERSIZE:]
        flag = int(fullMsg[-1])
        response = fullMsg[:-1]
        return response, flag

    def flagHandler(self, flag, response):
        if flag == 0:
            self.close()
        elif flag == 2:
            self.functions["2"](response)
            self.close()
        elif flag == 3:
            self.functions["3"](response)
            self.close()
        elif flag == 4:
            self.functions["4"](response)
            self.close()
        elif flag == 5:
            self.functions["5"](response)
            self.close() 
        elif flag == 6:
            self.functions["6"](response)
            self.close() 
        elif flag == 7:
            self.functions["7"](response)
            self.close()                   
        elif flag == 8:
            self.functions["8"](response)
            self.close()           
        
    def close(self):
        self.clientSocket.close()


