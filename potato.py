import socket
from usersock import ClientSock

# construct clientSock class and bind ip and port with socket
client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
client.connect()

while True:

    msg = input("Enter msg to potato: ")

    client.sendMsg(msg)
    response = client.recvMsg()
    print(response)