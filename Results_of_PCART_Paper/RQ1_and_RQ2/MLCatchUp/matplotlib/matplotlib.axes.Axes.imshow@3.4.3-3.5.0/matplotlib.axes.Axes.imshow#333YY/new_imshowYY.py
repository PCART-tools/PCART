import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, vmin=None, interpolation='nearest', cmap='viridis', norm=None, aspect='auto', filterrad=4.0, alpha=None, interpolation_stage=None)
