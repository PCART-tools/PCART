import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, interpolation='nearest', alpha=None, cmap='viridis', filterrad=4.0, norm=None, aspect='auto', interpolation_stage=None)
