from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(featurewise_center=False, samplewise_center=False, featurewise_std_normalization=False, samplewise_std_normalization=False, zca_whitening=False, brightness_range=None, validation_split=0.0)
