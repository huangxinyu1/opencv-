
import cv2 as cv
import numpy as np


#泛洪填充,改变图像
def fill_color_demo(image):
    #复制图像
    copyimg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyimg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_coor",copyimg)

#泛洪填充，不改变图像，只填充遮罩层本身，mask
def fill_binary():
    #复制图像
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill_binary",image)
    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(103,2,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill_binar",image)

print("---------------hello  python-------------------")

src = cv.imread('.\\imagel\\timg.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#获取图片某部分，高宽
face = src[70:300,150:400]
cv.imshow("face",face)
#变为灰度图
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
#把切出的灰度图放入原图
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)#灰度图转变为三通道图
src[70:300,150:400] = backface
cv.imshow("backface",src)
#图像泛洪填充
fill_color_demo(src)

fill_binary()
cv.waitKey(0)

cv.destroyAllWindows()

















































