import tensorflow as tf
tf.contrib.data.make_csv_dataset('/home/zhang/Packages/tensorflow_file/dev.csv', 1, None, None, None, select_columns=None, field_delim=',', use_quote_delim=True, na_value='', header=True, num_epochs=None, shuffle=True, shuffle_buffer_size=10000, shuffle_seed=None, prefetch_buffer_size=1, num_parallel_reads=1, sloppy=False, num_rows_for_inference=1, compression_type=2)
