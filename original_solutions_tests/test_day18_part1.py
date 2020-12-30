#replace 'template' with 'dayn'
import unittest
# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from original_solutions.day18_part1 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test1(self):
        test_input = '2 * 3 + (4 * 5)'
        self.assertEqual(solve(test_input), 26)

    def test2(self):
        test_input = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
        self.assertEqual(solve(test_input), 437)

    def test3(self):
        test_input = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
        self.assertEqual(solve(test_input), 12240)

    def test4(self):
        test_input = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        self.assertEqual(solve(test_input), 13632)

if __name__ == '__main__':
    unittest.main()