from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(10, 64)))
model.add(MaxPooling1D(), data_format='channels_last')
