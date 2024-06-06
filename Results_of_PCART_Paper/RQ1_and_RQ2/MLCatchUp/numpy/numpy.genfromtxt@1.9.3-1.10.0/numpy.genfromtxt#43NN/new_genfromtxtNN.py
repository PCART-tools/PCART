import numpy as np
from io import StringIO
with open('/home/zhang/Packages/data2.txt', 'rb') as f:
    data = np.genfromtxt(f, dtype=float, comments='#', delimiter=',', skip_header=0, skip_footer=0, converters=None, max_rows=0)
