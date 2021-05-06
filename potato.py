# import socket
# from usersock import ClientSock
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

# construct clientSock class and bind ip and port with socket
# client = ClientSock(socket.gethostbyname(socket.gethostname()),5000)
# client.connect()
WIN_WIDTH = 500
WIN_HEIGHT = 600
potatoWindow = tk.Tk()
potatoWindow.geometry('500x600')
potatoWindow.resizable(False,False)
potatoWindow.title("potato is here")
canvas = Canvas(potatoWindow,width = 500,height = 600, background = 'red')


img = ImageTk.PhotoImage(Image.open("hello.png"))  
canvas.create_image(0, 0, anchor=CENTER, image=img, tags="bg_img")

label = tk.Label(
    text="Hello, I'm your virtual assistant for today :) ",
    foreground="green",  # Set the text color to white
    background = "#ffe5b4",
    width= int(WIN_WIDTH/2),
    height= int(WIN_HEIGHT/0.7),
    font=("Symbol", 16)   
)
label.pack()
canvas.pack()
# while True:

#     msg = input("Enter msg to potato: ")

#     client.sendMsg(msg)
#     response = client.recvMsg()
#     print(response)

potatoWindow.mainloop()
