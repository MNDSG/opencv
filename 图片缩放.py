import cv2

img = cv2.imread("images/cat.jpg", 1)
# 打印图片信息,宽度,高度,颜色通道
imgInfo = img.shape
# 获取高度信息
height = imgInfo[0]
# 获取宽度信息
width = imgInfo[1]
# 获取颜色通道信息
mode = imgInfo[2]
print(imgInfo)

# 定义缩放倍数
dstHeight = int(height * 0.5)
dstWidth = int(width * 0.5)

# 双线性插值,参数1为原图片,参数2为修改后图像宽度和高度
dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imshow("show0", img)
cv2.imshow("show1", dst)
cv2.waitKey(0)