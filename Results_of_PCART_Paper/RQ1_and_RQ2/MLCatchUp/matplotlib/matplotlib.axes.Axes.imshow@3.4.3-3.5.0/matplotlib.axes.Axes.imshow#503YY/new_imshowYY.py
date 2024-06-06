import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', alpha=None, filterrad=4.0, aspect='auto', vmin=None, origin='upper', vmax=None, interpolation_stage=None)
