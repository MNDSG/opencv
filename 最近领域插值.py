'''
最近领域插值原理:
    假设源图片大小为10*20,目标图片大小为5*10
    那么目标图像上的每一个点都来自于原图像,eg:目标图上的(1,2)像素点可用原图的(2,4)表示
    如何由目标图像的点推算出原图像上对应的点呢?
    公式:源图上点 = 目标点 * (原图行数 / 目标行数)
    以上述例子为例:
        对于X:2 = 1 * (10 / 5)
        对于Y:4 = 2 * (20 / 10)
    当然,如果计算结果为小数,比如12.2,那么就会取与12.2最相近的整数12,故曰:最近领域

'''
import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height / 2)
dstWidth = int(width / 2)
# 定义目标图片矩阵
dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8)
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i * (height * 1.0 / dstHeight))
        jNew = int(j * (width * 1.0 / dstWidth))
        dstImage[i, j] = img[iNew, jNew]
cv2.imshow("show", dstImage)
cv2.waitKey(0)