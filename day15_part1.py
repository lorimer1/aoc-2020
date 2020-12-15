# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=15; PART=1

from aoc_utils import aoc_read_input, aoc_timer

@aoc_timer()
def solve(input):
    spoken = list(map(int,input.split(',')))
    latest = spoken[-1]
    spoken = list(reversed(spoken[:-1]))
    for turn in range(len(spoken)+1,2020):
        new_num = 0
        if latest in spoken:
            new_num = spoken.index(latest) + 1
        spoken.insert(0,latest)
        latest = new_num
    return latest

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))