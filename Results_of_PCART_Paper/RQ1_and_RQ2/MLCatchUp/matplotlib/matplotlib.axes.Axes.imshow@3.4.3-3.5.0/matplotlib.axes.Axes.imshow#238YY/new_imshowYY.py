import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', filterrad=4.0, filternorm=True, resample=None, alpha=None, aspect='auto', interpolation_stage=None)
