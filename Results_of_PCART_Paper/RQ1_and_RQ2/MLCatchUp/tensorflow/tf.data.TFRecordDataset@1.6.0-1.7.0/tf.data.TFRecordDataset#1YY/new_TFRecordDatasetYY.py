import tensorflow as tf
d = tf.data.TFRecordDataset(['valid.tfrecord'], num_parallel_reads=None)
