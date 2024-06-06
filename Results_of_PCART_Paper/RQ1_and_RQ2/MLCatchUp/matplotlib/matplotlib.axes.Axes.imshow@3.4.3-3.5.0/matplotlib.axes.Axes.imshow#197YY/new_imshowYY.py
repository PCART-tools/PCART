import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(interpolation='nearest', aspect='auto', norm=None, X=X, cmap='viridis', filterrad=4.0, filternorm=True, interpolation_stage=None)
