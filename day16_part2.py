# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=16; PART=2

from os import replace
import math
import copy

import aoc

criteria = {}
our_ticket = []
nearby_tickets = []

def parse_input(input):
    global our_ticket
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

def field_not_allocated(field_possibilities):
    for fields in field_possibilities.values():
        if len(fields):
            return True
    return False


@aoc.puzzle_timer()
def solve(input, qualifier):
    parse_input(input)
    
    valid_nums = set()
    for rule_nums in criteria.values():
        valid_nums.update(rule_nums)
    
    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid = True
        for num in ticket:
            if not (num in valid_nums):
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)
    valid_tickets.append(our_ticket)

    field_possibilities = {}
    for i in range(len(our_ticket)):
        field_possibilities[i]=[]
        field_val_all_tickets = [ticket[i] for ticket in valid_tickets]
        for field_name, field_rule in criteria.items():
            rule_vals_set = set(field_rule)
            ticket_vals_set = set(field_val_all_tickets)
            t = ticket_vals_set.intersection(rule_vals_set)
            if len(ticket_vals_set) == len(ticket_vals_set.intersection(rule_vals_set)):
                field_possibilities[i].append(field_name)

    our_full_ticket={}
    field_name = ''
    while field_not_allocated(field_possibilities):
        for index, fields in field_possibilities.items():
            if len(fields) == 1:
                field_name = fields[0]
                our_full_ticket[field_name]=our_ticket[index]
                break
        for index in field_possibilities.keys():
            if field_name in field_possibilities[index]:
                field_possibilities[index].remove(field_name)

    answer_vals = []
    for field_name, field_value in our_full_ticket.items():
        if field_name.startswith(qualifier):
            answer_vals.append(field_value)

    return math.prod(answer_vals)
    

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input, 'departure'))