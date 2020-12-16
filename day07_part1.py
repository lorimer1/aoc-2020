# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=7; PART=1

from aoc_utils import aoc_read_input, aoc_timer
from functools import lru_cache

bags = {}

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
    return bags

@lru_cache(maxsize=600)
def is_suitable_bag(test_bag, our_bag):
    test_bag_children = bags[test_bag]
    if not test_bag_children:
        return False
    if our_bag in test_bag_children.keys():
        return True
    for child_bag in test_bag_children.keys():
        return is_suitable_bag(child_bag, our_bag)

@aoc_timer()
def solve(input):
    make_bags_collection(input)
    count = 0
    for bag in bags.keys():
        count += 1 if is_suitable_bag(bag, 'shiny gold') else 0
    return count

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))