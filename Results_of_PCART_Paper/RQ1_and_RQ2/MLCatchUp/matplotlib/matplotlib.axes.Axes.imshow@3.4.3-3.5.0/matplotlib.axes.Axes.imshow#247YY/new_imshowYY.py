import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', interpolation='nearest', aspect='auto', norm=None, alpha=None, filterrad=4.0, filternorm=True, interpolation_stage=None)
