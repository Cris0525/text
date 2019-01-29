# -*-coding:utf-8-*-
import tensorflow as tf
#import numpy as np

v1 = tf.constant([[2,3]])
v2 = tf.constant([[2],[3]])

product = tf.matmul(v1,v2)
print(product)

sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
num = tf.Variable(0,name = "count")
new_value = tf.add(num,10)
op = tf.assign(num,new_value)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(num))
    for i in range(5):
	sess.run(op)
	print(sess.run(num))
