#replace 'template' with 'dayn'
import unittest
import aoc
from day19_part1 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test(self):
        test_input = aoc.puzzle_input(YEAR, DAY, is_test=True)
        self.assertEqual(solve(test_input), "todo")

if __name__ == '__main__':
    unittest.main()