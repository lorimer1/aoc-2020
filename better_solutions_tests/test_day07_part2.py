#replace 'template' with 'dayn'
import unittest
# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from original_solutions.day07_part2 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test(self):
        test_input = aoc.puzzle_input(YEAR, DAY, is_test=True)
        self.assertEqual(solve(test_input), 32)

if __name__ == '__main__':
    unittest.main()