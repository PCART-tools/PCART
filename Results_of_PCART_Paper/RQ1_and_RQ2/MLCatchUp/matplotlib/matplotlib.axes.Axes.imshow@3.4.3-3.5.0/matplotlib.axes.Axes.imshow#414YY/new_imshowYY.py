import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', interpolation='nearest', vmax=None, alpha=None, vmin=None, resample=None, norm=None, interpolation_stage=None)
