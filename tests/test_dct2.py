import pytest
import numpy as np

from dct.dct import dct2


def test_2d():
    input = np.array(
        [
            [231, 32, 233, 161, 24, 71, 140, 245],
            [247, 40, 248, 245, 124, 204, 36, 107],
            [234, 202, 245, 167, 9, 217, 239, 173],
            [193, 190, 100, 167, 43, 180, 8, 70],
            [11, 24, 210, 177, 81, 243, 8, 112],
            [97, 195, 203, 47, 125, 114, 165, 181],
            [193, 70, 174, 167, 41, 30, 127, 245],
            [87, 149, 57, 192, 65, 129, 178, 228],
        ]
    )
    solution = np.array(
        [
            [1.11e03, 4.40e01, 7.59e01, -1.38e02, 3.50e00, 1.22e02, 1.95e02, -1.01e02],
            [7.71e01, 1.14e02, -2.18e01, 4.13e01, 8.77e00, 9.90e01, 1.38e02, 1.09e01],
            [4.48e01, -6.27e01, 1.11e02, -7.63e01, 1.24e02, 9.55e01, -3.98e01, 5.85e01],
            [
                -6.99e01,
                -4.02e01,
                -2.34e01,
                -7.67e01,
                2.66e01,
                -3.68e01,
                6.61e01,
                1.25e02,
            ],
            [
                -1.09e02,
                -4.33e01,
                -5.55e01,
                8.17e00,
                3.02e01,
                -2.86e01,
                2.44e00,
                -9.41e01,
            ],
            [-5.38e00, 5.66e01, 1.73e02, -3.54e01, 3.23e01, 3.34e01, -5.81e01, 1.90e01],
            [
                7.88e01,
                -6.45e01,
                1.18e02,
                -1.50e01,
                -1.37e02,
                -3.06e01,
                -1.05e02,
                3.98e01,
            ],
            [
                1.97e01,
                -7.81e01,
                9.72e-01,
                -7.23e01,
                -2.15e01,
                8.13e01,
                6.37e01,
                5.90e00,
            ],
        ]
    )

    output = dct2(input)

    assert np.allclose(solution, output, rtol=1)


def test_2d_dimensions():
    invalid = [
        np.empty((0)),  # one value
        np.empty((1)),  # one value
        np.empty((2)),  # more than one value
        np.empty((1, 2)),  # not square
        np.empty((0, 2)),  # not square
        np.empty((1, 0)),  # not square
        np.empty((2, 2, 1)),
        np.empty((3, 3, 3)),
    ]

    valid = [
        np.empty((1, 1)),  # one value, multidimension
        np.empty((2, 2)),  # square
    ]

    with pytest.raises(ZeroDivisionError):
        dct2(np.empty((0, 0)))  # zero values

    with pytest.raises(ValueError):
        for x in invalid:
            dct2(x)

    for x in valid:
        try:
            dct2(x)
        except ValueError as e:
            pytest.fail(f"An exception has been raised: {e}")


def test_2d_zeros():
    input = np.zeros((8, 8))
    output = dct2(input)

    assert np.allclose(input, output)


def test_2d_ones():
    input = np.ones((8, 8))
    output = dct2(input)

    solution = np.zeros((8, 8))
    solution[0, 0] = 8

    assert np.allclose(solution, output)
