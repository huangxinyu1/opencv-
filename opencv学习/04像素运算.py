
import cv2 as cv
import numpy as np


#两张图相加
def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add",dst)
#两张图相减
def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract", dst)

#两张图相除
def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide", dst)

#两张图相乘
def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply", dst)

def logic_demo(m1,m2):
    #与运算
    dst = cv.bitwise_and(m1,m2)
    #或运算
    dsc = cv.bitwise_or(m1,m2)
    #非运算
    dsf = cv.bitwise_not(m1,m2)

#调节对比度和亮度
def contrast_brtness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con_bri-demo",dst)


def others(m1,m2):
    #方差越大图像的对比度差异越大
    #返回均值和方差
    M1,dev1 = cv.meanStdDev(m1)
    #返回均值
    M2 = cv.mean(m2)
    #获取图像宽高
    h,w = m1.shape[:2]
    print(M1)
    print(M2)
    img = np.zeros([h,w],np.uint8)
    m,dev = cv.meanStdDev(img)
    print(m)
    print(dev)



print("---------------hello  python-------------------")

src = cv.imread('D:\\image\\timg.jpg')
src1 = cv.imread('D:\\image\\1.png')
print(src.shape)
print(src1.shape)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src1)
cv.imshow("image1",src)
#两张图相加
add_demo(src,src1)
#两张图相减
subtract_demo(src,src1)
#两张图相除
divide_demo(src,src1)
#两张图相乘
multiply_demo(src,src1)
#图片的逻辑运算
logic_demo(src,src1)
#调节对比度和亮度
contrast_brtness_demo(src,1.5,0)
cv.waitKey(0)

cv.destroyAllWindows()

























































