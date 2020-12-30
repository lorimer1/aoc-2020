# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=10; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
import numpy

@aoc.puzzle_timer()
def solve(input):
    adaptors = [int(line.strip()) for line in input.splitlines()]
    adaptors.sort()
    last_adaptor = max(adaptors)
    index = [1] + [0] * last_adaptor + [0, 0]
    for adaptor in adaptors:
        index[adaptor] = index[adaptor-1] + index[adaptor-2] + index[adaptor-3]
        if adaptor == last_adaptor:
            return index[adaptor]

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))