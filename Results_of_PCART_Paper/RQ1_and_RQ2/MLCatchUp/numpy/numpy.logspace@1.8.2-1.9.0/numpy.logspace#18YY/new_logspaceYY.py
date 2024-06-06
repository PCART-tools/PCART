import numpy as np

def main():
    array = np.logspace(start=1.0, stop=3.0, num=5, endpoint=True, base=10.0, dtype=None)
    print(array)
if __name__ == '__main__':
    main()
