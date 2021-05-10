import socket
from usersock import ClientSock

client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)

while True:
      client.connect()

      while True:
                  msg = input("Enter msg to potato: ")
                  client.sendMsg(msg)
                  response, flag = client.recvMsg()
                  print(response)
                  if msg == "exit":
                        client.close()
                        exit(0)
                  if flag == "0":
                        client.close()
                        break