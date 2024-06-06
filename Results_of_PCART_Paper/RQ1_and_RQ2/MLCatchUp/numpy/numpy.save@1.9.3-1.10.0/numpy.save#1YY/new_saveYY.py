import numpy as np

def main():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    file_name = 'data.npy'
    np.save(file_name, arr, allow_pickle=True, fix_imports=True)
    print('Array saved to', file_name)
if __name__ == '__main__':
    main()
