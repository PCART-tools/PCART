import numpy as np
from io import StringIO
with open('/home/zhang/Packages/data2.txt', 'rb') as f:
    data = np.genfromtxt(f,  float,  '#',  ',',  0,  0,  0,  None,  '',  None,  None,  None,  None,  None,  None,  '_',  False, case_sensitive=True, defaultfmt='f%i', unpack=None, usemask=False, loose=True, invalid_raise=True)
