import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, vmin=None, filternorm=True, origin='upper', resample=None, aspect='auto', interpolation='nearest', alpha=None, filterrad=4.0, vmax=None, extent=None, interpolation_stage=None)
