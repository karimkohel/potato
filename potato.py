import socket
from usersock import ClientSock

client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
client.connect()

while True:


    msg = input("Enter msg to potato: ")

    client.sendMsg(msg) # this will send msg to server 

    # next we will accept responses here
    response = client.recvMsg()

    print(response)
    # test

