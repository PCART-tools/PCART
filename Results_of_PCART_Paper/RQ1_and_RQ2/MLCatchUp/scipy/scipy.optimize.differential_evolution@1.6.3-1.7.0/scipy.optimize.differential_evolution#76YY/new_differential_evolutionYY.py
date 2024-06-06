from scipy.optimize import differential_evolution

def func(x):
    return x[0] ** 2 + x[1] ** 2
bounds = [(-2, 2), (-2, 2)]
result = differential_evolution(func, bounds, (), 'best1bin', 1000, 15, 0.01, (0.5, 1), 0.7, None, None, False, x0=None)
