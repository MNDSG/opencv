import tensorflow as tf
tf.compat.v1.disable_eager_execution()

data1 = tf.constant(6)
data2 = tf.constant(2)
# +
dataAdd = tf.add(data1, data2)
# -
dataMul = tf.multiply(data1, data2)
# *
dataSub = tf.subtract(data1, data2)
# /
dataDiv = tf.divide(data1, data2)
# with用于释放内存,当tf.compat.v1.Session()代码执行完毕后,自动释放内存
with tf.compat.v1.Session() as sess:
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
print("end !")