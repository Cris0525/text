#coding:utf-8
# 一元的线性回归模型的训练
# 1.通过训练数据，推测出线性回归函数（y = w * x = b）中w和b的值
# 2.通过验证数据，验证得到的函数是否符合预期。

# 引入Tensorflow函数
import tensorflow as tf
# 引入绘图表（为了清晰了解训练结果）
import matplotlib.pyplot as plt
# 引入测试数据模块
import testData as td
# 1.获取训练数据
# 通过testData来模拟第三方接口
# get_train_data    获取训练数据 参数：data_length(获取数据的个数) 返回值：二维数组 [0]代表x（横坐标） [1]代表y（纵坐标）
# get_validate_data 获取验证数据 参数：data_length(获取数据的个数) 返回值：二维数组 [0]代表x（横坐标） [1]代表y（纵坐标）
trainData = td.get_train_data(2000)
trainx = [v[0] for v in trainData]
trainy = [v[1] for v in trainData]

# 2.构造预测的线性回归函数 有= W * x + b
W = tf.Variable(tf.random_uniform([1]))
b = tf.Variable(tf.zeros([1]))
y = W *W* trainx + b

# 3.判断假设函数的好坏
# 代价函数
cost = tf.reduce_mean(tf.square(y - trainy))

# 4.调整假设函数
# 梯度下降算法找最优解
optimizer = tf.train.GradientDescentOptimizer(0.08)
train = optimizer.minimize(cost)
Sess = tf.Session()
writer = tf.summary.FileWriter("logs/", Sess.graph)
with Sess as sess:
    
    ###########初始化所有变量值###########
    init = tf.global_variables_initializer()
    sess.run(init)
    #初始化W和b的值
    print("cost=",sess.run(cost),"W=",sess.run(W),"b=",sess.run(b))

    #循环运行
    for k in range(500):
        sess.run(train)
        #输出训练好的W和b
        print("cost=", sess.run(cost), "W=", sess.run(W), "b=", sess.run(b))
    print("执行完成！")
    	

    #构造图形结构
    plt.plot(trainx, trainy, 'ro', label='train data')
    plt.plot(trainx, sess.run(y), label='tain result')
    plt.legend()
    plt.show()

