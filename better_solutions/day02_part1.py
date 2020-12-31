# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=2; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

import re

@aoc.puzzle_timer()
def solve(input):

    re_policy = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    policies = re_policy.findall(input)

    valid_count = 0

    for min_rep, max_rep, letter, password in policies:
        if int(min_rep) <= password.count(letter) <= int(max_rep):
            valid_count += 1

    return valid_count

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))
