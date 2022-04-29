from client_fx import mappings
from usersock import ClientSock
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget
from speech import SpeechPatternRecognizer
import threading
from time import sleep

class Ui_voiceWindow(QWidget):

    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.spr = SpeechPatternRecognizer()
        self.client = ClientSock("172.104.141.41",5000, mappings)
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
        self.Form.setWindowIcon(QtGui.QIcon('hello.png'))
        self.endButton.setText(_translate("Voice Chat", "Back"))

    def handleVoiceControl(self):
        msg = ""
        while self.activeVoice:

            self.spr.waitForWakeupCall("potato")
            try:
                self.client.connect()
            except Exception as e:
                self.spr.speak(" - Connection Error : Server didn't connect : error code : 0CV360")
                print(e)
            
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
                except (ConnectionRefusedError, ConnectionAbortedError):
                    sleep(1)
                    self.spr.speak(" - Connection Error : Server didn't connect : error code : 0CV361")
                    self.activeVoice = False
                except OSError:
                    pass
                except ValueError as e:
                    self.spr.speak(" - Server Error : Pleas contact the developers : error code : 0CV362")
                    print(e)


            if "exit" in msg or not self.activeVoice:
                break

        self.closeButton()
    def closeButton(self):
        self.activeVoice = False
        
        if self.client.clientSocket:
            self.client.close()

        self.MainWindow.show()
        self.Form.close()