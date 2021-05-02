import socket

HEADERSIZE = 20

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((socket.gethostname(), 5000))
serverSocket.listen(5)

while True:

    clientSocket, address = serverSocket.accept()
    print(f"connection from : {address}")
    data = clientSocket.recv(30)
    msg = data.decode("utf-8")
    print(msg)
    clientSocket.close()