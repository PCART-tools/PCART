import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', origin='upper', filternorm=True, resample=None, extent=None, norm=None, alpha=None, vmin=None, aspect='auto', filterrad=4.0, interpolation='nearest', vmax=None, interpolation_stage=None)
