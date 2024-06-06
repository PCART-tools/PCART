import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filternorm=True, interpolation='nearest', vmin=None, resample=None, filterrad=4.0, norm=None, cmap='viridis', aspect='auto', alpha=None, interpolation_stage=None)
