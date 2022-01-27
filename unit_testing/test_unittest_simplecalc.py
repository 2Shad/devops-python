from simplecalc import SimpleCalc
import unittest

# Class that inherits from TestCase

class CalcTests(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalc()
        print('Setting Up')

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(4, 2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(4, 2)
        expected = 8
        self.assertEqual(actual, expected)

    def test_divide(self):
        actual = self.calc.divide(4, 2)
        expected = 2
        self.assertEqual(actual, expected)    