import socket

HEADERSIZE = 20
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 5000))

msg = "Hello there nourhan osama"

data = f'{len(msg):<{HEADERSIZE}}'+ msg

codedMsg = bytes(data, "utf-8")


clientSocket.send(codedMsg)
