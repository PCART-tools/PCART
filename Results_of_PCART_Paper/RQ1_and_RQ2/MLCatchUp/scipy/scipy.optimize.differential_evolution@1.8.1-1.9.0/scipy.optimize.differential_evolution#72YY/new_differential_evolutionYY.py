import numpy as np
from scipy.optimize import differential_evolution

def objective(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-1, 1), (-1, 1)]
result = differential_evolution(objective, bounds, (), strategy='best1bin', maxiter=1000, popsize=15, tol=0.01, mutation=(0.5, 1), recombination=0.7, seed=None, callback=None, integrality=None, vectorized=False)
print('Optimal Solution:', result.x)
print('Optimal Value:', result.fun)
