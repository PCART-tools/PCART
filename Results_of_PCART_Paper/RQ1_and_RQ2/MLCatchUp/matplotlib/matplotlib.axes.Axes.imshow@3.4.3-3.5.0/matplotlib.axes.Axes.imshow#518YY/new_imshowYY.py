import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', origin='upper', interpolation='nearest', filterrad=4.0, filternorm=True, norm=None, vmin=None, alpha=None, vmax=None, resample=None, aspect='auto', interpolation_stage=None)
