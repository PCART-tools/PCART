from scipy.integrate import solve_ivp

def fun(t, y):
    return t - y
t_span = (0, 2)
y0 = [2.0]
method = 'RK45'
t_eval = None
dense_output = False
events = None
vectorized = False
options = {'atol': 1e-06, 'rtol': 1e-06}
sol = solve_ivp(fun=fun, t_span=t_span, y0=y0, method=method, t_eval=t_eval, dense_output=dense_output, args=None)
