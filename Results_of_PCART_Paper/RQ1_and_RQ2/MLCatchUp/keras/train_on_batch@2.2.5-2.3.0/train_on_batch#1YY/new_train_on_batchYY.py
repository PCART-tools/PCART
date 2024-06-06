from keras.models import Sequential
from keras.layers import Dense
import numpy as np
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
x_batch = np.random.random((32, 10))
y_batch = np.random.randint(2, size=(32, 1))
output = model.train_on_batch(x_batch, y_batch, reset_metrics=True)
