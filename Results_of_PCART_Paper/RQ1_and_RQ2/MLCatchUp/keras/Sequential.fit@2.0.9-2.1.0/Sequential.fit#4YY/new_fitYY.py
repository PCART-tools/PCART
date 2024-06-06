from keras.models import Sequential
from keras.layers import Dense
import numpy as np
X = np.random.random((100, 20))
y = np.random.randint(2, size=(100, 1))
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, 32, steps_per_epoch=None, validation_steps=None)
