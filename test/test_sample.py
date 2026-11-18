from matplotlib.pylab import add

from src.sample import *


def test_answer():
    assert func(3) == 4

def test_add_negative_numbers():
    assert add(-2, -3) == -5