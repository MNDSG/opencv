import cv2
import numpy as np
'''
灰度图:
原图像灰度值为(0~255)
转换后灰度值为(255-原灰度值)
彩色图:
原彩色图每个通道值为(0~255)
转换后:newR = 255 - R
newB = 255 - B
newG = 255 - G
'''
# 灰度图颜色反转
image = cv2.imread("images/cat.jpg", 1)
imgInfo = image.shape
height = imgInfo[0]
width = imgInfo[1]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        grayNow = gray[i, j]    # 取出每个像素灰度值
        # print(gray[i, j])
        dst[i, j] = 255 - grayNow   # 对每个像素灰度值进行操作
cv2.imshow("0", gray)
cv2.imshow("1", dst)

# 彩色图颜色反转
dst1 = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (B, G, R) = image[i, j]
        # print(image[i, j])
        dst1[i, j] = (255 - B, 255 - G, 255 - R)
cv2.imshow("00", image)
cv2.imshow("01", dst1)
cv2.waitKey()
