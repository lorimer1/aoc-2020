# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=6; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    group_set = set()
    count = 0
    lines = input.splitlines()
    for line in lines:
        if len(line)==0: # end of group
            count += len(group_set)
            group_set = set()
            continue
        for c in line: # group results
            group_set.add(c)
    return count + len(group_set) #edge case ... last group with no blank line following

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))