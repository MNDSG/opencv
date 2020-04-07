'''
原理:用原图上的某一点周围随机像素点代替原图像素点
'''
import cv2
import numpy as np
import random

image = cv2.imread("images/cat.jpg", 1)
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]

dst = np.zeros((height, width, 3), np.uint8)
mm = 5
# 防止矩阵访问越界
for i in range(0, height - mm):
    for j in range(0, width - mm):
        index = int(random.random() * 5)
        (b, g, r) = image[i + index, j + index]
        dst[i, j] = (b, g, r)
cv2.imshow("0", image)
cv2.imshow("1", dst)
cv2.waitKey(0)
