from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, featurewise_std_normalization=False, brightness_range=None, validation_split=0.0)
