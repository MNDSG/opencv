import tensorflow as tf
tf.compat.v1.disable_eager_execution()

data1 = tf.compat.v1.placeholder(tf.float32)
data2 = tf.compat.v1.placeholder(tf.float32)

dataAdd = tf.add(data1, data2)
with tf.compat.v1.Session() as sess:
    print(sess.run(dataAdd, feed_dict={data1: 6, data2: 2}))    # 在run()中执行dataAdd操作,操作数为data1和data2,使用feed_dict()赋值
print('end !')
