# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=18; PART=1

from os import add_dll_directory
import aoc
from collections import deque
import re
import operator


# First 17 days were purely my own work. All other puzzles (day 18 onward) were done as learning exercises i.e.
# I revised a good solution to understand optimum ways to approach a these problems.
# The website I used: https://github.com/mebeim/aoc/blob/master/2020
def tokenize(expression): 
    """ Tokenize the expression i.e. turn into a list of tokens """
    return re.findall(r'\d+|[+*()]', expression)

def evaluate(tokens):
    """ Evaluate the tokens using the precedence rules of the puzzle """
    acc = 0
    op = operator.add

    while tokens:
        token = tokens.popleft()
        if token.isdigit():
            value = int(token)
            acc = op(acc,value)
        elif token=='+':
            op = operator.add
        elif token=='*':
            op = operator.mul
        elif token=='(':
            value = evaluate(tokens)
            acc = op(acc,value)
        elif token==')':
            break

    return acc    

@aoc.puzzle_timer()
def solve(input):
    expressions = tuple(map(tokenize, input))
    total = sum(map(evaluate, map(deque, expressions)))
    return total

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))