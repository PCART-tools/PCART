from sympy.logic.boolalg import simplify_logic, And, Or, Not
from sympy.abc import x, y, z
expr = And(Or(x, y), Not(And(x, Not(y))))
simplified_expr = simplify_logic(expr, form=None, deep=True, dontcare=None)
