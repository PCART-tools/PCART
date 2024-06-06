from scipy.ndimage import gaussian_filter
input_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sigma = 1.0
output_data = gaussian_filter(input_data, sigma, 0, None, mode='reflect', cval=0.0, truncate=4.0, radius=None)
print(output_data)
