from scipy import signal
(N, Wn, btype, analog, output, norm) = (4, 0.5, 'low', False, 'ba', 'phase')
result = signal.bessel(N, Wn, fs=None)
