
import cv2 as cv
import numpy as np

#改变一些图像
def access_pixels(image):
    print(image.shape)
    #获取图片的高宽和通道数
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width:%s,height:%s,channels:%s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels",image)
    cv.imwrite('D:\\image\\2.png',image)

def inverse(image):
    #像素取反
    dst = cv.bitwise_not(image)
    cv.imshow("new",dst)

#创建新的图像
def create_image():
    #创建400*400的三通道图像
    img = np.zeros([400,400,3],np.uint8)
    cv.imshow("input image",img)
    img[:,:,2]=np.ones([400,400])*200
    cv.imshow("new",img)
    cv.imwrite('D:\\image\\3.png', img)

    ml = np.ones([3,3],np.uint8)
    #填充数组
    ml.fill(122.33)
    print(ml)

    m2 =ml.reshape([1,9])
    print(m2)









print("******************************************")
#读取一张图片
src = cv.imread('D:\\image\\timg.jpg')#blue，green，red
print(src)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)

#cv.imshow("input image",static)
#获取当前cpu转的时间
t1 = cv.getTickCount()
create_image()

#access_pixels(static)
t2 = cv.getTickCount()
#cv.getTickFrequency()每秒cpu 转的时间
time = (t2-t1)/cv.getTickFrequency()
print("time:%s"%(time*1000))

#不断刷新图片单位为毫秒，视频时有用
cv.waitKey(0)
#释放所有的内存
cv.destroyAllWindows()





























































































