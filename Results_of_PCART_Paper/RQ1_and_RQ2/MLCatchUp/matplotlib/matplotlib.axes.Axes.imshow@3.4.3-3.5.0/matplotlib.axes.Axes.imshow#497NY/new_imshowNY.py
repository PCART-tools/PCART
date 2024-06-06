import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filterrad=4.0, vmax=None, vmin=None, alpha=None, filternorm=True, interpolation='nearest', origin='upper', aspect='auto', interpolation_stage=None)
