#replace 'template' with 'dayn'
import unittest
from aoc_utils import aoc_read_input
from day04_part1 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test(self):
        test_input = aoc_read_input(YEAR, DAY, extra='_test')
        self.assertEqual(solve(test_input), 2)

if __name__ == '__main__':
    unittest.main()