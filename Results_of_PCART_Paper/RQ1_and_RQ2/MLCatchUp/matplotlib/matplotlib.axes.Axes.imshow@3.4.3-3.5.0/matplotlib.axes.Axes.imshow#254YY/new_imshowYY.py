import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, interpolation='nearest', aspect='auto', norm=None, cmap='viridis', resample=None, alpha=None, interpolation_stage=None)
