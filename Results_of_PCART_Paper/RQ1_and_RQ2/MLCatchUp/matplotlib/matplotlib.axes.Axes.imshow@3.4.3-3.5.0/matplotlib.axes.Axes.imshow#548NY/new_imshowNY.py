import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filterrad=4.0, filternorm=True, resample=None, aspect='auto', interpolation='nearest', alpha=None, vmin=None, vmax=None, origin='upper', extent=None, interpolation_stage=None)
