from scipy.ndimage import median_filter
input_data = [[3, 2, 3], [4, 5, 6], [7, 8, 9]]
size = (3, 3)
output_data = median_filter(input=input_data, size=size, axes=None)
