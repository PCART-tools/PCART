import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, vmin=None, filternorm=True, vmax=None, origin='upper', filterrad=4.0, extent=None, resample=None, aspect='auto', interpolation='nearest', alpha=None, interpolation_stage=None)
