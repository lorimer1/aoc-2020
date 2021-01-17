# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=10; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
from functools import lru_cache

def arrangements(jolts, i):
	@lru_cache()
	def real_fn(i):
		if i+1 == len(jolts):
			return 1

		tot = 0
		for j in range(i + 1, min(i + 4, len(jolts))):
			if jolts[j] - jolts[i] <= 3:
				tot += real_fn(j)

		return tot

	return real_fn(i)

@aoc.puzzle_timer()
def solve(input):
    adaptors = sorted(map(int,input.splitlines()))
    jolts_sequence = [0] + adaptors + [max(adaptors) + 3]
    return arrangements(jolts_sequence,0)


if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))