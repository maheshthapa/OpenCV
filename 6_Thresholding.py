import cv2, os
import numpy as np

os.chdir(r'D:\MuensterCourse\UAV\opencv\resources')
img = cv2.imread('seedling.jpg')
retval, threshold = cv2.threshold(img,12,255, cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()


