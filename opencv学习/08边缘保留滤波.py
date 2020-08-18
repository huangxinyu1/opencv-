import cv2 as cv
import numpy as np

#高斯双边模糊(保留边缘)
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)

#高斯双边模糊(保留边缘)
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("shift_demo",dst)

print("---------------hello  python-------------------")

src = cv.imread('D:\\image\\timg.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()






