from scipy.signal import find_peaks
x = [1, 3, 7, 1, 2, 6, 4, 3, 2, 0]
(peaks, properties) = find_peaks(x, 4, 0.5, distance=2, prominence=1, width=2, wlen=None, rel_height=0.5, plateau_size=None)
peaks
