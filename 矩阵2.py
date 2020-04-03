import tensorflow as tf
tf.compat.v1.disable_eager_execution()

data1 = tf.constant([[6, 6]])
data2 = tf.constant([[2],
                     [2]])
data3 = tf.constant([[3, 3]])
data4 = tf.constant([[1, 2],
                     [3, 4],
                     [5, 6]])

print(data4.shape)
with tf.compat.v1.Session() as sess:
    print(sess.run(data4))  # 打印矩阵所有内容
    print(sess.run(data4[0]))   # 打印矩阵某一行内容
    print(sess.run(data4[:, 0]))    # 打印矩阵某一列内容
    print(sess.run(data4[0, 0]))    # 打印矩阵第1行第1列内容
