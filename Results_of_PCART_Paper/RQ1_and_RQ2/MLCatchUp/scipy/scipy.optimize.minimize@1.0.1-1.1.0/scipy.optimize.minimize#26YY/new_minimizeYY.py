from scipy.optimize import minimize
fun = lambda x: (x[0] - 2) ** 2 + (x[1] - 3) ** 2
x0 = [0, 0]
result = minimize(fun, x0=x0, args=(), method='Nelder-Mead', tol=1e-06, callback=None, options={'disp': True, 'maxiter': 100}, jac=None, hess=None, hessp=None, bounds=None, constraints=())
