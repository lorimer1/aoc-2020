# Advent of code
# Author = Rob Lorimer
YEAR = 2020
DAY = 1

from aoc_utils import aoc_read_input, aoc_timer
from itertools import combinations 

@aoc_timer()
def parse_input(input):
    return list(map(int, input.splitlines()))

@aoc_timer(YEAR, DAY, 1)
def part1(input):
    matching_pair = [pair for pair in combinations(input, 2) if sum(pair) == 2020]
    answer = [x * y for x, y in matching_pair]
    return answer[0]

@aoc_timer(YEAR, DAY, 2)
def part2(input):
    matching_entries = [entries for entries in combinations(input, 3) if sum(entries) == 2020]
    answer = [x * y * z for x, y, z in matching_entries]
    return answer[0]

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    input = parse_input(puzzle_input)
    part1(input)
    part2(input)