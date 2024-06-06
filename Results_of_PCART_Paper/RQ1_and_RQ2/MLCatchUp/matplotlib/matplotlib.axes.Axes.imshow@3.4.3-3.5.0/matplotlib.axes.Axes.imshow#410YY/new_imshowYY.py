import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, aspect='auto', filternorm=True, interpolation='nearest', resample=None, vmax=None, filterrad=4.0, vmin=None, alpha=None, data=None, url=None, interpolation_stage=None)
