import cv2
import numpy as np

# 原理:将某块区域的所有像素点用某一个像素点替换


def MosaicFun(image, w1, w2, h1, h2):
    img = cv2.imread(image, 1)
    for i in range(h1, h2):
        for j in range(w1, w2):
            if i % 10 == 0 and j % 10 == 0:
                for p in range(0, 10):
                    for q in range(0, 10):
                        (B, G, R) = img[i, j]
                        img[i + p, j + q] = (B, G, R)
    cv2.imshow("0", img)
    cv2.waitKey(0)
    return


MosaicFun("images/cat.jpg", 0, 500, 0, 200)
'''
image = cv2.imread("images/cat.jpg", 1)
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]

for i in range(0, 200):
    for j in range(0, 200):
        if i % 10 == 0 and j % 10 == 0:
            for p in range(0, 10):
                for q in range(0, 10):
                    (B, G, R) = image[i, j]
                    image[i + p, j + q] = (B, G, R)
cv2.imshow("0", image)
cv2.waitKey(0)
'''
