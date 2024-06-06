import tensorflow as tf
d = tf.data.TFRecordDataset(filenames=['valid.tfrecord'], num_parallel_reads=None)
