import tensorflow as tf
d = tf.data.TFRecordDataset(['valid.tfrecord'], None, None, num_parallel_reads=None)
