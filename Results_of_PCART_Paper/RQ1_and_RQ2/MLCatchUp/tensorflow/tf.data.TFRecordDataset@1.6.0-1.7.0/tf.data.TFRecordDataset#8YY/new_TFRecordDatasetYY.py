import tensorflow as tf
d = tf.data.TFRecordDataset(['valid.tfrecord'], compression_type=None, buffer_size=None, num_parallel_reads=None)
