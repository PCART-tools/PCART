from scipy.optimize import differential_evolution

def func(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-2, 2), (-2, 2)]
result = differential_evolution(func, bounds=bounds, args=(), strategy='best1bin', maxiter=1000, popsize=15, x0=None)
