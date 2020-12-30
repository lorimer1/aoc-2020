# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=1; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from utils import aoc
from itertools import combinations 

@aoc.puzzle_timer()
def solve(puzzle_input):
    input = list(map(int, puzzle_input.splitlines()))
    matching_pair = [pair for pair in combinations(input, 2) if sum(pair) == 2020]
    answer = [x * y for x, y in matching_pair]
    return answer[0]

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))
