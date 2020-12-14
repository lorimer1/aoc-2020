# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=14; PART=2

from aoc_utils import aoc_read_input, aoc_timer
import re

def get_addresses(pattern, addresses):
    if 'X' not in pattern:
        return addresses
    new_addresses = []
    for address in addresses:
        new_addresses.append(address.replace('X', '1', 1))
        new_addresses.append(address.replace('X', '0', 1))
    return get_addresses(pattern.replace('X', '0', 1),new_addresses)

def mask_vals(address, mask):
    address_binary = bin(address).replace('0b','').zfill(len(mask))
    address_masked = ''
    for i in range(len(address_binary)):
        if mask[i] == '0':
            address_masked = address_masked + address_binary[i]
        else:
            address_masked = address_masked + mask[i]
    address_masked_as_list = []
    address_masked_as_list.append(address_masked)
    addresses_binary = get_addresses(address_masked, address_masked_as_list)
    addresses = []
    for address_binary in addresses_binary:
        addresses.append(int(address_binary, 2))
    return addresses

@aoc_timer()
def solve(input):
    mask = ''
    program = {}
    lines = input.splitlines()
    for line in lines:
        left_of_equal, right_of_equal = line.split(' = ')
        if left_of_equal == 'mask':
            mask = right_of_equal
            continue
        matches = re.search('^mem\[(?P<mem_val>\d+)\]$', left_of_equal) #extract mem address as mem_val
        address_from_input = int(matches.group('mem_val'))
        value_from_input = int(right_of_equal)
        addresses = mask_vals(address_from_input, mask)
        for address in addresses:
            program[address] = value_from_input

    return sum( program.values() )

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))