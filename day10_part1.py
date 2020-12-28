# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=10; PART=1

import aoc
import numpy

@aoc.puzzle_timer()
def solve(input):
    adaptors = [0]
    adaptors = adaptors + [int(line.strip()) for line in input.splitlines()]
    adaptors.sort()
    diffs_array = numpy.diff(adaptors)
    diffs = diffs_array.tolist()
    return diffs.count(1) * (diffs.count(3) + 1)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))