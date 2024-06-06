import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, filterrad=4.0, vmin=None, resample=None, url=None, alpha=None, vmax=None, interpolation='nearest', aspect='auto', interpolation_stage=None)
