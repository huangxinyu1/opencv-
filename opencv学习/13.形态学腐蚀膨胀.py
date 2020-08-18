import cv2 as cv
import numpy as np

#腐蚀操作
def Erode_image():
    image = cv.imread("imagel/1.jpg",0)
    cv.imshow("00",image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    Kernel = np.ones((5,5),np.uint8)
    #进行腐蚀操作  iterations  腐蚀次数
    erosion = cv.erode(image,Kernel,iterations=3)
    cv.imshow("11",erosion)
    cv.waitKey(0)

    cv.destroyAllWindows()

#膨胀操作
def Erosin_image():
    image = cv.imread("imagel/1.jpg", 0)
    cv.imshow("00", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    Kernel = np.ones((5, 5), np.uint8)
    #膨胀运算
    dig_erosin = cv.dilate(image,Kernel,iterations=3)
    cv.imshow("11", dig_erosin)
    cv.waitKey(0)

    cv.destroyAllWindows()

#开  闭    运算
#开  :  先腐蚀在膨胀
def Morpholog_image():
    image = cv.imread("imagel/1.jpg", 0)
    cv.imshow("00", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    Kernel = np.ones((5, 5), np.uint8)
    #开运算
    dig_erosin = cv.morphologyEx(image,cv.MORPH_OPEN,Kernel)
    #闭运算
    #dig_erosin = cv.morphologyEx(image, cv.MORPH_CLOSE, Kernel)
    cv.imshow("11", dig_erosin)
    cv.waitKey(0)

    cv.destroyAllWindows()

# 梯度运算膨胀减去腐蚀
def Hstack_image():
    image = cv.imread("imagel/1.jpg", 0)
    cv.imshow("00", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    Kernel = np.ones((5, 5), np.uint8)
    #梯度运算
    dig_erosin =cv.morphologyEx(image,cv.MORPH_GRADIENT,Kernel)

    cv.imshow("00", dig_erosin)
    cv.waitKey(0)

    cv.destroyAllWindows()

#礼帽     原始输入-开运算结果
def Tophat_image():
    image = cv.imread("imagel/1.jpg", 0)
    Kernel = np.ones((5, 5), np.uint8)
    # 礼帽运算
    dig_erosin = cv.morphologyEx(image, cv.MORPH_TOPHAT, Kernel)
    cv.imshow("00", dig_erosin)
    cv.waitKey(0)
    cv.destroyAllWindows()

#黑帽     闭运算 - 原始输入
def Blackhat_image():
    image = cv.imread("imagel/1.jpg", 0)
    Kernel = np.ones((5, 5), np.uint8)
    # 礼帽运算
    dig_erosin = cv.morphologyEx(image, cv.MORPH_BLACKHAT, Kernel)
    cv.imshow("00", dig_erosin)
    cv.waitKey(0)
    cv.destroyAllWindows()



#Erode_image()
#Erosin_image()
#Morpholog_image()
#Hstack_image()
#Tophat_image()
Blackhat_image()



