from scipy.optimize import basinhopping

def my_function(x):
    return x ** 2
initial_x = 1.0
result = basinhopping(my_function, initial_x, 100, 1.0, 0.5, None, None, None, None, interval=50, disp=False, niter_success=None, seed=None)
