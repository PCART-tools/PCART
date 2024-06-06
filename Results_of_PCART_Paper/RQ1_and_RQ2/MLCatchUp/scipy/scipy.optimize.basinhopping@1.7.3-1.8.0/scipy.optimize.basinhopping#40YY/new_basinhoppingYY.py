from scipy.optimize import basinhopping

def objective(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2
x0 = [0.0, 0.0]
minimizer_kwargs = {'method': 'L-BFGS-B', 'bounds': [(-1, 4), (-1, 4)]}
result = basinhopping(objective, x0, niter=100, T=1.0, stepsize=0.5, minimizer_kwargs=minimizer_kwargs, take_step=None, accept_test=None, target_accept_rate=0.5, stepwise_factor=0.9)
print('Optimal value:', result.fun)
print('Optimal solution:', result.x)
