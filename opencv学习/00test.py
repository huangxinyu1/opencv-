import cv2 as cv
import numpy as np


print("---------------hello  python-------------------")
#读取图像
src = cv.imread('timg.jpg')
#加载图像窗体
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
#图像显示,也可加载多个窗体
cv.imshow("input image",src);
#等待时间,毫秒级,0表示任意键终止
cv.waitKey(0)
#关闭窗口
cv.destroyAllWindows()






