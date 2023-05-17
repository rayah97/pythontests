import unittest
from prime_calculator import calculate_nth_prime

class TestPrimeCalculator(unittest.TestCase):
    def test_calculate_nth_prime(self):
        self.assertEqual(calculate_nth_prime(1), 2)
        self.assertEqual(calculate_nth_prime(5), 11)
        self.assertEqual(calculate_nth_prime(10), 29)
        self.assertEqual(calculate_nth_prime(20), 71)

if __name__ == '__main__':
    unittest.main()
