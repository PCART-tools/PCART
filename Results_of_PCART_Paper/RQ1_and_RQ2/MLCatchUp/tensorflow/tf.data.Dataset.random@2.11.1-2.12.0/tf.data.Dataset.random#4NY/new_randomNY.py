import tensorflow as tf
ds1 = tf.data.Dataset.random(4, None).take(10, rerandomize_each_iteration=None)
