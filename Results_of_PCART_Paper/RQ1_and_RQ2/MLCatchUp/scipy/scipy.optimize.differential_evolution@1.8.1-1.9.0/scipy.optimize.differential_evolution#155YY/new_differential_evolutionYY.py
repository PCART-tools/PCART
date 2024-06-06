import numpy as np
from scipy.optimize import differential_evolution

def objective(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-1, 1), (-1, 1)]
result = differential_evolution(objective, bounds, (), 'best1bin', 1000, 15, 0.01, (0.5, 1), 0.7, None, None, False, True, init='latinhypercube', atol=0, updating='immediate', workers=1, integrality=None, vectorized=False)
print('Optimal Solution:', result.x)
print('Optimal Value:', result.fun)
