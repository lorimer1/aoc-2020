# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=12; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

N=0; E=1; S=2; W=3
DIRS = ['N','E','S','W']

def get_new_dir(current_dir, dir, degrees):
    steps = degrees//90
    index = DIRS.index(current_dir)
    if dir == 'R':
        new_index = (index + steps) % 4
    else:
        new_index = abs((index - steps) % 4)
    return DIRS[new_index]

@aoc.puzzle_timer()
def solve(input):
    units = {'N':0, 'E':0, 'S':0, 'W':0}
    current_dir = DIRS[E]
    instructions = input.splitlines()
    for instruction in instructions:
        dir = instruction[0]
        step = int(instruction[1:])
        if dir == 'F':
            units[current_dir]  = units[current_dir] + step
        elif dir == 'N':
            units['N']  = units['N'] + step
        elif dir == 'E':
            units['E']  = units['E'] + step
        elif dir == 'S':
            units['S']  = units['S'] + step
        elif dir == 'W':
            units['W']  = units['W'] + step
        elif dir == 'L' or 'R':
            current_dir = get_new_dir(current_dir, dir, step)
    return abs(units['N']-units['S']) + abs(units['E']-units['W'])

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))