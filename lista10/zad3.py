from scipy.linalg import lu_factor
import numpy as np
import unittest


def lu(matrix):
    _, pivot = lu_factor(matrix)
    return pivot


class LUTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_big_matrix(self):
        """
        Testing a large, 4x4 matrix
        """
        arr = np.array([[2, 5, 8, 7], [5, 2, 2, 8],
                       [7, 5, 6, 6], [5, 4, 4, 8]])
        self.assertTrue(np.array_equal(lu(arr), np.array([2, 2, 3, 3])))

    def test_small_matrix(self):
        """
        Testing a small, 2x2 matrix
        """
        arr = np.array([[1, 2], [2, 0]])
        self.assertTrue(np.array_equal(lu(arr), np.array([1, 1])))

    def test_zero_array(self):
        """
        Testing a matrix of zeroes
        """
        arr = np.array([[0, 0], [0, 0]])
        self.assertTrue(np.array_equal(lu(arr), np.array([0, 1])))

    def test_nonsquare_array(self):
        """
        Checking if a bad input value raises an error
        """
        with self.assertRaises(ValueError):
            lu(np.array([[1, 2, 3], [1, 2, 3]]))

    def test_bad_type(self):
        """
        Checking if a bad input type raises an error
        """
        with self.assertRaises(ValueError):
            lu("test")


if __name__ == '__main__':
    unittest.main()
