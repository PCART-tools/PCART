import scipy.integrate as spi

def f(x):
    return x ** 2
(result, error) = spi.quad_vec(f, 0, 1, 1e-200, 1e-08, '2', cache_size=100000000.0, limit=10000, workers=1, args=())
