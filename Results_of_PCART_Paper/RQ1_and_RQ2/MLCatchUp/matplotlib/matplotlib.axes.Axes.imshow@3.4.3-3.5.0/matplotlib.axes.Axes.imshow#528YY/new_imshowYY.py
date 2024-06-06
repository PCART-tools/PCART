import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, interpolation='nearest', origin='upper', resample=None, aspect='auto', filterrad=4.0, vmin=None, cmap='viridis', filternorm=True, vmax=None, norm=None, alpha=None, interpolation_stage=None)
