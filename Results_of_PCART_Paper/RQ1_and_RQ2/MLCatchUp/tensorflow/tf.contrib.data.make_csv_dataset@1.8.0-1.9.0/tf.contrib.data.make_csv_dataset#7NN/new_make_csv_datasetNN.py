import tensorflow as tf
tf.contrib.data.make_csv_dataset('/home/zhang/Packages/tensorflow_file/dev.csv',  1,  None,  None,  None,  ',',  True,  '',  True,  None,  None,  True,  1,  None, prefetch_buffer_size=1, num_parallel_reads=1, num_parallel_parser_calls=2, sloppy=False, default_float_type=tf.float32, num_rows_for_inference=1)
