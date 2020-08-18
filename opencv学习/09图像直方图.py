import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def plot_demo(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show()

#画出直方图图片的
def image_hist(image):
    color = ("blue","green","red")
    #绘制每个颜色对应的直方图
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()


print("---------------hello  python-------------------")

src = cv.imread('.\\imagel\\1.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#plot_demo(static)
image_hist(src)
cv.waitKey(0)

cv.destroyAllWindows()






