# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=18; PART=2

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    return "todo"

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))