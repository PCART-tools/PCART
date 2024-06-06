import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, aspect='auto', interpolation='nearest', alpha=None, filternorm=True, interpolation_stage=None)
