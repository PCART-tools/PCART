from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, featurewise_std_normalization=False, samplewise_std_normalization=False, zca_whitening=False, brightness_range=None, validation_split=0.0)
