# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=6; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    groups_text = input.split('\n\n')
    groups = tuple(map(lambda g: tuple(map(set, g.splitlines())), groups_text))
    return sum(len(set.union(*g)) for g in groups)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))