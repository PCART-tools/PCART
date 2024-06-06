import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, vmax=None, vmin=None, alpha=None, extent=None, filternorm=True, filterrad=4.0, origin='upper', aspect='auto', interpolation='nearest', interpolation_stage=None)
