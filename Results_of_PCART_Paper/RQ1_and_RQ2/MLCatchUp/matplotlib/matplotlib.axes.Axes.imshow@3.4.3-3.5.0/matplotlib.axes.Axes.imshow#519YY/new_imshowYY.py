import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', origin='upper', interpolation='nearest', filterrad=4.0, alpha=None, url=None, norm=None, vmin=None, resample=None, filternorm=True, vmax=None, interpolation_stage=None)
