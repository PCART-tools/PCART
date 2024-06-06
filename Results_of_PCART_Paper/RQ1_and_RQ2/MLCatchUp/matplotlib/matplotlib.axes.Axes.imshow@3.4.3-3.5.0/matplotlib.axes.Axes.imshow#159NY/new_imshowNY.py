import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filterrad=4.0, interpolation='nearest', url=None, filternorm=True, resample=None, aspect='auto', interpolation_stage=None)
