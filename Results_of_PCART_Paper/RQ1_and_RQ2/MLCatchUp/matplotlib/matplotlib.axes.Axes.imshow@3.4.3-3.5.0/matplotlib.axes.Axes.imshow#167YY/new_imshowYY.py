import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', filternorm=True, aspect='auto', filterrad=4.0, interpolation_stage=None)
