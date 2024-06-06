from scipy.optimize import basinhopping

def my_function(x):
    return x ** 2
initial_x = 1.0
result = basinhopping(my_function, x0=initial_x, niter=100, T=1.0, stepsize=0.5, minimizer_kwargs=None, take_step=None, accept_test=None, callback=None, seed=None)
