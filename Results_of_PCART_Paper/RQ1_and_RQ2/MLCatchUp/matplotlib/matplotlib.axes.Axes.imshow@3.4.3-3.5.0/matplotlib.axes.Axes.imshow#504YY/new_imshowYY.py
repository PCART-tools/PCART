import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', vmax=None, vmin=None, resample=None, alpha=None, origin='upper', aspect='auto', interpolation_stage=None)
