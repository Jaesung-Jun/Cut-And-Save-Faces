import cv2
import os
import dlib
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils

class CASF_Main():
    def __init__(self, options):
        
        path_list, file_list = self.getImagePath(options['input_path'])
        face_cascade = self.detectionFileLoad(options['detection_file'])
        detectFace(options, path_list, file_list, face_cascade)

    def detectFace(self, options, path_list, face_cascade):
        TrackingState = 0
        TrackingROI = (0,0,0,0)
        i=0, n=1
        for i in range(len(path_list)):

            img = cv2.imread(path_list)
            grayframe = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            grayframe = cv2.equalizeHist(grayframe)
            
            faces = face_cascade.detectMultiScale(grayframe, 1.1, 5, 0, (30, 30))
            
            if len(faces) > 0:
                (x,y,w,h) = faces[0]
                TrackingROI = (x,y,w,h)
                
                for(x, y, w, h) in faces:
                    cropped_img = dlib.rectangle(left=int(x), top=int(y), right=int(x+w), bottom=int(y+h))
                    if options['face_align']:
                        cropped_img = fa.align(img, grayframe, cropped_img)
                    if yorn == 'y':
                        aligned_cropped_img = cv2.resize(aligned_cropped_img, (int(resize_num), int(resize_num)))
                        
                    cv2.imwrite("./outputs/{0}_{1}_cropped.jpg".format(str(file_num[i]), str(n)), cropped_img)
                    n += 1
                print("Detected {0} {1} Face from ".format(str(len(faces)), file_num[i]))
            else:
                print(file_num[i] + " : Can't Detect Face :( ")

    def detectionFileLoad(self, detection_file_path):

        face_cascade = cv2.CascadeClassifier()
        face_cascade.load(detection_file_path)
        return face_cascade

    def getImagePath(self, input_path):
        paths = []
        files = []
        for (path, dir, files) in os.walk("c:/"):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.jpg' or ext == '.png' or ext == '.PNG' or ext == '.jpeg' or ext == '.JPEG' or ext == '.JPG':
                    img_file_path = path + "/" + filename
                    paths.append(img_file_path)
                    files.append(filename)
        return paths, files