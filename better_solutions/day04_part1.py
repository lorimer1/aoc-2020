# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=4; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):

    passports = input.split('\n\n')
    required_fields = 'byr', 'iyr', 'eyr', 'pid', 'hcl', 'ecl', 'hgt'
    valid_count = 0

    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))