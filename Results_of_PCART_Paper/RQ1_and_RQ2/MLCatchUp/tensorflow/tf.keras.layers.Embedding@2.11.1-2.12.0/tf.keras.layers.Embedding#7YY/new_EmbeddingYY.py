import tensorflow as tf
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim=1000, output_dim=64, embeddings_initializer='uniform'), sparse=False)
