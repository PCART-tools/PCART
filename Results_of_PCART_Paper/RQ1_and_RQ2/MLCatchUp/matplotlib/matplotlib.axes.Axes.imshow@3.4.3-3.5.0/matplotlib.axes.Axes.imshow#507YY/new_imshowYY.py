import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, interpolation='nearest', vmax=None, filternorm=True, vmin=None, filterrad=4.0, origin='upper', alpha=None, aspect='auto', interpolation_stage=None)
