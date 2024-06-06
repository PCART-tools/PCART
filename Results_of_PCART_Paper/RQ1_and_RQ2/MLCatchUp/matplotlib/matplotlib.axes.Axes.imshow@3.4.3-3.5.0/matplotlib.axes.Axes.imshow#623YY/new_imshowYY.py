import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', filterrad=4.0, norm=None, interpolation='nearest', vmax=None, alpha=None, extent=None, origin='upper', vmin=None, interpolation_stage=None)
