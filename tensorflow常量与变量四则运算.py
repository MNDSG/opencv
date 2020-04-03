import tensorflow as tf
tf.compat.v1.disable_eager_execution()

data1 = tf.constant(6)
data2 = tf.Variable(2)
# +
dataAdd = tf.add(data1, data2)
# 将dataAdd值拷贝给data2
dataCopy = tf.compat.v1.assign(data2, dataAdd)
# *
dataMul = tf.multiply(data1, data2)
# -
dataSub = tf.subtract(data1, data2)
# /
dataDiv = tf.divide(data1, data2)
init = tf.compat.v1.global_variables_initializer()
# with用于释放内存,当tf.compat.v1.Session()代码执行完毕后,自动释放内存
with tf.compat.v1.Session() as sess:
    sess.run(init)
    print(sess.run(dataAdd))
    print(sess.run(dataMul))
    print(sess.run(dataSub))
    print(sess.run(dataDiv))
    print("sess.run(dataCopy)", sess.run(dataCopy))
# .eval()同run()方法,这里再次执行拷贝操作,8+6
    print("dataCopy.eval()", dataCopy.eval())
    print("tf.compat.v1.get_default_session()", tf.compat.v1.get_default_session().run(dataCopy))
print("end !")