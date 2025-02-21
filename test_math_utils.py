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