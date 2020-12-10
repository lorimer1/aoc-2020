# Advent of code
# Author = Rob Lorimer
YEAR = 2020
DAY = 2

from typing import NamedTuple
from aoc_utils import aoc_read_input, aoc_timer

class Password_Record(NamedTuple):
    min: int
    max: int
    letter: str
    password: str

@aoc_timer()
def parse_input(input):
    lines = input.splitlines()
    records = []
    for line in lines:
        repetition_policy, letter, password = line.split()
        repetition_min, repetition_max = repetition_policy.split('-')
        record = Password_Record(min=int(repetition_min), max=int(repetition_max), letter=letter[:-1], password=password)
        records.append(record)
    return records


@aoc_timer(YEAR, DAY, 1)
def part1(input):
    compliant_records = [record for record in input if record.min <= record.password.count(record.letter) <= record.max]
    return len(compliant_records)

@aoc_timer(YEAR, DAY, 2)
def part2(input):
    compliant_records = [record for record in input if  bool(record.password[record.min-1] == record.letter) != bool(record.password[record.max-1] == record.letter)]
    return len(compliant_records)

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    input = parse_input(puzzle_input)
    part1(input)
    part2(input)