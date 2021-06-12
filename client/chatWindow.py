import sys, os
import socket
from unicodedata import name
from client_fx import mappings
from usersock import ClientSock
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QApplication, QWidget)


class Ui_chatWindow(QWidget):
    

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow

    def setupUi(self, Form):
        try:
            self.client = ClientSock("172.104.141.41",5000, mappings)
            self.client.connect()
        except ConnectionRefusedError:
            print(" - Connection Error: Server didn't connect")

        Form.setObjectName("Start Chat")
        Form.resize(500, 600)
        Form.setFixedSize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.Form = Form
        self.chatBox = QtWidgets.QTextBrowser(Form)
        self.chatBox.setGeometry(QtCore.QRect(20, 20, 461, 511))
        self.chatBox.setStyleSheet("background-color: rgb(250, 255, 228);\n"
                                    "background-color: rgb(255, 249, 239);"
                                    "border-radius: 4px;"
        )
        ## moved this from inside the send button to here
        self.chatBox.setStyleSheet("font:  75 16pt 'Optima';"
                                    "color: 'red';"
        )
        ##

        
        self.chatBox.setObjectName("chatBox")
        self.typingBox = QtWidgets.QLineEdit(Form)
        self.typingBox.setGeometry(QtCore.QRect(20, 545, 381, 31))
        self.typingBox.returnPressed.connect(self.clickButton)
        self.typingBox.setPlaceholderText("type here...")
        self.typingBox.setStyleSheet("background-color: rgb(253, 251, 255);"
                                    "border-radius: 4px;"
                                    "border: 1px solid 'gainsboro';"
                                    "font: 75 16pt 'Optima';"
        )
        self.typingBox.setPlaceholderText("type here...")
        self.typingBox.setObjectName("typingBox")
        self.typingBox.setFocus(True)
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(410, 545, 61, 21))
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.setStyleSheet("""QPushButton{color: rgb(255, 144, 77);
                                        background-color: 'white';
                                        font: 75 italic 16pt "Optima";
                                        border: 1px solid 'gainsboro';
                                        border-radius: 4px;}
                                        QPushButton::hover{background-color:lightcyan;
                                        }"""
        )
        self.endButton = QtWidgets.QPushButton(Form)
        self.endButton.setGeometry(QtCore.QRect(410, 570, 61, 21))
        self.endButton.setObjectName("endButton")
        self.endButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.endButton.setStyleSheet("""QPushButton{color: rgb(255, 144, 77);
                                        background-color: 'white';
                                        font: 75 italic 16pt "Optima";
                                        font-size: 13px;
                                        border: 1px solid 'gainsboro';
                                        border-radius: 4px;}
                                        QPushButton::hover{background-color:lightcyan;
                                        }"""
        )
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.sendButton.clicked.connect(self.clickButton)
        self.endButton.clicked.connect(self.closeButton)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Start Chat", "Start Chat"))
        self.sendButton.setText(_translate("Start Chat", "Send"))
        self.endButton.setText(_translate("Start Chat", "End Chat"))

    def showResponse(self, response, flag):
        """
        this is a private helper function to help claen the clickButton method
        takes in server response to show and handle on screen
        """
        if flag == 0 or flag == 1 or flag == 6 or flag == 7 or flag == 8:
            self.chatBox.append(f'<font color="orange"> <i> Potato: </i></font><font color="black"> {response}</font>')

    def showInput(self):
        """
        this is a private helper function to help claen the clickButton method
        returns the input of user when button is clicked
        """
        msg = self.typingBox.text()
        self.chatBox.append(f'<font color="blue"> <i> You: </i></font><font color="black"> {msg}</font>')
        self.typingBox.clear()
        self.typingBox.setPlaceholderText("")
        return msg

    def clickButton(self):


        msg = self.showInput()
        self.client.sendMsg(msg)

        response, flag = self.client.recvMsg()
        self.showResponse(response, flag)

        if self.client.flagHandler(flag, response):
            self.closeButton()


    def closeButton(self):
        self.client.close()
        self.MainWindow.show()
        self.Form.close()