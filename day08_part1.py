# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=8; PART=1

from utils import aoc


@aoc.puzzle_timer()
def solve(input):
    prog = [(line.split()[0],int(line.split()[1])) for line in input.splitlines()]
    iptr,acc=0,0
    visited=[]
    while not (iptr in visited):
        visited.append(iptr)
        opcode,operand=prog[iptr]
        if opcode=='nop':
            iptr+=1
        elif opcode=='acc':
            acc+=operand
            iptr+=1
        elif opcode=='jmp':
            iptr+=operand
    return acc

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))