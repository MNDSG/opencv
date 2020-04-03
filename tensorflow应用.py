'''
1.由于版本问题,想要使用之前的函数,需要在函数前加tf.compat.v1.函数名
2.所有数据均在sess.run()下执行,故使用前需要创建Session()函数
3.tensorfloat本质:tensor + 计算图
    tensor表示常量或变量,其纬度可以是一维或多维
    op表示操作,可为四则运算或者复制
    计算图(graphs)表示数据和操作的过程
4.在tensorfloat中,所有计算图都要放在Session下执行
'''
import tensorflow as tf
# 保证sess.run()能够正常运行,必须加上,否则Session会报错
tf.compat.v1.disable_eager_execution()

# 定义常量
data1 = tf.constant(2.5)

# 定义变量.并给变量取名为Var
data2 = tf.Variable(10, name="Var")

# 在tensorflow 2.0中使用下述代替tf.Session()
sess = tf.compat.v1.Session()

# 所有变量需要初始化,这里为变量初始化函数
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

# 更换数据类型
data3 = tf.constant(2, dtype=tf.float32)

print(sess.run(data1))
print(sess.run(data2))
print(sess.run(data3))

sess.close()

