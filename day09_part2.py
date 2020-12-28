# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=9; PART=2

import aoc
from collections import deque
from itertools import combinations 

def solve_part1(input, preamble):
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

@aoc.puzzle_timer()
def solve(input, preamble):
    part1 = solve_part1(input, preamble) 
    nums = list(map(int,input.splitlines()))
    for start in range(len(nums)):
        for stop in range(start+1,len(nums)+1):
            val = sum(nums[start:stop])
            if val > part1:
                break
            if val == part1:
                return min(nums[start:stop]) + max(nums[start:stop])

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input,preamble=25))