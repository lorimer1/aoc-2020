# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=13; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    arrival, timetable = input.splitlines()
    bus_t_offset = {int(k):i for i,k in enumerate(timetable.split(',')) if k != 'x'}
    t, step = 0, 1
    for bus, offset in bus_t_offset.items():
        while (t+offset) % bus!=0:
            t+=step
        step *= bus
    return t

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))