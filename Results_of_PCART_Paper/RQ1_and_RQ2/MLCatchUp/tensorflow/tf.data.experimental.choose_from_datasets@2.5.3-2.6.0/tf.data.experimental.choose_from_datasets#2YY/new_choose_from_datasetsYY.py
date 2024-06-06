import tensorflow as tf
datasets = [tf.data.Dataset.from_tensors('foo').repeat(), tf.data.Dataset.from_tensors('bar').repeat(), tf.data.Dataset.from_tensors('baz').repeat()]
choice_dataset = tf.data.Dataset.range(3).repeat(3)
result = tf.data.experimental.choose_from_datasets(datasets, choice_dataset=choice_dataset, stop_on_empty_dataset=False)
