import scipy.signal
numtaps = 50
bands = [0, 0.1, 0.2, 0.5]
desired = [1, 0]
weight = [1, 0.1]
Hz = 2
type = 'bandpass'
maxiter = 25
grid_density = 16
scipy.signal.remez(numtaps, bands, desired, weight, fs=None)
