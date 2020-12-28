# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=7; PART=1

from utils import aoc
from functools import lru_cache
import re

bags = {}

@lru_cache(600)
def has_shiny_gold(colour):
    if colour == "shiny gold": 
        return True
    else:
        return any(has_shiny_gold(c) for _, c in bags[colour] )

@aoc.puzzle_timer()
def solve(input):
    bag_count = 0

    for line in input.splitlines():
        colour = re.match(r"(.+?) bags contain", line)[1]  
        bags[colour] = re.findall(r"(\d+?) (.+?) bags?", line)

    for bag in bags:
        if has_shiny_gold(bag):
            bag_count += 1

    return bag_count - 1

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))