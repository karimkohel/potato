import sys, os
import socket
from client_fx import mappings
from usersock import ClientSock
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QApplication, QWidget)
from speech import SpeechPatternRecognizer

class Ui_voiceWindow(QWidget):

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.spr = SpeechPatternRecognizer()
        self.client = ClientSock(socket.gethostbyname(socket.gethostname()),5000, mappings)


    def voiceChat(self, greeting):
        self.spr.speak(greeting)
        while True:
            try:
                print("entered while loop")
                self.client.connect()
                msg = self.spr.listen()
                self.client.sendMsg(msg)
                response, flag = self.client.recvMsg()
                self.spr.speak(response)    
                self.client.flagHandler(flag, response)
            except ConnectionRefusedError:
                print(" - Connection Error: Server didn't connect")
            if msg == "exit":
                self.closeButton()

    

    def setupUi(self, Form):
        
        Form.setObjectName("Voice Chat")
        Form.resize(500,600)
        Form.setFixedSize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.Form = Form
        
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
        self.endButton.clicked.connect(self.closeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate #converts from ui to py
        self.Form.setWindowTitle(_translate("Voice Chat", "Potato is listening.."))
        self.endButton.setText(_translate("Voice Chat", "Back"))

    def closeButton(self):
        self.client.close()
        self.MainWindow.show()
        self.Form.close()