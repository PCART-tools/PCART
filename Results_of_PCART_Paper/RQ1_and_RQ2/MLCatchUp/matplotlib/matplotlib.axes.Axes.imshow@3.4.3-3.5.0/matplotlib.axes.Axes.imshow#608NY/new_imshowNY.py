import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', alpha=None, origin='upper', filterrad=4.0, vmax=None, vmin=None, extent=None, filternorm=True, resample=None, aspect='auto', interpolation_stage=None)
