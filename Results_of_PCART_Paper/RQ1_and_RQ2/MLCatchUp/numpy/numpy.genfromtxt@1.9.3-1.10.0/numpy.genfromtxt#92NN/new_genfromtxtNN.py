import numpy as np
from io import StringIO
with open('/home/zhang/Packages/data2.txt', 'rb') as f:
    data = np.genfromtxt(f,  float,  '#',  ',',  0,  0,  0,  None,  '',  None,  None,  None, names=None)
