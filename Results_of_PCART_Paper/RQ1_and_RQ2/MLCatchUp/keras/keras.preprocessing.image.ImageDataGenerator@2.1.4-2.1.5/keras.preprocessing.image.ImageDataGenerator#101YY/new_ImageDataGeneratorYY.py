from keras.preprocessing.image import ImageDataGenerator
data_generator = ImageDataGenerator(False, False, False, False, zca_whitening=False, zca_epsilon=1e-06, rotation_range=0.0, width_shift_range=0.0, height_shift_range=0.0, shear_range=0.0, zoom_range=0.0, channel_shift_range=0.0, fill_mode='nearest', brightness_range=None, validation_split=0.0)
