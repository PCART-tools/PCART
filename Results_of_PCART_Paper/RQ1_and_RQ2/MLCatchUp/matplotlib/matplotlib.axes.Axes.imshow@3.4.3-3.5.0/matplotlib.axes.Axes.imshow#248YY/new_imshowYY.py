import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', filterrad=4.0, interpolation='nearest', norm=None, resample=None, alpha=None, filternorm=True, interpolation_stage=None)
