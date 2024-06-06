import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', filternorm=True, aspect='auto', interpolation='nearest', vmin=None, norm=None, resample=None, alpha=None, filterrad=4.0, interpolation_stage=None)
