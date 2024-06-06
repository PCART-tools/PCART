from keras.utils import to_categorical
import numpy as np
class_vector = np.array([0, 1, 2, 3, 4])
categorical_matrix = to_categorical(class_vector, num_classes=None, dtype='float32')
