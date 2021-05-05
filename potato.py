import socket
from usersock import ClientSock
import tkinter as tk
from tkinter import *

# construct clientSock class and bind ip and port with socket
client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
client.connect()

potatoWindow = tk.Tk()
potatoWindow.geometry('800x600')
potatoWindow.title("potato is here")
#canvas= Canvas(potatoWindow)
label = tk.Label(
    text="Hello, I'm your virtual assistant for today :) ",
    foreground="white",  # Set the text color to white
    background="green",  # Set the background color to black
    width=200,
    height=200
)
label.pack()
while True:

    msg = input("Enter msg to potato: ")

    client.sendMsg(msg)
    response = client.recvMsg()
    print(response)

potatoWindow.mainloop()
