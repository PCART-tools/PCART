import tensorflow as tf
data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([0, 2])
tf.gather(data, indices, batch_dims=0)
