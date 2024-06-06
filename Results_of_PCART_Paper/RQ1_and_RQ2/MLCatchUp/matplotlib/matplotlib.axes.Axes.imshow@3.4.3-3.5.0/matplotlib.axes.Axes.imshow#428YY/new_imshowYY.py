import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, vmin=None, vmax=None, filterrad=4.0, aspect='auto', cmap='viridis', resample=None, alpha=None, filternorm=True, norm=None, interpolation='nearest', interpolation_stage=None)
