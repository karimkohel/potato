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
            self.connect()
        elif flag == 1:
            pass
        elif flag >= 2 or flag <= 8:
            self.functions[str(flag)](response)
            self.close()
            self.connect()
        elif flag == 9:
            return True
        else:
            print("usersockets class : unknown flag in flag handler: ", flag)
        
    def close(self):
        self.clientSocket.close()


