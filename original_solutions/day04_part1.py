# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=4; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

def is_valid(passport):
    if 'byr' not in passport: return False
    if 'iyr' not in passport: return False
    if 'eyr' not in passport: return False
    if 'hgt' not in passport: return False
    if 'hcl' not in passport: return False
    if 'ecl' not in passport: return False
    if 'pid' not in passport: return False
    # if 'cid' not in passport: return False
    return True


@aoc.puzzle_timer()
def solve(input):
    count = 0
    passport = {}
    lines = input.splitlines()
    for line in lines:
        if len(line)==0:
            if is_valid(passport):
                count+=1 
            passport = {}
            continue
        fields = line.split(' ')
        for field in fields:
            key, val = field.split(':')
            passport[key] = val
    if is_valid(passport): #last passport has no blank line following it
        count+=1 
    return count


if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))