from keras.models import Sequential
from keras.layers import Dense
import numpy as np
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
model.fit(x=x_train, y=y_train, batch_size=32, epochs=1, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, validation_freq=1, max_queue_size=10, workers=1, use_multiprocessing=False)
