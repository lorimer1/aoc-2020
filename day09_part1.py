# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=9; PART=1

from collections import deque
from itertools import combinations 
from aoc_utils import aoc_read_input, aoc_timer

@aoc_timer()
def solve(input, preamble):
    nums = list(map(int,input.splitlines()))
    q = deque(maxlen = preamble)
    for i,num in enumerate(nums):
        if i < preamble:
            q.append(num) 
        else:
            if len([pair for pair in combinations(q, 2) if sum(pair) == num]):
                q.append(num)
            else: 
                return num

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input, preamble=25))