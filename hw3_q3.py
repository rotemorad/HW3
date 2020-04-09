import numpy as np


def load_data(fname: str = 'data.npy'):
    """ Load and return an '.npy' file """
    return np.load(fname)


def find_in_range(data: np.ndarray = load_data(), num_range: tuple = (0.3, 0.4)):
    """ Return an array containing the values of 'data' that are inside 'num_range' """
    return data[(data < num_range[1]) & (data > num_range[0])]


def first_after_val(data: np.ndarray = load_data(), val: float = 0.9) -> np.ndarray:
    """ Return the position of the first value larger than val """
    for idx, element in np.ndenumerate(data):
        if element > val:
            return idx
