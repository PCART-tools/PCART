import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', alpha=None, aspect='auto', interpolation='nearest', filterrad=4.0, norm=None, interpolation_stage=None)
