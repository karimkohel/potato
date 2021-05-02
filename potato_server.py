import socket

HEADERSIZE = 20

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((socket.gethostname(), 5000))
serverSocket.listen(5)

while True:

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
            print(fullMsg[HEADERSIZE:])
            newMsg = True
            break
        


    clientSocket.close()
    print(fullMsg)
