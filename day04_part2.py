# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=4; PART=2

from utils import aoc
import re

def is_valid(passport):
    if 'byr' not in passport: return False
    if not re.match('^\d{4}$', passport['byr']): return False
    byr = int(passport['byr'])
    if not (1920 <= byr <= 2002): return False

    if 'iyr' not in passport: return False
    if not re.match('^\d{4}$', passport['iyr']): return False
    iyr = int(passport['iyr'])
    if not (2010 <= iyr <= 2020): return False
    
    if 'eyr' not in passport: return False
    if not re.match('^\d{4}$', passport['eyr']): return False
    eyr = int(passport['eyr'])
    if not (2020 <= eyr <= 2030): return False
    
    if 'hgt' not in passport: return False
    matches = re.search('^(?P<value>\d+)(?P<unit>in|cm)$', passport['hgt'])
    if not matches: return False
    unit = matches.group('unit')
    value = int(matches.group('value'))
    if unit=='in' and not (59 <= value <= 76): return False
    if unit=='cm' and not (150 <= value <= 193): return False    

    if 'hcl' not in passport: return False
    if not re.match('^#[0-9a-f]{6}$', passport['hcl']): return False

    if 'ecl' not in passport: return False
    if not re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']): return False

    if 'pid' not in passport: return False
    if not re.match('^[0-9]{9}$', passport['pid']): return False
    
    # if 'cid' not in passport: return False
    return True

@aoc.puzzle_timer()
def solve(input):
    count = 0
    passport = {}
    lines = input.splitlines()
    line_num=0
    for line in lines:
        line_num += 1
        if len(line)==0:
            if is_valid(passport):
                count+=1
            passport = {}
        else:
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