import os
os.chdir(os.path.join('D:\\','MuensterCourse','UAV','opencv','resources'))


import numpy as np
import cv2

img1 = cv2.imread('mosaic1.jpg')
img2 = cv2.imread('duplicate.jpg')

#img1[0:500,0:1000] = img2[500:1000,0:1000]

#add = img1 + img2
#img1 = img1/2
#img2 = img2/2

#add = cv2.add(img1, img2)

#weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

#logics




#cv2.imshow('weighted',weighted)



cv2.waitKey(0)
cv2.destroyAllWindows()

