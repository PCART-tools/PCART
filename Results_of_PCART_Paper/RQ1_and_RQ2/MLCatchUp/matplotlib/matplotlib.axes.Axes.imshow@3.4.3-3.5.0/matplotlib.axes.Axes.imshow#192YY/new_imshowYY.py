import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(interpolation='nearest', aspect='auto', filternorm=True, norm=None, cmap='viridis', X=X, interpolation_stage=None)
