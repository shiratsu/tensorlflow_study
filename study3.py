# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

var1 = tf.Variable(0)
const2 = tf.constant(3)

add_op = tf.add(var1, const2)

# 変数に値をセットするにはassignを使う
update_var1 = tf.assign(var1, add_op)
mul_op = tf.mul(add_op, update_var1)

# 実際の計算処理は以下で行う
with tf.Session() as sess:
   
  # 変数を初期化するには以下のメソッドを呼び出さないと行けないらしい。
  sess.run(tf.initialize_all_variables())
  
  print(sess.run([mul_op]))
  print(sess.run([mul_op]))

# 実際の計算処理は以下で行う
with tf.Session() as sess:
   
  # 変数を初期化するには以下のメソッドを呼び出さないと行けないらしい。
  sess.run(tf.initialize_all_variables())

  print(sess.run([mul_op]))
  print(sess.run([mul_op]))
  print(sess.run([mul_op, mul_op]))  
