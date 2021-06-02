from decimal import DivisionByZero
from numpy.lib import emath
import pytest
import numpy as np

from dct.dct import dct


def test_1d():
    input = np.array(
        [231, 32, 233, 161, 24, 71, 140, 245],
    )
    solution = np.array(
        [4.01e02, 6.60e00, 1.09e02, -1.12e02, 6.54e01, 1.21e02, 1.16e02, 2.88e01],
    )
    output = dct(input)

    assert np.allclose(solution, output, rtol=1)


def test_1d_dimensions():
    invalid = [
        np.empty((0, 0)),  # zero values
        np.empty((1, 1)),  # one value, multidimension
        np.empty((2, 1)),
        np.empty((1, 3)),
        np.empty((5, 4)),
    ]

    valid = [
        np.empty((1)),  # one value
        np.empty((2)),  # more than one value
    ]

    with pytest.raises(ZeroDivisionError):
        dct(np.empty((0)))  # zero values N = 0

    with pytest.raises(ValueError):
        for x in invalid:
            dct(x)

    for x in valid:
        try:
            dct(x)
        except ValueError as e:
            pytest.fail(f"An exception has been raised: {e}")


def test_1d_zeros():
    input = np.zeros((8))
    output = dct(input)

    assert np.allclose(input, output)


def test_1d_ones():
    input = np.ones((16))
    output = dct(input)

    solution = np.zeros((16))
    solution[0] = 4

    assert np.allclose(solution, output)
