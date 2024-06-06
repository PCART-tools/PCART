from scipy import fft
x = [1, 2, 3, 4, 5]
result = fft.dst(x, 2, None, orthogonalize=None)
