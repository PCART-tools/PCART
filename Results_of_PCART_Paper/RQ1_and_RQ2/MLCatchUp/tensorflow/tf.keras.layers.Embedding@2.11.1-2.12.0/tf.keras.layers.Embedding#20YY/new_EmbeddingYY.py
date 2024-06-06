import tensorflow as tf
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(1000, 64, 'uniform', None, None, embeddings_constraint=None), sparse=False)
