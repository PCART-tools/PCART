import tensorflow as tf
import itertools

def gen():
    for i in itertools.count(1):
        yield (i, [1] * i)
dataset = tf.data.Dataset.from_generator(gen, (tf.int64, tf.int64), (tf.TensorShape([]), tf.TensorShape([None])), None, output_signature=None)
