from keras.models import Sequential
from keras.layers import Dense
import numpy as np
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(20,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
x = np.random.random((1, 20))
y = np.random.randint(2, size=(1, 1))
score = model.test_on_batch(x, y=y, sample_weight=None, reset_metrics=True)
