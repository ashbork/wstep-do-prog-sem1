from numpy import array, array_equal
import unittest
from scipy.linalg.decomp_lu import lu_factor
from scipy.linalg.misc import LinAlgWarning


def factor(matrix):
    lu, _ = lu_factor(matrix)  # type: ignore
    return lu


class LUTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_matrix(self):
        arr = array([[1, 2], [1, 0]])
        self.assertTrue(array_equal(factor(arr), array(
            [[1., 2.], [1., -2.]])))

    def test_another_matrix(self):
        """
        Testing a small, 2x2 matrix
        """
        arr = array([[1, 2], [2, 0]])
        self.assertTrue(array_equal(factor(arr), array([[2., 0.], [0.5, 2.]])))

    def test_zero_array(self):
        """
        Testing a matrix of zeroes
        """
        arr = array([[0, 0], [0, 0]])
        with self.assertWarns(LinAlgWarning):
            factor(arr)

    def test_nonsquare_array(self):
        """
        Checking if a bad input value raises an error
        """
        with self.assertRaises(ValueError):
            factor(array([[1, 2, 3], [1, 2, 3]]))

    def test_bad_type(self):
        """
        Checking if a bad input type raises an error
        """
        with self.assertRaises(ValueError):
            factor("test")


if __name__ == '__main__':
    unittest.main()
