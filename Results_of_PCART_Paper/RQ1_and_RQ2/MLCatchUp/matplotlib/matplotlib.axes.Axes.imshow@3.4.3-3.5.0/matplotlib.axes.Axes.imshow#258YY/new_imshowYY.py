import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, interpolation='nearest', filternorm=True, filterrad=4.0, resample=None, alpha=None, cmap='viridis', aspect='auto', norm=None, interpolation_stage=None)
