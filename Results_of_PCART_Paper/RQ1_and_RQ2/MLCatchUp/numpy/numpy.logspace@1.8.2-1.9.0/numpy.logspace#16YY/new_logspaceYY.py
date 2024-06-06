import numpy as np

def main():
    array = np.logspace(1.0, 3.0, num=5, endpoint=True, base=10.0, dtype=None)
    print(array)
if __name__ == '__main__':
    main()
