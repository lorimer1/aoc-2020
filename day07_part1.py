# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=7; PART=1

from aoc_utils import aoc_read_input, aoc_timer
from functools import lru_cache

bags = {}
bags_outer={}

def make_bags_collection(input):
    input = input.replace(' bags', '').replace(' bag', '').replace(' contain ','|').replace('.','').replace(', ',',').splitlines()
    for line in input:
        parent_txt, children_txt = line.split('|')
        children = children_txt.split(',')
        child_bags = {}
        for child in children:
            if child == 'no other':
                break
            else:
                parts = child.split(' ',1) 
                child_bags[parts[1]] = int(parts[0]) #[1]=bag, [0]=quantity
        bags[parent_txt] = child_bags
        bags_outer[parent_txt]=False
    return bags

@lru_cache(maxsize=600)
def is_suitable_bag(test_bag, our_bag):
    test_bag_children = bags[test_bag]
    if not test_bag_children:
        return False
    if our_bag in test_bag_children.keys():
        bags_outer[test_bag]=True
        return True
    for child_bag in test_bag_children.keys():
        if is_suitable_bag(child_bag, our_bag):
            bags_outer[child_bag]=True
            return True
        return False

@aoc_timer()
def solve(input):
    make_bags_collection(input)
    l = len(bags)
    count = 0
    for bag in bags.keys():
        if bag == 'shiny gold':
            continue
        if is_suitable_bag(bag, 'shiny gold'):
            count += 1 
    return count

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))