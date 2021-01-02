# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=3; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

from itertools import count

@aoc.puzzle_timer()
def solve(input):
    grid = tuple(input.splitlines())
    height, width = len(grid), len(grid[0])

    trees = 0

    for row, col in zip(range(height), count(0, 3)):
        if grid[row][col % width] == '#':
            trees += 1

    return trees

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))