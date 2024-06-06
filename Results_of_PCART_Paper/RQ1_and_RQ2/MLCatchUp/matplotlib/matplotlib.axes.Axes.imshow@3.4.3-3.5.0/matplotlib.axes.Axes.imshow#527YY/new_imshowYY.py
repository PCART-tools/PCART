import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filternorm=True, cmap='viridis', filterrad=4.0, origin='upper', vmin=None, vmax=None, interpolation='nearest', alpha=None, aspect='auto', norm=None, interpolation_stage=None)
