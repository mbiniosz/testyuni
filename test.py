import unittest
from calculator import calculate
from calculator import str_calculator

class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate (1,2, '+')
        self.assertEqual(r,3)

    def test_odejmowanie(self):
        r = calculate (1,2, '-')
        self.assertEqual(r, -1)

    def test_mnozenia(self):
        r = calculate (3,8, '*')
        self.assertEqual(r,24)

class TestStringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator("a", "b", 'concat')
        self.assertEqual(r,'ab')
