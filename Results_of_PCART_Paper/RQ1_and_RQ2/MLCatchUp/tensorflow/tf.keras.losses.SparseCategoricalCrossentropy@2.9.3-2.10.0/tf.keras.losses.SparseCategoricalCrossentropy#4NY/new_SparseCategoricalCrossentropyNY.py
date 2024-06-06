import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(False, tf.keras.losses.Reduction.NONE, ignore_class=None)
