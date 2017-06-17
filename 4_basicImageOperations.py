import numpy as np
import cv2
import os

os.chdir(os.path.join('D:\\','MuensterCourse','UAV','opencv','resources'))

img = cv2.imread('patrick.png',cv2.IMREAD_COLOR)

px = img[55,55]

img [55,55] = [255,255,255]
px = img[55,55]
#print(px)

#img[0:100, 100:150] =[255,255,255]

watch_face = img[37:111, 100:150]
img[0:74, 0:50] = watch_face




cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
