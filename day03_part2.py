# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=3; PART=2

from typing import NamedTuple
from aoc_utils import aoc_read_input, aoc_timer

class Point(NamedTuple):
    x: int
    y: int
    
# global vars for input size
width = 0; height = 0

# recursively count trees encountered for a given slope
def tree_counter(tree_locations, location=Point(0,0), tree_count=0, slope=None):
    global width; global height
    tree_count = tree_count + 1 if location in tree_locations else tree_count # count a tree if location is found in tree_locations
    new_location = Point((location.x + slope.x) % width, location.y + slope.y) # use modulus to account for repeating horizontal pattern
    return tree_counter(tree_locations, new_location, tree_count, slope) if new_location.y < height else tree_count # continue recursion until the bottom is reached

@aoc_timer()
def solve(input): 
    global width; global height
    lines = list(input.splitlines())
    width = len(lines[0]); height = len(lines)
    tree_locations = [Point(x, y) for y in range(height) for x in range(width) if lines[y][x] == '#']  # co-ordinates of all trees
    return tree_counter(tree_locations, slope=Point(1,1)) \
        * tree_counter(tree_locations, slope=Point(3,1)) \
        * tree_counter(tree_locations, slope=Point(5,1)) \
        * tree_counter(tree_locations, slope=Point(7,1)) \
        * tree_counter(tree_locations, slope=Point(1,2))

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))