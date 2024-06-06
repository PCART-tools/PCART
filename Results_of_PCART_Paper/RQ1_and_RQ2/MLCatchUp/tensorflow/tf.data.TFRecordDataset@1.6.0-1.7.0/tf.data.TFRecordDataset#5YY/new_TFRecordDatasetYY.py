import tensorflow as tf
d = tf.data.TFRecordDataset(filenames=['valid.tfrecord'], compression_type=None, num_parallel_reads=None)
