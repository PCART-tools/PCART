import tensorflow as tf
dataset1 = tf.data.Dataset.range(0, 3)
dataset2 = tf.data.Dataset.range(100, 103)
tf.data.experimental.sample_from_datasets([dataset1, dataset2], weights=None, seed=None, stop_on_empty_dataset=False)
