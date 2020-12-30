# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=15; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    starting_nums = list(map(int,input.split(',')))
    latest_num = starting_nums[-1]
    spoken = {k:v+1 for v, k in enumerate(starting_nums[:-1])}
    for turn in range(len(starting_nums),30000000):
        new_num = 0
        if latest_num in spoken:
            new_num = turn - spoken[latest_num]
        spoken[latest_num] = turn
        latest_num = new_num
    return latest_num

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))