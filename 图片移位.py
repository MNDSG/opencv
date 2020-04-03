import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("show0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
matShift = np.float32([[1, 0, 100],
                     [0, 1, 200]])

dst = cv2.warpAffine(img, matShift, (height, width))
cv2.imshow("show1", dst)
cv2.waitKey(0)