import numpy as np


def load_data(fname: str = 'data.npy'):
    """ Load and return an '.npy' file """
    curr_data = np.load(fname)
    curr_data.tofile('my_data')
    return np.load('my_data.npy')


def find_in_range(data: np.ndarray, num_range: tuple = (0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    get_data = load_data()
    val_in_range = []
    for num in np.nditer(get_data):
        if num in num_range:
            val_in_range.append(num)
    return np.array(val_in_range)


def main():
    print(load_data())


if __name__ == '__main__':
    main()
