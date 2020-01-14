import cv2
import os
import dlib
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils

class CASF_Main():
    def __init__(self, options, dialog):
        try:
            path_list, file_list = self.getImagePath(options['input_path'])
        except:
            QMessageBox.about(dialog, "Error", "Error during get image path")
        try:
            face_cascade = self.detectionFileLoad(options['detection_file'])
        except:
            QMessageBox.about(dialog, "Error", "Error during load detection file")
            
        detect_face = self.detectFace(options, path_list, file_list, face_cascade, dialog)

        if detect_face == "0":
            QMessageBox.about(dialog, "Complete", "Complete :)")
        elif detect_face == "1":
            QMessageBox.about(dialog, "Complete", "Unknown Error during detect Faces :(")
        elif detect-face == "SaveError":
            QMessagebox.about(dialog, "Complete", "Error during save outputs :(")
    def detectFace(self, options, path_list, file_list, face_cascade, dialog):
        TrackingState = 0
        TrackingROI = (0,0,0,0)
        i=0
        n=1
        try:
            for i in range(len(file_list)):
                percent = self.percentReturn(i+1, len(file_list))
                dialog.progress_bar.setProperty("value", percent)
                img = cv2.imread(path_list[i])
                grayframe = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                grayframe = cv2.equalizeHist(grayframe)
                faces = face_cascade.detectMultiScale(grayframe, 1.1, 5, 0, (30, 30))

                if len(faces) > 0:
                    (x,y,w,h) = faces[0]
                    TrackingROI = (x,y,w,h)
                    for(x, y, w, h) in faces:
                        cropped_img = img[y:y+h, x:x+w]
                        if options['face_alignment']:
                            dlib_cropped_img = dlib.rectangle(left=int(x), top=int(y), right=int(x+w), bottom=int(y+h))
                            predictor = dlib.shape_predictor("./detection-files/shape_predictor_68_face_landmarks.dat")
                            fa = FaceAligner(predictor, desiredFaceWidth=256)
                            cropped_img = fa.align(img, grayframe, dlib_cropped_img)
                        if options['resize_output']:
                            cropped_img = cv2.resize(cropped_img, (int(options['resize_width']), int(options['resize_height'])))
                        try:
                            cv2.imwrite("{0}/{1}_{2}_cropped.jpg".format(options['output_path'], str(file_list[i]), str(n)), cropped_img)
                        except:
                            return "SaveError"
                        n += 1
                    print("Detected {} Objects from {}".format(str(len(faces)), file_list[i]))
                else:
                    print(file_list[i] + " : Can't Detect Objects :( ")
            return "0"
        except:
            return "1"
                
        
    def detectionFileLoad(self, detection_file_path):

        face_cascade = cv2.CascadeClassifier()
        face_cascade.load(detection_file_path)
        return face_cascade

    def getImagePath(self, input_path):
        path_list = []
        file_list = []
        for (path, dir, files) in os.walk(input_path):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.png' or ext == '.PNG' or ext == '.jpg' or ext == '.JPG' or ext == '.jpeg' or ext == '.JPEG' :
                    img_file_path = path + "/" + filename
                    path_list.append(img_file_path)
                    file_list.append(filename)

        return path_list, file_list
    
    def percentReturn(self, iteration, total):
            percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
            return int(round(float(percent)))