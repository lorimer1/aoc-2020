import unittest
from aoc_utils import aoc_read_input
from day01 import YEAR, DAY, part1, part2

class aoc_test(unittest.TestCase):

    def test_part1_test1(self):
        test_input = aoc_read_input(YEAR, DAY, extra='_part1_test1')
        self.assertEqual(part1(test_input), "todo")

    # def test_part1_test1(self):
    #     test_input = aoc_download.read_input_file(YEAR, DAY, extra='_part2_test1')
    #     self.assertEqual(part2(test_input), "todo")

if __name__ == '__main__':
    unittest.main()
