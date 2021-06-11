import sys, os
import socket
from client_fx import mappings
from usersock import ClientSock
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QApplication, QWidget)
from speech import SpeechPatternRecognizer
import threading
from time import sleep

class Ui_voiceWindow(QWidget):

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.spr = SpeechPatternRecognizer()
        self.client = ClientSock(socket.gethostbyname(socket.gethostname()),5000, mappings)
        # make a flag for the voice thread to watch and die when it is flipped
        self.activeVoice = True

        self.proc = threading.Thread(target=self.handleVoiceControl)
        self.proc.daemon = True
        self.proc.start()

    def setupUi(self, Form):
        
        Form.setObjectName("Voice Chat")
        Form.resize(500,600)
        Form.setFixedSize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.Form = Form
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 270, 151, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("kiss-01.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        
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

    def handleVoiceControl(self):
        while self.activeVoice:

            self.spr.waitForWakeupCall("potato")
            self.client.connect()
            
            while self.activeVoice:
                try:
                    msg = self.spr.listen()
                    self.client.sendMsg(msg)
                    response, flag = self.client.recvMsg()
                    if flag == 0 or flag == 1 or flag == 6 or flag == 7 or flag == 8 or flag == 9:
                        self.spr.speak(response)    
                    exitFlag = self.client.flagHandler(flag, response)
                    if "exit" in msg or flag == 9:
                        break
                except ConnectionRefusedError:
                    sleep(1)
                    self.spr.speak(" - Connection Error : Server didn't connect")
                    self.activeVoice = False


            if "exit" in msg or not self.activeVoice:
                break

        self.closeButton()
    def closeButton(self):
        self.activeVoice = False
        try:
            self.client.close()
        except Exception as e:
            print(e, '\n', "close voice window error")
        self.MainWindow.show()
        self.Form.close()