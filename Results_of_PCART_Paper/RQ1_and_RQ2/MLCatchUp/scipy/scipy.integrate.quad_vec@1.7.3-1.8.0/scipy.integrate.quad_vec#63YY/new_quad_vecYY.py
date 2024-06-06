import scipy.integrate as spi

def f(x):
    return x ** 2
(result, error) = spi.quad_vec(f, 0, 1, 1e-200, 1e-08, '2', 100000000.0, 10000, 1, points=None, quadrature=None, args=())
