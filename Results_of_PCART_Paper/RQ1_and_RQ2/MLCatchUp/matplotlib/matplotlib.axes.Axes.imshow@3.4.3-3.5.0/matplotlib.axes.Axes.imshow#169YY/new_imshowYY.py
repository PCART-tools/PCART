import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, filternorm=True, aspect='auto', resample=None, url=None, filterrad=4.0, interpolation='nearest', interpolation_stage=None)
