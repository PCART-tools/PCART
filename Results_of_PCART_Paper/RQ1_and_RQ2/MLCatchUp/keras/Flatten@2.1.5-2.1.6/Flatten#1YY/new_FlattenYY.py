from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D
model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Flatten(), data_format='channels_last')
