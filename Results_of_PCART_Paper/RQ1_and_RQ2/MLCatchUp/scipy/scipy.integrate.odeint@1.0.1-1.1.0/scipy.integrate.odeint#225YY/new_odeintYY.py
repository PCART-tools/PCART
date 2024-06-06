import scipy.integrate as spi

def myODE(y, t, x):
    return -x * y
y0 = 1.0
t = [0.0, 1.0, 2.0, 3.0]
result = spi.odeint(myODE, y0, t, (2.0,), None, 0, 1, None, None, None, None, None, 0.0, 0.0, 0.0, 0, 0, 0, mxordn=12, mxords=5, printmessg=1, tfirst=False)
