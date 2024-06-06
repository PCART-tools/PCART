import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', vmin=None, norm=None, aspect='auto', filterrad=4.0, alpha=None, interpolation='nearest', interpolation_stage=None)
