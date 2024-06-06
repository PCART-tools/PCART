import tensorflow as tf

def outer_product(a):
    return tf.tensordot(a, a, 0)
batch_size = 100
a = tf.ones((batch_size, 32, 32))
c = tf.vectorized_map(outer_product, elems=a, fallback_to_while_loop=True, warn=True)
