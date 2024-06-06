from keras.models import Sequential
from keras.layers import Conv1D, AveragePooling1D
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(10, 64)))
model.add(AveragePooling1D(2, strides=None, padding='valid'), data_format='channels_last')
