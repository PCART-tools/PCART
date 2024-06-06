from scipy.optimize import basinhopping

def my_function(x):
    return x ** 2
initial_x = 1.0
result = basinhopping(my_function, x0=initial_x, niter=100, T=1.0, seed=None)
