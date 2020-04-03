import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
newImgInfo = (height*2, width, deep)
# 创建一个三维矩阵
dst = np.zeros(newImgInfo, np.uint8)
print(dst)
for i in range(0, height):
    for j in range(0, width):
        dst[i, j] = img[i, j]
        dst[height*2-1-i, j] = img[i, j]
for i in range(0, width):
    dst[height, i] = (0, 0, 255)
cv2.imshow("1", dst)
cv2.waitKey(0)
