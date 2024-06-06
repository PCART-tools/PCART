import numpy as np

def main():
    loaded_data = np.load('/home/zhang/Packages/example.npy', allow_pickle=True, fix_imports=True, encoding='ASCII')
    print(loaded_data)
if __name__ == '__main__':
    main()
