import numpy as np

def main():
    arr = np.array([1, 2, 2, 3, 3, 4, 4, 5])
    (unique_elements, indices, inverse_indices) = np.unique(arr, return_index=True, return_inverse=True, axis=None)
    print('Unique elements:', unique_elements)
    print('Indices of unique elements:', indices)
    print('Inverse indices:', inverse_indices)
if __name__ == '__main__':
    main()
