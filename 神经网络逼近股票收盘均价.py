import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
tf.compat.v1.disable_eager_execution()

# 绘制坐标系,x表示天数(0~15),y表示
date = np.linspace(1, 15, 15)
# 收盘价格
endPrice = np.array([2511.90, 2538.26, 2510.68, 2591.66, 2732.98, 2701.69, 2701.29, 2678.67, 2726.50, 2681.50, 2739.17, 2715.07, 2823.58, 2864.90, 2919.08])
# 开盘价格
beginPrice = np.array([2438.71, 2500.88, 2534.95, 2512.52, 2594.04, 2743.26, 2697.47, 2695.24, 2678.23, 2722.13, 2674.93, 2744.13, 2717.46, 2832.73, 2877.40])
print(date)
print(beginPrice)
print(endPrice)
plt.figure()
for i in range(0, 15):
    # 创建一个数组,数组元素为0
    dataOne = np.zeros(2)
    dataOne[0] = i
    dataOne[1] = i
    # 创建一个数组,数组元素为0
    priceOne = np.zeros(2)
    priceOne[0] = beginPrice[i]
    priceOne[1] = endPrice[i]
    # 此图比较有意思,传入参数为一维数组
    if endPrice[i] > beginPrice[i]:
        plt.plot(dataOne, priceOne, 'r', lw=8)
    else:
        plt.plot(dataOne, priceOne, 'g', lw=8)
# plt.show()
# A(15x1)*w1(1x10)+b1(1x10)=B(15x10)
# B(15x10)*w2(10x1)+b2(15x1)=C(15x1)
dateNormal = np.zeros([15, 1])
priceNormal = np.zeros([15, 1])
print(dateNormal)
print(priceNormal)
for i in range(0, 15):
    # 归一化天数和价格两个参量
    dateNormal[i, 0] = i / 15.0
    priceNormal[i, 0] = endPrice[i] / 3000.0
# 定义输入层数据
x = tf.compat.v1.placeholder(tf.float32, [None, 1])
y = tf.compat.v1.placeholder(tf.float32, [None, 1])
'''
定义隐藏层数据,权重矩阵w1和偏置矩阵b1
    权重矩阵w1初始生成0~1间的随机数
    偏置矩阵b1初始值为0
'''
w1 = tf.Variable(tf.compat.v1.random_uniform([1, 10], 0, 1))
b1 = tf.Variable(tf.zeros([1, 10]))
# 定义运算操作,计算出中间层
wb1 = tf.matmul(x, w1) + b1
# 定义激励函数,将wb1映射出去
layer1 = tf.compat.v1.nn.relu(wb1)
# 定义输出层数据
w2 = tf.Variable(tf.compat.v1.random_uniform([10, 1], 0, 1))
b2 = tf.Variable(tf.zeros([15, 1]))
wb2 = tf.matmul(layer1, w2) + b2
layer2 = tf.compat.v1.nn.relu(wb2)

# 计算偏移量,y为真实值,layer2为预测值,标准差
loss = tf.reduce_mean(tf.square(y - layer2))
# 梯度下降法,将偏移量下降
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.1).minimize(loss)
with tf.compat.v1.Session() as sess:
    # 变量初始化
    sess.run(tf.compat.v1.global_variables_initializer())
    for i in range(0, 10000):
        sess.run(train_step, feed_dict={x: dateNormal, y: priceNormal})
    # 至此训练结束,在此测试训练效果,即给输入数据,判断输出数据
    pred = sess.run(layer2, feed_dict={x: dateNormal})
    predPrice = np.zeros([15, 1])
    for i in range(0, 15):
        predPrice[i, 0] = (pred * 3000)[i, 0]
    plt.plot(date, predPrice, 'b', lw=1)
plt.show()
