import tensorflow as tf
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(1000, 64, embeddings_initializer='uniform', embeddings_regularizer=None, activity_regularizer=None), sparse=False)
