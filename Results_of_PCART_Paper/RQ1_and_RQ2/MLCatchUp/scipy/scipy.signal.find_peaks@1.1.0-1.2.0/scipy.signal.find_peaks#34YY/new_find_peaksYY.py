from scipy.signal import find_peaks
x = [1, 3, 7, 1, 2, 6, 4, 3, 2, 0]
(peaks, properties) = find_peaks(x, height=4, threshold=0.5, distance=2, prominence=1, width=2, wlen=None, plateau_size=None)
peaks
