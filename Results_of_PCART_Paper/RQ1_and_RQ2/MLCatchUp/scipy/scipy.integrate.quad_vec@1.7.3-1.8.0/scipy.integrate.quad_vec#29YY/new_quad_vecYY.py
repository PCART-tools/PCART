import scipy.integrate as spi

def f(x):
    return x ** 2
(result, error) = spi.quad_vec(f, a=0, b=1, epsabs=1e-200, epsrel=1e-08, norm='2', cache_size=100000000.0, args=())
