# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=6; PART=2

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc

@aoc.puzzle_timer()
def solve(input):
    group_answers = {}
    count, person = 0, 0
    lines = input.splitlines()
    for line in lines:
        if len(line)==0: # end of group
            count += len([v for v in group_answers.values() if v==person])
            group_answers = {}
            person = 0
            continue
        person+=1
        for c in line: # group results
            if not c in group_answers:
                group_answers[c] = 1
            else:
                group_answers[c] += 1
    return count + len([v for v in group_answers.values() if v==person]) #edge case ... last group with no blank line following

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))