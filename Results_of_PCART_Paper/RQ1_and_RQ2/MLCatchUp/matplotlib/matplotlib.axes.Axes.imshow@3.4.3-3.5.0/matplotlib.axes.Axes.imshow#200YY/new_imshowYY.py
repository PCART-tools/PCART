import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X=X, filterrad=4.0, cmap='viridis', interpolation='nearest', filternorm=True, data=None, url=None, norm=None, aspect='auto', resample=None, interpolation_stage=None)
