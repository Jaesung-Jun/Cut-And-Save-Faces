# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Resize_Output.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
import os

class Resize_UI(QWidget):

    def setupUi(self, Resize, wh):    

        Resize.setObjectName("Resize")
        Resize.resize(290, 122)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Resize.setFont(font)
        self.width = QtWidgets.QTextEdit(Resize)
        self.width.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.width.setObjectName("width")
        self.label = QtWidgets.QLabel(Resize)
        self.label.setGeometry(QtCore.QRect(140, 60, 64, 15))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.height = QtWidgets.QTextEdit(Resize)
        self.height.setGeometry(QtCore.QRect(160, 50, 121, 31))
        self.height.setObjectName("height")
        self.label_2 = QtWidgets.QLabel(Resize)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Resize)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 64, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Resize)
        self.label_4.setGeometry(QtCore.QRect(200, 30, 64, 15))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Resize)
        self.pushButton.setGeometry(QtCore.QRect(12, 90, 271, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Resize)
        QtCore.QMetaObject.connectSlotsByName(Resize)

        self.event_handler = Resize_Form_Event_Handler(Resize, self, wh)

    def retranslateUi(self, Resize):
        _translate = QtCore.QCoreApplication.translate
        Resize.setWindowTitle(_translate("Resize", "Resize Output"))
        self.label.setText(_translate("Resize", "x"))
        self.label_2.setText(_translate("Resize", "Resize to"))
        self.label_3.setText(_translate("Resize", "Width"))
        self.label_4.setText(_translate("Resize", "Height"))
        self.pushButton.setText(_translate("Resize", "OK"))

    def getOutput(self):
        self._output = self.event_handler.getOutput()
        return self._output

class Resize_Form_Event_Handler():
    def __init__(self, dialog, widget, wh):
        self.wh = wh
        self.widget = widget
        self.dialog = dialog

        if self.wh[0] != "" or self.wh[1] != "":
            self.widget.width.setText(self.wh[0])
            self.widget.height.setText(self.wh[1])

        self.widget.pushButton.clicked.connect(self.okButton)
        self.widget.width.textChanged.connect(lambda: self.onlyNumberInTextEdit(self.widget.width.toPlainText()))
        self.widget.height.textChanged.connect(lambda: self.onlyNumberInTextEdit(self.widget.height.toPlainText()))

        #set icon
        self.setIcons()

    def setIcons(self):
        icons_dir = os.path.dirname(os.path.realpath(__file__)) + "/icons/"
        # ============Form Icon Setting============ #
        self.dialog.setWindowIcon(QtGui.QIcon(icons_dir + 'lena.ico'))
        # ============Button Icon Setting============ #
        self.widget.pushButton.setIcon(QtGui.QIcon(icons_dir + 'select.ico'))
        self.widget.pushButton.setIconSize(QtCore.QSize(17, 17))

    def okButton(self):
        regex = re.compile("^[0-9]+$")
        if self.widget.width.toPlainText() == "" or self.widget.height.toPlainText() == "":
            QMessageBox.about(self.widget, "Error", "You should enter any number")
        elif regex.match(self.widget.width.toPlainText()) == None or regex.match(self.widget.height.toPlainText()) == None:
            QMessageBox.about(self.widget, "Error", "You can enter only number")
            self.widget.width.setText("")
            self.widget.height.setText("")
        else:
            self.wh[0] = self.widget.width.toPlainText()
            self.wh[1] = self.widget.height.toPlainText()
            self.dialog.accept()

    def onlyNumberInTextEdit(self, text):
        regex = re.compile("^[0-9]+$")
        if text == "":
            pass
        elif regex.match(text) == None:
            QMessageBox.about(self.widget, "Error", "You can enter only number")
    
    def getOutput(self):
        return self.wh
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Resize = QtWidgets.QWidget()
    ui = Resize_UI()
    ui.setupUi(Resize)
    Resize.show()
    sys.exit(app.exec_())
"""