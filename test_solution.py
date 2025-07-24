import unittest
from solution import Solution

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_coins(self):
        self.assertEqual(self.solution.change(5, []), 0)

    def test_zero_amount(self):
        self.assertEqual(self.solution.change(0, [1, 2, 5]), 1)

    def test_single_coin(self):
        self.assertEqual(self.solution.change(5, [5]), 1)
        self.assertEqual(self.solution.change(3, [2]), 0)

    def test_multiple_coins(self):
        self.assertEqual(self.solution.change(5, [1, 2, 5]), 4)  
        self.assertEqual(self.solution.change(3, [2, 1]), 2)      

    def test_large_amount(self):
        self.assertEqual(self.solution.change(100, [1, 2, 5, 10, 20, 50]), 4562)

    def test_duplicate_coins(self):
        self.assertEqual(self.solution.change(5, [1, 1, 1, 1, 1]), 6) 

    def test_no_solution(self):
        self.assertEqual(self.solution.change(3, [2, 4]), 0)

if __name__ == '__main__':
    unittest.main()
