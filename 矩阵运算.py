import tensorflow as tf
tf.compat.v1.disable_eager_execution()

data1 = tf.constant([[1, 2, 3],
                     [4, 5, 6],
                     [7, 3, 2]])
data2 = tf.constant([[1, 5],
                     [2, 6],
                     [1, 1]])
data3 = tf.constant([[2, 2],
                     [1, 1],
                     [6, 6]])
mat0 = tf.constant([[0, 0, 0], [0, 0, 0]])  # 定义一个2行3列的空矩阵
mat1 = tf.zeros([2, 3])     # 同上
mat2 = tf.ones([2, 3])      # 定义一个2行3列的全1矩阵
mat3 = tf.fill([2, 3], 15)  # 向2行3列的矩阵中填充15
mat4 = tf.zeros_like(mat1)  # 定义一个纬度同mat1的全0矩阵
mat5 = tf.linspace(0.0, 2.0, 11)    # 将0~2分成11份,并生成矩阵
mat6 = tf.random_uniform_initializer([2, 3], -1, 2)     # 生成一个从-1到2的随机2行3列随机矩阵
dataMul = tf.matmul(data1, data2)   # 矩阵标准乘法
dataMul1 = tf.multiply(data2, data3)    # 矩阵纬度相乘
dataAdd = tf.add(data2, data3)
with tf.compat.v1.Session() as sess:
    print(sess.run(dataMul))
    print(sess.run(dataMul1))
    print(sess.run(dataAdd))
    print(sess.run([dataMul, dataAdd]))

