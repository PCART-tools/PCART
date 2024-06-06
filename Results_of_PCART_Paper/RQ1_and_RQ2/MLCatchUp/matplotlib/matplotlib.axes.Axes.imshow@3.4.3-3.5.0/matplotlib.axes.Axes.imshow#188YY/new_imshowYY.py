import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, aspect='auto', interpolation='nearest', filternorm=True, filterrad=4.0, resample=None, cmap='viridis', norm=None, interpolation_stage=None)
