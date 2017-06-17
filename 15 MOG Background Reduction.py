import cv2, os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('D:\\MuensterCourse\\UAV\\videoProcessingProject\\Resources\\RGB Video')
#os.chdir('D:/MuensterCourse/UAV/opencv/resources')

         
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('00003.mts')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k ==27:
        break
    




cap.release()
cv2.destroyAllWindows()



    
    


    
