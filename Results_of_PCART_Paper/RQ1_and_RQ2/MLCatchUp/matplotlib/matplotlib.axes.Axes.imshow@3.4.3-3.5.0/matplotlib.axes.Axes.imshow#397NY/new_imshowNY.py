import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', filterrad=4.0, vmax=None, alpha=None, filternorm=True, vmin=None, aspect='auto', interpolation_stage=None)
