import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(False, reduction=tf.keras.losses.Reduction.NONE, ignore_class=None)
