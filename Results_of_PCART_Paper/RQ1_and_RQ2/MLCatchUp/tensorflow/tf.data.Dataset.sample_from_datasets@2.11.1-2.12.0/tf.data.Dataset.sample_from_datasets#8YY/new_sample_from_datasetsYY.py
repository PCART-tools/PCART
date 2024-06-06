import tensorflow as tf
dataset1 = tf.data.Dataset.range(0, 3)
dataset2 = tf.data.Dataset.range(100, 103)
sample_dataset = tf.data.Dataset.sample_from_datasets([dataset1, dataset2], weights=[0.5, 0.5], seed=None, rerandomize_each_iteration=None)
