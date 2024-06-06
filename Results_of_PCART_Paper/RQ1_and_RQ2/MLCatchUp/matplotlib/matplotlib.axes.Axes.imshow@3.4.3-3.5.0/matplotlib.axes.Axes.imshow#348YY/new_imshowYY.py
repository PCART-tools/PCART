import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(interpolation='nearest', filterrad=4.0, aspect='auto', vmin=None, filternorm=True, cmap='viridis', resample=None, X=X, norm=None, alpha=None, interpolation_stage=None)
