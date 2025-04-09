
from percent import calculate_percentage

import unittest

# Перевірка на правильність роботи функції в різних ситуаціях
class TestCalculatePercentage(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(calculate_percentage(100, 0), 0)

    def test_full(self):
        self.assertEqual(calculate_percentage(100, 100), 100)

    def test_float_input(self):
        self.assertAlmostEqual(calculate_percentage(123.45, 15.5), 19.13475)


if __name__ == '__main__':
    unittest.main()


