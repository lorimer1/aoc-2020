# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=5; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    table  = str.maketrans('BFRL', '1010')
    seats  = input.translate(table).splitlines()
    ids    = tuple(map(lambda s: int(s, 2), seats))
    missing_seats= [s for s in range(min(ids), max(ids)+1) if s not in ids] 
    return missing_seats[0]

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))