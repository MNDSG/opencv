import cv2

# 参数1为图片路径,参数2为读取方式:0为灰度图,1为彩色图
img = cv2.imread("images/cat.jpg", 1)
# 参数1为窗体名称,参数2为显示的图片
img100 = img[100, 100]
cv2.imshow("img", img)
print(img100)
# 图片暂停
cv2.waitKey(0)