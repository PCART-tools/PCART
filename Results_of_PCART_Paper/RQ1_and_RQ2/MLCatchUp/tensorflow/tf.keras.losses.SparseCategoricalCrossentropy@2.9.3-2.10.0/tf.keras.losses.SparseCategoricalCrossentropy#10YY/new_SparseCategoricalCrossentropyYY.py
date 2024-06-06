import tensorflow as tf
scce = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False, reduction=tf.keras.losses.Reduction.NONE, name='sparse_categorical_crossentropy', ignore_class=None)
