# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Tracker_Type.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget

class Tracker_Type_Select_UI(QWidget):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog2")
        Dialog.resize(383, 213)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 151))
        self.groupBox.setObjectName("groupBox")

        self.MIL = QtWidgets.QRadioButton(self.groupBox)
        self.MIL.setGeometry(QtCore.QRect(10, 30, 108, 19))
        self.MIL.setObjectName("MIL")

        self.BOOSTING = QtWidgets.QRadioButton(self.groupBox)
        self.BOOSTING.setGeometry(QtCore.QRect(10, 70, 108, 19))
        self.BOOSTING.setObjectName("BOOSTING")

        self.GOTURN = QtWidgets.QRadioButton(self.groupBox)
        self.GOTURN.setGeometry(QtCore.QRect(200, 110, 108, 19))
        self.GOTURN.setObjectName("GOTURN")

        self.KCF = QtWidgets.QRadioButton(self.groupBox)
        self.KCF.setGeometry(QtCore.QRect(10, 110, 108, 19))
        self.KCF.setObjectName("KCF")

        self.MEDIANFLOW = QtWidgets.QRadioButton(self.groupBox)
        self.MEDIANFLOW.setGeometry(QtCore.QRect(200, 70, 151, 19))
        self.MEDIANFLOW.setObjectName("MEDIANFLOW")

        self.TLD = QtWidgets.QRadioButton(self.groupBox)
        self.TLD.setGeometry(QtCore.QRect(200, 30, 108, 19))
        self.TLD.setObjectName("TLD")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(202, 180, 171, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #OK Button Close
        self.event_handler = Tracker_Form_Event_Handler()
        self.pushButton.clicked.connect(self.event_handler.okButton)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tracker Type Select"))
        self.groupBox.setTitle(_translate("Dialog", "Select"))
        self.MIL.setText(_translate("Dialog", "MIL"))
        self.BOOSTING.setText(_translate("Dialog", "BOOSTING"))
        self.GOTURN.setText(_translate("Dialog", "GOTURN"))
        self.KCF.setText(_translate("Dialog", "KCF"))
        self.MEDIANFLOW.setText(_translate("Dialog", "MEDIANFLOW"))
        self.TLD.setText(_translate("Dialog", "TLD"))
        self.pushButton.setText(_translate("Dialog", "OK"))

class Tracker_Form_Event_Handler():

    def okButton(self):
        self.tracker_type_select = Tracker_Type_Select_UI()
        self.tracker_type_select.close()
"""
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    tracker_type_select = Tracker_Type_Select_UI()
    tracker_type_select.setupUi(dialog)

    #Text 바꾸는 예제
    #tracker_type_select.MIL.setText("mil")

    dialog.show()
    sys.exit(app.exec_())
"""