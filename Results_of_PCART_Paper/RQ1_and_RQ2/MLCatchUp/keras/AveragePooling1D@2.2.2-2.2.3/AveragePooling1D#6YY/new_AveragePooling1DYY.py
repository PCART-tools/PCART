from keras.models import Sequential
from keras.layers import Conv1D, AveragePooling1D
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(10, 64)))
model.add(AveragePooling1D(pool_size=2, strides=None), data_format='channels_last')
