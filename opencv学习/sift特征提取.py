import cv2
import numpy as np


img = cv2.imread("imagel/pinjie/1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.__version__

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
img = cv2.drawKeypoints(gray,kp,img)
cv2.imshow("00",img)
cv2.waitKey(0)
cv2.destroyAllWindows()











