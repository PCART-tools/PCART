import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, vmin=None, vmax=None, aspect='auto', interpolation='nearest', alpha=None, interpolation_stage=None)
