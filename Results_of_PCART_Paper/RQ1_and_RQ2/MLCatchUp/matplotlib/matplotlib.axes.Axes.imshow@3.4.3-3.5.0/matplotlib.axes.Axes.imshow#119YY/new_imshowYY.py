import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', aspect='auto', filternorm=True, norm=None, url=None, filterrad=4.0, resample=None, interpolation_stage=None)
