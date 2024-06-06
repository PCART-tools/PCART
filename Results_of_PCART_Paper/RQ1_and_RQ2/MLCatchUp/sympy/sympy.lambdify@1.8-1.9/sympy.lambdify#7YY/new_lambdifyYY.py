from sympy import symbols, sin, lambdify
import numpy as np
x = symbols('x')
expr = sin(x)
f = lambdify(args=x, expr=expr, modules='numpy', cse=False)
