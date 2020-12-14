# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=14; PART=2

from aoc_utils import aoc_read_input, aoc_timer
import re

def get_addresses(pattern, addresses):
    if 'X' not in pattern:
        return addresses
    for address in addresses:
        new_addresses = []
        for address in addresses:
            new_addresses.append(address.replace('X', '1', 1))
            new_addresses.append(address.replace('X', '0', 1))
        return get_addresses(pattern.replace('X', '0', 1),new_addresses)

def mask_vals( val, mask ):
    binary = bin(val).replace('0b','').zfill(len(mask))
    masked = ''
    for i in range(len(binary)):
        if mask[i] == '0':
            masked = masked + binary[i]
        else:
            masked = masked + mask[i]
    addresses = []
    addresses.append(masked)
    binary_addresses = get_addresses(masked, addresses)
    addresses = []
    for binary_address in binary_addresses:
        addresses.append(int(binary_address, 2))
    return addresses

@aoc_timer()
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
        addresses = mask_vals(index, mask)
        for address in addresses:
            program[address] = value

    return sum( program.values() )

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))