from scipy.optimize import basinhopping

def my_function(x):
    return x ** 2
initial_x = 1.0
result = basinhopping(my_function, initial_x, 100, 1.0, 0.5, None, take_step=None, accept_test=None, callback=None, interval=50, disp=False, seed=None)
