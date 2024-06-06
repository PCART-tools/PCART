import numpy as np

def main():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    median_value = np.median(data, axis=None, out=None, keepdims=False)
    print('Median:', median_value)
if __name__ == '__main__':
    main()
