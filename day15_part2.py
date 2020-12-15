# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=15; PART=2

from aoc_utils import aoc_read_input, aoc_timer

@aoc_timer()
def solve(input):
    spoken = list(map(int,input.split(',')))
    latest = spoken[-1]
    positions = {k:v+1 for v, k in enumerate(spoken[:-1])}
    for turn in range(len(spoken),30000000):
        new_num = 0
        if latest in positions:
            new_num = turn - positions[latest]
        positions[latest] = turn
        latest = new_num
    return latest

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))