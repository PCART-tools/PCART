import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', alpha=None, aspect='auto', filterrad=4.0, vmax=None, resample=None, filternorm=True, vmin=None, interpolation_stage=None)
