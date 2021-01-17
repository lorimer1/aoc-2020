#replace 'template' with 'dayn'
import unittest
# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from better_solutions.day10_part2 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test2(self):
        test_input = aoc.puzzle_input(YEAR, DAY, is_test=True, extra='_2')
        self.assertEqual(solve(test_input), 8)

    def test(self):
        test_input = aoc.puzzle_input(YEAR, DAY, is_test=True)
        self.assertEqual(solve(test_input), 19208)

if __name__ == '__main__':
    unittest.main()