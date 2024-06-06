import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(interpolation='nearest', resample=None, filterrad=4.0, cmap='viridis', X=X, filternorm=True, norm=None, aspect='auto', interpolation_stage=None)
