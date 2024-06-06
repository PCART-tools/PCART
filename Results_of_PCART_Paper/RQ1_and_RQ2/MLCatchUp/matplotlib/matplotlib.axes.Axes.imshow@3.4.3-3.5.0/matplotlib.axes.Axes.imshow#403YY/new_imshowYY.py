import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, aspect='auto', interpolation='nearest', vmax=None, vmin=None, filterrad=4.0, alpha=None, interpolation_stage=None)
