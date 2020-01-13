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
import ctypes
import ResizeForm
import CASF

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

        self.progress_bar = QtWidgets.QProgressBar(Dialog)
        self.progress_bar.setGeometry(QtCore.QRect(360, 550, 461, 41))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")

        self.group_box = QtWidgets.QGroupBox(Dialog)
        self.group_box.setGeometry(QtCore.QRect(20, 440, 331, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.group_box.setFont(font)
        self.group_box.setObjectName("group_box")

        self.face_align_checkBox = QtWidgets.QCheckBox(self.group_box)
        self.face_align_checkBox.setGeometry(QtCore.QRect(10, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.face_align_checkBox.setFont(font)
        self.face_align_checkBox.setObjectName("face_align_checkbox")

        self.line = QtWidgets.QFrame(self.group_box)
        self.line.setGeometry(QtCore.QRect(0, 100, 331, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.real_face_radio_button = QtWidgets.QRadioButton(self.group_box)
        self.real_face_radio_button.setGeometry(QtCore.QRect(10, 130, 161, 16))
        self.real_face_radio_button.setObjectName("real_face_radio_button")

        self.anime_face_radio_button = QtWidgets.QRadioButton(self.group_box)
        self.anime_face_radio_button.setGeometry(QtCore.QRect(10, 110, 141, 16))
        self.anime_face_radio_button.setObjectName("anime_face_radio_button")

        self.detection_select_group = QtWidgets.QButtonGroup()
        self.detection_select_group.addButton(self.anime_face_radio_button)
        self.detection_select_group.addButton(self.real_face_radio_button)
    
        self.custom_detection_file = QtWidgets.QPushButton(self.group_box)
        self.custom_detection_file.setGeometry(QtCore.QRect(180, 120, 141, 21))
        self.custom_detection_file.setObjectName("custom_detection_file")

        self.resize_checkBox = QtWidgets.QCheckBox(self.group_box)
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
        
        self.retranslateUi(dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CASF"))
        self.run_button.setText(_translate("Dialog", "Run"))
        self.group_box.setTitle(_translate("Dialog", "Options"))
        self.face_align_checkBox.setText(_translate("Dialog", "Face Alignment"))
        self.resize_checkBox.setText(_translate("Dialog", "Resize Outputs"))
        self.path_label.setText(_translate("Dialog", "Path"))
        self.browse_button.setText(_translate("Dialog", "Browse"))
        self.image_view_label.setText(_translate("Dialog", "Image View"))
        self.directory_view_label.setText(_translate("Dialog", "Directory View"))
        self.made_by_label.setText(_translate("Dialog", "Made by Jae-sung Jun"))
        self.real_face_radio_button.setText(_translate("Dialog", "Real Human Face Detect"))
        self.anime_face_radio_button.setText(_translate("Dialog", "Anime Face Detect"))
        self.custom_detection_file.setText(_translate("Dialog", "Select Detection File"))
       
class Main_Form_Event_Handle:

    def __init__(self, main_dialog):

        self.path = ""
        self.wh = ["",""]
        self.detection_file = ""

        self.main_dialog = main_dialog
        
        self.main_dialog.browse_button.clicked.connect(self.browseFileDialog)
        self.main_dialog.directory_tree_view.clicked.connect(self.directoryViewClick)
        self.main_dialog.resize_checkBox.stateChanged.connect(self.resizeCheckbox)
        self.main_dialog.custom_detection_file.clicked.connect(self.custom_detection_fileSelect)
        
        self.main_dialog.real_face_radio_button.clicked.connect(lambda: self.detectionFileCheck("real"))
        self.main_dialog.anime_face_radio_button.clicked.connect(lambda: self.detectionFileCheck("anime"))

        self.main_dialog.run_button.clicked.connect(self.run)
       
        #icon
        self.setIcons()
    def setIcons(self):
        icons_dir = os.path.dirname(os.path.realpath(__file__)) + "/icons/"

        # ============Form Icon Setting============ #
        
        dialog.setWindowIcon(QtGui.QIcon(icons_dir + 'lena.ico'))
        #print(now_dir + '/icon/lena.ico')
        myappid = 'Jaesung_Jun.github.CASF.1.5-GUI' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        # ============Button Icon Setting============ #

        self.main_dialog.browse_button.setIcon(QtGui.QIcon(icons_dir + 'browse.ico'))
        self.main_dialog.browse_button.setIconSize(QtCore.QSize(24, 24))

        self.main_dialog.run_button.setIcon(QtGui.QIcon(icons_dir + 'run.ico'))
        self.main_dialog.run_button.setIconSize(QtCore.QSize(24, 24))

    def browseFileDialog(self):
        self.path = str(QtWidgets.QFileDialog.getExistingDirectory(self.main_dialog, "Select Directory"))
        #Path is Exist
        if os.path.exists(self.path) == True:
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
        if ext == '.jpg' or ext == '.png' or ext == '.PNG' or ext == '.jpeg' or ext == '.JPEG' or ext == '.JPG':
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

    def detectionFileCheck(self, detection_object):
        if detection_object == "real":
            self.detection_file = ".\detection-files\haarcascade_frontalface_default.xml"
        elif detection_object == "anime":
            self.detection_file = ".\detection-files\lbpcascade_animeface.xml"
        else:
            self.detection_file = ""

    def custom_detection_fileSelect(self):
        
        self.main_dialog.detection_select_group.setExclusive(False)

        self.main_dialog.real_face_radio_button.setChecked(False)
        self.main_dialog.anime_face_radio_button.setChecked(False)

        self.main_dialog.detection_select_group.setExclusive(True)

        fname = QtWidgets.QFileDialog.getOpenFileName(self.main_dialog, 'Open file', "", "XML Files(*.xml);; All Files(*)")
        
        if os.path.isfile(fname[0]):
            self.detection_file = fname[0]
            self.main_dialog.custom_detection_file.setText("Selected")
        elif fname[0] == "":
            pass
        elif not os.path.isfile(fname[0]):
            self.errorMessageBox("Error", "Please select other detection file")


    def run(self):
        self.options = {
                        'input_path':self.path,
                        'face_alignment':self.main_dialog.face_align_checkBox.isChecked(), 
                        'resize_output':self.main_dialog.resize_checkBox.isChecked(), 
                        'resize_width':self.wh[0],
                        'resize_height':self.wh[1],
                        'detection_file':self.detection_file
                        }
        #print(self.options)
        if self.checkOptions(self.options) == False:
            self.main_dialog.progress_bar.setProperty("value", 0)
            run = CASF.CASF_Main(self.options, self.main_dialog)
    
    def checkOptions(self, options):
        err = False
        # Exception Handling
        if self.options['input_path'] == "":
            self.errorMessageBox("Error", "Please select your input directory path")
            err = True

        elif self.options['detection_file'] == "":
            self.errorMessageBox("Error", "Please select your detection object type ({0}, {1})".format("anime face", "real human face"))
            err = True

        if self.options['resize_output'] == True:
            if self.options['resize_width'] == "" or self.options['resize_height'] == "":
                self.errorMessageBox("Error", "Please enter the number of pixels you want to resize")
                err = True

        return err

    def errorMessageBox(self, title="", content="Error"):
        QtWidgets.QMessageBox.about(self.main_dialog, title, content)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QDialog()
    
    main_form_ui = Main_Form_Ui()
    main_form_ui.setupUi(dialog)

    # ===========Event Handle Codes=============== #
    event_handle = Main_Form_Event_Handle(main_form_ui)
    dialog.show()
    sys.exit(app.exec_())