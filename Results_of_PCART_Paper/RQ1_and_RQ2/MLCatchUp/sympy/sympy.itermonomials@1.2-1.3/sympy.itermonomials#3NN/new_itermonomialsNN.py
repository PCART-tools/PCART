from sympy import symbols, itermonomials
(x, y) = symbols('x y')
monomials = itermonomials(variables=[x, y], max_degree=2, min_degree=0)
