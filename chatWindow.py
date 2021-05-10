# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor, QIcon, QPixmap, QFont


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Start Chat")
        Form.resize(500, 600)
        Form.setFixedSize(500, 600)
        Form.setStyleSheet("background-color: rgb(255, 250, 199);")
        self.chatBox = QtWidgets.QTextBrowser(Form)
        self.chatBox.setGeometry(QtCore.QRect(20, 20, 461, 511))
        self.chatBox.setStyleSheet("background-color: rgb(250, 255, 228);\n"
"background-color: rgb(255, 249, 239);"
"border-radius: 4px;")
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
        self.sendButton.setGeometry(QtCore.QRect(410, 540, 61, 21))
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Start Chat", "Start Chat"))
        self.sendButton.setText(_translate("Start Chat", "Send"))
        self.endButton.setText(_translate("Start Chat", "End Chat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
