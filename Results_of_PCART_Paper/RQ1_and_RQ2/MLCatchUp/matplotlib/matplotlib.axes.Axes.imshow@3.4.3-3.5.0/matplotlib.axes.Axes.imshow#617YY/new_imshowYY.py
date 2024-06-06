import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, origin='upper', aspect='auto', vmin=None, vmax=None, filternorm=True, extent=None, alpha=None, interpolation='nearest', filterrad=4.0, interpolation_stage=None)
