import os
os.chdir(os.path.join('D:\\','MuensterCourse','UAV','opencv','resources'))


import numpy as np
import cv2

img1 = cv2.imread('mosaic.jpg')
img2 = cv2.imread('mavicsmall.jpg')


rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img2gray)
ret, mask = cv2.threshold(img2gray, 150, 225, cv2.THRESH_BINARY_INV)

cv2.imshow('mask',mask)


mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('img1_bg',img1_bg)


img2_fg = cv2.bitwise_and(img2, img2, mask = mask)
cv2.imshow('img2_fg',img2_fg)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst


cv2.imshow('res',img1)
#cv2.imshow('mask',mask)




cv2.waitKey(0)
cv2.destroyAllWindows()

