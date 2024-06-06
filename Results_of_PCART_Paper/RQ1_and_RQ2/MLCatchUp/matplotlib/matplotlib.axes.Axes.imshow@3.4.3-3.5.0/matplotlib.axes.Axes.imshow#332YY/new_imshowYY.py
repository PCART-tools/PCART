import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, vmin=None, interpolation='nearest', aspect='auto', filternorm=True, norm=None, cmap='viridis', alpha=None, interpolation_stage=None)
