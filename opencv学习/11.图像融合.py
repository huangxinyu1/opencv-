import cv2 as cv
import numpy as np


#图像融合
def RongHe():
    image1 = cv.imread("imagel/1.jpg")
    image2 = cv.imread("imagel/2.jpg")
    print(image1.shape)
    print(image2.shape)
    #把图片设置成宽高一样的
    image2 = cv.resize(image2,(658,987))
    print(image2.shape)

    #简单的图像相加
    res = cv.addWeighted(image1,0.8,image2,0.2,0)
    #拉伸图片
    #res = cv.resize(image1,(0,0),fx=3,fy=0.6)
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image",res)
    cv.waitKey(0)
    cv.destroyAllWindows()







RongHe()




































