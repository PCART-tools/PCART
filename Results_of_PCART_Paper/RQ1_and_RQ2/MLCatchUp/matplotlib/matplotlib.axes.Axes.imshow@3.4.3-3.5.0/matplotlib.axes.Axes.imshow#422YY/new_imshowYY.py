import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, vmin=None, interpolation='nearest', filternorm=True, norm=None, vmax=None, alpha=None, cmap='viridis', aspect='auto', interpolation_stage=None)
