# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=8; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
import re


@aoc.puzzle_timer()
def solve(input):
    re_statement = re.compile( r'(\w+) ([\+\-\d]+)' )
    prog = re_statement.findall(input)
    iptr, acc = 0, 0
    visited = set()

    while not (iptr in visited):
        visited.add(iptr)
        opcode, operand = prog[iptr]
        if opcode=='nop':
            iptr+=1
        elif opcode=='acc':
            acc += int(operand)
            iptr+=1
        elif opcode=='jmp':
            iptr += int(operand)
    
    return acc

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))