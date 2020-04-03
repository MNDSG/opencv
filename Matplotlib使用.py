import numpy as np
import matplotlib.pyplot as plt

'''
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 3, 3, 2, 2, 3, 8])
# 绘制折线图,参数1表示x轴坐标,参数2表示y轴坐标,参数3表示颜色,参数4表示线宽
plt.plot(x, y, 'r')
plt.plot(x, y, 'g', lw=10)
# 绘制柱状图参数3表示占用宽度比例,参数4表示透明度,参数5表示颜色
plt.bar(x, y, 0.5, alpha=1, color='b')
plt.show()
'''
x = np.zeros(2)
y = np.zeros([2])
a = np.array([1, 3, 5, 7, 9])
b = np.array([2, 4, 6, 8, 10])
for i in range(0, 5):
    x[0] = i
    x[1] = i
    y[0] = a[i]
    y[1] = b[i]
    print(y)
    plt.plot(x, y)
plt.show()