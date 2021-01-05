# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=4; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

def check_height(v):
	if v.endswith('cm'):
		return 150 <= int(v[:-2]) <= 193
	if v.endswith('in'):
		return 59 <= int(v[:-2]) <= 76
	return False

@aoc.puzzle_timer()
def solve(input):

    checks = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'pid': lambda v: len(v) == 9 and all(c.isdigit() for c in v),
        'hcl': lambda v: len(v) == 7 and all(c.isdigit() or c in 'abcdef' for c in v[1:]),
        'ecl': lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'cid': lambda v: True,
        'hgt': check_height
    }

    passports = input.split('\n\n')
    required_fields = 'byr', 'iyr', 'eyr', 'pid', 'hcl', 'ecl', 'hgt'
    valid_count = 0

    for potential_passport in passports:

        if all(required_field in potential_passport for required_field in required_fields):

            passport = {pair[0]:pair[1] for field in potential_passport.split() for pair in field.split(':') }
            
            passport = (field.split(':') for field in potential_passport.split())

            if all(checks[k](v) for k,v in passport):
                valid_count += 1

    return valid_count

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))