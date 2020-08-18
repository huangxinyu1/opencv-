import cv2 as cv
import numpy as np

#ret ,dst = cv.thrershold(src,thresh,maxval,type)
#ret 阈值
#*src:输入图,只能输入单通道图像
# dst :输出图
# thresh:阈值
# maxval :当超过了阈值或小于阈值所赋予的值(根据type来操作)
# type  : 操作类型包含以下5种
# CV.THRESH_BINARY  超过阈值部分取maxval(最大值),,否则取0
# CV.THRESH_BINARY_INY  THRESH_BINARY 的反转
# CV.THRESH_TRUNC   大于阈值的部分设为阈值,否则不变   大于127  为127
# CV.THRESH_TOZERO  大于阈值的部分不改变,否则设为0
# CV.THRESH_TOZERO_INY   THRESH_TOZERO 的反转
#
# *#
#图像阈值操作
def ThresHold1():
    image1 = cv.imread("imagel/1.jpg",0)
    image2 = cv.imread("imagel/2.jpg")
    #cv.imshow("dst1", image1)
    #cv.waitKey(0)

    ret, dst1 = cv.threshold(image1, 127, 254, cv.THRESH_BINARY)
    ret, dst2 = cv.threshold(image1, 175, 255, cv.THRESH_BINARY_INV)
    ret, dst3 = cv.threshold(image1, 175, 255, cv.THRESH_TRUNC)
    ret, dst4 = cv.threshold(image1, 175, 255, cv.THRESH_TOZERO)
    ret, dst5 = cv.threshold(image1, 175, 255, cv.THRESH_TOZERO_INV)
    print(ret)
    res = np.hstack((dst1,dst2,dst3,dst4,dst5))
    cv.imshow("00",res)
    cv.waitKey(0)
    cv.imshow("dst1",dst1)
    cv.imshow("dst2", dst2)
    cv.imshow("dst3", dst3)
    cv.imshow("dst4", dst4)
    cv.imshow("dst5", dst5)

    cv.waitKey(0)
    cv.destroyAllWindows()



ThresHold1()













