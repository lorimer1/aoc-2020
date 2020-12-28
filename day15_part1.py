# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=15; PART=1

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    starting_nums = list(map(int,input.split(',')))
    latest = starting_nums[-1]
    spoken = list(reversed(starting_nums[:-1]))
    for turn in range(len(spoken)+1,2020):
        new_num = 0
        if latest in spoken:
            new_num = spoken.index(latest) + 1
        spoken.insert(0,latest)
        latest = new_num
    return latest

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))