import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, aspect='auto', interpolation='nearest', vmax=None, filterrad=4.0, alpha=None, vmin=None, interpolation_stage=None)
