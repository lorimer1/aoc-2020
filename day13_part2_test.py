#replace 'template' with 'dayn'
import unittest
from aoc_utils import aoc_read_input
from day13_part2 import YEAR, DAY, solve

class aoc_test(unittest.TestCase):

    def test(self):
        test_input = aoc_read_input(YEAR, DAY, extra='_test')
        self.assertEqual(solve(test_input), 1068781)

    def test1(self):
        test_input = '4444\n67,7,59,61'
        self.assertEqual(solve(test_input), 754018)

    def test2(self):
        test_input = '4444\n67,x,7,59,61'
        self.assertEqual(solve(test_input), 779210)

    def test3(self):
        test_input = '4444\n67,7,x,59,61'
        self.assertEqual(solve(test_input), 1261476)

    def test4(self):
        test_input = '4444\n1789,37,47,1889'
        self.assertEqual(solve(test_input), 1202161486)

if __name__ == '__main__':
    unittest.main()