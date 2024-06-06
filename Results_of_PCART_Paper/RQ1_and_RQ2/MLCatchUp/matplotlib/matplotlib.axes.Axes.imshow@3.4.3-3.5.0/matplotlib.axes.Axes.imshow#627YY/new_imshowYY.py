import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', filterrad=4.0, norm=None, extent=None, filternorm=True, origin='upper', alpha=None, vmin=None, aspect='auto', interpolation='nearest', vmax=None, interpolation_stage=None)
