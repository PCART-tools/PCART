import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, resample=None, filterrad=4.0, vmin=None, aspect='auto', interpolation='nearest', alpha=None, interpolation_stage=None)
