import socket
from usersock import ClientSock
import tkinter
from tkinter import *

# construct clientSock class and bind ip and port with socket
client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
client.connect()

potatoWindow = Tk()
potatoWindow.geometry('800x600')
potatoWindow.title("potato is here")

while True:

    msg = input("Enter msg to potato: ")

    client.sendMsg(msg)
    response = client.recvMsg()
    print(response)

potatoWindow.mainloop()
