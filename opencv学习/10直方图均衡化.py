import cv2 as cv
import numpy as np


#直方图均衡化操作全部
def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("new",dst)
    # z = cv.calcHist([dst],[0],None,[256],[0,255])
    # cv.imshow("zzz", z)




#局部直方图均衡化
def clahe_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow("new1",dst)



#算出图片直方图
def create_rgb_hist(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0]+1
    return rgbHist

#直方图比较两张图像的相似性
def hist_compare(image1,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)
    print("巴氏距离：%s,相关性：%s,卡方：%s"%(match1,match2,match3))



print("---------------hello  python-------------------")

src = cv.imread('.\\imagel\\timg.jpg')
src1 = cv.imread('.\\imagel\\pinjie\\5.jpg')
src2 = cv.imread('.\\imagel\\pinjie\\6.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
equalHist_demo(src)
clahe_demo(src)
hist_compare(src2,src1)

cv.waitKey(0)

cv.destroyAllWindows()






