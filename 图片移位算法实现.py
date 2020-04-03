'''
定义偏移矩阵[1,0,100],
           [0,1,200]
将矩阵拆分为两个矩阵
矩阵A:
           [1,0],
           [0,1]和
矩阵B:
           [100],
           [200]
输入矩阵为C
           [x],
           [y]
A*C+B=[1*x+0*y],[0*x+1*y]+[100],[200]=[x+100],[y+200]
'''
import cv2
import numpy as np

img = cv2.imread("images/cat.jpg")
cv2.imshow("0", img)
imgInfo = img.shape
dst = np.zeros(img.shape, np.uint8)
height = imgInfo[0]
width = imgInfo[1]
for i in range(0, height - 100):
    for j in range(0, width - 100):
        dst[i+100, j+100] = img[i, j]
cv2.imshow("1", dst)
cv2.waitKey(0)