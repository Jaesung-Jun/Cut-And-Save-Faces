import cv2
import os
import dlib
import numpy as np
import threading
import concurrent.futures
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils

class CASF_Main():
    def __init__(self, options, dialog):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            get_image_path = executor.submit(self.getImagePath, (options['input_path']))
            detection_file_load = executor.submit(self.detectionFileLoad, options['detection_file'])

            path_list, file_list = get_image_path.result()
            face_cascade = detection_file_load.result()
            
            detect_face = executor.submit(self.detectFace, (options, path_list, file_list, face_cascade))
            print(detect_face.running())
            if detect_face.running() == False:
                detect_face.start()
                print(detect_face.isAlive())
            if detect_face.running() == True:
                print("Your Process is Running")
    def detectFace(self, options, path_list, file_list, face_cascade):
        TrackingState = 0
        TrackingROI = (0,0,0,0)
        i=0
        n=1
        for i in range(len(file_list)):

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
                print("Detected {} Face(s) from {}".format(str(len(faces)), file_list[i]))

            else:
                print(file_list[i] + " : Can't Detect Face :( ")

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
                if ext == '.jpg' or ext == '.png' or ext == '.PNG' or ext == '.jpeg' or ext == '.JPEG' or ext == '.JPG':
                    img_file_path = path + "/" + filename
                    path_list.append(img_file_path)
                    file_list.append(filename)

        return path_list, file_list