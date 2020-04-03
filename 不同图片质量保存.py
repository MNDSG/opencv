import cv2

img = cv2.imread("images/cat.jpg",1)
# jpg格式压缩:参数3表示压缩比(0~100),0质量最差
cv2.imwrite("images/cat3.jpg",img,[cv2.IMWRITE_JPEG_QUALITY,100])
# png格式压缩:参数3表示压缩比(0~9),o质量最好
cv2.imwrite("images/test3.png",img,[cv2.IMWRITE_PNG_COMPRESSION,0])