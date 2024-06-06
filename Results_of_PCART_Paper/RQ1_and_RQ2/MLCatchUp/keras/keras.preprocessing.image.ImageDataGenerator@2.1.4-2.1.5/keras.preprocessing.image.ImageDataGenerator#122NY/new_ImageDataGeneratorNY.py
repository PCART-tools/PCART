from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, False, False, False, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'nearest', 0.0, horizontal_flip=False, brightness_range=None, validation_split=0.0)
