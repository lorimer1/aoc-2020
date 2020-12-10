import unittest
from aoc_utils import aoc_read_input
from day01 import YEAR, DAY, parse_input, part1, part2

class aoc_test(unittest.TestCase):

    def test_part1_test1(self):
        puzzle_input = aoc_read_input(YEAR, DAY, extra='_part1_test1')
        test_input = parse_input(puzzle_input)
        self.assertEqual(part1(test_input), 514579)

    def test_part2_test1(self):
        puzzle_input = aoc_read_input(YEAR, DAY, extra='_part2_test1')
        test_input = parse_input(puzzle_input)
        self.assertEqual(part2(test_input), 241861950)

if __name__ == '__main__':
    unittest.main()
