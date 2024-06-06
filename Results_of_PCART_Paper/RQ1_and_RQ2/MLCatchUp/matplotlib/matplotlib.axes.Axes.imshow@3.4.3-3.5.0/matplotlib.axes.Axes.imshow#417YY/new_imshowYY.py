import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', norm=None, filterrad=4.0, interpolation='nearest', alpha=None, vmin=None, vmax=None, filternorm=True, interpolation_stage=None)
