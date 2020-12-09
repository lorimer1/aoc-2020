# Advent of code
# Author = Rob Lorimer
YEAR = 2020
DAY = 1

from aoc_utils import aoc_read_input, aoc_timer

@aoc_timer()
def parse_input(input):
    return input

@aoc_timer(YEAR, DAY, 1)
def part1(input):
    return "todo"

@aoc_timer(YEAR, DAY, 2)
def part2(input):
    return "todo"

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    input = parse_input(puzzle_input)
    part1(input)
    part2(input)