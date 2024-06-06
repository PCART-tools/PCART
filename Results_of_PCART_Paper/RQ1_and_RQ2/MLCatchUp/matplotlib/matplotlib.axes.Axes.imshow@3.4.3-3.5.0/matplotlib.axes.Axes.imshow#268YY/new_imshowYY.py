import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(aspect='auto', filterrad=4.0, X=X, resample=None, cmap='viridis', norm=None, filternorm=True, alpha=None, interpolation='nearest', interpolation_stage=None)
