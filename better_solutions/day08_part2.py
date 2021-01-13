# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=8; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
import re
import copy

def run(test_prog):
    iptr, acc = 0, 0
    visited = set()
    terminated = len(test_prog)
    while not (iptr in visited or iptr==terminated):
        visited.add(iptr)
        opcode, operand = test_prog[iptr]
        if opcode=='nop':
            iptr+=1
        elif opcode=='acc':
            acc += int(operand)
            iptr+=1
        elif opcode=='jmp':
            iptr += int(operand)
    
    return acc, iptr==terminated

@aoc.puzzle_timer()
def solve(input):
    re_statement = re.compile( r'(\w+) ([\+\-\d]+)' )
    prog = re_statement.findall(input)
    index=-1
    
    for opcode, operand in prog:

        index+=1
        test_prog = copy.deepcopy(prog)
        _, test_operand = prog[index]       

        if opcode=='jmp':
            test_prog[index] = ('nop', test_operand)
        elif opcode=='nop':
            test_prog[index] = ('jmp', test_operand)
        else:
            continue
       
        acc, terminated = run(test_prog)
        
        if terminated:
            return acc



if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))