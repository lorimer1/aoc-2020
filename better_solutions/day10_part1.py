# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=10; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    jolts_sequence = [0] + sorted(map(int,input.splitlines())) # [0] is charging outlet
    jolts_diffs = [j-i for i, j in zip(jolts_sequence[:-1], jolts_sequence[1:])]
    return jolts_diffs.count(1) * (jolts_diffs.count(3) + 1) # '+ 1' to include our device


if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))