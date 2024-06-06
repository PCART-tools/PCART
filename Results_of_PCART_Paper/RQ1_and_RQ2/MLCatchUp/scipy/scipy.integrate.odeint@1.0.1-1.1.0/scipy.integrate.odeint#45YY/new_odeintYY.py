import scipy.integrate as spi

def myODE(y, t, x):
    return -x * y
y0 = 1.0
t = [0.0, 1.0, 2.0, 3.0]
result = spi.odeint(func=myODE, y0=y0, t=t, args=(2.0,), Dfun=None, col_deriv=0, full_output=1, ml=None, mu=None, tfirst=False)
