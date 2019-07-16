import cv2
import os
import dlib
import numpy as np
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
from imutils import face_utils

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
fa = FaceAligner(predictor, desiredFaceWidth=256)

if os.path.isdir("konomi") == False :
    print("* Make Konomi Folder")
    os.makedirs(os.path.join("konomi"))

Exist_Folder = False
while Exist_Folder == False:
    print("_________         __       _____              .___   _________                   ")
    print("\_   ___ \ __ ___/  |_    /  _  \   ____    __| _/  /   _____/____ ___  __ ____  ")
    print("/    \  \/|  |  \   __\  /  /_\  \ /    \  / __ |   \_____  \\\__  \\\  \/ // __ \ ")
    print("\     \___|  |  /|  |   /    |    \   |  \/ /_/ |   /        \/ __ \\\   /\  ___/ ")
    print(" \______  /____/ |__|   \____|__  /___|  /\____ |  /_______  (____  /\_/  \___  >")
    print("        \/                      \/     \/      \/          \/     \/          \/ ")
    print("By Tudy")
    print("https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml")
    print("https://github.com/nagadomi/lbpcascade_animeface")
    print("====Input Folder Name====")
    pathofimg = input("-> ")
    if os.path.isdir(pathofimg) == False :
        print("\n")
        print("Error : Not exist Folder(Directory). Please select Folder(Directory) that your img files exist.")
        print("\n")
        Exist_Folder = False
    if os.path.isdir(pathofimg) == True :
        Exist_Folder = True

print("===========================\n1 : Real Human Face\n2 : Japanese Anime Face\n===========================\n[Default : Real Human Face]")
face = input("-> ")
print("Do you want to resize output Pics? (y, n) [Default : n]")
yorn = input("-> ")
if yorn == 'y':
    print("Plz Enter the number of pixels you want to resize [Default : 100]")
    resize_num = input("-> ")
    if resize_num == '':
        print("You selected Default(100)")
        resize_num = 100
if __name__ == '__main__' :
    #tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    print("Select tracker type : BOOSTING, MIL, KCF, TLD, MEDIANFLOW, GOTURN")
    print("DEFAULT : MIL")
    tracker_type = input("-> ")
    if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
    elif tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
    elif tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
    elif tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
    elif tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
    else:
        tracker = cv2.TrackerMIL_create()
    file_num = os.listdir(pathofimg)
    print(file_num)
    face_cascade = cv2.CascadeClassifier()

    if face == '1':
        face_cascade.load('.\haarcascade_frontalface_default.xml')
    if face == '2':
        face_cascade.load('.\lbpcascade_animeface.xml')
    else:
        face_cascade.load('.\haarcascade_frontalface_default.xml')
    TrackingState = 0
    TrackingROI = (0,0,0,0)
    i=0
    for i in range(len(file_num)):
        n=0
        print(pathofimg + "/" + file_num[i])
        img = cv2.imread(pathofimg + "/" + file_num[i])
        grayframe = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grayframe = cv2.equalizeHist(grayframe)
        faces = face_cascade.detectMultiScale(grayframe, 1.1, 5, 0, (30, 30))
        if len(faces) > 0:
            (x,y,w,h) = faces[0]
            TrackingROI = (x,y,w,h)
            for(x, y, w, h) in faces:
                cropped_img_dlib = dlib.rectangle(left=int(x), top=int(y), right=int(x+w), bottom=int(y+h))
                aligned_cropped_img = fa.align(img, grayframe, cropped_img_dlib)
                #cropped_img = img[int(y):int(y + h), int(x):int(x + w)]
                #cv2.imshow("not aligned", cropped_img)
                #cv2.imshow("aligned", aligned_cropped_img)
                #cv2.waitKey(0)
                if yorn == 'y':
                    aligned_cropped_img = cv2.resize(aligned_cropped_img, (int(resize_num), int(resize_num)))
                cv2.imwrite("./konomi/" + str(file_num[i]) + "_" + str(n) + "_cropped.jpg", aligned_cropped_img)
                n = n + 1
            print("Detected Face from " + file_num[i])
        else:
            print(file_num[i] + " : Can't Detect Face :( ")
