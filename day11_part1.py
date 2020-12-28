# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=11; PART=1

from utils import aoc
from copy import deepcopy

def seat_status(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return '.'

def seat_test(grid, row, col):
    if grid[row][col] == "L":
        if seat_status(grid,row,col-1)=="#": return "L"
        if seat_status(grid,row,col+1)=="#": return "L"
        for c in range(col-1,col+2,1):
            if seat_status(grid,row-1,c)=="#": return "L"
            if seat_status(grid,row+1,c)=="#": return "L"
        return "#"
    if grid[row][col] == "#":
        count=0
        if seat_status(grid,row,col-1)=="#": count+=1
        if seat_status(grid,row,col+1)=="#": count+=1
        for c in range(col-1,col+2,1):
            if seat_status(grid,row-1,c)=="#": count+=1
            if seat_status(grid,row+1,c)=="#": count+=1
        if count >= 4:
            return "L"
        else:
            return "#"
    return "."

@aoc.puzzle_timer()
def solve(input):
    grid_current = []
    grid_next = [list(line) for line in input.splitlines()]
    iterations = 0
    while grid_next!=grid_current:
        iterations+=1
        grid_current = deepcopy(grid_next)
        for row in range(len(grid_current)):
            for col in range(len(grid_current[0])):
                temp = seat_test(grid_current, row, col)
                grid_next[row][col] = seat_test(grid_current, row, col)
    return sum(s.count('#') for s in grid_current)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))