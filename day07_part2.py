# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=7; PART=2

import aoc
from functools import lru_cache
import re

bags = {}

@lru_cache(600)
def count_bags(bag_type):
    return 1 + sum(int(number)*count_bags(colour) for number, colour in bags[bag_type])

@aoc.puzzle_timer()
def solve(input):
    bag_count = 0

    for line in input.splitlines():
        colour = re.match(r"(.+?) bags contain", line)[1]  
        bags[colour] = re.findall(r"(\d+?) (.+?) bags?", line)

    return count_bags("shiny gold")-1

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))