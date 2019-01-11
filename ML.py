# TODO: here make (copy paste in)
# TODO: super simple ML thing
# TODO: for the google fire to connect to and run

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np


def test(digit: int = 0, shuffle: bool = False):
    digits = load_digits()
    if shuffle:
        np.random.shuffle(digits.images)
    plt.gray()
    plt.matshow(digits.images[digit])
    plt.show()
