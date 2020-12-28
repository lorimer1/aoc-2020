# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=16; PART=1

from os import replace
import aoc

criteria = {}
our_ticket = []
nearby_tickets = []

def parse_input(input):
    step = 'parse criteria'
    
    for line in input.splitlines():
        
        if not line:
            continue
        elif line=='your ticket:':
            step='parse our ticket'
            continue
        elif line=='nearby tickets:':
            step='parse nearby tickets'
            continue
        
        if step=='parse criteria':
            rule_text = line.replace(': ','|').replace(' or ',',')
            rule_name, rule_ranges_text = rule_text.split('|')
            rule_ranges = rule_ranges_text.split(',')
            rule_nums = []
            for rule_range in rule_ranges:
                low, high = rule_range.split('-')
                for num in range(int(low),int(high)+1):
                    rule_nums.append(int(num))
            criteria[rule_name] = rule_nums

        if step=='parse our ticket':
            our_ticket = list(map(int,(line.split(','))))

        if step=='parse nearby tickets':
            nearby_tickets.append( list(map(int,line.split(','))) )   

@aoc.puzzle_timer()
def solve(input):
    parse_input(input)
    
    valid_nums = set()
    for rule_nums in criteria.values():
        valid_nums.update(rule_nums)
    
    answer = 0
    for ticket in nearby_tickets:
        for num in ticket:
            if not num in valid_nums:
                answer += num

    return answer

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))