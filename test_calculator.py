# https://github.com/eperez0823/lab11-EP-CW
# Partner 1: Christopher Wilches
# Partner 2: Esteban Perez

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 5), -5)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 2), 0.5)
        self.assertAlmostEqual(div(-2, 10), -5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)


    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(9), 3)

        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
