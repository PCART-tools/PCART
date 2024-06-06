import scipy.integrate as spi

def myODE(y, t, x):
    return -x * y
y0 = 1.0
t = [0.0, 1.0, 2.0, 3.0]
result = spi.odeint(myODE, y0, t, (2.0,), None, col_deriv=0, full_output=1, ml=None, mu=None, rtol=None, atol=None, tcrit=None, h0=0.0, hmax=0.0, hmin=0.0, tfirst=False)
