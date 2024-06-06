import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', norm=None, interpolation='nearest', vmin=None, alpha=None, aspect='auto', filternorm=True, interpolation_stage=None)
