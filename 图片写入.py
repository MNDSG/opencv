import cv2

imag = cv2.imread("images/cat.jpg",1)
cv2.imshow("image",imag)
cv2.waitKey(0)
# 参数1表示写出图像名称,参数2表示读取的图片
cv2.imwrite("images/cat2.png",imag)