from scipy.ndimage import maximum_filter
input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
size = (2, 2)
output = maximum_filter(input, size=size, footprint=None, axes=None)
