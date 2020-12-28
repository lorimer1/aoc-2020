# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=2; PART=2

from typing import NamedTuple
from utils import aoc

class Password_Record(NamedTuple):
    min: int
    max: int
    letter: str
    password: str

@aoc.puzzle_timer()
def solve(input):
    lines = input.splitlines()
    records = []
    for line in lines:
        repetition_policy, letter, password = line.split()
        repetition_min, repetition_max = repetition_policy.split('-')
        record = Password_Record(min=int(repetition_min), max=int(repetition_max), letter=letter[:-1], password=password)
        records.append(record)
    compliant_records = [record for record in records if  bool(record.password[record.min-1] == record.letter) != bool(record.password[record.max-1] == record.letter)]
    return len(compliant_records)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))