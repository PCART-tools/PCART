import numpy as np
result = np.fromregex(file='/home/zhang/Packages/data.txt', regexp='(\\d+), (\\d+)', dtype=[('num1', int), ('num2', int)], encoding=None)
