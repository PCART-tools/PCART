import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', interpolation='nearest', filternorm=True, aspect='auto', resample=None, norm=None, filterrad=4.0, interpolation_stage=None)
