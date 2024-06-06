import tensorflow as tf
tf.contrib.data.make_csv_dataset('/home/zhang/Packages/tensorflow_file/dev.csv', 1, None, None, None, None, ',', True, '', True, None, True, 10000, None, prefetch_buffer_size=1, num_parallel_reads=1, sloppy=False, num_rows_for_inference=1, compression_type=2)
