import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, origin='upper', interpolation='nearest', alpha=None, vmax=None, filternorm=True, vmin=None, aspect='auto', interpolation_stage=None)
