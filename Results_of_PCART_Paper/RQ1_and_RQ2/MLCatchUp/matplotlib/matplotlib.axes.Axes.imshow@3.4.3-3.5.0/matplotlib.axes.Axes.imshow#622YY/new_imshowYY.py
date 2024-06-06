import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', vmin=None, filternorm=True, norm=None, extent=None, alpha=None, interpolation='nearest', origin='upper', aspect='auto', vmax=None, interpolation_stage=None)
