# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=14; PART=1

import aoc
import re

def mask_val( val, mask ):
    binary = bin(val).replace('0b','').zfill(len(mask))
    masked = ''
    for i in range(len(binary)):
        if mask[i] == 'X':
            masked = masked + binary[i]
        else:
            masked = masked + mask[i]
    val = int(masked, 2)
    return val

@aoc.puzzle_timer()
def solve(input):
    mask = ''
    program = {}
    lines = input.splitlines()
    for line in lines:
        left, right = line.split(' = ')
        if left == 'mask':
            mask = right
            continue
        matches = re.search('^mem\[(?P<index>\d+)\]$', left)
        index = int(matches.group('index'))
        value = int(right)
        program[index] = mask_val(value, mask)

    return sum( program.values() )

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))