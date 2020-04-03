import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 定义缩放矩阵
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
# 对图片进行仿射变换
dst = cv2.warpAffine(img, matScale, (int(width/2), int(height/2)))
cv2.imshow("1", dst)
cv2.waitKey(0)