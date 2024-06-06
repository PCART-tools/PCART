import numpy as np
result = np.fromregex('/home/zhang/Packages/data.txt', '(\\d+), (\\d+)', [('num1', int), ('num2', int)], encoding=None)
