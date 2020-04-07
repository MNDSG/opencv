import cv2
import numpy as np
import random

'''
图片缩放函数
src:图片路径
dstHeight:图片高度缩放倍数
dstWidth:图片宽度缩放倍数
'''


def pZoom(src, dstHeight, dstWidth):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    imgHeight = imgInfo[0]
    imgWidth = imgInfo[1]
    dstImgHeight = int(imgHeight * dstHeight)
    dstImgWidth = int(imgWidth * dstWidth)
    dst = cv2.resize(img, (dstImgWidth, dstImgHeight))
    cv2.imshow("dst", dst)
    cv2.imshow("src", img)
    cv2.waitKey(0)
    return


'''
图片剪切函数
src:图片路径
start_height:起始高度剪切处
end_height:结尾高度剪切处
start_width:起始宽度剪切处
end_width:结尾宽度剪切处
'''


def pCut(src, start_height, end_height, start_width, end_width):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    imgHeigth = imgInfo[0]
    imgWidth = imgInfo[1]
    if start_height <= end_height and start_width <= end_width:
        if start_height >= 0 and end_height <= imgHeigth and start_width >= 0 and end_width <= imgWidth:
            if isinstance(start_height, int) and isinstance(end_height, int) and isinstance(start_width, int) and isinstance(end_width, int):
                dst = img[start_height:end_height,start_width:end_width]
                cv2.imshow("pCut", dst)
                cv2.waitKey(0)
                return
            else:
                print("输入范围非整数")
                return
        else:
            print("输入范围超过图片大小")
            return
    else:
        print("输入数据不合法")
        return


'''
图片移位函数
src:图片路径
x:向水平方向移动
y:向竖直方向移动
'''


def pShift(src, x, y):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    matShift = np.float32([[1, 0, x],
                           [0, 1, y]])
    dst = cv2.warpAffine(img, matShift, (height, width))
    cv2.imshow("pShift", dst)
    cv2.waitKey(0)
    return


'''
图片镜像函数
src:图片路径
m_way:为x表示上下镜像,为y表示左右镜像
'''


def pMirror(src, m_way):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    deep = imgInfo[2]
    if m_way == 'x':
        newImgInfo = (height * 2, width, deep)
        dst = np.zeros(newImgInfo, np.uint8)
        for i in range(0, height):
            for j in range(0, width):
                dst[i, j] = img[i, j]
                dst[2 * height - i - 1, j] = img[i, j]
        for i in range(0, width):
            dst[height, i] = (0, 0, 255)
        cv2.imshow("pMirror_x", dst)
        cv2.waitKey(0)
        return
    elif m_way == 'y':
        newIngInfo = (height, width * 2, deep)
        dst = np.zeros(newIngInfo, np.uint8)
        for i in range(0, height):
            for j in range(0, width):
                dst[i, j] = img[i, j]
                dst[i, 2*width-1-j] = img[i, j]
        for i in range(0, height):
            dst[i, width] = (0, 0, 255)
        cv2.imshow("pMirror_y", dst)
        cv2.waitKey(0)
    else:
        print("输入参数非法")


'''
图片仿射变换函数
src:图片路径
x1,y1:原图左上角映射点
x2,y2:原图左下角映射点
x3,y3:原图右上角映射点
'''


def pAffine(src, x1, y1, x2, y2, x3, y3):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    matSrc = np.float32([[0, 0], [0, height - 1], [width - 1, 0]])
    matDst = np.float32([[x1, y1], [x2, y2], [x3, y3]])
    matAffine = cv2.getAffineTransform(matSrc, matDst)
    dst = cv2.warpAffine(img, matAffine, (width, height))
    cv2.imshow("pAffine", dst)
    cv2.waitKey(0)
    return


'''
图片旋转函数
src:图片路径
angle:旋转角度
scale:缩放系数,原图直接旋转肯能会超出窗体范围,故需要缩放系数
'''


def pRotate(src, angle, scale):
    img = cv2.imread(src, 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    # 参数1为图片中心点,参数2为旋转角度,参数3为缩放系数
    matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), angle, scale)
    dst = cv2.warpAffine(img, matRotate, (height, width))
    cv2.imshow("1", dst)
    cv2.waitKey(0)
    return


'''
灰度图颜色反转函数
src:图片路径
'''


def pReversalGray(src):
    image = cv2.imread(src, 1)
    imgInfo = image.shape
    height = imgInfo[0]
    width = imgInfo[1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = np.zeros((height, width, 1), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            grayNow = gray[i, j]
            dst[i, j] = 255 - grayNow
    cv2.imshow("pReversalGray", dst)
    cv2.waitKey(0)
    return

'''
BGR图颜色反转函数
src:图片路径
'''


def pReversalBGR(src):
    image = cv2.imread(src, 1)
    imgInfo = image.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.zeros((height, width, 3), np.uint8)
    for i in range(0, height):
        for j in range(0, width):
            (b, g, r) = image[i, j]
            dst[i, j] = (255 - b, 255 - g, 255 - r)
    cv2.imshow("pReversalBGR", dst)
    cv2.waitKey(0)
    return


'''
马赛克函数
src:图片路径
w1:w2:水平方向马赛克区域
h1:h2:垂直方向马赛克区域
'''


def MosaicFun(src, w1, w2, h1, h2):
    img = cv2.imread(src, 1)
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


'''
毛玻璃函数
src:图片路径
rd:取值越大,生成图像越难看
'''


def pGlass(src, rd):
    image = cv2.imread(src, 1)
    imgInfo = image.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.zeros((height, width, 3), np.uint8)
    mm = rd
    # 防止矩阵访问越界
    for i in range(0, height - rd):
        for j in range(0, width - rd):
            # 生成0~5的随机数
            index = int(random.random() * rd)
            (b, g, r) = image[i + index, j + index]
            dst[i, j] = (b, g, r)
    cv2.imshow("pGlass", dst)
    cv2.waitKey(0)
