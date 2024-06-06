from scipy.optimize import minimize
fun = lambda x: (x[0] - 2) ** 2 + (x[1] - 3) ** 2
x0 = [0, 0]
result = minimize(fun, x0, (), 'Nelder-Mead', jac=None, hess=None, hessp=None, bounds=None, constraints=())
