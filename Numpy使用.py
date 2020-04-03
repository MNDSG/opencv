import numpy as np

'''
data1 = np.array([[1, 2, 3, 4, 5]])
print(data1)
data2 = np.array([[1, 2],
                  [3, 4]])
# 打印矩阵
print(data2)
# 打印矩阵纬度
print(data1.shape, data2.shape)
# 生成特殊矩阵
print(np.zeros([2, 3]), np.ones([2, 2]))
# 矩阵改
data2[1, 0] = 5
print(data2)
# 矩阵查
print(data2[1, 0])
# 普通运算
data3 = np.ones([2, 3])
print(data3 * 2)
print(data3 / 3)
print(data3 + 1)
print(data3 - 1)
# 矩阵运算
data4 = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(data3 + data4)
print(data3 * data4)
'''

# 创建1行3列的矩阵
data1 = np.zeros([1, 2])
# 创建数组,数组大小为2
data2 = np.zeros([2])
# 创建数组,数组大小为2
data3 = np.zeros(2)
print(data1)
print(data2)
print(data3)