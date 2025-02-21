import unittest
from math_utils import MathUtils
class TestMathUtils(unittest.TestCase):
    """
    """
    def test_add(self):
        """
        """
        self.assertEqual(MathUtils.add(1, 2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        """
        """
        self.assertEqual(MathUtils.subtract(2, 1), 1)
        self.assertEqual(MathUtils.subtract(4, 2), 2.0)
        self.assertEqual(MathUtils.subtract(1, 1), 0)
        self.assertEqual(MathUtils.subtract(7, 3), 4.0)

    def test_divide(self):
        """
        """
        self.assertEqual(MathUtils.divide(2, 1), 2)
        self.assertEqual(MathUtils.divide(4, 2), 2.0)
        self.assertEqual(MathUtils.divide(10, 2), 5)
        self.assertEqual(MathUtils.divide(9, 3), 3.0)

    def test_multiply(self):
        """
        """
        self.assertEqual(MathUtils.multiply(2, 1), 2)
        self.assertEqual(MathUtils.multiply(4, 2), 8.0)
        self.assertEqual(MathUtils.multiply(10, 2), 20)
        self.assertEqual(MathUtils.multiply(9, 3), 27.0)

    def test_exponent(self):
        """
        """
        self.assertEqual(MathUtils.exponent(2, 1), 2)
        self.assertEqual(MathUtils.exponent(4, 2), 16.0)
        self.assertEqual(MathUtils.exponent(10, 2), 100)
        self.assertEqual(MathUtils.exponent(9, 3), 729.0)

    def test_mod(self):
        """
        """
        self.assertEqual(MathUtils.mod(2, 1), 0)
        self.assertEqual(MathUtils.mod(4, 2), 0)
        self.assertEqual(MathUtils.mod(10, 3), 1)
        self.assertEqual(MathUtils.mod(16, 3), 1.0)

