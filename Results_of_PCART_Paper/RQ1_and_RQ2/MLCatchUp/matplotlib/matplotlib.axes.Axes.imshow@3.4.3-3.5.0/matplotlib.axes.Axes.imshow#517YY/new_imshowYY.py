import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', alpha=None, filterrad=4.0, filternorm=True, vmax=None, norm=None, vmin=None, interpolation='nearest', aspect='auto', origin='upper', interpolation_stage=None)
