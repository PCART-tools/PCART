import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filternorm=True, norm=None, interpolation='nearest', cmap='viridis', aspect='auto', interpolation_stage=None)
