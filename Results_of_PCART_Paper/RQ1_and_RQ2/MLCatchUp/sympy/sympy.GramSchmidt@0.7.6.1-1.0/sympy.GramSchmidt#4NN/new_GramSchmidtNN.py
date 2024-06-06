import sympy as sp
v1 = sp.Matrix([1, 0, 0])
v2 = sp.Matrix([0, 1, 0])
v3 = sp.Matrix([0, 0, 1])
independent_vectors = [v1, v2, v3]
orthogonalized_vectors = sp.GramSchmidt(independent_vectors, orthonormal=True)
