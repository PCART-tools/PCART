import numpy as np
from io import StringIO
with open('/home/zhang/Packages/data2.txt', 'rb') as f:
    data = np.genfromtxt(f, float, '#', ',', skip_header=0, skip_footer=0, converters=None, missing='', missing_values=None, filling_values=None, max_rows=0)
