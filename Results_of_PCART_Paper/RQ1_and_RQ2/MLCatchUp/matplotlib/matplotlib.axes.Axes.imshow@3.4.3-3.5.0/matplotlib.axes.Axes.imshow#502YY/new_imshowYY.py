import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, vmax=None, interpolation='nearest', origin='upper', vmin=None, aspect='auto', alpha=None, interpolation_stage=None)
