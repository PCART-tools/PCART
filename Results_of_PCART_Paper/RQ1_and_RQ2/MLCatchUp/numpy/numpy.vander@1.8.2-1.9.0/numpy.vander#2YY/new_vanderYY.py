import numpy as np

def main():
    array = np.vander(x=np.array([1, 2, 3, 4]), increasing=False)
    print(array)
if __name__ == '__main__':
    main()
