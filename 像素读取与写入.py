'''
 1.像素:每一张图片可拆分为若干像素点
 2.RGB:每一个像素点的颜色构成都是由red,green,blue按照不同比例构成
 3.颜色深度:表示R,G,B每一种颜色的大小,如果为8bit,则其表示范围是(0~255)
 4.图片的宽度和高度:(1920*1080)表示在宽上有1920个像素点,高上有1080个像素点
 5.图片大小计算:1920*1080*3*8bit
 6.jpg与png:jpg图片参数如上述,png在有RGB基础上还有一个透明度通道(alpha通道);jpg为有损压缩,png为无损压缩
 7.RGB与BGR:二者在颜色通道分布上顺序存在差异
 8.图片坐标系:
    --------------------->行
    |
    |
    |
    |
    |
    列

'''
import cv2

img = cv2.imread("images/cat.jpg", 1);
# 读取某一像素点通道值,opencv默认为BGR格式;img为矩阵格式存储,[Y,X]
(BlueChannel, GreenChannel, RedChannel) = img[100, 100]
print(BlueChannel, GreenChannel, RedChannel)
for i in range(0, 100):
    img[0 + i, 100] = (0, 0, 255)
    img[100, 0 + i] = (0, 0, 255)
cv2.imshow("show", img)
cv2.waitKey(0)