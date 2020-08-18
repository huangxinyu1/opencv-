
import cv2 as cv
import numpy as np


#模糊操作，均值模糊
def blur_demo(image):
    #在水平操作1和垂直操作15，均值模糊
    dst = cv.blur(image,(15,15))
    cv.imshow("blur_image",dst)


#中值模糊，去噪声，椒盐噪声
def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("blur_image",dst)

#自定义滤波
def custom_blur_demo(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) # 锐化。算子不一样
    #kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], np.float32) / 9
    #kernel = np.ones([5,5],np.float32)/25 #除与25防止溢出
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("custom",dst)

print("---------------hello  python-------------------")

src = cv.imread('imagel/timg.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()











































