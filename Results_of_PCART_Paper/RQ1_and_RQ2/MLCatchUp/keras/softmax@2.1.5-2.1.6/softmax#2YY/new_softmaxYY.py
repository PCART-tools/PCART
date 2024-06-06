from keras import backend as K
import numpy as np
data = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
tensor = K.variable(data)
softmax_tensor = K.softmax(x=tensor, axis=(- 1))
