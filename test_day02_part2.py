#replace 'template' with 'dayn'
import unittest
from utils import aoc
from day02_part2 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test(self):
        test_input = aoc.puzzle_input(YEAR, DAY, is_test=True)
        self.assertEqual(solve(test_input), 1)

if __name__ == '__main__':
    unittest.main()