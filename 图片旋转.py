import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 参数1为图片中心点,参数2为旋转角度,参数3为缩放系数
matRotate = cv2.getRotationMatrix2D((height*0.5, width*0.5), 45, 0.5)
dst = cv2.warpAffine(img, matRotate, (height, width))
cv2.imshow("1", dst)
cv2.waitKey(0)