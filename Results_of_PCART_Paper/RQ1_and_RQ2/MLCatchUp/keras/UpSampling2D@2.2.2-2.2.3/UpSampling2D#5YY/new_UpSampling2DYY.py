from keras.models import Sequential
from keras.layers import UpSampling2D, Conv2D
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(UpSampling2D(size=(2, 2), data_format=None), interpolation='nearest')
