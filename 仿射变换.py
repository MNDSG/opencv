import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

'''
仿射变换原理:将原图片上3个点(左上角,左下角,右上角)映射到新图片的3个位置上,
'''
matSrc = np.float32([[0, 0], [0, height-1], [width-1, 0]])
matDst = np.float32([[50, 50], [200, height-50], [width-200, 100]])
# 定义仿射变换矩阵
# 改方法得到一个矩阵组合,参数1表示源,参数2表示目标
matAffine = cv2.getAffineTransform(matSrc, matDst)
dst = cv2.warpAffine(img, matAffine, (width, height))
cv2.imshow("1", dst)
cv2.waitKey(0)