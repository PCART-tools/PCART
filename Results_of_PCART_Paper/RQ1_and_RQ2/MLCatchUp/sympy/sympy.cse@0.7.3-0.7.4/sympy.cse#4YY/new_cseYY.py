import sympy as sp
(x, y, z) = sp.symbols('x y z')
expr = sp.sin(x) + sp.cos(y) + sp.sin(x) * sp.cos(y)
(replacements, reduced_expr) = sp.cse(expr, symbols=None, order='canonical')
