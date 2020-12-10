# Advent of code
# Author = Rob Lorimer
YEAR = 2020
DAY = 3

from typing import NamedTuple
from aoc_utils import aoc_read_input, aoc_timer

class Point(NamedTuple):
    x: int
    y: int
    
# global vars for input size
width = 0; height = 0

# convert input into a list of tree coordinates e.g. [(2,0),(3,0),...]
@aoc_timer()
def parse_input(input):
    global width; global height
    lines = list(input.splitlines())
    width = len(lines[0]); height = len(lines)
    tree_coordinates = [Point(x, y) for y in range(height) for x in range(width) if lines[y][x] == '#']  # co-ordinates of all trees
    return tree_coordinates 

# recursively count trees encountered for a given slope
def tree_counter(tree_locations, location=Point(0,0), tree_count=0, slope=None):
    global width; global height
    tree_count = tree_count + 1 if location in tree_locations else tree_count # count a tree if location is found in tree_locations
    new_location = Point((location.x + slope.x) % width, location.y + slope.y) # use modulus to account for repeating horizontal pattern
    return tree_counter(tree_locations, new_location, tree_count, slope) if new_location.y < height else tree_count # continue recursion until the bottom is reached

@aoc_timer(YEAR, DAY, 1)
def part1(input): 
    return tree_counter(tree_locations=input, slope=Point(3,1))

@aoc_timer(YEAR, DAY, 2)
def part2(input): 
    return tree_counter(tree_locations=input, slope=Point(1,1)) \
        * tree_counter(tree_locations=input, slope=Point(3,1)) \
        * tree_counter(tree_locations=input, slope=Point(5,1)) \
        * tree_counter(tree_locations=input, slope=Point(7,1)) \
        * tree_counter(tree_locations=input, slope=Point(1,2))

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    input = parse_input(puzzle_input)
    part1(input)
    part2(input)