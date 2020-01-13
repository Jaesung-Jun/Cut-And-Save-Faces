import cv2
import os
import dlib
import numpy as np
import threading
import concurrent.futures
from PyQt5.QtWidgets import QMessageBox
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils

class CASF_Main():
    def __init__(self, options, dialog):

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            
            get_image_path = executor.submit(self.getImagePath, (options['input_path']))
            detection_file_load = executor.submit(self.detectionFileLoad, (options['detection_file']))
            path_list, file_list = get_image_path.result()
            face_cascade = detection_file_load.result()
            detect_face = executor.submit(lambda p: self.detectFace(*p), [options, path_list, file_list, face_cascade, dialog] )
            is_complete = detect_face.result()
                
        if get_image_path.exception() != None :
            QMessageBox.about(dialog, "Error", "File Information Load Error")

        if detection_file_load.exception() != None or detect_face.exception() != None:
            QMessageBox.about(dialog, "Error", "Face Detecting Error")
            if not os.path.isfile(options['detection_file']):
                QMessageBox.about(dialog, "Error", "Can't Find Detection File")
        
        if detect_face.result() == True:
            QMessageBox.about(dialog, "Complete", "Complete :)")
        elif detect_face.result() == False:
            QMessageBox.about(dialog, "Complete", "Error during detecting Faces :(")

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
                        cv2.imwrite("./outputs/{0}_{1}_cropped.jpg".format(str(file_list[i]), str(n)), cropped_img)
                        n += 1
                    print("Detected {} Objects from {}".format(str(len(faces)), file_list[i]))

                else:
                    print(file_list[i] + " : Can't Detect Objects :( ")
            return True
        except:
            return False
                
        
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