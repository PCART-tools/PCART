import tensorflow as tf
import itertools

def gen():
    for i in itertools.count(1):
        yield (i, [1] * i)
dataset = tf.data.Dataset.from_generator(gen, output_types=(tf.int64, tf.int64), output_signature=None)
