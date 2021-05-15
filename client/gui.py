# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import socket
from client_fx import mappings
from usersock import ClientSock
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(500, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 250, 199);")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate #converts from ui to py
        MainWindow.setWindowTitle(_translate("MainWindow", "Potato is here.."))
        self.label.setText(_translate("MainWindow", "How do you want to ask potato?"))
        self.chatButton.setText(_translate("MainWindow", "Chat"))
        self.voiceButton.setText(_translate("MainWindow", "Voice"))
    def startChat(self):
            self.window2 = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.window2)
            self.window2.show()
class Ui_Form(object):

    def setupUi(self, Form):
        try:
            self.client = ClientSock(socket.gethostbyname(socket.gethostname()),5000, mappings)
            self.client.connect()
        except ConnectionRefusedError:
            print(" - Connection Error: Server didn't connect")

        Form.setObjectName("Start Chat")
        Form.resize(500, 600)
        Form.setFixedSize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.chatBox = QtWidgets.QTextBrowser(Form)
        self.chatBox.setGeometry(QtCore.QRect(20, 20, 461, 511))
        self.chatBox.setStyleSheet("background-color: rgb(250, 255, 228);\n"
                                    "background-color: rgb(255, 249, 239);"
                                    "border-radius: 4px;"
        )
        self.chatBox.setObjectName("chatBox")
        self.typingBox = QtWidgets.QTextEdit(Form)
        self.typingBox.setGeometry(QtCore.QRect(20, 545, 381, 31))
        self.typingBox.setPlaceholderText("type here...")
        self.typingBox.setStyleSheet("background-color: rgb(253, 251, 255);"
                                    "border-radius: 4px;"
                                    "border: 1px solid 'gainsboro';"
                                    "font: 75 16pt 'Optima';"
        )
        self.typingBox.setPlaceholderText("type here...")
        self.typingBox.setObjectName("typingBox")
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
        if flag == 0 or flag == 1:
            self.chatBox.append(f"potato: " + response)

    def showInput(self):
        """
        this is a private helper function to help claen the clickButton method
        returns the input of user when button is clicked
        """
        msg = self.typingBox.toPlainText()
        self.chatBox.append(f"you: " + self.typingBox.toPlainText())
        self.typingBox.clear()
        self.typingBox.setPlaceholderText("")
        return msg

    def clickButton(self):

        self.chatBox.setStyleSheet("font:  75 italic 16pt 'Optima';"
                                    "color: 'red';"
        )

        msg = self.showInput()
        self.client.sendMsg(msg)

        response, flag = self.client.recvMsg()
        self.showResponse(response, flag)

        self.client.flagHandler(flag, response)

    def closeButton(self):
        self.client.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
