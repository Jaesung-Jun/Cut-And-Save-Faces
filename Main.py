# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

#Class : Class_Test
#Function : functionTest
#Variable : variable_test

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QDir 
import os
import TrackerForm
import ctypes
import ResizeForm

class Main_Form_Ui(QDialog):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(823, 600)

        self.run_button = QtWidgets.QPushButton(Dialog)
        self.run_button.setGeometry(QtCore.QRect(360, 470, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.run_button.setFont(font)
        self.run_button.setObjectName("run_button")

        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(360, 550, 461, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 440, 331, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.face_align_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.face_align_checkBox.setGeometry(QtCore.QRect(10, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.face_align_checkBox.setFont(font)
        self.face_align_checkBox.setObjectName("face_align_checkbox")

        self.resize_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.resize_checkBox.setGeometry(QtCore.QRect(10, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.resize_checkBox.setFont(font)
        self.resize_checkBox.setObjectName("resize_checkBox")

        self.path_text = QtWidgets.QTextEdit(Dialog)
        self.path_text.setGeometry(QtCore.QRect(70, 10, 591, 31))
        self.path_text.setObjectName("path_text")
        self.path_text.setText("please select path")
        self.path_text.setEnabled(False)

        self.path_label = QtWidgets.QLabel(Dialog)
        self.path_label.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")

        self.browse_button = QtWidgets.QPushButton(Dialog)
        self.browse_button.setGeometry(QtCore.QRect(670, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")

        self.sample_photo_view = QtWidgets.QLabel(Dialog)
        self.sample_photo_view.setGeometry(QtCore.QRect(20, 70, 381, 341))
        self.sample_photo_view.setObjectName("sample_photo_view")
        self.sample_photo_view.setAlignment(QtCore.Qt.AlignCenter)

        self.image_box = QtWidgets.QGroupBox(Dialog)
        self.image_box.setGeometry(QtCore.QRect(20, 70, 382, 342))

        self.directory_tree_view = QtWidgets.QTreeView(Dialog)
        self.directory_tree_view.setGeometry(QtCore.QRect(430, 70, 381, 341))
        self.directory_tree_view.setObjectName("directory_tree_view")
        self.directory_tree_view.setAnimated(False)
        self.directory_tree_view.setIndentation(20)
        self.directory_tree_view.setSortingEnabled(True)
        self.directory_tree_view.setWindowTitle("directory view")

        self.image_view_label = QtWidgets.QLabel(Dialog)
        self.image_view_label.setGeometry(QtCore.QRect(20, 50, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.image_view_label.setFont(font)
        self.image_view_label.setObjectName("image_view_label")

        self.directory_view_label = QtWidgets.QLabel(Dialog)
        self.directory_view_label.setGeometry(QtCore.QRect(430, 50, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.directory_view_label.setFont(font)
        self.directory_view_label.setObjectName("directory_view_label")

        self.made_by_label = QtWidgets.QLabel(Dialog)
        self.made_by_label.setGeometry(QtCore.QRect(360, 440, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.made_by_label.setFont(font)
        self.made_by_label.setObjectName("made_by_label")

        self.tracker_type_button = QtWidgets.QPushButton(Dialog)
        self.tracker_type_button.setGeometry(QtCore.QRect(580, 420, 231, 41))
        self.tracker_type_button.setObjectName("tracker_type_button")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CASF"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.groupBox.setTitle(_translate("Dialog", "Options"))
        self.face_align_checkBox.setText(_translate("Dialog", "Face Alignment"))
        self.resize_checkBox.setText(_translate("Dialog", "Resize Outputs"))
        self.path_label.setText(_translate("Dialog", "Path"))
        self.browse_button.setText(_translate("Dialog", "Browse"))
        self.image_view_label.setText(_translate("Dialog", "Image View"))
        self.directory_view_label.setText(_translate("Dialog", "Directory View"))
        self.made_by_label.setText(_translate("Dialog", "Made by Jae-sung Jun"))
        self.tracker_type_button.setText(_translate("Dialog", "Tracker Type Select"))

class Main_Form_Event_Handle:

    def __init__(self, main_dialog):
        self.tracker_type = ""
        self.path = ""
        self.wh = ["",""]
        self.main_dialog = main_dialog
        
        self.main_dialog.tracker_type_button.clicked.connect(self.trackerTypeButtonEvent)
        self.main_dialog.browse_button.clicked.connect(self.browseFileDialog)
        self.main_dialog.directory_tree_view.clicked.connect(self.directoryViewClick)
        self.main_dialog.resize_checkBox.stateChanged.connect(self.resizeCheckbox)
    
    def trackerTypeButtonEvent(self):
        tracker_form_dialog = QtWidgets.QDialog()
        tracker_type_select = TrackerForm.Tracker_Type_Select_UI()
        tracker_type_select.setupUi(tracker_form_dialog, self.tracker_type)
        tracker_form_dialog.show()
        tracker_form_dialog.exec_()
        self.tracker_type = tracker_type_select.getOutput()
        if self.tracker_type != "":
            self.main_dialog.tracker_type_button.setText("Selected Tracker Type : {}".format(self.tracker_type))
    
    def browseFileDialog(self):

        self.path = str(QtWidgets.QFileDialog.getExistingDirectory(self.main_dialog, "Select Directory"))
        #Path is Exist
        if os.path.exists(self.path) == True:
            """
            for (path, dir, files) in os.walk("c:/"):
                for filename in files:
                    ext = os.path.splitext(filename)[-1]
                    if ext == '.jpg' or ext == '.png':
                        img_file_path = path + "/" + filename
                        print(img_file_path)
            """
            self.main_dialog.path_text.setText(self.path)  
            self.model = QtWidgets.QFileSystemModel()
            self.model.setRootPath('')
            self.main_dialog.directory_tree_view.setModel(self.model) 
            self.main_dialog.directory_tree_view.setRootIndex(self.model.index(self.path))
        #Path Not Selected
        elif self.path == "":
            pass

        #Path is Not Exist
        elif os.path.exists(self.path) == False:
            self.errorMessageBox("Directory Load Error", "Please select other directory")
    
    def directoryViewClick(self, index):
        path = self.main_dialog.sender().model().filePath(index)
        fname, ext = os.path.splitext(path)
        if ext == '.jpg' or ext == '.png':
            image_profile = QtGui.QPixmap(path)
            image_profile = image_profile.scaledToHeight(381)
            image_profile = image_profile.scaledToWidth(341)
            self.main_dialog.sample_photo_view.setPixmap(image_profile)
        else:
            self.main_dialog.sample_photo_view.setText("This File is Not Support")

    def resizeCheckbox(self):
        if self.main_dialog.resize_checkBox.isChecked() == True:
            resize_form_dialog = QtWidgets.QDialog()
            resize_output = ResizeForm.Resize_UI()
            resize_output.setupUi(resize_form_dialog, self.wh)
            resize_form_dialog.show()
            resize_form_dialog.exec_()
            self.wh = resize_output.getOutput()

            
    def errorMessageBox(self, title="", content="Error"):
        QtWidgets.QMessageBox.about(self.main_dialog, title, content)


#class CASF_Main_Function():


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QDialog()
    
    main_form_ui = Main_Form_Ui()
    main_form_ui.setupUi(dialog)

    # ===========Event Handle Codes=============== #
    event_handle = Main_Form_Event_Handle(main_form_ui)

    # ============Icon Setting============#
    now_dir = os.path.dirname(os.path.realpath(__file__))
    dialog.setWindowIcon(QtGui.QIcon(now_dir + '/lena.ico'))
    myappid = 'Jaesung_Jun.github.CASF.1.5-GUI' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    dialog.show()
    sys.exit(app.exec_())
