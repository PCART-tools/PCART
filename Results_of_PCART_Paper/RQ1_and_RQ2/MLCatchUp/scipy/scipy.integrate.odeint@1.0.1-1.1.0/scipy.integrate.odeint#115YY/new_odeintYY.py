import scipy.integrate as spi

def myODE(y, t, x):
    return -x * y
y0 = 1.0
t = [0.0, 1.0, 2.0, 3.0]
result = spi.odeint(myODE, y0, t, (2.0,), None, 0, 1, None, None, None, None, tcrit=None, h0=0.0, hmax=0.0, hmin=0.0, tfirst=False)
