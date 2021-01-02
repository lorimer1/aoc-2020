# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=3; PART=2

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

    total = trees

    for dr, dc in ((1, 1), (1, 5), (1, 7), (2, 1)):
        trees = 0

        for row, col in zip(range(0, height, dr), count(0, dc)):
            if grid[row][col % width] == '#':
                trees += 1

        total *= trees

    return total

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))