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
        arr = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
        self.assertTrue(np.array_equal(lu(arr), np.array([2, 2, 3, 3])))

    def test_small_matrix(self):
        arr = np.array([[1, 2], [2, 0]])
        self.assertTrue(np.array_equal(lu(arr), np.array([1, 1])))

    def test_zero_array(self):
        arr = np.array([[0, 0], [0, 0]])
        self.self.assertTrue(np.array_equal(lu(arr), np.array([0, 1])))

    def test_zero_array(self):
        arr = np.array([[0, 0], [0, 0]])
        self.assertTrue(np.array_equal(lu(arr), np.array([0, 1])))

    def test_nonsquare_array(self):
        with self.assertRaises(ValueError):
            lu(np.array([[1, 2, 3], [1, 2, 3]]))


if __name__ == '__main__':
    unittest.main()
