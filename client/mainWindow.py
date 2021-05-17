import sys, os
import socket
from client_fx import mappings
from usersock import ClientSock
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont
from chatWindow import Ui_chatWindow
from voiceWindow import Ui_voiceWindow

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 210, 301, 81))
        self.label.setStyleSheet("font: 87 18pt \"Optima\";\n"
        "color: rgb(147, 0, 0);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.chatButton = QtWidgets.QPushButton(self.centralwidget)
        self.chatButton.setGeometry(QtCore.QRect(130, 300, 113, 32))
        self.chatButton.setStyleSheet("""QPushButton{color: rgb(255, 144, 77);
        background-color: 'white';
        font: 75 italic 16pt "Optima";
        border:0px solid;
        border-radius: 6px;}
        QPushButton::hover{background-color:bisque;
        }"""
        )
        
        self.chatButton.setObjectName("chatButton")
        self.voiceButton = QtWidgets.QPushButton(self.centralwidget)
        self.voiceButton.setGeometry(QtCore.QRect(250, 300, 113, 32))
        self.chatButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.voiceButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.voiceButton.setStyleSheet("""QPushButton{color: rgb(255, 144, 77);
        background-color: 'white';
        font: 75 italic 16pt "Optima";
        border:0px solid;
        border-radius: 6px;}
        QPushButton::hover{background-color:bisque;
        }"""
        )

        self.voiceButton.setObjectName("voiceButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 340, 151, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("kiss-01.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.chatButton.clicked.connect(self.startChat)
        self.voiceButton.clicked.connect(self.startVoice)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate #converts from ui to py
        MainWindow.setWindowTitle(_translate("MainWindow", "Potato is here.."))
        self.label.setText(_translate("MainWindow", "How do you want to ask potato?"))
        self.chatButton.setText(_translate("MainWindow", "Chat"))
        self.voiceButton.setText(_translate("MainWindow", "Voice"))

    def startChat(self):
            self.window2 = QtWidgets.QWidget()
            self.ui = Ui_chatWindow(self.MainWindow)
            self.ui.setupUi(self.window2)
            self.window2.show()
            self.MainWindow.hide()
    
    def startVoice(self):
        self.window3 = QtWidgets.QWidget()
            self.ui = Ui_chatWindow(self.MainWindow)
            self.ui.setupUi(self.window3)
            self.window3.show()
            self.MainWindow.hide()
