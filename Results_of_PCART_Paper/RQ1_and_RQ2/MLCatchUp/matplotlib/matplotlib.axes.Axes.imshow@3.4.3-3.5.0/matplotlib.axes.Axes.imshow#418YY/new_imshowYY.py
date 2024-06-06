import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', interpolation='nearest', aspect='auto', filterrad=4.0, resample=None, filternorm=True, vmax=None, alpha=None, norm=None, vmin=None, interpolation_stage=None)
