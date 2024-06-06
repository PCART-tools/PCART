import tensorflow as tf
d = tf.data.TFRecordDataset(['valid.tfrecord'], None, num_parallel_reads=None)
