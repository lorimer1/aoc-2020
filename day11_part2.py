# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=11; PART=2

from aoc_utils import aoc_read_input, aoc_timer
from copy import deepcopy
import math

def seat_status(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return '.'

r, c = 0, 1  # index of x and y axis in a point

def get_angle(seat1, seat2): 
    return math.atan2(seat2[c] - seat1[c], seat1[r] - seat2[r]) % (2 * math.pi)
            
def get_seats(grid):
    seats = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#" or grid[row][col] == "L": 
                seats.append((row,col))
    return seats

def seat_test(grid, test_seat):
    seats = get_seats(grid)

    if test_seat in seats: seats.remove(test_seat)

    # sort each seat by it's length from our test_seat, sort seats by distance from our test_seat
    seats.sort(key=lambda seat: math.hypot(seat[c] - test_seat[c], seat[r] - test_seat[r]))

    # rank each seat based on the number of seats on the same angle. 0 for closest, 1 for next closest
    ranks = {seat: sum(get_angle(test_seat, seat) == get_angle(test_seat, other_seat)
                for other_seat in seats[:i]) for i, seat in enumerate(seats)}
    
    # keep only closest
    visible_seats = {key:val for key, val in ranks.items() if val == 0}

    # # sort by closet asteroids on each angle ... get 199th asteroid in this list
    # # x1, y1 = sorted(asteroids, key=lambda asteroid: (
    # #     ranks[asteroid], angle(our_base, asteroid)))[199]

    return None

@aoc_timer()
def solve(input):
    grid_current = []
    grid_next = [list(line) for line in input.splitlines()]
    iterations = 0
    while grid_next!=grid_current:
        iterations+=1
        grid_current = deepcopy(grid_next)
        for row in range(len(grid_current)):
            for col in range(len(grid_current[0])):
                grid_next[row][col] = seat_test(grid_current, (row, col))
    return sum(s.count('#') for s in grid_current)

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))