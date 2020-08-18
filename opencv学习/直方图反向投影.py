
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    #样本要采集的颜色
    sample = cv.imread(".\\imagel\\timg.jpg")
    #采集的图片
    target = cv.imread(".\\imagel\\timg.jpg")

    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)

    #show image
    cv.imshow("sample",sample)
    cv.imshow("target",target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[180,256],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    cv.calcBackProject(target,[0,1],roiHist,[0,180,0,256],1)
    cv.imshow("back",roiHist)


#2d直方图显示
def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    #cv.imshow("hist2d",hist)
    plt.imshow(hist,interpolation="nearest")
    plt.title("2D Histogram")
    plt.show()










print("---------------hello  python-------------------")

src = cv.imread('.\\imagel\\timg.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
hist2d_demo(src)
back_projection_demo()
cv.waitKey(0)

cv.destroyAllWindows()



























































