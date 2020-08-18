
import cv2 as cv
import numpy as np

def ReadImage():
    #读取一张图片
    src = cv.imread('timg.jpg')
    print(src)
    cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
    cv.imshow("input image",src)
    #不断刷新图片单位为毫秒，视频时有用
    cv.waitKey(0)
    #释放所有的内存
    cv.destroyAllWindows()
    print("HI python")
#############################################图像保存加载33333333333333
#读取视频数据
def video_demo():
    #打开相机,或视频文件路径
    capture = cv.VideoCapture(0)
    while(True):
        #frame是视频的每一帧
        #返回值ret读到返回Ture ,frame  图片数组
        ret,frame =capture.read()
        #print(ret)
        #print(frame)
        #左右变换，上下用-1
        frame = cv.flip(frame,1)
        cv.imshow("Video",frame)
        s= cv.waitKey(500)
        #超时则返回-1
        print(s)
        if s >= 0:
            break
#读取图像数据
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)
#保存图片,灰度图
def SaveImage():
    #读取一张图片
    src = cv.imread('timg.jpg')
    print(src)
    cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)

    cv.imshow("input image",src)
    get_image_info(src)
    #获取灰度图像
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    cv.imshow("input image", gray)
    #保存图片
    cv.imwrite('1.png',gray)
#图片的截取
def JieQu():
    image = cv.imread("imagel/timg.jpg")
    jie = image[50:200,30:200]
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", jie)
#读取颜色通道
def Colo():
    image = cv.imread("imagel/timg.jpg")

    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cur_image = image.copy()
    b,g,r = cv.split(image)
    cv.imshow("input image", r)
    cv.waitKey(0)
    cur_image[:,:,0] = 0
    cur_image[:, :, 1] = 0
    cv.imshow("input image", cur_image)



#读取图像
#ReadImage()
#读取视频
#video_demo()
#保存图片,灰度图
SaveImage()
#截取图片
#JieQu()
#颜色通道读取
#Colo()


#等待相应操作
cv.waitKey(0)
#释放所有的内存
cv.destroyAllWindows()

print("HI python")














