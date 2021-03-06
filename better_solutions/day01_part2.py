# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=1; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from itertools import combinations 

@aoc.puzzle_timer()
def solve(puzzle_input):
    numbers = tuple(map(int, puzzle_input.splitlines()))
    matches = [x*y*z for (x,y,z) in combinations(numbers, 3) if x+y+z == 2020]
    return matches[0] # there will be only one match in the resulting matches collection 

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))