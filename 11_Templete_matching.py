import cv2, os
import numpy as np

os.chdir(r'D:\MuensterCourse\UAV\opencv\resources')
img_bgr = cv2.imread('whole.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('control.jpg', 0)

template2 = cv2.imread('control2.jpg', 0)

w , h = template.shape[::1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
print type(res)
threshold = 0.8
loc = np.where(res>=threshold)
print loc
loc2 = np.where(res2>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255),2)

for pt in zip(*loc2[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255),2)


cv2.imshow('detected', img_bgr)
    
cv2.waitKey(0)
cv2.destroyAllWindows()



    
    


    
