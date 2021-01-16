# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=9; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from collections import deque
from itertools import combinations, count 

def solve_part1(input, preamble):
    nums = list(map(int,input.splitlines()))
    q = deque(maxlen = preamble)
    for i, num in enumerate(nums):
        if i < preamble:
            q.append(num) 
        else:
            if len([pair for pair in combinations(q, 2) if sum(pair) == num and pair[0]!=pair[1]]):
                q.append(num)
            else: 
                return num

@aoc.puzzle_timer()
def solve(input, preamble):
    target = solve_part1(input, preamble) 
    nums = list(map(int,input.splitlines()))
    for start, _ in enumerate(nums):
        for stop in count(start+1):
            val = sum(nums[start:stop])
            if val > target:
                break
            if val == target:
                return min(nums[start:stop]) + max(nums[start:stop])

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input,preamble=25))