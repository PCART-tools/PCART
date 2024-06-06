import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', filternorm=True, vmin=None, aspect='auto', interpolation='nearest', norm=None, filterrad=4.0, alpha=None, interpolation_stage=None)
