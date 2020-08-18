import cv2
import numpy as np

img = cv2.imread("imagel/pinjie/5.jpg")
img1 = cv2.imread("imagel/pinjie/6.jpg")
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.__version__

sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(gray1,None)
kp2,des2 = sift.detectAndCompute(gray2,None)
bf = cv2.BFMatcher()
matches = bf.match(des1,des2)

matches = sorted(matches,key=lambda x:x.distance)
img3 = cv2.drawMatches(gray1,kp1,gray2,kp2,matches[:4],None,flags=2)
cv2.imshow("00",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()













