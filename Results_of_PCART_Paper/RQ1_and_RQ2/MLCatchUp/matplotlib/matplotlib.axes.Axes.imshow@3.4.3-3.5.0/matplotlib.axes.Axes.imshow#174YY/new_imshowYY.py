import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', interpolation='nearest', norm=None, resample=None, interpolation_stage=None)
