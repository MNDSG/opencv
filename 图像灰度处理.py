import cv2
img0 = cv2.imread("images/cat.jpg", 0)
img1 = cv2.imread("images/cat.jpg", 1)
# 颜色空间转换
img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print(img0.shape)
print(img1.shape)
cv2.imshow("0", img0)
cv2.imshow("1", img1)
cv2.imshow("2", img3)
cv2.waitKey(0)