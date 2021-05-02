import socket

HEADERSIZE = 20

def startConnection(ip, port):

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind((ip, port))
    serverSocket.listen(5)

    return serverSocket

def getMessage(serverSocket):

    clientSocket, address = serverSocket.accept()
    print(f"connection from : {address}")
    fullMsg = ''
    newMsg = True

    while True:

        msg = clientSocket.recv(HEADERSIZE+5)

        # if msg start then get it's len from the header
        if newMsg:
            decodedMsg = msg[:HEADERSIZE].decode("utf-8")
            msgLen = int(decodedMsg)
            newMsg = False

        fullMsg += msg.decode("utf-8")

        if len(fullMsg)-HEADERSIZE == msgLen:
            newMsg = True
            break
        
    clientSocket.close()
    return fullMsg[HEADERSIZE:]