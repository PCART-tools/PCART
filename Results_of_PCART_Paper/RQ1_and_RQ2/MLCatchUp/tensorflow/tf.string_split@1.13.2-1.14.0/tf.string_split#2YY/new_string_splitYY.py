import tensorflow as tf
string_values = ['Hello', 'TensorFlow', 'OpenAI']
string_tensor = tf.convert_to_tensor(string_values, dtype=tf.string)
tf.string_split(source=string_tensor, sep=None, result_type='SparseTensor', name=None)
