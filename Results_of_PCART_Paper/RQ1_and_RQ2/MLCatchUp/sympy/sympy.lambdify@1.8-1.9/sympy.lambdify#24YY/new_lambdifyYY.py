from sympy import symbols, sin, lambdify
import numpy as np
x = symbols('x')
expr = sin(x)
f = lambdify(x, expr=expr, modules='numpy', printer=None, use_imps=True, dummify=False, cse=False)
