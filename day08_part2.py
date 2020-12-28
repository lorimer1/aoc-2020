# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=8; PART=2

import aoc
import copy

def run(test_prog):
    iptr,acc=0,0
    visited=[]
    terminated=len(test_prog)
    while not (iptr in visited or iptr==terminated):
        visited.append(iptr)
        opcode,operand=test_prog[iptr]
        if opcode=='nop':
            iptr+=1
        elif opcode=='acc':
            acc+=operand
            iptr+=1
        elif opcode=='jmp':
            iptr+=operand
    return acc, iptr==terminated

@aoc.puzzle_timer()
def solve(input):
    prog = [(line.split()[0],int(line.split()[1])) for line in input.splitlines()]
    index=-1
    for opcode,operand in prog:
        index+=1
        test_prog=copy.deepcopy(prog)
        if opcode=='jmp':
            test_prog[index]=('nop',prog[index][1])
        elif opcode=='nop':
            test_prog[index]=('jmp',prog[index][1])
        else:
            continue
        acc, terminated = run(test_prog)
        if terminated:
            return acc



if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))