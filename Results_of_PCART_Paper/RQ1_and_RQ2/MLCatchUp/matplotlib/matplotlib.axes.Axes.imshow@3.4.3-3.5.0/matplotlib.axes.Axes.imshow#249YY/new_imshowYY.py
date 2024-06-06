import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', filterrad=4.0, norm=None, interpolation='nearest', alpha=None, resample=None, url=None, filternorm=True, aspect='auto', interpolation_stage=None)
