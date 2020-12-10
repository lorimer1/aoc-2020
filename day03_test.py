#replace 'template' with 'dayn'
import unittest
from aoc_utils import aoc_read_input
from day03 import YEAR, DAY, parse_input, part1, part2

class aoc_test(unittest.TestCase):

    def test_part1_test1(self):
        puzzle_input = aoc_read_input(YEAR, DAY, extra='_part1_test1')
        test_input = parse_input(puzzle_input)
        self.assertEqual(part1(test_input), 7)

    def test_part2_test1(self):
        puzzle_input = aoc_read_input(YEAR, DAY, extra='_part2_test1')
        test_input = parse_input(puzzle_input)
        self.assertEqual(part2(test_input), 336)

if __name__ == '__main__':
    unittest.main()