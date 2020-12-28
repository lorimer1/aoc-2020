# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=12; PART=2

import aoc

N=0; E=1; S=2; W=3
DIRS = ['N','E','S','W']

def get_new_pos(position, dir, degrees):
    steps = degrees//90
    rel_steps = steps % 4
    if rel_steps == 0: 
        return position
    elif rel_steps == 2:
        temp = position['N']
        position['N'] = -1 * position['N']
        position['E'] = -1 * position['E']   
        return position     
    temp = position['N']
    position['N'] = position['E']
    position['E'] = temp   
    if rel_steps == 1:
        if dir == 'L':
            position['E'] = -1 * position['E']
        else:
            position['N'] = -1 * position['N']
        return position
    # 3 steps
    if dir == 'L':
        position['N'] = -1 * position['N']
    else:
        position['E'] = -1 * position['E']
    return position

@aoc.puzzle_timer()
def solve(input):
    way_rel_pos = {'N':1, 'E':10}
    ship_pos = {'N':0, 'E':0}
    instructions = input.splitlines()
    for instruction in instructions:
        dir = instruction[0]
        step = int(instruction[1:])
        if dir == 'F':
            ship_pos['N']  = ship_pos['N'] + step * way_rel_pos['N']
            ship_pos['E']  = ship_pos['E'] + step * way_rel_pos['E']
        elif dir == 'N':
            way_rel_pos['N']  = way_rel_pos['N'] + step
        elif dir == 'E':
            way_rel_pos['E']  = way_rel_pos['E'] + step
        elif dir == 'S':
            way_rel_pos['N']  = way_rel_pos['N'] - step
        elif dir == 'W':
            way_rel_pos['E']  = way_rel_pos['E'] - step
        elif dir == 'L' or 'R':
             way_rel_pos = get_new_pos(way_rel_pos, dir, step)
    return abs(ship_pos['N']) + abs(ship_pos['E'])

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))