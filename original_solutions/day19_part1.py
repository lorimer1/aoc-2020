# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=19; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    return "todo"

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))