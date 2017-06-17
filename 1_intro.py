
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

os.chdir(os.path.join("D:\\","MuensterCourse","UAV","opencv","resources"))

img = cv2.imread("bulb.jpg")
#img = cv2.imread("leon.jpg",cv2.IMREAD_GRAYSCALE)
print img.shape

#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img,cmap='gray', interpolation='bicubic')
##plt.plot([50,100],[80,100],'c',linewidth=5)
##plt.show()

cv2.imwrite('patrickgrey.png',img)
