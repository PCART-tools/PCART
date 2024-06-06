import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', norm=None, interpolation='nearest', vmax=None, vmin=None, aspect='auto', alpha=None, filterrad=4.0, origin='upper', interpolation_stage=None)
