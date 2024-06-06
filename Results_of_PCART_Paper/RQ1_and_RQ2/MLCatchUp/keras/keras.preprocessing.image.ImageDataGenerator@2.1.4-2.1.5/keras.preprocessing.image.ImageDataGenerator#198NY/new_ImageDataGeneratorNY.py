from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, False, False, False, 1e-06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, fill_mode='nearest', cval=0.0, horizontal_flip=False, vertical_flip=False, rescale=None, preprocessing_function=None, data_format=None, brightness_range=None, validation_split=0.0)
