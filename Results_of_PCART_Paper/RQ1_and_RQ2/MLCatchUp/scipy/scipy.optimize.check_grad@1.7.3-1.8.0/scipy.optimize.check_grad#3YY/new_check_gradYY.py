from scipy.optimize import check_grad

def func(x, *args):
    return x[0] ** 2 + x[1] ** 3

def grad(x, *args):
    return [2 * x[0], 3 * x[1] ** 2]
x0 = [1.0, 2.0]
result = check_grad(func, grad=grad, x0=x0, epsilon=1.4901161193847656e-08, direction='all', seed=None)
