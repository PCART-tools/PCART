import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(False, ignore_class=None)
