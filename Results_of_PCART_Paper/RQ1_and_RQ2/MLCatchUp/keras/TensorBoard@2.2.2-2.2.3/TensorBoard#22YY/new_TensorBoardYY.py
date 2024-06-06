from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(100,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
tensorboard_callback = TensorBoard('./keras_file/logs', 0, 32, True, False, False, update_freq='epoch')
