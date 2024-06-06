import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filterrad=4.0, interpolation='nearest', norm=None, url=None, aspect='auto', filternorm=True, resample=None, cmap='viridis', interpolation_stage=None)
