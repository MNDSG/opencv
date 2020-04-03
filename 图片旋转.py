import cv2
import numpy as np

img = cv2.imread("images/cat.jpg", 1)
cv2.imshow("0", img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

