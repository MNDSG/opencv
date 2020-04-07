'''
原理:灰度图像的BGR三通道值相等,此处取BGR三通道均值
'''
import cv2
import numpy as np
image = cv2.imread("images/cat.jpg", 1)
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = image[i, j]
        gray = (int(b) + int(g) + int(r)) / 3
        dst[i, j] = np.uint8(gray)
cv2.imshow("0", dst)
cv2.waitKey(0)