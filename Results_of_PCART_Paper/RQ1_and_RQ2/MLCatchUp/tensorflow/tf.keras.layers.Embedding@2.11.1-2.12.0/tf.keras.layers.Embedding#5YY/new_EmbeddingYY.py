import tensorflow as tf
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(1000, 64, embeddings_initializer='uniform'), sparse=False)
