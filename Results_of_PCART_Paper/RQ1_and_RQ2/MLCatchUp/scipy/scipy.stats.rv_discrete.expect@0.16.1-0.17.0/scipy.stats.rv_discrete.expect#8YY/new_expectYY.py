import numpy as np
from scipy.stats import rv_discrete
xk = np.arange(1, 6)
pk = (0.1, 0.2, 0.3, 0.2, 0.2)
custom_distribution = rv_discrete(name='custom', values=(xk, pk))
mean = custom_distribution.expect((lambda x: (x ** 2)), (), loc=0, maxcount=1000, tolerance=1e-10, chunksize=32)
print(mean)
