
import cv2 as cv
import numpy as np

#读取视频分离出颜色
def extrace_object_demo():
    #读取视频
    caapture = cv.VideoCapture("路径")
    while(True):
        ret,frame = caapture.read()
        if ret == False:
            break
        #把视频中有颜色的图像分离出来
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        #分离颜色的重要函数
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask)
        cv.imshow("video",frame)
        cv.imshow("video1", dst)
        c = cv.waitKey(40)
        #按ESC退出
        if c == 27:
            break





def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb", ycrcb)



print("*******************************************")
#读取一张图片
src = cv.imread('.\\imagel\\timg.jpg')
print(src)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)

cv.imshow("input image",src)

#分割出三颜色通道
b,g,r = cv.split(src)
cv.imshow("bule",b)
cv.imshow("green",g)
cv.imshow("red",r)
#某个通道变为0
src[:,:,:2] = 0
#合并并多通道
src = cv.merge([b,g,r])

color_space_demo(src)
#不断刷新图片单位为毫秒，视频时有用
cv.waitKey(0)
#释放所有的内存
cv.destroyAllWindows()

print("HI python")














































































